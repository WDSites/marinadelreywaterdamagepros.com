# Marina Del Rey Water Damage Pros: generator source

Requires Python 3.10+ and Pillow (`pip install pillow`) for `assets.py`. Playwright and lxml are only needed for the optional `pw.py` and `tools/matrix.py` checks.

Build the site:

    python3 gen.py

This deletes and recreates `site/` (flat root, `slug/index.html` routes). Deploy the contents of `site/` to Cloudflare Pages with no build command and `site` as output.

Where things live:
- `content/*.py`: page content (services, locations, neighborhoods, blogs). `content/neighborhood.py` holds the three neighborhood pages.
- `content_patches.py`: small additions applied by slug (links, FAQs, CTAs).
- `home.py`: homepage sections. `gen.py`: templates, nav, footer, schema, sitemap. `css.py`: stylesheet.
- `images/`: converted WebP images and `alt.json`. `tools/convert.py` rebuilds them from the WD-IMG repo.
- Checks: `lint.py content/<file>.py`, `qa.py`, `pw.py` (needs a local server on port 8765 serving `site/`), `tools/matrix.py`.
- `facts.md`, `SCHEMA.md`, `NEWPAGES_BRIEF.md`: verified facts and content rules.
