# Toybird Apps Site

GitHub Pages website for Toybird Apps.

## Purpose

Toybird Apps publishes useful utilities designed to make everyday work and daily life clearer, smoother, and easier.

## Published URLs

If the GitHub account is `toybird-apps` and the repository is `toybird-apps-site`, the public URLs are:

```text
Top:
https://toybird-apps.github.io/toybird-apps-site/

DropReady Media:
https://toybird-apps.github.io/toybird-apps-site/apps/dropready-media/

DropReady Media Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/dropready-media/privacy.html

DropReady Media Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/dropready-media/support.html

DropReady Media Japanese Page:
https://toybird-apps.github.io/toybird-apps-site/apps/dropready-media/ja/

DropReady Media Japanese Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/dropready-media/ja/privacy.html

DropReady Media Japanese Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/dropready-media/ja/support.html

Pointer Cue:
https://toybird-apps.github.io/toybird-apps-site/apps/pointer-cue/

Pointer Cue Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/pointer-cue/privacy.html

Pointer Cue Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/pointer-cue/support.html

Meet Here Card:
https://toybird-apps.github.io/toybird-apps-site/apps/meet-here-card/

Meet Here Card Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/meet-here-card/privacy.html

Meet Here Card Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/meet-here-card/support.html

Meet Here Card Japanese Page:
https://toybird-apps.github.io/toybird-apps-site/apps/meet-here-card/ja/

Meet Here Card Japanese Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/meet-here-card/ja/privacy.html

Meet Here Card Japanese Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/meet-here-card/ja/support.html

Art Spot:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/

Art Spot Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/privacy.html

Art Spot Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/support.html

Art Spot Japanese Page:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/ja/

Art Spot Japanese Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/ja/privacy.html

Art Spot Japanese Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/ja/support.html

Yuru Dansha:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/

Yuru Dansha Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/privacy.html

Yuru Dansha Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/support.html

Yuru Dansha Japanese Page:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/

Yuru Dansha Japanese Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/privacy.html

Yuru Dansha Japanese Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/support.html
```

## App Information

### DropReady Media

```text
App Name: DropReady Media
Bundle ID: com.toybirdapps.dropreadymedia
Platform: macOS
Minimum OS: macOS Ventura 13 or later
```

### Meet Here Card

```text
App Name: Meet Here Card
Bundle ID: com.toybirdapps.meetherecard
Platform: iOS
```

### Art Spot

```text
Japanese App Name: 名画まちがい探し
English App Name: Art Spot
Bundle ID: com.toybird.oddspot
Platform: iOS
Privacy: Uses Google AdMob and Google UMP
```

### Yuru Dansha

```text
Japanese App Name: ゆる断写
English App Name: Yuru Dansha
Bundle ID: com.toybird.yurudansha
Platform: iOS / iPadOS
Privacy: Photo-library access with user permission; original media remains local; discarded-item thumbnails are stored locally for up to 30 days; uses Google AdMob and Google UMP
```

## Support

- Email: `support@toybird.com`

## Manual Upload

1. Download and extract the ZIP package.
2. Open the extracted `toybird-apps-site_yuru-dansha_added` folder.
3. Upload the contents of that folder to the root of the `toybird-apps-site` GitHub repository.
4. Commit the changes.
5. Wait for GitHub Pages deployment to finish.
6. Open the URLs above and verify that the pages load correctly.

## Structure

```text
toybird-apps-site/
├── index.html
├── styles.css
├── README.md
├── app-ads.txt
├── assets/
│   ├── logo.svg
│   ├── meet-here-card-icon.png
│   ├── dropready-media-icon.png
│   ├── art-spot-icon.png
│   └── yuru-dansha-icon.png
└── apps/
    ├── dropready-media/
    │   ├── index.html
    │   ├── privacy.html
    │   ├── support.html
    │   └── ja/
    │       ├── index.html
    │       ├── privacy.html
    │       └── support.html
    ├── pointer-cue/
    │   ├── index.html
    │   ├── privacy.html
    │   └── support.html
    ├── meet-here-card/
    │   ├── index.html
    │   ├── privacy.html
    │   ├── support.html
    │   └── ja/
    │       ├── index.html
    │       ├── privacy.html
    │       └── support.html
    ├── art-spot/
    │   ├── index.html
    │   ├── privacy.html
    │   ├── support.html
    │   └── ja/
    │       ├── index.html
    │       ├── privacy.html
    │       └── support.html
    └── yuru-dansha/
        ├── index.html
        ├── privacy.html
        ├── support.html
        └── ja/
            ├── index.html
            ├── privacy.html
            └── support.html
```

## Verification Checklist

After publishing, verify:

- The top page shows DropReady Media, Pointer Cue, Meet Here Card, Art Spot, and Yuru Dansha.
- Existing app pages still load correctly.
- Yuru Dansha English and Japanese product, support, and privacy pages load correctly.
- Yuru Dansha language-switch links work.
- The `support@toybird.com` mail links open correctly.
- The Yuru Dansha icon loads correctly on the top page and product pages.
- `app-ads.txt` is present at the repository root.
