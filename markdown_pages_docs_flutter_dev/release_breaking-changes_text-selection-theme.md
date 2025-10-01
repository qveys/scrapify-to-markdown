TextSelectionTheme migration
============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [TextSelectionTheme migration](/release/breaking-changes/text-selection-theme)

Summary
-------

[#](#summary)

The `ThemeData` properties that controlled the look of selected text in Material widgets have been moved into their own `TextSelectionTheme`. These properties include `cursorColor`, `textSelectionColor`, and `textSelectionHandleColor`. The defaults for these properties have also been changed to match the Material Design specification.

Context
-------

[#](#context)

As part of the larger [Material Theme Updates](/go/material-theme-system-updates), we have introduced a new [Text Selection Theme](/go/text-selection-theme) used to specify the properties of selected text in `TextField` and `SelectableText` widgets. These replace several top-level properties of `ThemeData` and update their default values to match the Material Design specification. This document describes how applications can migrate to this new API.

Migration guide
---------------

[#](#migration-guide)

If you are currently using the following properties of `ThemeData`, you need to update them to use the new equivalent properties on `ThemeData.textSelectionTheme`:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Before After|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `ThemeData.cursorColor` `TextSelectionThemeData.cursorColor`| `ThemeData.textSelectionColor` `TextSelectionThemeData.selectionColor`| `ThemeData.textSelectionHandleColor` `TextSelectionThemeData.selectionHandleColor` | | | | | | | |

  

**Code before migration:**

dart

```
ThemeData(
  cursorColor: Colors.red,
  textSelectionColor: Colors.green,
  textSelectionHandleColor: Colors.blue,
)
```

**Code after migration:**

dart

```
ThemeData(
  textSelectionTheme: TextSelectionThemeData(
    cursorColor: Colors.red,
    selectionColor: Colors.green,
    selectionHandleColor: Colors.blue,
  )
)
```

**Default changes**

If you weren't using these properties explicitly, but depended on the previous default colors used for text selection you can add a new field to your `ThemeData` for your app to return to the old defaults as shown:

dart

```
// Old defaults for a light theme
ThemeData(
  textSelectionTheme: TextSelectionThemeData(
    cursorColor: const Color.fromRGBO(66, 133, 244, 1.0),
    selectionColor: const Color(0xff90caf9),
    selectionHandleColor: const Color(0xff64b5f6),
  )
)
```

dart

```
// Old defaults for a dark theme
ThemeData(
  textSelectionTheme: TextSelectionThemeData(
    cursorColor: const Color.fromRGBO(66, 133, 244, 1.0),
    selectionColor: const Color(0xff64ffda),
    selectionHandleColor: const Color(0xff1de9b6),
  )
)
```

If you are fine with the new defaults, but have failing golden file tests, you can update your master golden files using the following command:

```
flutter test --update-goldens
```

Timeline
--------

[#](#timeline)

Landed in version: 1.23.0-4.0.pre  
 In stable release: 2.0.0

References
----------

[#](#references)

API documentation:

* [`TextSelectionThemeData`](https://api.flutter.dev/flutter/material/TextSelectionThemeData-class.html)* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)

Relevant PRs:

* [PR 62014: TextSelectionTheme support](https://github.com/flutter/flutter/pull/62014)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-selection-theme/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-selection-theme.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-selection-theme/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-selection-theme.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-selection-theme.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-selection-theme/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-selection-theme.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   