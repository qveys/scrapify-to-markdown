Deprecate `ButtonBar` in favor of `OverflowBar`
===============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecate `ButtonBar` in favor of `OverflowBar`](/release/breaking-changes/deprecate-buttonbar)

Summary
-------

[#](#summary)

The `ButtonBar` widget was deprecated in favor of the more efficient `OverflowBar` widget. As a result, `ThemeData.buttonBarTheme` and `ButtonBarTheme` were also deprecated.

Context
-------

[#](#context)

The `ButtonBar` widget lays out its children in a row and in a column if there is not enough horizontal space. The `OverflowBar` widget does the same, but it's not tied to the Material library and is part of the core `widgets.dart` library.

Description of change
---------------------

[#](#description-of-change)

* Replace `ButtonBar` widget with `OverflowBar` widget.* By default, `ButtonBar` aligns its children to the end of the layout, while `OverflowBar` aligns its children to the start. To align the `OverflowBar` children to the end, set the `OverflowBar.alignment` property to `MainAxisAlignment.end`.* `ButtonBar.buttonPadding` provides spacing between buttons and padding around buttons. Replace it with `OverflowBar.spacing`, which provides spacing between buttons. Wrap the `OverflowBar` widget with `Padding` widget to provide padding around the buttons.* Replace `ButtonBar.overflowButtonSpacing` with `OverflowBar.overflowSpacing`, which provides spacing between buttons when the buttons are laid in a column when there is not enough horizontal space.* If it is specified, remove `ButtonBarThemeData` from `ThemeData`.

Migration guide
---------------

[#](#migration-guide)

Replace `ButtonBar` with `OverflowBar`, override the default alignment if necessary, replace `ButtonBar.buttonPadding` with `Padding` widget and `OverflowBar.spacing` for spacing between and around buttons, and replace `ButtonBar.overflowButtonSpacing` with `OverflowBar.overflowSpacing` for spacing between buttons when the buttons are laid in a column when there is not enough horizontal space.

Before:

dart

```
ButtonBar(
  buttonPadding: const EdgeInsets.all(8.0),
  overflowButtonSpacing: 8.0,
  children: <Widget>[
    TextButton(child: const Text('Button 1'), onPressed: () {}),
    TextButton(child: const Text('Button 2'), onPressed: () {}),
    TextButton(child: const Text('Button 3'), onPressed: () {}),
  ],
),
```

After:

dart

```
Padding(
  padding: const EdgeInsets.all(8.0),
  child: OverflowBar(
    alignment: MainAxisAlignment.end,
    spacing: 8.0,
    overflowSpacing: 8.0,
    children: <Widget>[
      TextButton(child: const Text('Button 1'), onPressed: () {}),
      TextButton(child: const Text('Button 2'), onPressed: () {}),
      TextButton(child: const Text('Button 3'), onPressed: () {}),
    ],
  ),
),
```

If you specify a `ThemeData.buttonBarTheme`, remove it and use the `OverflowBar` widget properties to customize the `OverflowBar` widget.

Before:

dart

```
ThemeData(
  buttonBarTheme: ButtonBarThemeData(
    alignment: MainAxisAlignment.center,
  ),
),
```

After:

dart

```
ThemeData(
  // ...
),
```

If you use the `ButtonBarTheme` widget, remove it and use the `OverflowBar` widget properties to customize the `OverflowBar` widget.

Before:

dart

```
ButtonBarTheme(
  data: ButtonBarThemeData(
    alignment: MainAxisAlignment.center,
  ),
  child: ButtonBar(
    children: <Widget>[
      // ...
    ],
  ),
),
```

After:

dart

```
OverflowBar(
  alignment: MainAxisAlignment.center,
  children: <Widget>[
    // ...
  ],
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.22.0-2.0.pre  
 In stable release: 3.24.0

References
----------

[#](#references)

API documentation:

* [`OverflowBar`](https://api.flutter.dev/flutter/widgets/OverflowBar-class.html)* [`ButtonBar`](https://api.flutter.dev/flutter/material/ButtonBar-class.html)

Relevant issues:

* [Issue #127955](https://github.com/flutter/flutter/issues/127955)

Relevant PRs:

* [Deprecate `ButtonBar`, `ButtonBarThemeData`, and `ThemeData.buttonBarTheme`](https://github.com/flutter/flutter/pull/145523)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-buttonbar/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-buttonbar.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-buttonbar/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-buttonbar.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-08-06. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-buttonbar.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-buttonbar/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-buttonbar.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   