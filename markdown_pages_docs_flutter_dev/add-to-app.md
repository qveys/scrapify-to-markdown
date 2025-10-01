Add Flutter to an existing app
==============================

1. [Add to app](/add-to-app)

Add-to-app
----------

[#](#add-to-app)

If you are writing a new application from scratch, it is easy to [get started](/get-started/codelab) using Flutter. But what if you already have an app that's not written in Flutter, and it's impractical to start from scratch?

For those situations, Flutter can be integrated into your existing application piecemeal, as a module. This feature is known as "add-to-app". The module can be imported into your existing app to render part of your app using Flutter, while the rest can be rendered using existing technology. This method can also be used to run shared non-UI logic by taking advantage of Dart's portability and interoperability with other languages.

Add-to-app is currently supported on Android, iOS, and web.

Flutter supports two flavors of add-to-app:

* **Multi-engine**: supported on Android and iOS, allows running one or more instances of Flutter, each rendering a widget embedded into the host application. Each instance is a separate Dart program, running in isolation from other programs. Having multiple Flutter instances allows each instance to maintain independent application and UI state while using minimal memory resources. See more in the [multiple Flutters](/add-to-app/multiple-flutters) page.* **Multi-view**: supported on the web, allows creating multiple [FlutterView](https://api.flutter.dev/flutter/dart-ui/FlutterView-class.html)s, each rendering a widget embedded into the host application. In this mode there's only one Dart program and all views and widgets can share objects.

Add-to-app supports integrating multiple Flutter views of any size, supporting various use-cases. Two of the most common use-cases are:

* **Hybrid navigation stacks**: an app is made of multiple screens, some of which are rendered by Flutter, and others by another framework. The user can navigate from one screen to another freely, no matter which framework is used to render the screen.* **Partial-screen views**: a screen in the app renders multiple widgets, some of which are rendered by Flutter, and others by another framework. The user can scroll and interact with any widget freely, no matter which framework is used to render the widget.

Supported features
------------------

[#](#supported-features)

### Add to Android applications

[#](#add-to-android-applications)

![Add-to-app steps on Android](/assets/images/docs/development/add-to-app/android-overview.webp)

* Auto-build and import the Flutter module by adding a Flutter SDK hook to your Gradle script.* Build your Flutter module into a generic [Android Archive (AAR)](https://developer.android.com/studio/projects/android-library) for integration into your own build system and for better Jetifier interoperability with AndroidX.* [`FlutterEngine`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html) API for starting and persisting your Flutter environment independently of attaching a [`FlutterActivity`](https://api.flutter.dev/javadoc/io/flutter/embedding/android/FlutterActivity.html)/[`FlutterFragment`](https://api.flutter.dev/javadoc/io/flutter/embedding/android/FlutterFragment.html) etc.* Android Studio Android/Flutter co-editing and module creation/import wizard.* Java and Kotlin host apps are supported.* Flutter modules can use [Flutter plugins](https://pub.dev/flutter) to interact with the platform.* Support for Flutter debugging and stateful hot reload by using `flutter attach` from IDEs or the command line to connect to an app that contains Flutter.

### Add to iOS applications

[#](#add-to-ios-applications)

![Add-to-app steps on iOS](/assets/images/docs/development/add-to-app/ios-overview.webp)

* Auto-build and import the Flutter module by adding a Flutter SDK hook to your CocoaPods and to your Xcode build phase.* Build your Flutter module into a generic [iOS Framework](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WhatAreFrameworks.html) for integration into your own build system.* [`FlutterEngine`](https://api.flutter.dev/ios-embedder/interface_flutter_engine.html) API for starting and persisting your Flutter environment independently of attaching a [`FlutterViewController`](https://api.flutter.dev/ios-embedder/interface_flutter_view_controller.html).* Objective-C and Swift host apps supported.* Flutter modules can use [Flutter plugins](https://pub.dev/flutter) to interact with the platform.* Support for Flutter debugging and stateful hot reload by using `flutter attach` from IDEs or the command line to connect to an app that contains Flutter.

See our [add-to-app GitHub Samples repository](https://github.com/flutter/samples/tree/main/add_to_app) for sample projects in Android and iOS that import a Flutter module for UI.

### Add to web applications

[#](#add-to-web-applications)

Flutter can be added to any existing HTML DOM-based web app written in any client-side Dart web framework ([jaspr](https://pub.dev/packages/jaspr), [ngdart](https://pub.dev/packages/ngdart), [over\_react](https://pub.dev/packages/over_react), etc), any client-side JS framework ([React](https://react.dev/), [Angular](https://angular.dev/), [Vue.js](https://vuejs.org/), etc), any server-side rendered framework ([Django](https://www.djangoproject.com/), [Ruby on Rails](https://rubyonrails.org/), [Apache Struts](https://struts.apache.org/), etc), or even no framework (affectionately known as "[VanillaJS](http://vanilla-js.com/)"). The minimum requirement is only that your existing application and its framework support importing JavaScript libraries, and creating HTML elements for Flutter to render into.

To add Flutter to an existing app, build it normally, then follow the [embedding instructions](/platform-integration/web/embedding-flutter-web#embedded-mode) for putting Flutter views onto the page.

Get started
-----------

[#](#get-started)

To get started, see our project integration guide for Android and iOS:

[Android](/add-to-app/android/project-setup)[iOS](/add-to-app/ios/project-setup)[Web](/platform-integration/web/embedding-flutter-web#embedded-mode)

API usage
---------

[#](#api-usage)

After Flutter is integrated into your project, see our API usage guides at the following links:

[Android](/add-to-app/android/add-flutter-screen)[iOS](/add-to-app/ios/add-flutter-screen)[Web](/platform-integration/web/embedding-flutter-web#manage-flutter-views-from-js)

Limitations
-----------

[#](#limitations)

Mobile limitations:

* Multi-view mode is not supported (multi-engine only).* Packing multiple Flutter libraries into an application isn't supported.* Plugins that don't support `FlutterPlugin` might have unexpected behaviors if they make assumptions that are untenable in add-to-app (such as assuming that a Flutter `Activity` is always present).* On Android, the Flutter module only supports AndroidX applications.

Web limitations:

* Multi-engine mode is not supported (multi-view only).* There's no way to completely "shutdown" the Flutter engine. The app can remove all the [FlutterView](https://api.flutter.dev/flutter/dart-ui/FlutterView-class.html) objects and make sure all data is garbage collected using normal Dart concepts. However, the engine will remain warmed up, even if it's not rendering anything.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/index.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/index.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/add-to-app/index.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/index.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   