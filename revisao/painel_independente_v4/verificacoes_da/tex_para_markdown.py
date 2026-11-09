"""
Gera artigo_hipotese_lara_resende.md a partir de artigo_svar_lara_resende.tex e referencias.bib.

Mantém o espelho em Markdown sincronizado com o manuscrito LaTeX: citações autor-ano a partir do
.bib, equações numeradas com \\tag, tabelas em Markdown (com \\multicolumn e \\multirow achatados),
figuras como imagens e lista de referências gerada apenas com as obras citadas.

Uso:  python3 scripts/tex_para_markdown.py
Autor: Ângelo Augusto Bonvenuto
"""

import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX = os.path.join(ROOT, "artigo_svar_lara_resende.tex")
BIB = os.path.join(ROOT, "referencias.bib")
OUT = os.path.join(ROOT, "artigo_hipotese_lara_resende.md")

ACC_MAP = {"'": {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "A": "Á", "E": "É", "O": "Ó"},
           "~": {"a": "ã", "o": "õ", "n": "ñ", "A": "Ã"},
           "^": {"a": "â", "e": "ê", "o": "ô"},
           "`": {"a": "à", "A": "À", "O": "Ò"}}


def decode_latex(s):
    for a, b in [("{\\'\\i}", "í"), ("\\'\\i", "í"), ("{\\c{c}}", "ç"), ("\\c{c}", "ç"), ("{\\o}", "ø"), ("\\o", "ø")]:
        s = s.replace(a, b)
    s = re.sub(r"\{\\([`'~^])\{?(\w)\}?\}", lambda m: ACC_MAP[m.group(1)].get(m.group(2), m.group(2)), s)
    s = re.sub(r"\\([`'~^])\{?(\w)\}?", lambda m: ACC_MAP[m.group(1)].get(m.group(2), m.group(2)), s)
    return s


