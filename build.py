"""Builds the privacy pages from the EcoField app's locale files.

Usage: python3 build.py <path to frontend/src/i18n/locales>
"""
import html
import json
import re
import sys
from pathlib import Path

LANGS = [
    ("tr", "Türkçe"), ("en", "English"), ("de", "Deutsch"), ("fr", "Français"),
    ("es", "Español"), ("it", "Italiano"), ("ja", "日本語"), ("zh", "中文"),
]
EMAIL = "burakavar@gmail.com"
OUT = Path(__file__).parent


def inline(text: str) -> str:
    text = html.escape(text)
    return text.replace(EMAIL, f'<a href="mailto:{EMAIL}">{EMAIL}</a>')


def lang_nav(current: str) -> str:
    links = []
    for code, label in LANGS:
        attr = ' aria-current="page"' if code == current else ""
        links.append(f'<a href="{code}.html" hreflang="{code}"{attr}>{label}</a>')
    return '<nav class="lang">' + "".join(links) + "</nav>"


def render_body(content: str) -> tuple[str, str, str]:
    lines = [l.rstrip() for l in content.split("\n")]
    title, updated, rest = lines[0], lines[1], lines[2:]
    out, in_list = [], False
    for line in rest:
        if line.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if not line.strip():
            continue
        if re.match(r"^\d+\.\s", line):
            out.append(f"<h2>{inline(line)}</h2>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    if in_list:
        out.append("</ul>")
    return title, updated, "\n".join(out)


def page(lang: str, title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
{body}
<footer>© Burak Avar · ecoField · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</main>
</body>
</html>
"""


def main(locales: Path) -> None:
    for code, _ in LANGS:
        data = json.loads((locales / f"{code}.json").read_text(encoding="utf-8"))
        title, updated, body = render_body(data["privacy_page"]["content"])
        header = (
            f'<header><div class="brand">ecoField</div><h1>{inline(title)}</h1>'
            f'<div class="meta">{inline(updated)}</div>{lang_nav(code)}</header>'
        )
        (OUT / f"{code}.html").write_text(page(code, title, header + "\n" + body), encoding="utf-8")
        print(f"{code}.html")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
