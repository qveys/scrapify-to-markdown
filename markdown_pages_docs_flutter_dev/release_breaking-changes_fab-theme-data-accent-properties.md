FloatingActionButton and ThemeData's accent properties
======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [FloatingActionButton and ThemeData's accent properties](/release/breaking-changes/fab-theme-data-accent-properties)

Summary
-------

[#](#summary)

Removed Flutter's `FloatingActionButton` (FAB) dependency on `ThemeData` accent properties.

Context
-------

[#](#context)

This was a small part of the [Material Theme System Updates](/go/material-theme-system-updates) project.

Previously, the `ThemeData` [`accentIconTheme`](https://api.flutter.dev/flutter/material/ThemeData/accentIconTheme.html) property was only used by [`FloatingActionButton`](https://api.flutter.dev/flutter/material/FloatingActionButton/foregroundColor.html) to determine the default color of the text or icons that appeared within the button.

`FloatingActionButton` also used the `ThemeData accentTextTheme` property, however this dependency was undocumented and unnecessary.

Both of these dependencies were confusing. For example if one configured the `Theme`'s `accentIconTheme` to change the appearance of all floating action buttons, it was difficult to know what other components would be affected, or might be affected in the future.

The [Material Design spec](https://m3.material.io/styles/color) no longer includes an "accent" color. The `ColorScheme`'s [secondary color](https://m3.material.io/styles/color/the-color-system/color-roles#904230ec-ae73-4f0f-8bff-4024a036ca66) is now used instead.

Previously, applications could configure the color of text and icons within `FloatingActionButtons` with the widget's `foregroundColor` property, or with the `FloatingActionButtonTheme`'s `foregroundColor`. If neither `foregroundColor` property was specified, the foreground color defaulted to the `accentIconTheme`'s color.

With this change, the default behavior uses the color scheme's `onSecondary` color instead.

Description of change
---------------------

[#](#description-of-change)

Previously, the `accentIconTheme` provided a default for the `FloatingActionButton`'s `foregroundColor` property:

dart

```
    final Color foregroundColor = this.foregroundColor
      ?? floatingActionButtonTheme.foregroundColor
      ?? theme.accentIconTheme.color // To be removed.
      ?? theme.colorScheme.onSecondary;
```

Apps that configure their theme's `accentIconTheme` to effectively configure the `foregroundColor` of all floating action buttons, can get the same effect by configuring the `foregroundColor` of their theme's `floatingActionButtonTheme`.

The `FloatingActionButton`'s `foregroundColor` is now used to configure the `textStyle` of the `RawMaterialButton` created by `FloatingActionButton`. Previously, this text style was based on the button style of `ThemeData.accentTextTheme`:

dart

```
// theme.accentTextTheme becomes theme.textTheme
final TextStyle textStyle = theme.accentTextTheme.button.copyWith(
  color: foregroundColor,
  letterSpacing: 1.2,
);
```

Except in a case where an app has explicitly configured the `accentTextTheme` to take advantage of this undocumented dependency, this use of `accentTextTheme` is unnecessary. This change replaces this use of `accentTextTheme` with `textTheme`.

Migration guide
---------------

[#](#migration-guide)

This change occurred in two steps:

1. If the foreground of a `FloatingActionButton` is set to a non-default color, a warning is now printed.- The `accentIconTheme` dependency was removed. If you haven't already done so, migrate your apps per the pattern below.

To configure the `FloatingActionButton`'s `foregroundColor` for all FABs, you can configure the theme's `floatingActionButtonTheme` instead of its `accentIconTheme`.

Code before migration:

dart

```
MaterialApp(
  theme: ThemeData(
    accentIconTheme: IconThemeData(color: Colors.red),
  ),
)
```

Code after migration:

dart

```
MaterialApp(
  theme: ThemeData(
    floatingActionButtonTheme: FloatingActionButtonThemeData(
      foregroundColor: Colors.red,
    ),
  ),
)
```

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

Design doc:

* [Remove FAB Accent Theme Dependency](/go/remove-fab-accent-theme-dependency)

API documentation:

* [`FloatingActionButton`](https://api.flutter.dev/flutter/material/FloatingActionButton/foregroundColor.html)* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData/floatingActionButtonTheme.html)* [`FloatingActionButtonThemeData`](https://api.flutter.dev/flutter/material/FloatingActionButtonThemeData-class.html)

Relevant PRs:

* [Step 1 of 2](https://github.com/flutter/flutter/pull/48435) Warn about Flutter's FloatingActionButton dependency on ThemeData accent properties* [Step 2 of 2](https://github.com/flutter/flutter/pull/46923) Remove Flutter's FloatingActionButton dependency on ThemeData accent properties

Other:

* [Material Theme System Updates](/go/material-theme-system-updates)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/fab-theme-data-accent-properties/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/fab-theme-data-accent-properties.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/fab-theme-data-accent-properties/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/fab-theme-data-accent-properties.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/fab-theme-data-accent-properties.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/fab-theme-data-accent-properties/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/fab-theme-data-accent-properties.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   