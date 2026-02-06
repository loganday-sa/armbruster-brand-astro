#!/usr/bin/env python3
"""
Migrate Ghost CMS blog posts to Astro content collection.
Fetches all posts via Ghost Content API, converts HTML to Markdown,
downloads featured images, and creates .md files with proper frontmatter.
"""

import json
import os
import re
import urllib.request
import urllib.error
from datetime import datetime
from html import unescape
from pathlib import Path
from markdownify import markdownify as md
from bs4 import BeautifulSoup

# Configuration
GHOST_URL = "https://the-bridge.ghost.io"
GHOST_API_KEY = "3baa09ac6be7c6e49d7b17f8b7"
ASTRO_CONTENT_DIR = Path(__file__).parent / "src" / "content" / "blog"
ASTRO_IMAGES_DIR = Path(__file__).parent / "public" / "images" / "blog"

# Category mapping: Ghost tag names -> Astro categories
CATEGORY_MAP = {
    "newsletter": "AI Strategy",
    "ai strategy": "AI Strategy",
    "automation": "Automation",
    "side business": "Side Business",
    "case studies": "Case Studies",
    "tools & tech": "Tools & Tech",
    "implementation": "Implementation",
    "career": "Career",
}


def fetch_ghost_posts():
    """Fetch all posts from Ghost Content API."""
    url = (
        f"{GHOST_URL}/ghost/api/content/posts/"
        f"?key={GHOST_API_KEY}&limit=all&include=tags,authors&formats=html"
    )
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    return data.get("posts", [])


def download_image(image_url, slug):
    """Download a featured image and save it locally. Returns relative path."""
    if not image_url:
        return None

    # Determine file extension from URL
    ext = os.path.splitext(image_url.split("?")[0])[1] or ".png"
    filename = f"{slug}{ext}"
    local_path = ASTRO_IMAGES_DIR / filename
    relative_path = f"/images/blog/{filename}"

    if local_path.exists():
        print(f"  Image already exists: {filename}")
        return relative_path

    try:
        req = urllib.request.Request(image_url)
        req.add_header("User-Agent", "Mozilla/5.0")
        with urllib.request.urlopen(req) as response:
            local_path.write_bytes(response.read())
        print(f"  Downloaded image: {filename}")
        return relative_path
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  WARNING: Failed to download image for {slug}: {e}")
        return None


def ghost_html_to_markdown(html_content):
    """Convert Ghost HTML content to clean Markdown."""
    if not html_content:
        return ""

    # Pre-process: some Ghost posts wrap content in extra HTML/head/body tags
    # Strip those wrapper elements before converting
    html_content = re.sub(r"</?html[^>]*>", "", html_content, flags=re.IGNORECASE)
    html_content = re.sub(r"<head>.*?</head>", "", html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r"</?body[^>]*>", "", html_content, flags=re.IGNORECASE)
    html_content = re.sub(r"</?meta[^>]*>", "", html_content, flags=re.IGNORECASE)
    html_content = re.sub(r"<title>.*?</title>", "", html_content, flags=re.IGNORECASE | re.DOTALL)

    # Convert HTML to markdown
    markdown = md(
        html_content,
        heading_style="ATX",
        bullets="-",
        strong_em_symbol="**",
        strip=["script", "style"],
    )

    # Clean up the markdown
    # Remove excessive blank lines (more than 2 consecutive)
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)

    # Clean up any leftover HTML entities
    markdown = markdown.replace("&nbsp;", " ")
    markdown = markdown.replace("&amp;", "&")
    markdown = markdown.replace("&lt;", "<")
    markdown = markdown.replace("&gt;", ">")
    markdown = markdown.replace("\u200b", "")  # zero-width space

    # Remove ```html code fences that markdownify might add
    markdown = re.sub(r"```html\s*\n?", "", markdown)
    markdown = re.sub(r"```\s*\n?", "", markdown)

    # Strip leading/trailing whitespace
    markdown = markdown.strip()

    return markdown


def determine_category(post):
    """Determine the Astro category from Ghost tags."""
    primary_tag = post.get("primary_tag")
    if primary_tag:
        tag_name = primary_tag.get("name", "").lower()
        if tag_name in CATEGORY_MAP:
            return CATEGORY_MAP[tag_name]
        # Title-case the tag name as fallback
        return primary_tag["name"].title()

    return "AI Strategy"  # Default category


