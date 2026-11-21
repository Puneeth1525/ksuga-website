# KSUGA INC website

Wholesale juices and energy drinks (VINUT, Monster, Red Bull) for stores and gas stations around Chicago.

## Structure
- `index.html`: the site (generated, do not edit by hand)
- `images/`: product photos
- `KSUGA-INC-Catalog.pdf`: downloadable catalog
- `og-image.png`, `favicon.png`, `apple-touch-icon.png`: link preview and icons
- `404.html`: not-found page
- `src/`: source. Edit `src/template.html`, `src/head.html` or the product list in `src/build_site.py`, then run `python3 src/build_site.py` to regenerate `index.html`.

## Deploy
Hosted on Vercel. Every push to `main` deploys automatically.
