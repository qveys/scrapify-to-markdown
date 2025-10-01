Nullable CupertinoThemeData.brightness
======================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Nullable CupertinoThemeData.brightness](/release/breaking-changes/nullable-cupertinothemedata-brightness)

Summary
-------

[#](#summary)

[`CupertinoThemeData.brightness`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/brightness.html) is now nullable.

Context
-------

[#](#context)

[`CupertinoThemeData.brightness`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/brightness.html) is now used to override `MediaQuery.platformBrightness` for Cupertino widgets. Before this change, the [`CupertinoThemeData.brightness`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/brightness.html) getter returned `Brightness.light` when it was set to null.

Description of change
---------------------

[#](#description-of-change)

Previously [`CupertinoThemeData.brightness`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/brightness.html) was implemented as a getter:

dart

```
Brightness get brightness => _brightness ?? Brightness.light;
final Brightness _brightness;
```

It is now a stored property:

dart

```
final Brightness brightness;
```

Migration guide
---------------

[#](#migration-guide)

Generally [`CupertinoThemeData.brightness`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/brightness.html) is rarely useful outside of the Flutter framework. To retrieve the brightness for Cupertino widgets, now use [`CupertinoTheme.brightnessOf`](https://api.flutter.dev/flutter/cupertino/CupertinoTheme/brightnessOf.html) instead.

With this change, it is now possible to override `CupertinoThemeData.brightness` in a `CupertinoThemeData` subclass to change the brightness override. For example:

dart

```
class AlwaysDarkCupertinoThemeData extends CupertinoThemeData {
  Brightness brightness => Brightness.dark;
}
```

When a `CupertinoTheme` uses the above `CupertinoThemeData`, dark mode is enabled for all its Cupertino descendants that are affected by this `CupertinoTheme`.

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

Design doc:

* [Make `CupertinoThemeData.brightness nullable`](/go/nullable-cupertinothemedata-brightness)

API documentation:

* [`CupertinoThemeData.brightness`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/brightness.html)

Relevant issue:

* [Issue 47255](https://github.com/flutter/flutter/issues/47255)

Relevant PR:

* [Let material `ThemeData` dictate brightness if `cupertinoOverrideTheme.brightness` is null](https://github.com/flutter/flutter/pull/47249)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/nullable-cupertinothemedata-brightness/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/nullable-cupertinothemedata-brightness.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/nullable-cupertinothemedata-brightness/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/nullable-cupertinothemedata-brightness.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/nullable-cupertinothemedata-brightness.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/nullable-cupertinothemedata-brightness/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/nullable-cupertinothemedata-brightness.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   