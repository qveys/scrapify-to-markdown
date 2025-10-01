Removal of v1 Android embedding Java APIs
=========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Removal of v1 Android embedding Java APIs](/release/breaking-changes/v1-android-embedding)

Summary
-------

[#](#summary)

Android's v1 embedding has been removed in Flutter 3.29.0. This follows the deprecation described in [Android v1 embedding app and plugin creation deprecation](/release/breaking-changes/android-v1-embedding-create-deprecation). The following is a full list of classes removed.

text

```
io.flutter.app.FlutterActivity
io.flutter.app.FlutterActivityDelegate
io.flutter.app.FlutterActivityEvents
io.flutter.app.FlutterApplication
io.flutter.app.FlutterFragmentActivity
io.flutter.app.FlutterPlayStoreSplitApplication
io.flutter.app.FlutterPluginRegistry

io.flutter.embedding.engine.plugins.shim.ShimPluginRegistry
io.flutter.embedding.engine.plugins.shim.ShimRegistrar

io.flutter.view.FlutterMain
io.flutter.view.FlutterNativeView
io.flutter.view.FlutterView
```

If your project references any of the above classes, consult the following list for instructions on migration.

* `io.flutter.app.FlutterActivity` was replaced with `io.flutter.embedding.android.FlutterActivity`.* `io.flutter.app.FlutterActivityDelegate` was replaced with `io.flutter.embedding.android.FlutterActivityAndFragmentDelegate`.* `io.flutter.app.FlutterActivityEvents` was removed.* `io.flutter.app.FlutterApplication` was removed. Flutter projects with custom `Application` implementations should instead extend the base `android.app.Application`.* `io.flutter.app.FlutterFragmentActivity` was replaced with `io.flutter.embedding.android.FlutterFragmentActivity`.* `io.flutter.app.FlutterPlayStoreSplitApplication` was replaced with `io.flutter.embedding.android.FlutterPlayStoreSplitApplication`.* `io.flutter.app.FlutterPluginRegistry` was removed, as it only served to let plugins support apps using the v1 embedding.* `io.flutter.embedding.engine.plugins.shim.ShimPluginRegistry` was removed, as it only served to support let plugins support apps using the v1 embedding.* `io.flutter.embedding.engine.plugins.shim.ShimRegistrar` was removed, as it only served to support let plugins support apps using the v1 embedding.* `io.flutter.view.FlutterMain` was replaced by `io.flutter.embedding.engine.loader.FlutterLoader`.* `io.flutter.view.FlutterNativeView` was replaced by `io.flutter.embedding.android.FlutterView`.* `io.flutter.view.FlutterView` was replaced by `io.flutter.embedding.android.FlutterView`.

Plugin authors
--------------

[#](#plugin-authors)

Plugins should remove the `registerWith` method from their `FlutterPlugin` interface implementation:

java

```
public static void registerWith(@NonNull io.flutter.plugin.common.PluginRegistry.Registrar registrar);
```

For an example of this migration, check out the pull request to remove this method from the Flutter team-owned plugins: [flutter/packages#6494](https://github.com/flutter/packages/pull/6494).

Timeline
--------

[#](#timeline)

Landed in version: 3.28.0-0.1.pre  
 In stable release: 3.29

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/v1-android-embedding/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/v1-android-embedding.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/v1-android-embedding/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/v1-android-embedding.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-28. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/v1-android-embedding.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/v1-android-embedding/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/v1-android-embedding.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   