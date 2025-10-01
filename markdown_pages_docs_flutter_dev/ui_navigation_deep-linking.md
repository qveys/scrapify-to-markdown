Deep linking
============

1. [UI](/ui) chevron\_right- [Navigation and routing](/ui/navigation) chevron\_right- [Deep linking](/ui/navigation/deep-linking)

Deep links are links that not only open an app, but also take the user to a specific location "deep" inside the app. For example, a deep link from an advertisement for a pair of sneakers might open a shopping app and display the product page for those particular shoes.

Flutter supports deep linking on iOS, Android, and the web. Opening a URL displays that screen in your app. With the following steps, you can launch and display routes by using named routes (either with the [`routes`](https://api.flutter.dev/flutter/material/MaterialApp/routes.html) parameter or [`onGenerateRoute`](https://api.flutter.dev/flutter/material/MaterialApp/onGenerateRoute.html)), or by using the [`Router`](https://api.flutter.dev/flutter/widgets/Router-class.html) widget.

*info* Note

Named routes are no longer recommended for most applications. For more information, see [Limitations](/ui/navigation#limitations) in the [navigation overview](/ui/navigation) page.

If you're running the app in a web browser, there's no additional setup required. Route paths are handled in the same way as an iOS or Android deep link. By default, web apps read the deep link path from the url fragment using the pattern: `/#/path/to/app/screen`, but this can be changed by [configuring the URL strategy](/ui/navigation/url-strategies) for your app.

If you are a visual learner, check out the following video:

[Watch on YouTube in a new tab: "Deep linking in Flutter"](https://www.youtube.com/watch/KNAb2XL7k2g)

Get started
-----------

[#](#get-started)

To get started, see our cookbooks for Android and iOS:

[Android](/cookbook/navigation/set-up-app-links)[iOS](/cookbook/navigation/set-up-universal-links)

Migrating from plugin-based deep linking
----------------------------------------

[#](#migrating-from-plugin-based-deep-linking)

If you have written a plugin to handle deep links, as described in [Deep Links and Flutter applications](https://medium.com/flutter-community/deep-links-and-flutter-applications-how-to-handle-them-properly-8c9865af9283) (a free article on Medium), you should opt out the Flutter's default deep link handler. To do this, set `FlutterDeepLinkingEnabled` to false in `Info.plist` *or* `flutter_deeplinking_enabled` to false in `AndroidManifest.xml`.

Behavior
--------

[#](#behavior)

The behavior varies slightly based on the platform and whether the app is launched and running.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Platform / Scenario Using Navigator Using Router|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | iOS (not launched) App gets initialRoute ("/") and a short time after gets a pushRoute App gets initialRoute ("/") and a short time after uses the RouteInformationParser to parse the route and call RouterDelegate.setNewRoutePath, which configures the Navigator with the corresponding Page.|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Android - (not launched) App gets initialRoute containing the route ("/deeplink") App gets initialRoute ("/deeplink") and passes it to the RouteInformationParser to parse the route and call RouterDelegate.setNewRoutePath, which configures the Navigator with the corresponding Pages.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | iOS (launched) pushRoute is called Path is parsed, and the Navigator is configured with a new set of Pages.|  |  |  | | --- | --- | --- | | Android (launched) pushRoute is called Path is parsed, and the Navigator is configured with a new set of Pages. | | | | | | | | | | | | | | |

When using the [`Router`](https://api.flutter.dev/flutter/widgets/Router-class.html) widget, your app has the ability to replace the current set of pages when a new deep link is opened while the app is running.

To learn more
-------------

[#](#to-learn-more)

* [Learning Flutter's new navigation and routing system](https://blog.flutter.dev/learning-flutters-new-navigation-and-routing-system-7c9068155ade) provides an introduction to the Router system.* [Deep dive into Flutter deep linking](https://www.youtube.com/watch?v=6RxuDcs6jVw&t=3s) video from Google I/O 2023* [Flutter Deep Linking: The Ultimate Guide](https://codewithandrea.com/articles/flutter-deep-links/), a step-by-step tutorial showing how to implement deep links in Flutter.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/navigation/deep-linking/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/navigation/deep-linking.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/navigation/deep-linking/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/navigation/deep-linking.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-27. [View source](https://github.com/flutter/website/tree/main/src/content/ui/navigation/deep-linking.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/navigation/deep-linking/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/navigation/deep-linking.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   