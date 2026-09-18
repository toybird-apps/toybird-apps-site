#!/usr/bin/env python3
"""Normalize non-visual SEO/AIO metadata for public Toybird Labs landing pages.

This script intentionally modifies only <head> metadata plus sitemap <lastmod> values.
It does not change <body>, CSS, visible copy, layout, buttons, or images.
"""

from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

BASE_URL = "https://labs.toybird.com/"
SITEMAP = Path("sitemap.xml")

LOCALE_MAP = {"en": "en_US", "ja": "ja_JP"}
SOCIAL_IMAGE_OVERRIDES = {
    "index.html": "https://labs.toybird.com/assets/toybird-labs-og.png",
    "apps/pocket-screen/index.html": "https://lp.toybird.com/pocket-screen/assets/og-image.png",
    "apps/pointer-cue/index.html": "https://lp.toybird.com/pointer-cue/assets/og-image.png",
    "apps/ai-memorize-sheet/index.html": "https://lp.toybird.com/shared/ai-study-sheet-v3/en-overview.png",
    "apps/ai-memorize-sheet/ja/index.html": "https://lp.toybird.com/shared/ai-study-sheet-v3/ja-overview.png",
    "apps/prompt-ready/index.html": "https://lp.toybird.com/prompt-ready/assets/og-image.png",
    "apps/prompt-ready/ja/index.html": "https://lp.toybird.com/prompt-ready/assets/og-image.png",
    "apps/koesub/index.html": "https://labs.toybird.com/assets/koesub-og.png",
}

HOME_TITLE = "Toybird Labs | Productivity Apps for macOS, iPhone & iPad"
HOME_DESCRIPTION = (
    "Toybird Labs creates useful macOS, iPhone, and iPad apps for productivity, "
    "study, communication, and daily tasks, including Pocket Screen and AI Study Sheet."
)
AI_STUDY_JA_DESCRIPTION = (
    "AI赤シートは、教科書・プリント・ノート・写真・PDFを取り込み、重要語句を隠してタップで答えを確認できるiPhone・iPad向け暗記学習アプリです。"
    "通常教材と赤シート用教材に対応し、PDFの途中再開、ランダム・弱点優先の復習、検索・バックアップも利用できます。"
    "教材データは外部AIへ送らず端末内で処理されます。"
)

MANAGED_META_START = "<!-- SEO-AIO-METADATA:START -->"
MANAGED_META_END = "<!-- SEO-AIO-METADATA:END -->"
MANAGED_SCHEMA_START = "<!-- SEO-AIO-STRUCTURED-DATA:START -->"
MANAGED_SCHEMA_END = "<!-- SEO-AIO-STRUCTURED-DATA:END -->"

META_DESCRIPTION_RE = re.compile(
    r"<meta\b(?=[^>]*\bname=[\"']description[\"'])[^>]*>", re.I
)
TITLE_RE = re.compile(r"<title>.*?</title>", re.I | re.S)
CANONICAL_RE = re.compile(
    r"<link\b(?=[^>]*\brel=[\"']canonical[\"'])[^>]*>", re.I
)
ICON_RE = re.compile(
    r"<link\b(?=[^>]*\brel=[\"']icon[\"'])[^>]*\bhref=[\"']([^\"']+)[\"'][^>]*>",
    re.I,
)
H1_RE = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.I | re.S)
HTML_LANG_RE = re.compile(r"<html\b[^>]*\blang=[\"']([^\"']+)[\"']", re.I)
JSONLD_RE = re.compile(
    r"<script\b[^>]*type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>",
    re.I | re.S,
)
OG_META_RE = re.compile(
    r"<meta\b(?=[^>]*\bproperty=[\"']og:(?:title|description|url|type|site_name|image)[\"'])[^>]*>\s*",
    re.I,
)
HREFLANG_RE = re.compile(
    r"<link\b(?=[^>]*\brel=[\"']alternate[\"'])(?=[^>]*\bhreflang=[\"'][^\"']+[\"'])[^>]*>\s*",
    re.I,
)


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value).strip()


def get_meta_description(text: str) -> str:
    m = META_DESCRIPTION_RE.search(text)
    if not m:
        return ""
    tag = m.group(0)
    cm = re.search(r"\bcontent=[\"']([^\"']*)[\"']", tag, re.I)
    return html.unescape(cm.group(1)) if cm else ""


def replace_meta_description(text: str, description: str) -> str:
    tag = f'<meta name="description" content="{html.escape(description, quote=True)}">'
    if META_DESCRIPTION_RE.search(text):
        return META_DESCRIPTION_RE.sub(tag, text, count=1)
    return text.replace("</head>", f"  {tag}\n</head>", 1)


