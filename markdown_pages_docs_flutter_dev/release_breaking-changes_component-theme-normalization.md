Component theme normalization
=============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Component theme normalization](/release/breaking-changes/component-theme-normalization)

Summary
-------

[#](#summary)

`CardTheme`, `DialogTheme` and `TabBarTheme` were refactored to conform to Flutter's conventions for component themes. `CardThemeData`, `DialogThemeData`, and `TabBarThemeData` were added to define overrides for the defaults of the component visual properties. Releases of Flutter continue to normalize component themes like these for a more consistent theming experience in the material library.

Migration guide
---------------

[#](#migration-guide)

In `ThemeData`:

* The type of the `cardTheme` property has been changed from `CardTheme` to `CardThemeData`.* The type of the `dialogTheme` property has been changed from the `DialogTheme` to `DialogThemeData`.* The type of `tabBarTheme` property has been changed from `TabBarTheme` to `TabBarThemeData`.

The return type of the component theme `xTheme.of()` methods and `Theme.of().xTheme` have also changed to `xThemeData` accordingly.

Code before migration:

dart

```
final CardTheme cardTheme = Theme.of(context).cardTheme;
final CardTheme cardTheme = CardTheme.of(context);

final DialogTheme dialogTheme = Theme.of(context).dialogTheme;
final DialogTheme dialogTheme = DialogTheme.of(context);

final TabBarTheme tabBarTheme = Theme.of(context).tabBarTheme;
final TabBarTheme tabBarTheme = TabBarTheme.of(context);
```

Code after migration:

dart

```
final CardThemeData cardTheme = Theme.of(context).cardTheme;
final CardThemeData cardTheme = CardTheme.of(context);

final DialogThemeData dialogTheme = Theme.of(context).dialogTheme;
final DialogThemeData dialogTheme = DialogTheme.of(context);

final TabBarThemeData tabBarTheme = Theme.of(context).tabBarTheme;
final TabBarThemeData tabBarTheme = TabBarTheme.of(context);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.27.0-0.0.pre  
 Stable release: 3.27

References
----------

[#](#references)

API documentation:

* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)* [`CardTheme`](https://api.flutter.dev/flutter/material/CardTheme-class.html)* [`DialogTheme`](https://api.flutter.dev/flutter/material/DialogTheme-class.html)* [`TabBarTheme`](https://api.flutter.dev/flutter/material/TabBarTheme-class.html)

Relevant PRs:

* [Normalize ThemeData.cardTheme](https://github.com/flutter/flutter/pull/153254)* [Normalize ThemeData.dialogTheme](https://github.com/flutter/flutter/pull/155129)* [Normalize ThemeData.tabBarTheme](https://github.com/flutter/flutter/pull/156253)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/component-theme-normalization/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/component-theme-normalization/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-12-16. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/component-theme-normalization/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/component-theme-normalization.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   