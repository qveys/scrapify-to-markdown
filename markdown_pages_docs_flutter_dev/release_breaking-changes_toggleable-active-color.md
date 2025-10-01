ThemeData's toggleableActiveColor property has been deprecated
==============================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [ThemeData's toggleableActiveColor property has been deprecated](/release/breaking-changes/toggleable-active-color)

Summary
-------

[#](#summary)

The Material widgets `Switch`, `SwitchListTile`, `Checkbox`, `CheckboxListTile`, `Radio`, `RadioListTile` now use `ColorScheme.secondary` color for their toggleable widget. `ThemeData.toggleableActiveColor` is deprecated and will eventually be removed.

Context
-------

[#](#context)

The migration of widgets that depend on `ThemeData.toggleableActiveColor` to `ColorScheme.secondary` caused the `toggleableActiveColor` property to be unnecessary. This property will eventually be removed, as per Flutter's [deprecation policy](/release/compatibility-policy#deprecation-policy).

Description of change
---------------------

[#](#description-of-change)

The widgets using `ThemeData.toggleableActiveColor` color for the active/selected state now use `ColorScheme.secondary`.

Migration guide
---------------

[#](#migration-guide)

Toggleable widgets' active/selected color can generally be customized in 3 ways:

1. Using ThemeData's `ColorScheme.secondary`.- Using components themes `SwitchThemeData`, `ListTileThemeData`, `CheckboxThemeData`, and `RadioThemeData`.- By customizing the widget's color properties.

Code before migration:

dart

```
MaterialApp(
  theme: ThemeData(toggleableActiveColor: myColor),
  // ...
);
```

Code after migration:

dart

```
final ThemeData theme = ThemeData();
MaterialApp(
  theme: theme.copyWith(
    switchTheme: SwitchThemeData(
      thumbColor: MaterialStateProperty.resolveWith<Color?>(
          (Set<MaterialState> states) {
        if (states.contains(MaterialState.disabled)) {
          return null;
        }
        if (states.contains(MaterialState.selected)) {
          return myColor;
        }
        return null;
      }),
      trackColor: MaterialStateProperty.resolveWith<Color?>(
          (Set<MaterialState> states) {
        if (states.contains(MaterialState.disabled)) {
          return null;
        }
        if (states.contains(MaterialState.selected)) {
          return myColor;
        }
        return null;
      }),
    ),
    radioTheme: RadioThemeData(
      fillColor: MaterialStateProperty.resolveWith<Color?>(
          (Set<MaterialState> states) {
        if (states.contains(MaterialState.disabled)) {
          return null;
        }
        if (states.contains(MaterialState.selected)) {
          return myColor;
        }
        return null;
      }),
    ),
    checkboxTheme: CheckboxThemeData(
      fillColor: MaterialStateProperty.resolveWith<Color?>(
          (Set<MaterialState> states) {
        if (states.contains(MaterialState.disabled)) {
          return null;
        }
        if (states.contains(MaterialState.selected)) {
          return myColor;
        }
        return null;
      }),
    ),
  ),
  //...
)
```

Timeline
--------

[#](#timeline)

In stable release: 3.7

References
----------

[#](#references)

API documentation:

* [`ThemeData.toggleableActiveColor`](https://api.flutter.dev/flutter/material/ThemeData/toggleableActiveColor.html)* [`ColorScheme.secondary`](https://api.flutter.dev/flutter/material/ColorScheme/secondary.html)

Relevant issues:

* [`Switch` widget color doesn't use `ColorScheme`](https://github.com/flutter/flutter/issues/93709)

Relevant PRs:

* [Deprecate `toggleableActiveColor`](https://github.com/flutter/flutter/pull/97972).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/toggleable-active-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/toggleable-active-color.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/toggleable-active-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/toggleable-active-color.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/toggleable-active-color.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/toggleable-active-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/toggleable-active-color.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   