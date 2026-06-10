# Yuru Dansha deployment note

## Manual upload

Upload the contents of this extracted folder to the root of the existing `toybird-apps-site` repository and commit the changes. Existing app pages remain included.

## URLs to register in App Store Connect

```text
Marketing URL:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/

Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/support.html

Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/privacy.html
```

## Japanese pages

```text
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/support.html
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/privacy.html
```

## app-ads.txt note

The repository includes:

```text
app-ads.txt
```

With GitHub project Pages, this file is published at:

```text
https://toybird-apps.github.io/toybird-apps-site/app-ads.txt
```

AdMob may look for a file at the host root (`https://toybird-apps.github.io/app-ads.txt`) depending on the store URL and crawler behavior. If AdMob does not verify the file after the App Store listing is linked, create or update the separate `toybird-apps.github.io` user-site repository and place the same `app-ads.txt` at its root.

## Verification

After GitHub Pages deployment, open every URL above and confirm that the pages, icon, language-switch links, and mail links load correctly.
