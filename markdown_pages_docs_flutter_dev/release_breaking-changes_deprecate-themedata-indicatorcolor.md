Deprecate `ThemeData.indicatorColor` in favor of `TabBarThemeData.indicatorColor`
=================================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecate `ThemeData.indicatorColor` in favor of `TabBarThemeData.indicatorColor`](/release/breaking-changes/deprecate-themedata-indicatorcolor)

Summary
-------

[#](#summary)

The [`ThemeData.indicatorColor`](https://api.flutter.dev/flutter/material/ThemeData/indicatorColor.html) parameter was deprecated in favor of the [`TabBarThemeData.indicatorColor`](https://api.flutter.dev/flutter/material/TabBarThemeData/indicatorColor.html) parameter.

Context
-------

[#](#context)

The defaults for the [`TabBar`](https://api.flutter.dev/flutter/material/TabBar-class.html) widget can be overridden with a component-specific theme like [`TabBarThemeData`](https://api.flutter.dev/flutter/material/TabBarThemeData-class.html). Previously, the `ThemeData.indicatorColor` parameter was used to override the default tab bar indicator color in Material Design 2, which was made redundant by [`TabBarThemeData`](https://api.flutter.dev/flutter/material/TabBarThemeData-class.html).

Description of change
---------------------

[#](#description-of-change)

The [`ThemeData.indicatorColor`](https://api.flutter.dev/flutter/material/ThemeData/indicatorColor.html) is deprecated in favor of a component-specific theme. Use [`TabBarThemeData`](https://api.flutter.dev/flutter/material/TabBarThemeData-class.html) to override the default indicator color.

Migration guide
---------------

[#](#migration-guide)

Replace [`ThemeData.indicatorColor`](https://api.flutter.dev/flutter/material/ThemeData/indicatorColor.html) with [`TabBarThemeData.indicatorColor`](https://api.flutter.dev/flutter/material/TabBarThemeData/indicatorColor.html) to override the default tab bar indicator color when [`ThemeData.useMaterial3`](https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html) flag is set to `false`.

Code before migration:

dart

```
theme: ThemeData(
  indicatorColor: Colors.red,
  useMaterial3: false,
),
```

Code after migration:

dart

```
theme: ThemeData(
  tabBarTheme: const TabBarThemeData(indicatorColor: Colors.red),
  useMaterial3: false,
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.30.0-0.0.pre  
 In stable release: 3.32

References
----------

[#](#references)

API documentation:

* [`ThemeData.indicatorColor`](https://api.flutter.dev/flutter/material/ThemeData/indicatorColor.html)* [`ThemeData.useMaterial3`](https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html)* [`TabBarThemeData.indicatorColor`](https://api.flutter.dev/flutter/material/TabBarThemeData/indicatorColor.html)* [`TabBarThemeData`](https://api.flutter.dev/flutter/material/TabBarThemeData-class.html)* [`TabBar`](https://api.flutter.dev/flutter/material/TabBar-class.html)

Relevant issues:

* [Issue #91772](https://github.com/flutter/flutter/issues/91772)

Relevant PRs:

* [Deprecate `ThemeData.indicatorColor` in favor of `TabBarThemeData.indicatorColor`](https://github.com/flutter/flutter/pull/160024)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-themedata-indicatorcolor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-indicatorcolor.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-themedata-indicatorcolor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-indicatorcolor.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-indicatorcolor.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-themedata-indicatorcolor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-indicatorcolor.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   