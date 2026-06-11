# AdMob root repository deployment note

Upload the CONTENTS of this folder to a NEW public GitHub repository named:

`toybird-apps.github.io`

Then enable GitHub Pages:

- Settings
- Pages
- Deploy from a branch
- Branch: `main`
- Folder: `/ (root)`

After deployment, confirm that this URL opens in a browser:

`https://toybird-apps.github.io/app-ads.txt`

Expected content:

`google.com, pub-6129814643212445, DIRECT, f08c47fec0942fa0`

This root repository is required because AdMob checks the hostname root.
Uploading app-ads.txt only to the existing `toybird-apps-site` project repository
would publish it under `/toybird-apps-site/app-ads.txt`, which is not the root URL.
