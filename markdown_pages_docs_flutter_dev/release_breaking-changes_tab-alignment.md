Customizing tabs alignment using the new TabBar.tabAlignment property
=====================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Customizing tabs alignment using the new TabBar.tabAlignment property](/release/breaking-changes/tab-alignment)

Summary
-------

[#](#summary)

Using `TabBar.tabAlignment` to customize the alignment of tabs in a `TabBar`.

Context
-------

[#](#context)

The `TabBar.tabAlignment` property sets where a Material 3 `TabBar` places tabs. The `TabAlignment` enum has the following values:

* `TabAlignment.start`: Aligns the tabs to the start of the scrollable `TabBar`.* `TabAlignment.startOffset`: Aligns the tabs to the start of the scrollable `TabBar` with an offset of `52.0` pixels.* `TabAlignment.center`: Aligns the tabs to the center of the `TabBar`.* `TabAlignment.fill`: Aligns the tabs to the start and stretches the tabs to fill the fixed `TabBar`.

The scrollable `TabBar` supports the following alignments:

* `TabAlignment.start`* `TabAlignment.startOffset`* `TabAlignment.center`

The fixed `TabBar` supports the following alignments:

* `TabAlignment.fill`* `TabAlignment.center`

When you set `ThemeData.useMaterial3` to `true`, a scrollable `TabBar` aligns tabs as `TabAlignment.startOffset` by default. To change this alignment, set the `TabBar.tabAlignment` property for widget level customization. Or, set the `TabBarThemeData.tabAlignment` property for app level customization.

Description of change
---------------------

[#](#description-of-change)

When you set `TabBar.isScrollable` and `ThemeData.useMaterial3` to `true`, the tabs in a scrollable `TabBar` defaults to `TabAlignment.startOffset`. This aligns the tabs to the start of the scrollable `TabBar` with an offset of `52.0` pixels. This changes the previous behavior. The tabs were aligned to the start of the scrollable `TabBar` when more tabs needed to display than the width allowed.

Migration guide
---------------

[#](#migration-guide)

A Material 3 scrollable `TabBar` uses `TabAlignment.startOffset` as the default tab alignment. This aligns the tabs to the start of the scrollable `TabBar` with an offset of `52.0` pixels.

To align the tabs to the start of the scrollable `TabBar`, set `TabBar.tabAlignment` to `TabAlignment.start`. This change also removed the `52.0` pixel offset. The following code snippets show how to use `TabBar.tabAlignment` to align tabs to the start of the scrollable `TabBar`:

Code before migration:

dart

```
TabBar(
  isScrollable: true,
  tabs: List<Tab>.generate(
    count,
    (int index) => Tab(text: 'Tab $index'),
  ).toList(),
);
```

Code after migration:

dart

```
TabBar(
  tabAlignment: TabAlignment.start,
  isScrollable: true,
  tabs: List<Tab>.generate(
    count,
    (int index) => Tab(text: 'Tab $index'),
  ).toList(),
);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.13.0-17.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

API documentation:

* [`TabBar`](https://api.flutter.dev/flutter/material/TabBar-class.html)* [`TabBar.tabAlignment`](https://api.flutter.dev/flutter/material/TabBar/tabAlignment.html)* [`TabAlignment`](https://api.flutter.dev/flutter/material/TabAlignment.html)

Relevant PRs:

* [Introduce `TabBar.tabAlignment`](https://github.com/flutter/flutter/pull/125036)* [Fix Material 3 Scrollable `TabBar`](https://github.com/flutter/flutter/pull/131409)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/tab-alignment/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tab-alignment.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/tab-alignment/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tab-alignment.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tab-alignment.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/tab-alignment/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tab-alignment.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   