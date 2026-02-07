# Scott Armbruster

Personal brand site and professional blog for Scott Armbruster.

- URL: armbruster-brand-astro.pages.dev
- Author: Scott Armbruster
- Categories: AI Strategy, Implementation, Industry, Career
- Deployed to Cloudflare Pages

## Tech

Astro 5 with MDX, RSS, and Sitemap integrations. Blog posts are markdown files in `src/content/blog/`.

## Key Files

- `BRAND_VOICE.md` -- Editorial guidelines. Read before writing any content.
- `src/consts.ts` -- Site metadata, categories, branding, social links.
- `src/content/config.ts` -- Blog post schema and validation.

## Site Structure

Additional pages beyond blog:
- `/about` - About Scott
- `/agency` - Agency services
- `/contact` - Contact form
- `/demos` - Project demos
- `/education` - Educational resources
- `/services` - Service offerings
- `/resources` - Resource library

## Development

```bash
npm install
npm run dev    # Dev server
npm run build  # Production build
```

## Writing Posts

Posts go in `src/content/blog/` as `.md` files. Hero images are plain string paths (NOT Astro image imports).

Frontmatter:

```yaml
---
title: "Post Title"
description: "150-160 char meta description"
author: "Scott Armbruster"
category: "AI Strategy"  # or Implementation, Industry, Career
pubDate: "Mon DD YYYY"
heroImage: "/images/blog/<slug>.jpg"
tags: ["tag1", "tag2"]
---
```

Internal links use category paths: `/ai-strategy/<slug>/`, `/implementation/<slug>/`, etc.

Always read `BRAND_VOICE.md` before writing content for this site.
