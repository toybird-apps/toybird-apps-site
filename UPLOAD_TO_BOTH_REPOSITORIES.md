# ToyBird Apps GitHub Pages 共通アップロード用パッケージ

このZIPの中身を、以下の2つのGitHubリポジトリのルートへ同じようにアップロードしてください。

1. `toybird-apps/toybird-apps-site`
2. `toybird-apps/toybird-apps.github.io`

## 目的

- 既存のアプリ紹介・サポート・プライバシーポリシーページを維持する
- `https://toybird-apps.github.io/app-ads.txt` を公開する
- `https://toybird-apps.github.io/toybird-apps-site/app-ads.txt` も維持する
- アプリやApp Store Connectから参照される既存URLを壊さない

## app-ads.txt

ルートの `app-ads.txt` には、以下の行が1回だけ入っています。

```text
google.com, pub-6129814643212445, DIRECT, f08c47fec0942fa0
```

## GitHubでのアップロード方法

各リポジトリで以下を行います。

1. リポジトリを開く
2. `Add file` → `Upload files`
3. このZIPを展開したフォルダの**中身**をすべてアップロード
4. `Commit changes`
5. `Settings` → `Pages`
6. `Deploy from a branch`
7. `main` / `/ (root)` を選択して保存

## 公開後の確認URL

最低限、以下をブラウザで確認してください。

```text
https://toybird-apps.github.io/app-ads.txt
https://toybird-apps.github.io/toybird-apps-site/app-ads.txt
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/support.html
https://toybird-apps.github.io/toybird-apps-site/apps/yuru-dansha/ja/privacy.html
```

ルート側にも同じページが公開されます。

```text
https://toybird-apps.github.io/apps/yuru-dansha/ja/
```

ページが重複しても問題ありません。App Storeやアプリで参照済みのURLは、そのまま維持してください。
