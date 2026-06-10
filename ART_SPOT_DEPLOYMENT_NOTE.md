# Art Spot Deployment Note

## Public URLs after GitHub Pages deployment

```text
Product page:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/

Privacy Policy URL:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/privacy.html

Support URL:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/support.html

Japanese product page:
https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/ja/
```

## Important: update the iOS app code before App Store submission

The current `ExternalLinks.swift` in the app project still contains placeholder `example.com` URLs. Replace them with:

```swift
static let privacyPolicy = URL(string: "https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/privacy.html")!
static let support = URL(string: "https://toybird-apps.github.io/toybird-apps-site/apps/art-spot/support.html")!
static let reportAd = URL(string: "mailto:support@toybird.com?subject=Art%20Spot%20-%20Report%20an%20Ad")!
```
