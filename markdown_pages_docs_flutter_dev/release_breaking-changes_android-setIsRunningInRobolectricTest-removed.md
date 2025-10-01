FlutterMain.setIsRunningInRobolectricTest on Android removed
============================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [FlutterMain.setIsRunningInRobolectricTest on Android removed](/release/breaking-changes/android-setIsRunningInRobolectricTest-removed)

Summary
-------

[#](#summary)

If you write Java JUnit tests (such as Robolectric tests) against the Flutter engine's Java embedding and used the `FlutterMain.setIsRunningInRobolectricTest(true)` API, replace it with the following:

java

```
FlutterJNI mockFlutterJNI = mock(FlutterJNI.class);
FlutterInjector.setInstance(
        new FlutterInjector.Builder()
            .setFlutterLoader(new FlutterLoader(mockFlutterJNI))
            .build());
```

This should be very uncommon.

Context
-------

[#](#context)

The `FlutterMain` class itself is being deprecated and replaced with the `FlutterInjector` class. The `FlutterMain` class uses a number of static variables and functions than make it difficult to test. `FlutterMain.setIsRunningInRobolectricTest()` is one ad-hoc static mechanism to allow tests to run on the host machine on JVM without loading the `libflutter.so` native library (which can't be done on the host machine).

Rather than one-off solutions, all dependency injections needed for tests in Flutter's Android/Java engine embedding are now moved to the [`FlutterInjector`](https://cs.opensource.google/flutter/engine/+/master:shell/platform/android/io/flutter/FlutterInjector.java) class.

Within the `FlutterInjector` class, the `setFlutterLoader()` Builder function allows for control of how the [`FlutterLoader`](https://cs.opensource.google/flutter/engine/+/master:shell/platform/android/io/flutter/embedding/engine/loader/FlutterLoader.java) class locates and loads the `libflutter.so` library.

Description of change
---------------------

[#](#description-of-change)

This [engine commit](https://github.com/flutter/engine/commit/15f5696c4139a21e1fc54014ce17d01f6ad1737c#diff-599e1d64442183ead768757cca6805c3L154) removed the `FlutterMain.setIsRunningInRobolectricTest()` testing function; and the following [commit](https://github.com/flutter/engine/commit/15f5696c4139a21e1fc54014ce17d01f6ad1737c#diff-f928557f2d60773a8435366400fa42ed) added a `FlutterInjector` class to assist testing. [PR 20473](https://github.com/flutter/engine/pull/20473) further refactored `FlutterLoader` and `FlutterJNI` to allow for additional mocking and testing.

to allow for additional mocking/testing.

Migration guide
---------------

[#](#migration-guide)

Code before migration:

java

```
FlutterMain.setIsRunningInRobolectricTest(true);
```

Code after migration:

java

```
FlutterJNI mockFlutterJNI = mock(FlutterJNI.class);
FlutterInjector.setInstance(
        new FlutterInjector.Builder()
            .setFlutterLoader(new FlutterLoader(mockFlutterJNI))
            .build());
```

Timeline
--------

[#](#timeline)

Landed in version: 1.22.0-2.0.pre.133  
 In stable release: 2.0.0

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-setIsRunningInRobolectricTest-removed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-setIsRunningInRobolectricTest-removed.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-setIsRunningInRobolectricTest-removed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-setIsRunningInRobolectricTest-removed.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-setIsRunningInRobolectricTest-removed.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-setIsRunningInRobolectricTest-removed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-setIsRunningInRobolectricTest-removed.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   