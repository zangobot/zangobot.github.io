#!/usr/bin/env python3
"""
Fetch all papers authored by Luca Demetrio using the Findpapers library.
The script writes a JSON file and generates a Markdown index with a search bar.
"""

import json
import html
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

index_path = Path(__file__).parent / "posts" / "science" / "index.md"

lines = ["# Publications by year", ""]
for year in sorted({p["year"] for p in papers}, reverse=True):
    lines.append(f"## {year}")
    for p in [x for x in papers if x["year"] == year]:
        title = html.unescape(p.get("title", ""))
        url = p.get("link", "#")
        authors = ", ".join(p.get("authors", []))
        venue = html.unescape(p.get("venue", ""))
        abstract_raw = p.get("abstract", "") or "(No abstract)"
        abstract_md = html.unescape(abstract_raw).replace("\n", "<br>")
        lines.append(f"<strong>**[{title}]({url})**</strong>")
        lines.append(f"*Authors:* {authors}")
        lines.append(f"*Published on:* {venue}")
        lines.append("  <details>")
        lines.append("    <summary>Abstract</summary>")
        lines.append(f"\n{abstract_md}\n")
        lines.append("  </details>")
        lines.append("<br>")
    lines.append("")

header = """---
layout: default
title: Science Publications
---
# Publications

<div style="margin-bottom:1rem;">
  <input type="text" id="pub-search" placeholder="Search publications...">
</div>
<script>
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('pub-search');
  function build() {
    const links = document.querySelectorAll('strong a');
    links.forEach(link => {
      const strong = link.closest('strong');
      if (!strong) return;
      const paragraph = strong.parentNode; // <p>
      if (paragraph.classList.contains('publication')) return;

      const wrapper = document.createElement('div');
      wrapper.className = 'publication';

      // Find the <br> that separates this publication from the next
      let end = paragraph.nextElementSibling;
      while (end && end.tagName !== 'BR') {
        end = end.nextElementSibling;
      }

      // Move all nodes from paragraph up to (but not including) the <br> into wrapper
      const grandParent = paragraph.parentNode;
      grandParent.insertBefore(wrapper, paragraph);
      let node = paragraph;
      while (node && node !== end) {
        const next = node.nextSibling; // include text nodes
        wrapper.appendChild(node);
        node = next;
      }

      // Store searchable text (title, authors, venue)
      wrapper.dataset.text = link.textContent.toLowerCase();
    });
  }

  build();

  input.addEventListener('input', () => {
    const q = input.value.toLowerCase().trim();
    document.querySelectorAll('.publication').forEach(pub => {
      pub.style.display = pub.dataset.text.includes(q) ? '' : 'none';
    });
  });
});
</script>
"""

with open(index_path, "w", encoding="utf-8") as f:
    f.write(header + "\n".join(lines))

print(f"Markdown index written to {index_path}")