def extract_tags(post):
    """Extract tag names from Ghost post."""
    tags = post.get("tags", [])
    return [t["name"].lower().replace(" ", "-") for t in tags if t.get("name")]


def format_date(date_str):
    """Format Ghost date string to YYYY-MM-DD."""
    if not date_str:
        return datetime.now().strftime("%Y-%m-%d")
    # Ghost dates look like: 2026-01-16T16:00:06.000+00:00
    return date_str[:10]


def clean_description(text):
    """Clean a description/excerpt to be a single-line plain text string."""
    if not text:
        return ""
    # Strip any HTML tags
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text(separator=" ")
    # Unescape HTML entities
    text = unescape(text)
    # Collapse all whitespace (newlines, tabs, multiple spaces) to single spaces
    text = re.sub(r"\s+", " ", text).strip()
    # Remove any markdown code fence artifacts
    text = text.replace("```html", "").replace("```", "")
    # Truncate to reasonable length for meta description
    if len(text) > 250:
        text = text[:247] + "..."
    return text


def escape_yaml_string(s):
    """Escape a string for YAML frontmatter."""
    if not s:
        return '""'
    # If string contains colons, quotes, or special chars, wrap in quotes
    s = s.replace('"', '\\"')
    return f'"{s}"'


def create_markdown_file(post, image_path):
    """Create an Astro-compatible markdown file from a Ghost post."""
    slug = post["slug"]
    title = post.get("title", "Untitled")
    raw_description = post.get("custom_excerpt") or post.get("excerpt") or ""
    description = clean_description(raw_description)
    pub_date = format_date(post.get("published_at"))
    updated_date = format_date(post.get("updated_at"))
    category = determine_category(post)
    tags = extract_tags(post)
    featured = post.get("featured", False)

    # Convert HTML content to markdown
    content_md = ghost_html_to_markdown(post.get("html", ""))

    # Build frontmatter
    frontmatter_lines = [
        "---",
        f"title: {escape_yaml_string(title)}",
        f"description: {escape_yaml_string(description.strip())}",
        f"pubDate: {pub_date}",
    ]

    if updated_date and updated_date != pub_date:
        frontmatter_lines.append(f"updatedDate: {updated_date}")

    if image_path:
        frontmatter_lines.append(f"heroImage: {escape_yaml_string(image_path)}")

    frontmatter_lines.append(f"category: {escape_yaml_string(category)}")

    if tags:
        tags_yaml = json.dumps(tags)
        frontmatter_lines.append(f"tags: {tags_yaml}")

    if featured:
        frontmatter_lines.append("featured: true")

    frontmatter_lines.append("---")

    # Combine frontmatter and content
    full_content = "\n".join(frontmatter_lines) + "\n\n" + content_md + "\n"

    # Write file
    filepath = ASTRO_CONTENT_DIR / f"{slug}.md"
    filepath.write_text(full_content, encoding="utf-8")
    print(f"  Created: {slug}.md")

    return filepath


def main():
    print("=" * 60)
    print("Ghost to Astro Blog Migration")
    print("=" * 60)

    # Ensure output directories exist
    ASTRO_CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    ASTRO_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Remove existing placeholder posts
    placeholder_posts = [
        "building-your-first-ai-agent.md",
        "future-proofing-your-career-with-ai.md",
        "getting-started-with-ai-automation.md",
    ]
    for pp in placeholder_posts:
        pp_path = ASTRO_CONTENT_DIR / pp
        if pp_path.exists():
            pp_path.unlink()
            print(f"  Removed placeholder: {pp}")

    # Fetch posts from Ghost
    print("\nFetching posts from Ghost...")
    posts = fetch_ghost_posts()
    print(f"  Found {len(posts)} posts\n")

    # Process each post
    success_count = 0
    error_count = 0

    for i, post in enumerate(posts, 1):
        title = post.get("title", "Untitled")
        slug = post["slug"]
        print(f"[{i}/{len(posts)}] {title}")

        try:
            # Download featured image
            image_path = download_image(post.get("feature_image"), slug)

            # Create markdown file
            create_markdown_file(post, image_path)
            success_count += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            error_count += 1

    print("\n" + "=" * 60)
    print(f"Migration complete!")
    print(f"  Successfully migrated: {success_count} posts")
    if error_count:
        print(f"  Errors: {error_count} posts")
    print(f"  Output directory: {ASTRO_CONTENT_DIR}")
    print(f"  Images directory: {ASTRO_IMAGES_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
