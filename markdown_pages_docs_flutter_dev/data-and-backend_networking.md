Networking
==========

1. [Data & backend](/data-and-backend) chevron\_right- [Networking](/data-and-backend/networking)

Cross-platform http networking
------------------------------

[#](#cross-platform-http-networking)

The [`http`](https://pub.dev/packages/http) package provides the simplest way to issue http requests. This package is supported on Android, iOS, macOS, Windows, Linux and the web.

Platform notes
--------------

[#](#platform-notes)

Some platforms require additional steps, as detailed below.

### Android

[#](#android)

Android apps must [declare their use of the internet](https://developer.android.com/training/basics/network-ops/connecting) in the Android manifest (`AndroidManifest.xml`):

xml

```
<manifest xmlns:android...>
 ...
 <uses-permission android:name="android.permission.INTERNET" />
 <application ...
</manifest>
```

### macOS

[#](#macos)

macOS apps must allow network access in the relevant `*.entitlements` files.

xml

```
<key>com.apple.security.network.client</key>
<true/>
```

Learn more about [setting up entitlements](/platform-integration/macos/building#setting-up-entitlements).

Samples
-------

[#](#samples)

For a practical sample of various networking tasks (incl. fetching data, WebSockets, and parsing data in the background) see the [networking cookbook recipes](/cookbook/networking).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/data-and-backend/networking/&page-source=https://github.com/flutter/website/tree/main/src/content/data-and-backend/networking.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/data-and-backend/networking/&page-source=https://github.com/flutter/website/tree/main/src/content/data-and-backend/networking.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-02. [View source](https://github.com/flutter/website/tree/main/src/content/data-and-backend/networking.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/data-and-backend/networking/&page-source=https://github.com/flutter/website/tree/main/src/content/data-and-backend/networking.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   