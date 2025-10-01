ThemeData's accent properties have been deprecated
==================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [ThemeData's accent properties have been deprecated](/release/breaking-changes/theme-data-accent-properties)

Summary
-------

[#](#summary)

The ThemeData [accentColor](https://api.flutter.dev/flutter/material/ThemeData/accentColor.html), [accentColorBrightness](https://api.flutter.dev/flutter/material/ThemeData/accentColorBrightness.html), [accentIconTheme](https://api.flutter.dev/flutter/material/ThemeData/accentIconTheme.html) and [accentTextTheme](https://api.flutter.dev/flutter/material/ThemeData/accentTextTheme.html) properties have been deprecated.

The [Material Design spec](https://m3.material.io/styles/color) no longer specifies or uses an "accent" color for the Material components. The default values for component colors are derived from the overall theme's [color scheme](https://api.flutter.dev/flutter/material/ThemeData/colorScheme.html). The `ColorScheme`'s [secondary color](https://api.flutter.dev/flutter/material/ColorScheme/secondary.html) is now typically used instead of `accentColor` and the [onSecondary color](https://api.flutter.dev/flutter/material/ColorScheme/onSecondary.html) is used when a contrasting color is needed.

Context
-------

[#](#context)

This was a small part of the [Material Theme System Updates](/go/material-theme-system-updates) project.

As of Flutter 1.17, the ThemeData accent properties - accentColor, accentColorBrightness, accentIconTheme, and accentTextTheme - were no longer used by the Material library. They had been replaced by dependencies on the theme's [`colorScheme`](https://api.flutter.dev/flutter/material/ThemeData/colorScheme.html) and [`textTheme`](https://api.flutter.dev/flutter/material/ThemeData/textTheme.html) properties as part of the long-term goal of making the default configurations of the material components depend almost exclusively on these two properties.

The motivation for these changes is to make the theme system easier to understand and use. The default colors for all components are to be defined by the components themselves and based on the color scheme. The defaults for specific component types can be overridden with component-specific themes like [`FloatingActionButtonThemeData`](https://api.flutter.dev/flutter/material/FloatingActionButtonThemeData-class.html) or [`CheckBoxTheme`](https://api.flutter.dev/flutter/material/CheckboxTheme-class.html). Previously, properties like accentColor were used by a handful of component types and only in some situations, which made it difficult to understand the implications of overriding them.

Description of change
---------------------

[#](#description-of-change)

The ThemeData accentColor, accentColorBrightness, accentIconTheme and accentTextTheme properties have been deprecated because the Material library no longer uses them.

Migration guide
---------------

[#](#migration-guide)

### Application theme

[#](#application-theme)

[`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html) values no longer need to specify accentColor, accentColorBrightness, accentIconTheme, or accentTextTheme.

To configure the appearance of the material components in about the same way as before, specify the color scheme's secondary color instead of accentColor.

Code before migration:

dart

```
MaterialApp(
  theme: ThemeData(accentColor: myColor),
  // ...
);
```

Code after migration:

dart

```
final ThemeData theme = ThemeData();
MaterialApp(
  theme: theme.copyWith(
    colorScheme: theme.colorScheme.copyWith(secondary: myColor),
  ),
  //...
)
```

### `accentColor`

[#](#accentcolor)

The closest backwards compatible [`ColorScheme`](https://api.flutter.dev/flutter/material/ColorScheme-class.html) color is [`ColorScheme.secondary`](https://api.flutter.dev/flutter/material/ColorScheme/secondary.html). To hew most closely to the latest Material Design guidelines one can substitute `ColorScheme.primary` instead. If a contrasting color is needed then use [`ColorScheme.onSecondary`](https://api.flutter.dev/flutter/material/ColorScheme/onSecondary.html).

Custom components that used to look up the theme's accentColor, can look up the `ColorScheme.secondary` instead.

Code before migration:

dart

```
Color myColor = Theme.of(context).accentColor;
```

Code after migration:

dart

```
Color myColor = Theme.of(context).colorScheme.secondary;
```

### `accentColorBrightness`

[#](#accentcolorbrightness)

The static [`ThemeData.estimateBrightnessForColor()`](https://api.flutter.dev/flutter/material/ThemeData/estimateBrightnessForColor.html) method can be used to compute the brightness of any color.

### `accentTextTheme`

[#](#accenttexttheme)

This was white [`TextStyle`](https://api.flutter.dev/flutter/painting/TextStyle-class.html)s for dark themes, black TextStyles for light themes. In most cases textTheme can be used instead. A common idiom was to refer to one TextStyle from accentTextTheme, since the text style's color was guaranteed to contrast well with the accent color (now `ColorScheme.secondaryColor`). To get the same result now, specify the text style's color as `ColorScheme.onSecondary`:

Code before migration:

dart

```
TextStyle style = Theme.of(context).accentTextTheme.headline1;
```

Code after migration:

dart

```
final ThemeData theme = Theme.of(context);
TextStyle style = theme.textTheme.headline1.copyWith(
  color: theme.colorScheme.onSecondary,
)
```

### `accentIconTheme`

[#](#accenticontheme)

This property had only been used to configure the color of icons within a [`FloatingActionButton`](https://api.flutter.dev/flutter/material/FloatingActionButton-class.html). It's now possible to configure the icon color directly or with the [`FloatingActionButtonThemeData`](https://api.flutter.dev/flutter/material/FloatingActionButtonThemeData-class.html). See [FloatingActionButton and ThemeData's accent properties](/release/breaking-changes/fab-theme-data-accent-properties).

Timeline
--------

[#](#timeline)

Landed in version: 2.3.0-0.1.pre  
 In stable release: 2.5

References
----------

[#](#references)

API documentation:

* [`ColorScheme`](https://api.flutter.dev/flutter/material/ColorScheme-class.html)* [`FloatingActionButton`](https://api.flutter.dev/flutter/material/FloatingActionButton-class.html)* [`FloatingActionButtonThemeData`](https://api.flutter.dev/flutter/material/FloatingActionButtonThemeData-class.html)* [`TextStyle`](https://api.flutter.dev/flutter/painting/TextStyle-class.html)* [`TextTheme`](https://api.flutter.dev/flutter/material/TextTheme-class.html)* [`Theme`](https://api.flutter.dev/flutter/material/Theme-class.html)* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)

Relevant issues:

* [Issue #56918](https://github.com/flutter/flutter/issues/56918)

Relevant PRs:

* [PR #81336](https://github.com/flutter/flutter/pull/81336)

Other:

* [Material Theme System Updates](/go/material-theme-system-updates)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/theme-data-accent-properties/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/theme-data-accent-properties.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/theme-data-accent-properties/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/theme-data-accent-properties.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/theme-data-accent-properties.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/theme-data-accent-properties/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/theme-data-accent-properties.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   