Configuring the URL strategy on the web
=======================================

1. [UI](/ui) chevron\_right- [Navigation and routing](/ui/navigation) chevron\_right- [Configuring the URL strategy on the web](/ui/navigation/url-strategies)

Flutter web apps support two ways of configuring URL-based navigation on the web:

**Hash (default)**: Paths are read and written to the [hash fragment](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax). For example, `flutterexample.dev/#/path/to/screen`. **Path**: Paths are read and written without a hash. For example, `flutterexample.dev/path/to/screen`.

Configuring the URL strategy
----------------------------

[#](#configuring-the-url-strategy)

To configure Flutter to use the path instead, use the [usePathUrlStrategy](https://api.flutter.dev/flutter/flutter_web_plugins/usePathUrlStrategy.html) function provided by the [flutter\_web\_plugins](https://api.flutter.dev/flutter/flutter_web_plugins/flutter_web_plugins-library.html) library, which is part of the Flutter SDK.

You can't directly add `flutter_web_plugins` using `pub add`. Include it as a Flutter [SDK dependency](https://dart.dev/tools/pub/dependencies#sdk) in your `pubspec.yaml` file:

yaml

```
dependencies:
  flutter:
    sdk: flutter
  flutter_web_plugins:
    sdk: flutter
```

Then call the `usePathUrlStrategy` function before `runApp`:

dart

```
import 'package:flutter_web_plugins/url_strategy.dart';

void main() {
  usePathUrlStrategy();
  runApp(ExampleApp());
}
```

Configuring your web server
---------------------------

[#](#configuring-your-web-server)

PathUrlStrategy uses the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API), which requires additional configuration for web servers.

To configure your web server to support PathUrlStrategy, check your web server's documentation to rewrite requests to `index.html`. Check your web server's documentation for details on how to configure single-page apps.

If you are using Firebase Hosting, choose the "Configure as a single-page app" option when initializing your project. For more information see Firebase's [Configure rewrites](https://firebase.google.com/docs/hosting/full-config#rewrites) documentation.

The local dev server created by running `flutter run -d chrome` is configured to handle any path gracefully and fallback to your app's `index.html` file.

Hosting a Flutter app at a non-root location
--------------------------------------------

[#](#hosting-a-flutter-app-at-a-non-root-location)

Update the `<base href="/">` tag in `web/index.html` to the path where your app is hosted. For example, to host your Flutter app at `my_app.dev/flutter_app`, change this tag to `<base href="/flutter_app/">`.

Relative `base href` tags are supported for release builds but they must take into account the full URL where the page was served from. This means a relative `base href` for a request to `/flutter_app/`, `/flutter_app/nested/route`, and `/flutter_app/nested/route/` will be different (for example `"."`, `".."`, and `"../.."` respectively).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/navigation/url-strategies/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/navigation/url-strategies.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/navigation/url-strategies/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/navigation/url-strategies.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-10-16. [View source](https://github.com/flutter/website/tree/main/src/content/ui/navigation/url-strategies.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/navigation/url-strategies/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/navigation/url-strategies.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   