def get_title(text: str) -> str:
    m = TITLE_RE.search(text)
    return strip_tags(m.group(0)[7:-8]) if m else ""


def get_canonical(text: str) -> str:
    m = CANONICAL_RE.search(text)
    if not m:
        return ""
    hm = re.search(r"\bhref=[\"']([^\"']+)[\"']", m.group(0), re.I)
    return html.unescape(hm.group(1)) if hm else ""


def ensure_canonical(text: str, canonical: str) -> str:
    if CANONICAL_RE.search(text):
        return text
    return text.replace(
        "</head>", f'  <link rel="canonical" href="{html.escape(canonical, quote=True)}">\n</head>', 1
    )


def get_icon_url(text: str, canonical: str) -> str | None:
    m = ICON_RE.search(text)
    if not m:
        return None
    return urljoin(canonical, html.unescape(m.group(1)))


def get_h1(text: str) -> str:
    m = H1_RE.search(text)
    return strip_tags(m.group(1)) if m else ""


def get_lang(text: str) -> str:
    m = HTML_LANG_RE.search(text)
    return m.group(1).lower() if m else "en"


def remove_managed_block(text: str, start: str, end: str) -> str:
    return re.sub(
        rf"\s*{re.escape(start)}.*?{re.escape(end)}\s*",
        "\n",
        text,
        flags=re.S,
    )


def landing_paths_from_sitemap() -> list[tuple[Path, str]]:
    tree = ET.parse(SITEMAP)
    root = tree.getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    result: list[tuple[Path, str]] = []
    for url_node in root.findall("sm:url", ns):
        loc = url_node.findtext("sm:loc", default="", namespaces=ns).strip()
        if not loc.startswith(BASE_URL):
            continue
        parsed = urlparse(loc)
        rel = parsed.path.lstrip("/")
        path = Path(rel) / "index.html" if rel else Path("index.html")
        if path.exists():
            result.append((path, loc))
    return result


def localized_links(path: Path) -> list[str]:
    parts = path.parts
    if not parts or parts[0] != "apps":
        return []

    if len(parts) >= 4 and parts[-2] == "ja":
        app_dir = Path(*parts[:-2])
    else:
        app_dir = path.parent

    en_file = app_dir / "index.html"
    ja_file = app_dir / "ja" / "index.html"
    if not (en_file.exists() and ja_file.exists()):
        return []

    app_rel = app_dir.as_posix().rstrip("/") + "/"
    en_url = urljoin(BASE_URL, app_rel)
    ja_url = urljoin(BASE_URL, app_rel + "ja/")
    return [
        f'<link rel="alternate" hreflang="en" href="{en_url}">',
        f'<link rel="alternate" hreflang="ja" href="{ja_url}">',
        f'<link rel="alternate" hreflang="x-default" href="{en_url}">',
    ]


def managed_meta_block(path: Path, text: str, canonical: str) -> str:
    title = get_title(text)
    description = get_meta_description(text)
    icon = get_icon_url(text, canonical)
    lang = get_lang(text)
    locale = LOCALE_MAP.get(lang, lang.replace("-", "_"))
    image = SOCIAL_IMAGE_OVERRIDES.get(path.as_posix(), icon)
    image_alt = get_h1(text) or title.split(" | ", 1)[0] or "Toybird Labs"
    if path == Path("index.html"):
        image_alt = "Toybird Labs apps and products"
    lines = [
        MANAGED_META_START,
        f'<meta property="og:title" content="{html.escape(title, quote=True)}">',
        f'<meta property="og:description" content="{html.escape(description, quote=True)}">',
        f'<meta property="og:url" content="{html.escape(canonical, quote=True)}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Toybird Labs">',
        f'<meta property="og:locale" content="{html.escape(locale, quote=True)}">',
    ]
    if image:
        lines.append(f'<meta property="og:image" content="{html.escape(image, quote=True)}">')
        lines.append(f'<meta property="og:image:alt" content="{html.escape(image_alt, quote=True)}">')
    lines.extend(localized_links(path))
    lines.append(MANAGED_META_END)
    return "\n".join(lines)


