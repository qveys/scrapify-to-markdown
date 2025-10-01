Migration guide for material localized strings
==============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for material localized strings](/release/breaking-changes/material-localized-strings)

Summary
-------

[#](#summary)

`ReorderableListView`'s localized strings were moved from material localizations to widgets localizations. These strings were deprecated in material localizations.

Context
-------

[#](#context)

[`ReorderableListView`](https://api.flutter.dev/flutter/material/ReorderableListView-class.html) uses these strings to annotate its semantics actions. To apply the same annotations to [`ReorderableList`](https://api.flutter.dev/flutter/widgets/ReorderableList-class.html) and [`SliverReorderableList`](https://api.flutter.dev/flutter/widgets/SliverReorderableList-class.html), they need to access these strings from widgets library.

Description of change
---------------------

[#](#description-of-change)

The [`MaterialLocalizations`](https://api.flutter.dev/flutter/material/MaterialLocalizations-class.html) strings for `reorderItemToStart`, `reorderItemToEnd`, `reorderItemUp`, `reorderItemDown`, `reorderItemLeft`, and `reorderItemRight` are deprecated and replaced by the same strings in [`WidgetsLocalizations`](https://api.flutter.dev/flutter/widgets/WidgetsLocalizations-class.html).

Migration guide
---------------

[#](#migration-guide)

If you use these strings in your code, you can access them from `WidgetsLocalizations`instead.

Code before migration:

dart

```
MaterialLocalizations.of(context).reorderItemToStart;
```

Code after migration:

dart

```
WidgetsLocalizations.of(context).reorderItemToStart;
```

If you override `MaterialLocalizations` or `WidgetsLocalizations`, make sure to remove the translations from the `MaterialLocalizations` subclass and move them to the `WidgetsLocalizations` subclass.

Code before migration:

dart

```
class MaterialLocalizationsMyLanguage extends MaterialLocalizationsEn {
  // ...
  @override
  String get reorderItemRight => 'my translation';
}
```

Code after migration:

dart

```
class MaterialLocalizationsMyLanguage extends MaterialLocalizationsEn {
  // ...
}

class WidgetsLocalizationsMyLanguage extends WidgetsLocalizationsEn {
  // ...
  @override
  String get reorderItemRight => 'my translation';
}
```

Timeline
--------

[#](#timeline)

Landed in version: v3.10.0-2.0.pre  
 In stable release: 3.13.0

References
----------

[#](#references)

Relevant PR:

* [PR 124711](https://github.com/flutter/flutter/pull/124711): Deprecates string for ReorderableList in material\_localizations.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-localized-strings/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-localized-strings.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-localized-strings/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-localized-strings.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-localized-strings.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-localized-strings/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-localized-strings.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   