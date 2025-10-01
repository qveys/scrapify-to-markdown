Component theme normalization updates
=====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Component theme normalization updates](/release/breaking-changes/component-theme-normalization-updates)

Summary
-------

[#](#summary)

`AppBarTheme`, `BottomAppBarTheme` and `InputDecorationTheme` were refactored to conform to Flutter's conventions for component themes. `AppBarThemeData`, `BottomAppBarThemeData` and `InputDecorationThemeData` were added to define overrides for the defaults of the component visual properties. Releases of Flutter continue to normalize component themes like these for a more consistent theming experience in the material library.

Migration guide
---------------

[#](#migration-guide)

In `ThemeData`:

* The type of the `appBarTheme` property has been changed from `AppBarTheme` to `AppBarThemeData`.* The type of `bottomAppBarTheme` property has been changed from `BottomAppBarTheme` to `BottomAppBarThemeData`.* The type of `inputDecorationTheme` property has been changed from `InputDecorationTheme` to `InputDecorationThemeData`.

The return type of the component theme `xTheme.of()` methods and `Theme.of().xTheme` have also changed to `xThemeData`.

In `DatePickerThemeData` and `TimePickerThemeData`, the type of the `inputDecorationTheme` property has been changed from `InputDecorationTheme` to `InputDecorationThemeData`.

Code before migration:

dart

```
final AppBarTheme appBarTheme = Theme.of(context).appBarTheme;
final AppBarTheme appBarTheme = AppBarTheme.of(context);

final BottomAppBarTheme bottomAppBarTheme = Theme.of(context).bottomAppBarTheme;
final BottomAppBarTheme bottomAppBarTheme = BottomAppBarTheme.of(context);

final InputDecorationTheme inputDecorationTheme = Theme.of(context).inputDecorationTheme;
final InputDecorationTheme inputDecorationTheme = InputDecorationTheme.of(context);
final InputDecorationTheme inputDecorationTheme = Theme.of(context).datePickerTheme.inputDecorationTheme;
final InputDecorationTheme inputDecorationTheme = Theme.of(context).timePickerTheme.inputDecorationTheme;
```

dart

```
final ThemeData theme = ThemeData(
  appBarTheme: AppBarTheme(),
  bottomAppBarTheme: BottomAppBarTheme(),
  inputDecorationTheme: InputDecorationTheme(),
);

final ThemeData theme = ThemeData().copyWith(
  appBarTheme: AppBarTheme(),
  bottomAppBarTheme: BottomAppBarTheme(),
  inputDecorationTheme: InputDecorationTheme(),
);

const DatePickerThemeData datePickerTheme = DatePickerThemeData(inputDecorationTheme: InputDecorationTheme());
const TimePickerThemeData timePickerTheme = TimePickerThemeData(inputDecorationTheme: InputDecorationTheme());
```

Code after migration:

dart

```
final AppBarThemeData appBarTheme = Theme.of(context).appBarTheme;
final AppBarThemeData appBarTheme = AppBarTheme.of(context);

final BottomAppBarThemeData bottomAppBarTheme = Theme.of(context).bottomAppBarTheme;
final BottomAppBarThemeData bottomAppBarTheme = BottomAppBarTheme.of(context);

final InputDecorationThemeData inputDecorationTheme = Theme.of(context).inputDecorationTheme;
final InputDecorationThemeData inputDecorationTheme = InputDecorationTheme.of(context);
final InputDecorationThemeData inputDecorationTheme = Theme.of(context).datePickerTheme.inputDecorationTheme;
final InputDecorationThemeData inputDecorationTheme = Theme.of(context).timePickerTheme.inputDecorationTheme;
```

dart

```
final ThemeData theme = ThemeData(
  appBarTheme: AppBarThemeData(),
  bottomAppBarTheme: BottomAppBarThemeData(),
  inputDecorationTheme: InputDecorationThemeData(),
);

final ThemeData theme = ThemeData().copyWith(
  appBarTheme: AppBarThemeData(),
  bottomAppBarTheme: BottomAppBarThemeData(),
  inputDecorationTheme: InputDecorationThemeData(),
);

const DatePickerThemeData datePickerTheme = DatePickerThemeData(inputDecorationTheme: InputDecorationThemeData());
const TimePickerThemeData timePickerTheme = TimePickerThemeData(inputDecorationTheme: InputDecorationThemeData());
```

Timeline
--------

[#](#timeline)

Landed in version: 3.33.0-1.0.pre through 3.35.0-0.0.pre  
 Stable release: 3.35

References
----------

[#](#references)

API documentation:

* [`AppBarTheme`](https://api.flutter.dev/flutter/material/AppBarTheme-class.html)* [`BottomAppBarTheme`](https://api.flutter.dev/flutter/material/BottomAppBarTheme-class.html)* [`InputDecorationTheme`](https://api.flutter.dev/flutter/material/InputDecorationTheme-class.html)

Relevant PRs:

* [Normalize ThemeData.appBarTheme](https://github.com/flutter/flutter/pull/169130)* [Normalize ThemeData.bottomAppBarTheme](https://github.com/flutter/flutter/pull/168586)* [Normalize InputDecorationTheme](https://github.com/flutter/flutter/pull/168981)* [Apply normalization to TimePickerThemeData.inputDecorationTheme](https://github.com/flutter/flutter/pull/171584)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/component-theme-normalization-updates/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization-updates.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/component-theme-normalization-updates/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization-updates.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization-updates.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/component-theme-normalization-updates/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization-updates.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   