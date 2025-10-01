Deprecated API removed after v3.16
==================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v3.16](/release/breaking-changes/3-16-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 3.16 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. To further aid your migration, check out this [quick reference sheet](/go/deprecations-removed-after-3-16).

Changes
-------

[#](#changes)

This section lists the deprecations by the package and affected class.

### Button `styleFrom` properties

[#](#button-stylefrom-properties)

Package: flutter Supported by Flutter Fix: yes

The `TextButton`, `ElevatedButton` and `OutlinedButton` widgets all have a static `styleFrom` method for generating the `ButtonStyle`. The following color properties of this method for each class were deprecated in v3.1:

* `TextButton.styleFrom`
  + `primary`+ `onSurface`* `ElevatedButton.styleFrom`
    + `primary`+ `onPrimary`+ `onSurface`* `OutlinedButton.styleFrom`
      + `primary`+ `onSurface`

These changes better aligned the API with updated Material Design specifications. The changes also provided more clarity in how the colors would be applied to the buttons, by replacing these properties with `backgroundColor`, `foregroundColor`, and `disabledForegroundColor`.

**Migration guide**

Code before migration:

dart

```
TextButton.styleFrom(
  primary: Colors.red,
  onSurface: Colors.black,
);
ElevatedButton.styleFrom(
  primary: Colors.red,
  onPrimary: Colors.blue,
  onSurface: Colors.black,
);
OutlinedButton.styleFrom(
  primary: Colors.red,
  onSurface: Colors.black,
);
```

Code after migration:

dart

```
TextButton.styleFrom(
  foregroundColor: Colors.red,
  disabledForegroundColor: Colors.black,
);
ElevatedButton.styleFrom(
  backgroundColor: Colors.red,
  foregroundColor: Colors.blue,
  disabledForegroundColor: Colors.black,
);
OutlinedButton.styleFrom(
  foregroundColor: Colors.red,
  disabledForegroundColor: Colors.black,
);
```

**References**

API documentation:

* [`TextButton`](https://api.flutter.dev/flutter/material/TextButton-class.html)* [`ElevatedButton`](https://api.flutter.dev/flutter/material/ElevatedButton-class.html)* [`OutlinedButton`](https://api.flutter.dev/flutter/material/OutlinedButton-class.html)* [`ButtonStyle`](https://api.flutter.dev/flutter/material/ButtonStyle-class.html)

Relevant PRs:

* Deprecated in [#105291](https://github.com/flutter/flutter/pull/105291)* Removed in [#139267](https://github.com/flutter/flutter/pull/139267)

---

### ThemeData.selectedRowColor

[#](#themedata-selectedrowcolor)

Package: flutter Supported by Flutter Fix: yes

The `selectedRowColor` property of `ThemeData` was deprecated in v3.1.

The property was no longer used by the framework, as widgets using it migrated to other component themes or no longer required it in the updated specification for Material Design.

**Migration guide**

Code before migration:

dart

```
ThemeData(
  // ...
  selectedRowColor: Colors.pink, // Would have no effect.  
);
```

Code after migration:

dart

```
ThemeData(
  // ...
  // Remove uses.  
);
```

**References**

API documentation:

* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)

Relevant PRs:

* Deprecated in [#109070](https://github.com/flutter/flutter/pull/109070)* Removed in [#139080](https://github.com/flutter/flutter/pull/139080)

---

### NavigatorState.focusScopeNode

[#](#navigatorstate-focusscopenode)

Package: flutter Supported by Flutter Fix: yes

The `focusScopeNode` property of `NavigatorState` was deprecated in v3.1.

This change was made to resolve several issues stemming around the `FocusScopeNode` introduced by the `Navigator`. Instead, the `FocusScope` was moved to enclose the topmost `Navigator` in a `WidgetsApp`. `NavigatorState` was changed to contain its own `FocusNode`, from where it can refer to its `FocusNode.enclosingScope` to access the correct `FocusScopeNode`.

**Migration guide**

Code before migration:

dart

```
Navigator.of(context).focusScopeNode;
```

Code after migration:

dart

```
Navigator.of(context).focusNode.enclosingScope!;
```

**References**

API documentation:

* [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html)* [`NavigatorState`](https://api.flutter.dev/flutter/widgets/NavigatorState-class.html)* [`FocusScope`](https://api.flutter.dev/flutter/widgets/FocusScope-class.html)* [`FocusScopeNode`](https://api.flutter.dev/flutter/widgets/FocusScopeNode-class.html)* [`FocusNode`](https://api.flutter.dev/flutter/widgets/FocusNode-class.html)

Relevant PRs:

* Deprecated in [#109702](https://github.com/flutter/flutter/pull/109702)* Removed in [#139260](https://github.com/flutter/flutter/pull/139260)

---

### PlatformMenuBar.body

[#](#platformmenubar-body)

Package: flutter Supported by Flutter Fix: yes

The `body` property of `PlatformMenuBar` was deprecated in v3.1.

This change was made to align `PlatformMenuBar` with other widgets in the framework, renaming it to `child`.

**Migration guide**

Code before migration:

dart

```
PlatformMenuBar(
  body: myWidget,
);
```

Code after migration:

dart

```
PlatformMenuBar(
  child: myWidget,
);
```

**References**

API documentation:

* [`PlatformMenuBar`](https://api.flutter.dev/flutter/widgets/PlatformMenuBar-class.html)

Relevant PRs:

* Deprecated in [#104565](https://github.com/flutter/flutter/pull/104565)* Removed in [#138509](https://github.com/flutter/flutter/pull/138509)

---

The [previously announced](https://groups.google.com/g/flutter-announce/c/DLnuqZo714o) deprecations for `TextTheme`, `WidgetInspectorService`, and `WidgetInspectorServiceExtensions` were not removed during this cycle. The `WidgetInspectorService` and `WidgetInspectorServiceExtensions` deprecation on `setPubRootDirectories` has been extended another year to allow IDEs and other customer to migrate. Expect the `TextTheme` deprecations to be removed in the next cycle, which will be announced again when it comes.

---

Timeline
--------

[#](#timeline)

In stable release: 3.19.0

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-16-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-16-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-16-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-16-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-16-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-16-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-16-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   