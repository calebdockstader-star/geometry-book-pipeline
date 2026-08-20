#!/usr/bin/env python3
"""Build a labelled, one-figure-per-page PDF of likely multipart figures.

This is a visual audit aid, not a geometry verifier.  It deliberately errs on
the side of including a figure: multiple TikZ pictures, horizontally shifted
scopes, repeated shifted scopes, or printed (a)/(b) panel labels all qualify.

Usage:
    python3 tools/audit_multipart_figures.py

Output:
    build/audit/multipart-figures.pdf
    build/audit/multipart-figures.tsv
"""

from __future__ import annotations

import glob
import os
import re
import subprocess


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(ROOT, "chapters")
OUT = os.path.join(ROOT, "build", "audit")


def macro_chunks(source: str):
    starts = list(re.finditer(r"(?m)^\\newcommand\{(\\FIG[A-Z]+)\}", source))
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(source)
        yield match.group(1), source[match.start():end]


def is_multipart(chunk: str) -> bool:
    if chunk.count(r"\begin{tikzpicture}") > 1:
        return True
    if len(re.findall(r"\\begin\{scope\}\[[^]]*(?:xshift|shift)", chunk)) > 1:
        return True
    if r"\foreach" in chunk and "xshift=" in chunk:
        return True
    return len(re.findall(r"\{\([a-z]\)\}", chunk)) > 1


def candidates():
    found = []
    for path in sorted(glob.glob(os.path.join(CHAPTERS, "figures*.tex"))):
        source = open(path, encoding="utf-8").read()
        for macro, chunk in macro_chunks(source):
            if is_multipart(chunk):
                found.append((os.path.basename(path), macro))
    return found


def driver(rows):
    inputs = sorted({filename for filename, _ in rows})
    lines = [
        r"\documentclass[11pt]{book}",
        r"\usepackage[paperwidth=145mm,paperheight=200mm,top=14mm,bottom=14mm,inner=14mm,outer=14mm]{geometry}",
        r"\usepackage{brumfiel}",
    ]
    lines.extend(r"\input{" + name.removesuffix(".tex") + "}" for name in inputs)
    lines.extend([r"\pagestyle{empty}", r"\begin{document}"])
    for filename, macro in rows:
        label = f"{filename}: {macro}"
        lines.append(r"\noindent\ttfamily\footnotesize\detokenize{" + label + r"}\par\vspace{4mm}")
        lines.append(macro + r"\clearpage")
    lines.append(r"\end{document}")
    return "\n".join(lines) + "\n"


def main():
    rows = candidates()
    os.makedirs(OUT, exist_ok=True)
    tex = os.path.join(OUT, "multipart-figures.tex")
    with open(tex, "w", encoding="utf-8") as handle:
        handle.write(driver(rows))
    with open(os.path.join(OUT, "multipart-figures.tsv"), "w", encoding="utf-8") as handle:
        handle.write("page\tfile\tmacro\n")
        for page, (filename, macro) in enumerate(rows, 1):
            handle.write(f"{page}\t{filename}\t{macro}\n")
    subprocess.run(
        ["tectonic", "-Z", "search-path=../../style", "-Z", "search-path=../../chapters",
         "--outdir", OUT, tex],
        cwd=OUT,
        check=True,
    )
    print(f"built {len(rows)} multipart candidates: {os.path.join(OUT, 'multipart-figures.pdf')}")


if __name__ == "__main__":
    main()
