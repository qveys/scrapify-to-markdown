Updated default text styles for menus
=====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Updated default text styles for menus](/release/breaking-changes/menus-text-style)

Summary
-------

[#](#summary)

The default text styles used for menus are updated to match the Material 3 specification.

Context
-------

[#](#context)

The default text style for `MenuItemButton` (a widget used in a `MenuBar`, and in a menu created with `MenuAnchor`), and `DropdownMenuEntry` (in the `DropdownMenu`) is updated to match the Material 3 specification.

Likewise, the default text style for the `DropdownMenu`s `TextField` is updated to match the Material 3 specification.

Description of change
---------------------

[#](#description-of-change)

The default text style for `MenuItemButton` (a widget used in a `MenuBar`, and in a menu created with `MenuAnchor`), and `DropdownMenuEntry` (in the `DropdownMenu`) is updated from `TextTheme.bodyLarge` to `TextTheme.labelLarge` for Material 3.

The default text style for the `DropdownMenu`s `TextField` is updated from `TextTheme.labelLarge` to `TextTheme.bodyLarge` for Material 3.

Migration guide
---------------

[#](#migration-guide)

A `MenuItemButton` for Material 3 uses `TextTheme.labelLarge` as the default text style. To use the previous default text style, set the `TextTheme.bodyLarge` text style in the `MenuItemButton.style` or `MenuButtonThemeData.style` properties.

Code before migration:

dart

```
MenuItemButton(
  child: Text(MenuEntry.about.label),
  onPressed: () => _activate(MenuEntry.about),
),
```

dart

```
menuButtonTheme: MenuButtonThemeData(
  style: MenuItemButton.styleFrom(
    /// ...
  ),
),
```

Code after migration:

dart

```
MenuItemButton(
  style: MenuItemButton.styleFrom(
    textStyle: Theme.of(context).textTheme.bodyLarge,
  ),
  child: Text(MenuEntry.about.label),
  onPressed: () => _activate(MenuEntry.about),
),
```

dart

```
menuButtonTheme: MenuButtonThemeData(
  style: MenuItemButton.styleFrom(
    textStyle: Theme.of(context).textTheme.bodyLarge,
  ),
),
```

A `DropdownMenu`'s `TextField` for Material 3 uses `TextTheme.bodyLarge` as the default text style. To use the previous default text style, set the `TextTheme.labelLarge` text style in the `DropdownMenu.textStyle` or `DropdownMenuThemeData.textStyle` properties.

Code before migration:

dart

```
DropdownMenu<ColorLabel>(
  initialSelection: ColorLabel.green,
  controller: colorController,
  label: const Text('Color'),
  dropdownMenuEntries: colorEntries,
  onSelected: (ColorLabel? color) {
    setState(() {
      selectedColor = color;
    });
  },
),
```

dart

```
dropdownMenuTheme: DropdownMenuThemeData(
  /// ...
),
```

Code after migration:

dart

```
DropdownMenu<ColorLabel>(
  textStyle: Theme.of(context).textTheme.labelLarge,
  initialSelection: ColorLabel.green,
  controller: colorController,
  label: const Text('Color'),
  dropdownMenuEntries: colorEntries,
  onSelected: (ColorLabel? color) {
    setState(() {
      selectedColor = color;
    });
  },
),
```

dart

```
dropdownMenuTheme: DropdownMenuThemeData(
  textStyle: TextStyle(
    fontStyle: FontStyle.italic,
    fontWeight: FontWeight.bold,
  ),
),
```

A `DropdownMenu`'s `DropdownMenuEntry` for Material 3 uses `TextTheme.labelLarge` as the default text style. To use the previous default text style, set the `TextTheme.bodyLarge` text style in the `DropdownMenuEntry.style` or `MenuButtonThemeData.style` properties.

Code before migration:

dart

```
DropdownMenuEntry<ColorLabel>(
  value: color,
  label: color.label,
),
```

dart

```
menuButtonTheme: MenuButtonThemeData(
  style: MenuItemButton.styleFrom(
    /// ...
  ),
),
```

Code after migration:

dart

```
DropdownMenuEntry<ColorLabel>(
  style: MenuItemButton.styleFrom(
    textStyle: Theme.of(context).textTheme.bodyLarge,
  ),
  value: color,
  label: color.label,
),
```

dart

```
menuButtonTheme: MenuButtonThemeData(
  style: MenuItemButton.styleFrom(
    textStyle: Theme.of(context).textTheme.bodyLarge,
  ),
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.14.0-11.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

API documentation:

* [`MenuBar`](https://api.flutter.dev/flutter/material/MenuBar-class.html)* [`MenuAnchor`](https://api.flutter.dev/flutter/material/MenuAnchor-class.html)* [`MenuItemButton`](https://api.flutter.dev/flutter/material/MenuItemButton-class.html)* [`MenuButtonTheme`](https://api.flutter.dev/flutter/material/MenuButtonTheme-class.html)* [`DropdownMenu`](https://api.flutter.dev/flutter/material/DropdownMenu-class.html)* [`DropdownMenuEntry`](https://api.flutter.dev/flutter/material/DropdownMenuEntry-class.html)* [`DropdownMenuTheme`](https://api.flutter.dev/flutter/material/DropdownMenuTheme-class.html)* [`TextTheme`](https://api.flutter.dev/flutter/material/TextTheme-class.html)

Relevant PRs:

* [Update default menu text styles for Material 3](https://github.com/flutter/flutter/pull/131930)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/menus-text-style/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/menus-text-style.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/menus-text-style/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/menus-text-style.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/menus-text-style.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/menus-text-style/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/menus-text-style.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   