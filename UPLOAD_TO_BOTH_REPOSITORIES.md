# Canonical publishing policy for Toybird Labs (2026-10-08)

**The old instruction to upload identical HTML to two repositories is retired.**

The goal of this policy is to keep `https://labs.toybird.com/` as the single canonical host for Toybird Labs product, Support, and Privacy pages.

| Repository | Current role |
|---|---|
| `toybird-apps/toybird-apps-site` | **Source of truth.** Edit and publish the full pages here. GitHub Pages serves `labs.toybird.com`. |
| `toybird-apps/toybird-apps.github.io` | **Legacy redirects only.** Existing HTML paths immediately forward to the equivalent path on `labs.toybird.com`. Do not sync content from the canonical repo. |
| `toybird-apps/toybird-lp-site` | Separate portfolio and marketing site. Its independent product landing pages have their own canonical URLs. It may link to the canonical Labs product documentation. |

## Update procedure
1. Make product-page and Support/Privacy changes **only** in `toybird-apps-site`.
2. Preserve correct `index,follow` on searchable product pages, intentional `noindex,follow` on utility pages, and valid canonical URLs.
3. Maintain the Labs sitemap only for pages intended for Google indexing; update `lastmod` when substantive content actually changes.
4. Do **not** copy HTML to the legacy `toybird-apps.github.io` repository. New old-host paths require an explicit redirect to an existing Labs page.
5. Keep `app-ads.txt` and ownership verification files at their required historical locations. They are **not** product HTML and must not be removed by the redirect migration.
6. Test canonical page access, redirect target availability, cross-site links, and Search Console indexing separately after deployment.

## Search Console note
A successful GitHub Pages deployment, canonical link, or live URL inspection means the page can be served; it does **not** guarantee that Google has indexed the URL. Judge success from the Google Index status in Search Console, not from the GitHub build or a simple `site:` query.

Retained file name `UPLOAD_TO_BOTH_REPOSITORIES.md` is historical only. **Do not follow the old duplicate-upload process.**
