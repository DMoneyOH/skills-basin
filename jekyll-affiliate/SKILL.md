---
name: jekyll-affiliate
description: Expert Jekyll static site developer for affiliate content sites. Covers Liquid templating, frontmatter standards, _config.yml, GitHub Pages deployment, affiliate link patterns, SEO structure, and the PawPicks two-pass generation pipeline. Use for any Jekyll site work, post scaffolding, layout edits, or affiliate integration.
risk: none
source: custom
date_added: '2026-04-08'
author: derek
tags:
  - jekyll
  - affiliate
  - static-site
  - github-pages
  - liquid
  - pawpicks
---

# Jekyll Affiliate Site Expert

Expert in Jekyll static sites for affiliate content, specifically the PawPicks/happypetproductreviews.com stack.

## Use this skill when
- Writing, reviewing, or fixing Jekyll posts in `_posts/`
- Editing `_config.yml`, layouts, or includes
- Working on Liquid templates (`_layouts/`, `_includes/`)
- Inserting or auditing affiliate links (Amazon, Chewy, Petco)
- Debugging GitHub Pages / Actions deploy failures
- Scaffolding new post frontmatter
- Optimizing for jekyll-seo-tag, jekyll-sitemap, jekyll-feed
- Reviewing CSS in `assets/css/style.css`
- Working on `generate_posts.py` or `autopublish.sh`

## Do not use this skill when
- The task has no Jekyll or static site component
- Working on a React/Next.js or WordPress stack

---

## PawPicks Stack Reference

| Component | Detail |
|---|---|
| Engine | Jekyll (GitHub Pages) |
| Theme | Custom -- `_layouts/default.html`, `home.html`, `post.html` |
| CSS | `assets/css/style.css` (custom, Tailwind-free) |
| Plugins | jekyll-feed, jekyll-sitemap, jekyll-seo-tag |
| Deploy | GitHub Actions → `.github/workflows/deploy.yml` |
| URL | https://happypetproductreviews.com |
| Permalink | `/:categories/:title/` |
| Generator | `generate_posts.py` (Gemini 2.0 Flash, two-pass) |
| Autopublish | `autopublish.sh` (cron Mon/Thu 7am ET) |

---

## Frontmatter Standard

Every post MUST include all of these fields:

```yaml
---
layout: post
title: "Best [Product] for [Specific Use Case]"
date: YYYY-MM-DD
categories: [slug-no-spaces]
species: dog | cat | both
tags: [tag1, tag2]
description: "150-160 char meta description. Keyword-rich, benefit-focused, no clickbait."
image: /assets/images/posts/slug.jpg   # optional, og:image override
affiliate: true
---
```

**Rules:**
- `title` -- always "Best X for Y" format, 50-60 chars
- `categories` -- single slug matching permalink, lowercase-hyphenated
- `description` -- used by jekyll-seo-tag as meta description; 150-160 chars exactly
- `affiliate: true` -- flags posts with monetized links

---

## Post Structure Standard

Every affiliate post follows this exact structure:

```
1. Hook paragraph (2-3 sentences, problem/empathy angle)
2. ## Quick Picks (H2) -- 3-5 bullet links to anchors below
3. ### Featured Pick (H3) -- longest review, 150-200 words
4. ### Pick 2-5 (H3) -- 80-120 words each
5. ## Buying Guide (H2) -- 3-5 factors, 200-300 words total
6. ## FAQ (H2) -- 3-5 Q&A pairs
7. ## Final Thoughts (H2) -- 2-3 sentence close + primary CTA
```

---

## Affiliate Link Patterns

### Amazon Associates
```markdown
[Product Name on Amazon](https://amzn.to/XXXXXXX)
```
- Always use short `amzn.to` links (never full URLs)
- One primary CTA link per product section
- Anchor text: "[Product Name] on Amazon" or "Check price on Amazon"
- Disclosure required -- jekyll-seo-tag handles via `affiliate: true` frontmatter

### Chewy / Petco (Impact / CJ)
```markdown
[Product Name at Chewy](https://www.chewy.com/...)
```
- Apply after 10 posts live
- Add disclosure block in `_includes/affiliate-disclosure.html`

### FTC Disclosure
Include at TOP of every post body (before first paragraph):
```markdown
*Disclosure: This post contains affiliate links. We may earn a commission at no extra cost to you.*
```

---

## Liquid Templating Patterns

### Conditional affiliate disclosure
```liquid
{% if page.affiliate %}
  {% include affiliate-disclosure.html %}
{% endif %}
```

### Category-based species filtering
```liquid
{% assign dog_posts = site.posts | where: "species", "dog" %}
{% assign cat_posts = site.posts | where: "species", "cat" %}
```

### Related posts by tag
```liquid
{% assign related = site.posts | where_exp: "p", "p.tags contains page.tags[0]" | limit: 3 %}
```

### SEO image override
```liquid
{% if page.image %}
  <meta property="og:image" content="{{ page.image | absolute_url }}">
{% endif %}
```

---

## GitHub Pages / Actions

### Deploy workflow trigger
```yaml
on:
  push:
    branches: [main]
```

### Common deploy failures
| Symptom | Fix |
|---|---|
| Build fails on plugin | Ensure plugin in both `Gemfile` and `_config.yml` plugins list |
| Permalink 404 | Check `baseurl` is `''` not `/pawpicks` |
| SEO tags missing | Confirm `jekyll-seo-tag` in plugins + `{% seo %}` in `<head>` |
| Feed not generating | Add `{% feed_meta %}` to head layout |
| Sitemap wrong URLs | Verify `url:` in `_config.yml` matches custom domain |

---

## generate_posts.py Integration

### Two-pass pipeline
- **Pass 1 (Draft):** Gemini generates raw post from product keyword + species
- **Pass 2 (Review):** Gemini rewrites for grammar, facts, humanization, affiliate CTA placement
- Output: valid Jekyll frontmatter + body, written to `_posts/YYYY-MM-DD-slug.md`

### Frontmatter injection (Python)
```python
frontmatter = f"""---
layout: post
title: "{title}"
date: {today}
categories: [{slug}]
species: {species}
tags: {tags}
description: "{description}"
affiliate: true
---
"""
```

### Quality gates before write
1. Description is 150-160 chars
2. At least 3 H3 product sections present
3. At least 1 `amzn.to` link present
4. No placeholder text (`[INSERT]`, `TODO`, `PRODUCT_NAME`)
5. Word count 800-1500

---

## Common Issues & Fixes

| Issue | Root Cause | Fix |
|---|---|---|
| Posts not appearing | Wrong date format or future date | Use `YYYY-MM-DD`, no future dates |
| Broken permalinks | Space in category slug | Always use hyphenated slugs |
| og:image not showing | Missing `/assets/images/og-image.png` | Create placeholder or set in `_config.yml` |
| Duplicate meta description | Description in both frontmatter and body | Remove from body, keep in frontmatter only |
| Affiliate links stripped | GitHub Pages safe mode | Disable safe mode in `_config.yml`: `safe: false` |
| CSS not loading | Wrong `baseurl` | Ensure `baseurl: ''` for custom domain |
