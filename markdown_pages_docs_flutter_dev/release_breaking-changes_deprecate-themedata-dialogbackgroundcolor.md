Deprecate `ThemeData.dialogBackgroundColor` in favor of `DialogThemeData.backgroundColor`
=========================================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecate `ThemeData.dialogBackgroundColor` in favor of `DialogThemeData.backgroundColor`](/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor)

Summary
-------

[#](#summary)

The [`ThemeData.dialogBackgroundColor`](https://api.flutter.dev/flutter/material/ThemeData/dialogBackgroundColor.html) parameter was deprecated in favor of the [`DialogThemeData.backgroundColor`](https://api.flutter.dev/flutter/material/DialogThemeData/backgroundColor.html) parameter.

Context
-------

[#](#context)

The defaults for the [`Dialog`](https://api.flutter.dev/flutter/material/Dialog-class.html) and [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html) widgets can be overridden with a component-specific theme like [`DialogThemeData`](https://api.flutter.dev/flutter/material/DialogThemeData-class.html). Previously, the `ThemeData.dialogBackgroundColor` parameter was used to override the default dialog background color, which was made redundant by [`DialogThemeData`](https://api.flutter.dev/flutter/material/DialogThemeData-class.html).

Description of change
---------------------

[#](#description-of-change)

The [`ThemeData.dialogBackgroundColor`](https://api.flutter.dev/flutter/material/ThemeData/dialogBackgroundColor.html) is deprecated in favor of a component-specific theme. Use [`DialogThemeData`](https://api.flutter.dev/flutter/material/DialogThemeData-class.html) to override the default background color.

Migration guide
---------------

[#](#migration-guide)

Replace [`ThemeData.dialogBackgroundColor`](https://api.flutter.dev/flutter/material/ThemeData/dialogBackgroundColor.html) with [`DialogThemeData.backgroundColor`](https://api.flutter.dev/flutter/material/DialogThemeData/backgroundColor.html) to override the default dialog background color.

Code before migration:

dart

```
theme: ThemeData(
  dialogBackgroundColor: Colors.orange,
),
```

Code after migration:

dart

```
theme: ThemeData(
  dialogTheme: const DialogThemeData(backgroundColor: Colors.orange),
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.28.0-0.1.pre  
 In stable release: 3.29

References
----------

[#](#references)

API documentation:

* [`ThemeData.dialogBackgroundColor`](https://api.flutter.dev/flutter/material/ThemeData/dialogBackgroundColor.html)* [`DialogThemeData.backgroundColor`](https://api.flutter.dev/flutter/material/DialogThemeData/backgroundColor.html)* [`DialogThemeData`](https://api.flutter.dev/flutter/material/DialogThemeData-class.html)* [`Dialog`](https://api.flutter.dev/flutter/material/Dialog-class.html)* [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html)

Relevant issues:

* [Issue #91772](https://github.com/flutter/flutter/issues/91772)

Relevant PRs:

* [Deprecate `ThemeData.dialogBackgroundColor` in favor of `DialogTheme.backgroundColor`](https://github.com/flutter/flutter/pull/155072)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-themedata-dialogbackgroundcolor.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   