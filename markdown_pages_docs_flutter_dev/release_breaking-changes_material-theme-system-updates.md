Material Theme System Updates
=============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Material Theme System Updates](/release/breaking-changes/material-theme-system-updates)

Summary
-------

[#](#summary)

`CardTheme`, `DialogTheme` and `TabBarTheme` were refactored to conform to Flutter's conventions for component themes. `CardThemeData`, `DialogThemeData` and `TabBarThemeData` were added to define overrides for the defaults of the component visual properties.

During card theme normalization, the type of `ThemeData.cardTheme` is changed to `Object?` to accept both `CardTheme` and `CardThemeData`, in order to have a smooth transition for the breaking changes. The same approach was used for `dialogTheme` and `tabBarTheme`.

To complete the transition and fully conform to the `ThemeData` convention, the type of `ThemeData.cardTheme` has been changed to `CardThemeData?`; the type of `ThemeData.dialogTheme` has been changed to `DialogThemeData?`; and the type of `ThemeData.tabBarTheme` has been changed to `TabBarThemeData?`.

Migration guide
---------------

[#](#migration-guide)

Previously, the type of `ThemeData.cardTheme` was `Object?` to accept both `CardTheme` and `CardThemeData`. Now that the type has been changed to `CardThemeData?`, a migration is required if `ThemeData.cardTheme` is used. Similarly, the types of `ThemeData.dialogTheme` and `ThemeData.tabBarTheme` should be migrated to `DialogThemeData` and `TabBarThemeData`, respectively.

Code before migration:

dart

```
final ThemeData theme = ThemeData(
    cardTheme: CardTheme(),
    dialogTheme: DialogTheme(),
    tabBarTheme: TabBarTheme(),
);
```

Code after migration:

dart

```
final ThemeData theme = ThemeData(
    cardTheme: CardThemeData(),
    dialogTheme: DialogThemeData(),
    tabBarTheme: TabBarThemeData(),
);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.31.0-0.0.pre  
 In stable release: 3.32

References
----------

[#](#references)

API documentation:

* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)* [`CardTheme`](https://api.flutter.dev/flutter/material/CardTheme-class.html)* [`DialogTheme`](https://api.flutter.dev/flutter/material/DialogTheme-class.html)* [`TabBarTheme`](https://api.flutter.dev/flutter/material/TabBarTheme-class.html)

Relevant PRs:

* [Change cardTheme, dialogTheme, and tabBarTheme type to xxxThemeData](https://github.com/flutter/flutter/pull/157292)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-theme-system-updates/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-theme-system-updates.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-theme-system-updates/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-theme-system-updates.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-theme-system-updates.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-theme-system-updates/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-theme-system-updates.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   