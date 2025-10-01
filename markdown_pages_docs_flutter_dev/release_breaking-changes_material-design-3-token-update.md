Material 3 tokens update in Flutter
===================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Material 3 tokens update in Flutter](/release/breaking-changes/material-design-3-token-update)

Summary
-------

[#](#summary)

The Material Design tokens updated the mapping of 4 color roles in light mode to be more visually appealing while retaining accessible contrast. Testing identified this change as [non-breaking](https://github.com/flutter/flutter/flutter/blob/master/docs/contributing/Tree-hygiene.md#1-determine-if-your-change-is-a-breaking-change) in Flutter, but some customers might notice this small change. The update affected the following color properties:

* `onPrimaryContainer` (Primary10 to Primary30)* `onSecondaryContainer` (Secondary10 to Secondary30)* `onTertiaryContainer` (Tertiary10 to Tertiary30)* `onErrorContainer` (Error10 to Error30)

Widgets that have been using these roles as their default values might look different.

Additionally, the Material 3 tokens updated the border color of chip widgets from `ColorScheme.outline` to `ColorScheme.outlineVariant` to improve visual hierarchy between chips and buttons. Chips (`Chip`, `ActionChip`, `ChoiceChip`, `FilterChip`, and `InputChip`) that have been using the chip border tokens may look different.

Migration guide
---------------

[#](#migration-guide)

The differences in the mappings of the color roles are small. Use `ColorScheme.copyWith` to revert to the original default colors:

Code before migration:

dart

```
final ColorScheme colors = ThemeData().colorScheme;
```

Code after migration:

dart

```
final ColorScheme colors = ThemeData().colorScheme.copyWith(
  onPrimaryContainer: const Color(0xFF21005D),
  onSecondaryContainer: const Color(0xFF1D192B),
  onTertiaryContainer: const Color(0xFF31111D),
  onErrorContainer: const Color(0xFF410E0B),
);
```

After applying the token update, the default border color of M3 chips looks lighter. Take `ActionChip` as an example:

Code before migration:

dart

```
final chip = ActionChip(
  label: const Text('action chip'),
  onPressed: () {},
);
```

Code after migration:

dart

```
final chip = ChipTheme(
  data: ChipThemeData(
    side: BorderSide(
      color: Theme.of(context).colorScheme.outline
    ),
  ),
  child: ActionChip(
    label: const Text('action chip'), 
    onPressed: () {}
  )
);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.26.0-0.0.pre  
 In stable release: 3.27

References
----------

[#](#references)

API documentation:

* [`ColorScheme`](https://api.flutter.dev/flutter/material/ColorScheme-class.html)* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)* [`Chip`](https://api.flutter.dev/flutter/material/Chip-class.html)

Relevant PRs:

* [Update tokens to v5.0.0](https://github.com/flutter/flutter/pull/153385)* [Update tokens to v6.1.0](https://github.com/flutter/flutter/pull/153722)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-design-3-token-update/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-design-3-token-update.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-design-3-token-update/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-design-3-token-update.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-12-16. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-design-3-token-update.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-design-3-token-update/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-design-3-token-update.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   