def update_existing_software_schema(text: str, description: str, canonical: str, icon: str | None) -> tuple[str, bool]:
    found = False

    def repl(match: re.Match[str]) -> str:
        nonlocal found
        raw = match.group(1).strip()
        try:
            data = json.loads(raw)
        except Exception:
            return match.group(0)
        if not isinstance(data, dict) or data.get("@type") != "SoftwareApplication":
            return match.group(0)
        found = True
        data["url"] = canonical
        data["description"] = description
        if icon:
            data.setdefault("image", icon)
        author = data.get("author")
        if isinstance(author, dict):
            author.setdefault("@type", "Organization")
            author.setdefault("name", "Toybird Labs")
            author.setdefault("url", BASE_URL)
        else:
            data["author"] = {"@type": "Organization", "name": "Toybird Labs", "url": BASE_URL}
        data.setdefault(
            "publisher", {"@type": "Organization", "name": "Toybird Labs", "url": BASE_URL}
        )
        pretty = json.dumps(data, ensure_ascii=False, indent=2)
        return f'<script type="application/ld+json">\n{pretty}\n</script>'

    return JSONLD_RE.sub(repl, text), found


def schema_block(path: Path, text: str, canonical: str) -> str:
    description = get_meta_description(text)
    icon = get_icon_url(text, canonical)
    lang = get_lang(text)

    if path == Path("index.html"):
        data = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebSite",
                    "@id": BASE_URL + "#website",
                    "url": BASE_URL,
                    "name": "Toybird Labs",
                    "description": description,
                    "inLanguage": lang,
                    "publisher": {"@id": BASE_URL + "#organization"},
                },
                {
                    "@type": "Organization",
                    "@id": BASE_URL + "#organization",
                    "name": "Toybird Labs",
                    "url": BASE_URL,
                },
            ],
        }
    else:
        name = get_h1(text) or get_title(text).split(" | ", 1)[0]
        data = {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": name,
            "url": canonical,
            "description": description,
            "inLanguage": lang,
            "author": {"@type": "Organization", "name": "Toybird Labs", "url": BASE_URL},
            "publisher": {"@type": "Organization", "name": "Toybird Labs", "url": BASE_URL},
        }
        if icon:
            data["image"] = icon

    pretty = json.dumps(data, ensure_ascii=False, indent=2)
    return f"{MANAGED_SCHEMA_START}\n<script type=\"application/ld+json\">\n{pretty}\n</script>\n{MANAGED_SCHEMA_END}"


def update_page(path: Path, canonical: str) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original

    # Fix the specific Bing findings without changing visible page content.
    if path == Path("index.html"):
        text = TITLE_RE.sub(f"<title>{HOME_TITLE}</title>", text, count=1)
        text = replace_meta_description(text, HOME_DESCRIPTION)
    elif path == Path("apps/ai-memorize-sheet/ja/index.html"):
        text = replace_meta_description(text, AI_STUDY_JA_DESCRIPTION)

    text = ensure_canonical(text, canonical)

    # Rebuild only the hidden metadata that this normalization owns.
    text = remove_managed_block(text, MANAGED_META_START, MANAGED_META_END)
    text = remove_managed_block(text, MANAGED_SCHEMA_START, MANAGED_SCHEMA_END)
    text = OG_META_RE.sub("", text)
    text = HREFLANG_RE.sub("", text)

    # If the page already has a hand-authored SoftwareApplication block, enrich it in place.
    if path != Path("index.html"):
        desc = get_meta_description(text)
        icon = get_icon_url(text, canonical)
        text, has_software_schema = update_existing_software_schema(text, desc, canonical, icon)
    else:
        has_software_schema = False

    meta = managed_meta_block(path, text, canonical)
    additions = [meta]
    if path == Path("index.html") or not has_software_schema:
        additions.append(schema_block(path, text, canonical))

    text = text.replace("</head>", "\n" + "\n".join(additions) + "\n</head>", 1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def update_sitemap_lastmod(changed_urls: set[str]) -> bool:
    ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    tree = ET.parse(SITEMAP)
    root = tree.getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    today = date.today().isoformat()
    changed = False
    for url_node in root.findall("sm:url", ns):
        loc = url_node.findtext("sm:loc", default="", namespaces=ns).strip()
        if loc not in changed_urls:
            continue
        lastmod = url_node.find("sm:lastmod", ns)
        if lastmod is None:
            lastmod = ET.SubElement(url_node, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")
        if lastmod.text != today:
            lastmod.text = today
            changed = True
    if changed:
        tree.write(SITEMAP, encoding="utf-8", xml_declaration=True)
    return changed


def main() -> None:
    targets = landing_paths_from_sitemap()
    changed_urls: set[str] = set()
    changed_paths: list[str] = []
    for path, canonical in targets:
        if update_page(path, canonical):
            changed_urls.add(canonical)
            changed_paths.append(path.as_posix())

    sitemap_changed = update_sitemap_lastmod(changed_urls)
    if sitemap_changed:
        changed_paths.append(SITEMAP.as_posix())

    print(f"Processed {len(targets)} public landing pages.")
    print(f"Changed {len(changed_paths)} files.")
    for item in changed_paths:
        print(item)


if __name__ == "__main__":
    main()