# ---------------------------------------------------------------------------
# Utilidades de parsing
# ---------------------------------------------------------------------------
def match_brace(s, i):
    """s[i] == '{'; devolve o índice do '}' correspondente."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    raise ValueError("chave não balanceada")


def replace_cmd(s, cmd, fn):
    """Substitui \\cmd[opt]{arg} por fn(arg), respeitando chaves aninhadas."""
    pat = re.compile(r"\\" + cmd + r"(?![A-Za-z])\s*(\[[^\]]*\])?\s*\{")
    while True:
        m = pat.search(s)
        if not m:
            return s
        j = match_brace(s, m.end() - 1)
        s = s[:m.start()] + fn(s[m.end():j]) + s[j + 1:]


def split_top(s, sep):
    """Divide s em sep apenas no nível zero de chaves."""
    parts, depth, cur, i = [], 0, "", 0
    while i < len(s):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
        if depth == 0 and s.startswith(sep, i):
            parts.append(cur)
            cur, i = "", i + len(sep)
            continue
        cur += s[i]
        i += 1
    parts.append(cur)
    return parts


# ---------------------------------------------------------------------------
# Bibliografia
# ---------------------------------------------------------------------------
def parse_bib(path):
    text = open(path, encoding="utf-8").read()
    entries = {}
    for m in re.finditer(r"@(\w+)\{([^,]+),", text):
        end = match_brace(text, m.end() - len(m.group(2)) - 2)
        body = text[m.end():end]
        fields = {"_type": m.group(1).lower()}
        for fm in re.finditer(r"(\w+)\s*=\s*\{", body):
            j = match_brace(body, fm.end() - 1)
            fields[fm.group(1).lower()] = body[fm.end():j].strip()
        entries[m.group(2).strip()] = fields
    return entries


def strip_braces(s):
    return s.replace("{", "").replace("}", "")


def authors(entry):
    out = []
    for a in entry["author"].split(" and "):
        last, _, first = decode_latex(a.strip()).partition(",")
        out.append((strip_braces(last.strip()), strip_braces(first.strip())))
    return out


def cite_name(entry):
    au = authors(entry)
    if len(au) == 1:
        return au[0][0]
    if len(au) == 2:
        return f"{au[0][0]} & {au[1][0]}"
    return f"{au[0][0]} et al."


def initials(first):
    return " ".join(p[0] + "." for p in first.split() if p)


ARG = r"\{(?:[^{}]|\{[^{}]*\})*\}"  # argumento com um nível de chaves aninhadas
BIBDB = parse_bib(BIB)
CITED = set()
LABELS = {}
MATH = []


def cite(keys, mode):
    keys = [k.strip() for k in keys.split(",")]
    CITED.update(keys)
    groups = []
    for k in keys:
        e = BIBDB[k]
        nm, yr = cite_name(e), e["year"]
        if groups and groups[-1][0] == nm:
            groups[-1][1].append(yr)
        else:
            groups.append((nm, [yr]))
    if mode == "t":
        return "; ".join(f"{n} ({', '.join(y)})" for n, y in groups)
    body = "; ".join(f"{n}, {', '.join(y)}" for n, y in groups)
    return f"({body})" if mode == "p" else body


def protect_math(s):
    def keep(m):
        MATH.append(m.group(0))
        return f"\x00{len(MATH) - 1}\x00"
    return re.sub(r"(?<!\\)\$(?:\\\$|[^$])+?(?<!\\)\$", keep, s)


def restore_math(s):
    return re.sub(r"\x00(\d+)\x00", lambda m: MATH[int(m.group(1))], s)


def latex_inline(s):
    """Converte comandos de texto (fora da matemática) para Markdown."""
    s = protect_math(s)
    s = replace_cmd(s, "citet", lambda k: cite(k, "t"))
    s = replace_cmd(s, "citep", lambda k: cite(k, "p"))
    s = replace_cmd(s, "citealt", lambda k: cite(k, "alt"))
    s = replace_cmd(s, "ref", lambda k: str(LABELS.get(k, "??")))
    s = replace_cmd(s, "url", lambda u: f"<{u}>")
    s = replace_cmd(s, "texttt", lambda x: "`" + x.replace("\\_", "_") + "`")
    s = replace_cmd(s, "textbf", lambda x: f"**{x}**")
    s = replace_cmd(s, "textit", lambda x: f"*{x}*")
    s = replace_cmd(s, "emph", lambda x: f"*{x}*")
    s = replace_cmd(s, "shortstack", lambda x: " ".join(p.strip() for p in split_top(x, "\\\\")))
    s = s.replace("``", "“").replace("''", "”").replace("---", "—").replace("--", "–")
    s = s.replace("\\%", "%").replace("\\&", "&").replace("\\_", "_").replace("~", " ")
    s = re.sub(r"\\(noindent|small|centering|par)\b\s*", "", s)
    s = restore_math(s)
    return s.strip()


def ref_line(entry):
    au = authors(entry)
    names = [f"{l}, {initials(f)}" for l, f in au]
    nm = names[0] if len(names) == 1 else ", ".join(names[:-1]) + ", & " + names[-1]
    t = entry["_type"]
    title = latex_inline(decode_latex(entry.get("title", "")))
    title = strip_braces(title)
    year = entry.get("year", "")
    get = lambda f: decode_latex(strip_braces(entry.get(f, "")))
    if t == "article":
        vol = entry.get("volume", "")
        num = f"({entry['number']})" if "number" in entry else ""
        pages = entry.get("pages", "").replace("--", "–")
        tail = ", ".join(x for x in [f"{vol}{num}" if vol else "", pages] if x)
        return f"- **{nm}** ({year}). {title}. *{get('journal')}*" + (f", {tail}" if tail else "") + "."
    if t == "book":
        return f"- **{nm}** ({year}). *{title}*. {get('address')}: {get('publisher')}."
    if t == "incollection":
        ed_list = []
        for e in decode_latex(strip_braces(entry.get("editor", ""))).split(" and "):
            last, _, first = e.strip().partition(",")
            ed_list.append(f"{initials(first.strip())} {last.strip()}")
        eds = ed_list[0] if len(ed_list) == 1 else ", ".join(ed_list[:-1]) + ", & " + ed_list[-1]
        pages = entry.get("pages", "").replace("--", "–")
        return (f"- **{nm}** ({year}). {title}. In {eds} (Eds.), *{get('booktitle')}* (pp. {pages}). "
                f"{get('address')}: {get('publisher')}.")
    if t == "techreport":
        num = f", n. {entry['number']}" if "number" in entry else ""
        return f"- **{nm}** ({year}). {title}. *{entry.get('type', 'Working Paper')}*{num}, {get('institution')}."
    how = latex_inline(decode_latex(entry.get("howpublished", "")))
    note = latex_inline(decode_latex(entry.get("note", "")))
    line = f"- **{nm}** ({year}). {title}. {how}. {note}".rstrip()
    return line if line.endswith(".") else line + "."


# ---------------------------------------------------------------------------
# Tabelas
# ---------------------------------------------------------------------------
def unmakecell(c):
    """\\makecell[pos]{a\\\\ b} -> 'a<br>b' (quebra de linha dentro da célula)."""
    while True:
        m = re.search(r"\\makecell(\[[^\]]*\])?\{", c)
        if not m:
            return c
        end = match_brace(c, m.end() - 1)
        inner = c[m.end():end].replace("\\scriptsize", "").replace("\\\\", "<br>")
        c = c[:m.start()] + inner + c[end + 1:]


def convert_table(block, number):
    cap = re.search(r"\\caption\{", block)
    caption = block[cap.end():match_brace(block, cap.end() - 1)]
    tab_start = block.index("\\begin{tabular}")
    spec_open = block.index("{", tab_start + len("\\begin{tabular}"))
    body = block[match_brace(block, spec_open) + 1:block.index("\\end{tabular}")]
    header_rows, body_rows, in_body = [], [], False
    for raw in split_top(body, "\\\\"):
        line = raw.strip()
        if "\\midrule" in line and not in_body:
            in_body = True
        line = re.sub(r"\\(toprule|midrule|bottomrule)", "", line)
        line = re.sub(r"\\cmidrule\([^)]*\)\{[^}]*\}", "", line).strip()
        if not line:
            continue
        cells = []
        for c in split_top(line, "&"):
            c = c.strip()
            mc = re.match(r"\\multicolumn\{(\d+)\}\{[^}]*\}\{", c)
            if mc:
                inner = c[mc.end() - 1:]
                val, span = latex_inline(inner[1:match_brace(inner, 0)]), int(mc.group(1))
                # no cabeçalho, o rótulo do grupo se repete em cada coluna; no corpo, só na primeira
                cells += [val] * span if not in_body else [val] + [""] * (span - 1)
                continue
            mr = re.match(r"\\multirow\{\d+\}\{[^}]*\}\{", c)
            if mr:
                inner = c[mr.end() - 1:]
                c = inner[1:match_brace(inner, 0)]
            cells.append(latex_inline(unmakecell(c)).replace("< br>", "<br>"))
        (body_rows if in_body else header_rows).append(cells)
    ncols = max(len(r) for r in header_rows + body_rows)
    header = []
    for j in range(ncols):
        parts = []
        for r in header_rows:
            if j < len(r) and r[j] and r[j] not in parts:
                parts.append(r[j])
        header.append("<br>".join(parts) if parts else " ")
    lines = [f"#### Tabela {number}: {latex_inline(caption)}", "",
             "| " + " | ".join(header) + " |",
             "| :--- |" + " :---: |" * (ncols - 1)]
    for r in body_rows:
        if len(r) == 1:  # linha de rótulo de \multirow sozinha
            r = [r[0]] + [""] * (ncols - 1)
        r = r + [""] * (ncols - len(r))
        lines.append("| " + " | ".join(x.replace("|", "\\|") for x in r) + " |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Conversão principal
# ---------------------------------------------------------------------------
def main():
    tex = open(TEX, encoding="utf-8").read()
    doc = tex[tex.index("\\begin{document}") + len("\\begin{document}"):tex.index("\\end{document}")]
    doc = re.sub(r"(?<!\\)%.*", "", doc)
    # versão não anônima: \ifanonimo A \else B \fi -> B; \repositorio -> URL; center -> conteúdo
    repo = re.search(r"\\newcommand\{\\repositorio\}\{\\url\{([^}]+)\}\}", tex).group(1)
    doc = re.sub(r"\\ifanonimo\s*(.*?)\\else\s*(.*?)\\fi\b", lambda m: m.group(2), doc, flags=re.S)
    doc = doc.replace("\\repositorio", "\\url{" + repo + "}")
    doc = re.sub(r"\\begin\{center\}(.*?)\\end\{center\}", lambda m: m.group(1), doc, flags=re.S)

    # Numeração de equações, tabelas e figuras na ordem do documento
    counters = {"equation": 0, "table": 0, "figure": 0}
    for m in re.finditer(r"\\begin\{(equation|table|figure)\}(.*?)\\end\{\1\}", doc, re.S):
        counters[m.group(1)] += 1
        for lab in re.findall(r"\\label\{([^}]+)\}", m.group(2)):
            LABELS[lab] = counters[m.group(1)]

    title = re.search(r"\\title\{\\textbf\{(.*?)\}\}\n", tex, re.S).group(1)
    author = re.search(r"\\textbf\{([^}]+)\}\\thanks\{(.*?)\}\}?\n", tex, re.S)
    out = [f"# {latex_inline(title)}", "", f"**Autor:** {author.group(1)}  ",
           f"*{latex_inline(author.group(2).replace(chr(92) + 'repositorio', chr(92) + 'url{' + repo + '}'))}*", "", "---", ""]

    abstracts = re.findall(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", doc, re.S)
    for heading, ab in zip(["Resumo", "Abstract"], abstracts):
        out += [f"### {heading}", ""]
        for para in re.split(r"\\vspace\{[^}]*\}", ab):
            para = latex_inline(" ".join(para.split()))
            if para:
                out += [para, ""]
        out += ["---", ""]
    doc = doc[doc.rindex("\\end{abstract}") + len("\\end{abstract}"):]
    doc = doc.replace("\\selectlanguage{brazil}", "").replace("\\newpage", "")
    doc = re.sub(r"\\bibliographystyle\{[^}]*\}|\\bibliography\{[^}]*\}", "", doc)

    state = {"sec": 0, "sub": 0, "appendix": False, "pending": None}
    num = {"equation": 0, "table": 0, "figure": 0}
    list_stack = []  # cada nível: [é_numerada, contador]
    buf = []

    def indent():
        return "   " * (len(list_stack) - 1) if list_stack else ""

    def flush():
        text = latex_inline(" ".join(" ".join(buf).split())) if buf else ""
        buf.clear()
        if not text:
            return
        if state["pending"] is not None:
            out.append(state["pending"] + text)
            state["pending"] = None
        elif list_stack:
            out.append(indent() + "   " + text)
        else:
            out.append(text)
        out.append("")

    pieces = []
    parts = re.split(r"(\\begin\{(equation|table|figure)\}.*?\\end\{\2\})", doc, flags=re.S)
    k = 0
    while k < len(parts):
        if k % 3 == 1:
            pieces.append(("env", parts[k]))
            k += 2
            continue
        split_re = (r"(\\begin\{(?:enumerate|itemize)\}|\\end\{(?:enumerate|itemize)\}|\\item\b|"
                    r"\\(?:section|subsection|paragraph)" + ARG + r"|\\appendix|\n\s*\n)")
        for t in re.split(split_re, parts[k]):
            if t:
                pieces.append(("txt", t))
        k += 1

    for kind, t in pieces:
        if kind == "env":
            env = re.match(r"\\begin\{(\w+)\}", t).group(1)
            flush()
            num[env] += 1
            if env == "equation":
                content = t[len("\\begin{equation}"):t.rindex("\\end{equation}")]
                content = re.sub(r"\\label\{[^}]+\}", "", content).strip()
                lead = (indent() + "   ") if list_stack else ""
                out += [lead + "$$" + content + " \\tag{" + str(num[env]) + "}$$", ""]
            elif env == "table":
                out += [convert_table(t, num[env]), ""]
            else:
                img = re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", t).group(1)
                cap = re.search(r"\\caption\{", t)
                caption = latex_inline(t[cap.end():match_brace(t, cap.end() - 1)])
                # texto alternativo de imagem não renderiza matemática: simplifica a notação
                caption = caption.replace("{,}", ",").replace("\\hat{\\gamma}^h", "γ̂ʰ").replace("\\gamma", "γ")
                caption = re.sub(r"\$([^$]*)\$", lambda m: m.group(1).replace("\\", ""), caption)
                out += [f"![Figura {num[env]}: {caption}](figuras/{img})", ""]
            continue

        if re.fullmatch(r"\n\s*\n", t):
            flush()
            continue
        m = re.fullmatch(r"\\section\{(.*)\}", t)
        if m:
            flush()
            state["sub"] = 0
            if state["appendix"]:
                out += [f"## Apêndice {chr(65 + state['sec'])}. {latex_inline(m.group(1))}", ""]
                state["sec"] += 1
            else:
                state["sec"] += 1
                out += [f"## {state['sec']}. {latex_inline(m.group(1))}", ""]
            continue
        m = re.fullmatch(r"\\subsection\{(.*)\}", t)
        if m:
            flush()
            state["sub"] += 1
            out += [f"### {state['sec']}.{state['sub']}. {latex_inline(m.group(1))}", ""]
            continue
        m = re.fullmatch(r"\\paragraph\{(.*)\}", t)
        if m:
            flush()
            buf.append("\\textbf{" + m.group(1) + "}")
            continue
        if t == "\\appendix":
            flush()
            state["appendix"], state["sec"] = True, 0
            continue
        if t in ("\\begin{enumerate}", "\\begin{itemize}"):
            flush()
            list_stack.append(["enumerate" in t, 0])
            continue
        if t in ("\\end{enumerate}", "\\end{itemize}"):
            flush()
            list_stack.pop()
            continue
        if t == "\\item":
            flush()
            list_stack[-1][1] += 1
            numbered, n = list_stack[-1]
            state["pending"] = indent() + (f"{n}. " if numbered else "- ")
            continue
        buf.append(t)
    flush()

    def sort_key(e):
        plain = unicodedata.normalize("NFKD", authors(e)[0][0]).encode("ascii", "ignore").decode()
        return (plain.lower(), len(authors(e)) > 1, e["year"])

    refs = sorted((BIBDB[k] for k in CITED), key=sort_key)
    out += ["---", "", "## Referências Bibliográficas", ""] + [ref_line(e) for e in refs]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    open(OUT, "w", encoding="utf-8").write(text.strip() + "\n")
    print(f"Salvo: {OUT} ({len(CITED)} obras citadas)")


if __name__ == "__main__":
    main()
