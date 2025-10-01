Flutter's build modes
=====================

1. [Testing & debugging](/testing) chevron\_right- [Flutter's build modes](/testing/build-modes)

The Flutter tooling supports three modes when compiling your app, and a headless mode for testing. You choose a compilation mode depending on where you are in the development cycle. Are you debugging your code? Do you need profiling information? Are you ready to deploy your app?

A quick summary for when to use which mode is as follows:

* Use [debug](#debug) mode during development, when you want to use [hot reload](/tools/hot-reload).* Use [profile](#profile) mode when you want to analyze performance.* Use [release](#release) mode when you are ready to release your app.

The rest of the page details these modes.

* To learn about the headless testing mode, refer to the engine wiki's docs on [Flutter's build modes](https://github.com/flutter/flutter/blob/main/engine/src/flutter/docs/Flutter's-modes.md).* To learn how to detect the build mode, check out the [Check for Debug/Release Mode in Flutter Apps](https://retroportalstudio.medium.com/check-for-debug-release-mode-in-flutter-apps-d8d545f20da3) blog post.

Debug
-----

[#](#debug)

In *debug mode*, the app is set up for debugging on the physical device, emulator, or simulator.

Debug mode for mobile apps mean that:

* [Assertions](https://dart.dev/language/error-handling#assert) are enabled.* Service extensions are enabled.* Compilation is optimized for fast development and run cycles (but not for execution speed, binary size, or deployment).* Debugging is enabled, and tools supporting source level debugging (such as [DevTools](/tools/devtools)) can connect to the process.

Debug mode for a web app means that:

* The build is *not* minified and tree shaking has *not* been performed.* The app is compiled with the [dartdevc](https://dart.dev/tools/dartdevc) compiler for easier debugging.

By default, `flutter run` compiles to debug mode. Your IDE supports this mode. Android Studio, for example, provides a **Run > Debug...** menu option, as well as a green bug icon overlaid with a small triangle on the project page.

*info* Note

* Hot reload works *only* in debug mode.* The emulator and simulator execute *only* in debug mode.* Application performance can be janky in debug mode. Measure performance in [profile](#profile) mode on an actual device.

Release
-------

[#](#release)

Use *release mode* for deploying the app, when you want maximum optimization and minimal footprint size. For mobile, release mode (which is not supported on the simulator or emulator), means that:

* Assertions are disabled.* Debugging information is stripped out.* Debugging is disabled.* Compilation is optimized for fast startup, fast execution, and small package sizes.* Service extensions are disabled.

Release mode for a web app means that:

* The build is minified and tree shaking has been performed.* The app is compiled with the [dart2js](https://dart.dev/tools/dart2js) compiler for best performance.

The command `flutter run --release` compiles to release mode. Your IDE supports this mode. Android Studio, for example, provides a **Run > Run...** menu option, as well as a triangular green run button icon on the project page. You can compile to release mode for a specific target with `flutter build <target>`. For a list of supported targets, use `flutter help build`.

For more information, see the docs on releasing [iOS](/deployment/ios) and [Android](/deployment/android) apps.

Profile
-------

[#](#profile)

In *profile mode*, some debugging ability is maintained—enough to profile your app's performance. Profile mode is disabled on the emulator and simulator, because their behavior is not representative of real performance. On mobile, profile mode is similar to release mode, with the following differences:

* Some service extensions, such as the one that enables the performance overlay, are enabled.* Tracing is enabled, and tools supporting source-level debugging (such as [DevTools](/tools/devtools)) can connect to the process.

Profile mode for a web app means that:

* The build is *not* minified but tree shaking has been performed.* The app is compiled with the [dart2js](https://dart.dev/tools/dart2js) compiler.* DevTools can't connect to a Flutter web app running in profile mode. Use Chrome DevTools to [generate timeline events](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/performance-reference) for a web app.

Your IDE supports this mode. Android Studio, for example, provides a **Run > Profile...** menu option. The command `flutter run --profile` compiles to profile mode.

*info* Note

Use the [DevTools](/tools/devtools) suite to profile your app's performance.

For more information on the build modes, see [Flutter's build modes](https://github.com/flutter/flutter/blob/main/engine/src/flutter/docs/Flutter's-modes.md).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/build-modes/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/build-modes.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/build-modes/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/build-modes.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/testing/build-modes.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/build-modes/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/build-modes.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   