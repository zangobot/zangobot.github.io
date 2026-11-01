#!/usr/bin/env python3
"""
Fetch all papers authored by Luca Demetrio using the Findpapers library.

The script performs a simple author search (``au[Luca Demetrio]``) and stores the
results in ``luca_demetrio_papers.json``.  Each entry contains:

* title (string)
* authors (list of author names)
* venue (publication source title, e.g. journal or conference name)
* year (int)
* abstract (string, may be empty if unavailable)

The output is a plain JSON array that can easily be consumed by other tools.
"""

import json
from pathlib import Path

import findpapers

AUTHOR = "Luca Demetrio"
QUERY = f"au[{AUTHOR}]"
engine = findpapers.Engine()
print(f"Searching for papers by {AUTHOR}…")
result = engine.search(QUERY)
print(f"Found {len(result.papers)} papers.")

papers = []
for paper in result.papers:
    d = paper.to_dict()
    pub_year = int(d.get("publication_date", "0000-01-01").split("-")[0])
    authors = [a.get("name") for a in d.get("authors", [])]
    venue = d.get("source", {}).get("title") or ""

    papers.append(
        {
            "title": d.get("title", ""),
            "authors": authors,
            "venue": venue,
            "year": pub_year,
            "abstract": d.get("abstract", ""),
            "link": d.get("url", ""),
            "tags": d.get("keywords", []),
        }
    )

output_file = Path(__file__).parent / "luca_demetrio_papers.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(papers, f, ensure_ascii=False, indent=2)

print(f"Results written to {output_file}")

index_path = Path(__file__).parent /"posts" / "science"/"index.md"


lines = ["# Publications by year", ""]
for year in sorted({p["year"] for p in papers}, reverse=True):
    lines.append(f"## {year}")
    for p in [x for x in papers if x["year"] == year]:
        title = p.get("title", "")
        url = p.get("link", "#")
        authors = ", ".join(p.get("authors", []))
        venue = p.get("venue", "")
        abstract = p.get("abstract", "") or "(No abstract)"
        lines.append(f"**[{title}]({url})**\n")
        lines.append(f"  *Authors:* {authors}\n")
        lines.append(f"  *Published on:* {venue}\n")
        lines.append("  <details>")
        lines.append("    <summary>Abstract</summary>")
        lines.append(f"\n{abstract}\n")
        lines.append("  </details>\n")
    lines.append("")

header = """---
layout: default
title: Science Publications
---
"""
with open(index_path, "w", encoding="utf-8") as f:
    
    f.write(header + "\n".join(lines))

print(f"Markdown index written to {index_path}")
