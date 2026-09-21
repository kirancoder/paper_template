#!/usr/bin/env python3
import re, sys, os

src = "answer_final.md"
html = "answer.html"

def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return t

lines = open(src, encoding="utf-8").read().split("\n")
out = []
i = 0
in_list = False
def close_list():
    global in_list
    if in_list:
        out.append("</ul>")
        in_list = False

while i < len(lines):
    line = lines[i]
    if line.startswith("### "):
        close_list()
        out.append(f"<h3>{inline(line[4:].strip())}</h3>")
    elif line.startswith("## "):
        close_list()
        out.append(f"<h2>{inline(line[3:].strip())}</h2>")
    elif line.startswith("# "):
        close_list()
        out.append(f"<h1>{inline(line[2:].strip())}</h1>")
    elif line.startswith("- "):
        if not in_list:
            out.append("<ul>")
            in_list = True
        out.append(f"<li>{inline(line[2:].strip())}</li>")
    elif line.strip() == "":
        close_list()
    else:
        close_list()
        if line.strip():
            out.append(f"<p>{inline(line.strip())}</p>")
    i += 1
close_list()

css = """
<style>
@page { size: A4; margin: 15mm 14mm 14mm 14mm; }
body { font-family: "Liberation Serif", "Times New Roman", serif;
       font-size: 10.2pt; line-height: 1.22; margin: 0; color: #000; }
h1 { font-size: 14pt; text-align: center; margin: 0 0 6pt 0; }
h2 { font-size: 11.5pt; margin: 9pt 0 3pt 0; border-bottom: 0.5pt solid #444; padding-bottom: 1pt; }
h3 { font-size: 10.6pt; margin: 7pt 0 2pt 0; }
p  { margin: 3pt 0; text-align: justify; }
ul { margin: 2pt 0 2pt 0; padding-left: 16pt; }
li { margin: 1.5pt 0; }
strong { font-weight: bold; }
</style>
"""

doc = f"<!DOCTYPE html><html><head><meta charset='utf-8'>{css}</head><body>" + "".join(out) + "</body></html>"
open(html, "w", encoding="utf-8").write(doc)
print("wrote", html, "bytes:", len(doc))
