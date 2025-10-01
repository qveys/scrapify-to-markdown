Introduce new ColorScheme roles for Material 3
==============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Introduce new ColorScheme roles for Material 3](/release/breaking-changes/new-color-scheme-roles)

Summary
-------

[#](#summary)

New color roles in `ColorScheme` include seven tone-based surfaces and containers, and twelve accent colors for primary, secondary, and tertiary groups. This update deprecates three existing color roles: `background`, `onBackground`, and `surfaceVariant`. The `ColorScheme` constructed by the updated `ColorScheme.fromSeed` method now generates different values compared to the previous version, adapting to the Material Design 3 guidelines.

Background
----------

[#](#background)

The tone-based surface colors include:

* `surfaceBright`* `surfaceDim`* `surfaceContainer`* `surfaceContainerLow`* `surfaceContainerLowest`* `surfaceContainerHigh`* `surfaceContainerHighest`

These changes help eliminate the use of widgets' `surfaceTintColor`, and replaces the old opacity-based model that applied a tinted overlay on top of surfaces based on their elevation.

The default `surfaceTintColor` for all widgets is now `null` and their default background color is now based on the new tone-based surface colors.

`ColorScheme.fromSeed` has also been updated to use the latest algorithm from the [Material color utilities](https://pub.dev/packages/material_color_utilities) package. This change prevents the constructed `ColorScheme` from being too bright, even if the source color looks bright and had a high chroma (contained little black, white, and shades of grey).

Migration guide
---------------

[#](#migration-guide)

The differences caused by the updated `ColorScheme.fromSeed` and the new color roles should be small and acceptable. However, when providing a brighter seed color to `ColorScheme.fromSeed`, it might construct a relatively darker version of `ColorScheme`. To force the output to still be bright, set `dynamicSchemeVariant: DynamicSchemeVariant.fidelity` in `ColorScheme.fromSeed`. For example:

Code before migration:

dart

```
ColorScheme.fromSeed(
    seedColor: Color(0xFF0000FF), // Bright blue
)
```

Code after migration:

dart

```
ColorScheme.fromSeed(
    seedColor: Color(0xFF0000FF), // Bright blue
    dynamicSchemeVariant: DynamicSchemeVariant.fidelity,
)
```

Material Design 3 removes 3 colors.

To configure the appearance of the material components, `background` should be replaced with `surface`, `onBackground` should be replaced with `onSurface`, and `surfaceVariant` should be migrated to `surfaceContainerHighest`.

Code before migration:

dart

```
final ColorScheme colorScheme = ColorScheme();
MaterialApp(
  theme: ThemeData(
    //...
    colorScheme: colorScheme.copyWith(
      background: myColor1,
      onBackground: myColor2,
      surfaceVariant: myColor3,
    ),
  ),
  //...
)
```

Code after migration:

dart

```
final ColorScheme colorScheme = ColorScheme();
MaterialApp(
  theme: ThemeData(
    //...
    colorScheme: colorScheme.copyWith(
      surface: myColor1,
      onSurface: myColor2,
      surfaceContainerHighest: myColor3,
    ),
  ),
  //...
)
```

Custom components that used to look up `ColorScheme.background`, `ColorScheme.onBackground`, and `ColorScheme.surfaceVariant` can look up `ColorScheme.surface`, `ColorScheme.onSurface` and `ColorScheme.surfaceContainerHighest` instead.

Code before migration:

dart

```
Color myColor1 = Theme.of(context).colorScheme.background;
Color myColor2 = Theme.of(context).colorScheme.onBackground;
Color myColor3 = Theme.of(context).colorScheme.surfaceVariant;
```

Code after migration:

dart

```
Color myColor1 = Theme.of(context).colorScheme.surface;
Color myColor2 = Theme.of(context).colorScheme.onSurface;
Color myColor3 = Theme.of(context).colorScheme.surfaceContainerHighest;
```

Timeline
--------

[#](#timeline)

Landed in version: 3.21.0-4.0.pre  
 In stable release: 3.22.0

References
----------

[#](#references)

Relevant issues:

* [Support tone-based surface and surface container ColorScheme roles](https://github.com/flutter/flutter/issues/115912)* [Support fidelity variant for ColorScheme.fromSeed](https://github.com/flutter/flutter/issues/144649)

Relevant PRs:

* [Introduce tone-based surfaces and accent color add-ons - Part 1](https://github.com/flutter/flutter/pull/142654)* [Introduce tone-based surfaces and accent color add-ons - Part 2](https://github.com/flutter/flutter/pull/144273)* [Enhance ColorScheme.fromSeed with a new variant parameter](https://github.com/flutter/flutter/pull/144805)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/new-color-scheme-roles/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/new-color-scheme-roles.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/new-color-scheme-roles/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/new-color-scheme-roles.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-10-08. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/new-color-scheme-roles.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/new-color-scheme-roles/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/new-color-scheme-roles.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   