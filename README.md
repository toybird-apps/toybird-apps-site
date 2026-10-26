# Toybird Labs product site

Public site: https://labs.toybird.com/  
Repository: `toybird-apps/toybird-apps-site`  
Publishing branch: `main` (GitHub Pages)

## Content

- `index.html`: English app directory and workflow overview.
- `apps/<slug>/index.html`: canonical product details.
- `apps/<slug>/support.html`, `privacy.html`, and any app-specific `terms.html`: help and policies.
- `apps/<slug>/ja/`: Japanese pages where available.
- `support/`, `privacy/`, `terms/`, `legal/`: shared help and policy directories.
- `styles.css` and `assets/`: shared presentation and media.
- `sitemap.xml`: indexable canonical pages only; help/policy pages marked noindex are not included.
- `robots.txt`, verification files, `app-ads.txt`, and IndexNow key: operational files to preserve.

The portfolio, localized landing pages, and blog are maintained separately at https://lp.toybird.com/ in `toybird-lp-site`.

## Maintenance

1. Confirm public release information and actual app behavior before changing features, pricing, system requirements, or download links.
2. Keep English/Japanese pages, support instructions, metadata, structured data, and root app cards consistent.
3. Preserve established slugs, including `brainlot-puzzle` for Brainrot Tile Quest and `gmail-spotlight-indexer` for Toybird Webmail Indexer.
4. Check relative links, image targets, language links, anchors, JSON-LD, and mobile wrapping.
5. Set sitemap `lastmod` to the actual date of the relevant page change, not the date of an unrelated site deployment.
6. Commit the reviewed files together to `main`; verify the live site after GitHub Pages publishes.

Existing one-off maintenance workflows reflect earlier updates. Review their scripts and scope before running them against current content.

## Distribution

Use the verified store links on each product page. Prompt Ready and Pointer Cue have Windows distribution links; Pointer Cue's existing Windows edition is not feature-equivalent to the current macOS edition. Do not fabricate an App Store ID for Toybird Webmail Indexer; its product page directs availability questions to support.

## Support

support@toybird.com
