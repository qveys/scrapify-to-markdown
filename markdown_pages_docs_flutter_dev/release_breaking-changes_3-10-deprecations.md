Deprecated API removed after v3.10
==================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v3.10](/release/breaking-changes/3-10-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 3.10 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. A [quick reference sheet](/go/deprecations-removed-after-3-10) is available as well.

Changes
-------

[#](#changes)

This section lists the deprecations, listed by the package and affected class.

### ThemeData.fixTextFieldOutlineLabel

[#](#themedata-fixtextfieldoutlinelabel)

Package: flutter Supported by Flutter Fix: yes

`ThemeData.fixTextFieldOutlineLabel` was deprecated in v2.5. References to this property can be removed.

The `fixTextFieldOutlineLabel` was a temporary migration flag that allowed users to gracefully migrate to a new behavior rather than experiencing a hard break. Before deprecating, this property was transitioned to the new default from the fix to the label for text fields.

**Migration guide**

Code before migration:

dart

```
var themeData = ThemeData(
  fixTextFieldOutlineLabel: true,  
);
```

Code after migration:

dart

```
var themeData = ThemeData(
);
```

**References**

API documentation:

* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)

Relevant PRs:

* Deprecated in [#87281](https://github.com/flutter/flutter/pull/87281)* Removed in [#125893](https://github.com/flutter/flutter/pull/125893)

---

### OverscrollIndicatorNotification.disallowGlow

[#](#overscrollindicatornotification-disallowglow)

Package: flutter Supported by Flutter Fix: yes

`OverscrollIndicatorNotification.disallowGlow` was deprecated in v2.5. The replacement is the `disallowIndicator` method.

The `disallowIndicator` was created as a replacement for the original method with the introduction of the `StretchingOverscrollIndicator`. Previously, the `GlowingOverscrollIndicator` was the only kind to dispatch `OverscrollIndicatorNotification`s, and so the method was updated to better reflect multiple kinds of indicators.

**Migration guide**

Code before migration:

dart

```
bool _handleOverscrollIndicatorNotification(OverscrollIndicatorNotification notification) {
  notification.disallowGlow();
  return false;
}
```

Code after migration:

dart

```
bool _handleOverscrollIndicatorNotification(OverscrollIndicatorNotification notification) {
  notification.disallowIndicator();
  return false;
}
```

**References**

API documentation:

* [`OverscrollIndicatorNotification`](https://api.flutter.dev/flutter/widgets/OverscrollIndicatorNotification-class.html)* [`StretchingOverscrollIndicator`](https://api.flutter.dev/flutter/widgets/StretchingOverscrollIndicator-class.html)* [`GlowingOverscrollIndicator`](https://api.flutter.dev/flutter/widgets/GlowingOverscrollIndicator-class.html)

Relevant PRs:

* Deprecated in [#87839](https://github.com/flutter/flutter/pull/87839)* Removed in [#127042](https://github.com/flutter/flutter/pull/127042)

---

### ColorScheme primaryVariant & secondaryVariant

[#](#colorscheme-primaryvariant-secondaryvariant)

Package: flutter Supported by Flutter Fix: yes

`ColorScheme.primaryVariant` and `ColorScheme.secondaryVariant` were deprecated in v2.6. The replacements are the `ColorScheme.primaryContainer` and `ColorScheme.secondaryContainer`, respectively.

These changes were made to align with the updated Material Design specification for `ColorScheme`. The updates to `ColorScheme` are covered more extensively in the [ColorScheme for Material 3](/go/colorscheme-m3) design document.

**Migration guide**

Code before migration:

dart

```
var colorScheme = ColorScheme(
  primaryVariant: Colors.blue,
  secondaryVariant: Colors.amber,
);
var primaryColor = colorScheme.primaryVariant;
var secondaryColor = colorScheme.secondaryVariant;
```

Code after migration:

dart

```
var colorScheme = ColorScheme(
  primaryContainer: Colors.blue,
  secondaryContainer: Colors.amber,
);
var primaryColor = colorScheme.primaryContainer;
var secondaryColor = colorScheme.secondaryContainer;
```

**References**

Design Document:

* [ColorScheme for Material 3](/go/colorscheme-m3)

API documentation:

* [`ColorScheme`](https://api.flutter.dev/flutter/material/ColorScheme-class.html)

Relevant PRs:

* Deprecated in [#93427](https://github.com/flutter/flutter/pull/93427)* Removed in [#127124](https://github.com/flutter/flutter/pull/127124)

---

### ThemeData.primaryColorBrightness

[#](#themedata-primarycolorbrightness)

Package: flutter Supported by Flutter Fix: yes

`ThemeData.primaryColorBrightness` was deprecated in v2.6, and has not been used by the framework since then. References should be removed. The `Brightness` is now extrapolated from the `ThemeData.primaryColor` if `ThemeData.brightness` has not been explicitly provided.

This change was made as part of the update to `Theme` to match new Material Design guidelines. The overall update to the theming system, including the removal of `primaryColorBrightness` is discussed more extensively in the [Material Theme System Updates](/go/material-theme-system-updates) design document.

**Migration guide**

Code before migration:

dart

```
var themeData = ThemeData(
  primaryColorBrightness: Brightness.dark,
);
```

Code after migration:

dart

```
var themeData = ThemeData(
);
```

**References**

Design Document:

* [Material Theme System Updates](/go/material-theme-system-updates)

API documentation:

* [`Theme`](https://api.flutter.dev/flutter/material/Theme-class.html)* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)* [`Brightness`](https://api.flutter.dev/flutter/dart-ui/Brightness.html)

Relevant PRs:

* Deprecated in [#93396](https://github.com/flutter/flutter/pull/93396)* Removed in [#127238](https://github.com/flutter/flutter/pull/127238)

---

### RawScrollbar & subclasses updates

[#](#rawscrollbar-subclasses-updates)

Package: flutter Supported by Flutter Fix: yes

The `isAlwaysShown` property of `RawScrollbar`, `Scrollbar`, `ScrollbarThemeData` and `CupertinoScrollbar` was deprecated in v2.9. The replacement in all cases is `thumbVisibility`.

This change was made since `isAlwaysShown` always referred to the scrollbar thumb. With the addition of a scrollbar track, and varying configurations for its visibility in response to mouse hovering and dragging, we renamed this property for a clearer API.

Additionally, `Scrollbar.hoverThickness` was also deprecated in v2.9. Its replacement is the `MaterialStateProperty` `ScrollbarThemeData.thickness`.

This change was made to allow the thickness of a `Scrollbar` to respond to all kind of states, including and beyond just hovering. The use of `MaterialStateProperties` also matches the convention in the material library of configuring widgets based on their state, rather than enumerating properties for every permutation of interactive states.

**Migration guide**

Code before migration:

dart

```
var rawScrollbar = RawScrollbar(
  isAlwaysShown: true,
);
var scrollbar = Scrollbar(
  isAlwaysShown: true,
  hoverThickness: 15.0,
);
var cupertinoScrollbar = CupertinoScrollbar(
  isAlwaysShown: true,
);
var scrollbarThemeData = ScrollbarThemeData(
  isAlwaysShown: true,
);
```

Code after migration:

dart

```
var rawScrollbar = RawScrollbar(
  thumbVisibility: true,
);
var scrollbar = Scrollbar(
  thumbVisibility: true,
);
var cupertinoScrollbar = CupertinoScrollbar(
  thumbVisibility: true,
);
var scrollbarThemeData = ScrollbarThemeData(
  thumbVisibility: true,
  thickness: MaterialStateProperty.resolveWith((Set<MaterialState> states) {
    return states.contains(MaterialState.hovered) ? null : 15.0;
  }),
);
```

**References**

API documentation:

* [`RawScrollbar`](https://api.flutter.dev/flutter/widgets/RawScrollbar-class.html)* [`Scrollbar`](https://api.flutter.dev/flutter/material/Scrollbar-class.html)* [`CupertinoScrollbar`](https://api.flutter.dev/flutter/cupertino/CupertinoScrollbar-class.html)* [`ScrollbarThemeData`](https://api.flutter.dev/flutter/material/ScrollbarThemeData-class.html)* [`MaterialStateProperty`](https://api.flutter.dev/flutter/material/MaterialStateProperty-class.html)* [`MaterialState`](https://api.flutter.dev/flutter/material/MaterialState.html)

Relevant PRs:

* Deprecated in [#96957](https://github.com/flutter/flutter/pull/96957)* Deprecated in [#97173](https://github.com/flutter/flutter/pull/97173)* Removed in [#127351](https://github.com/flutter/flutter/pull/127351)

---

### AnimationSheetBuilder display & sheetSize

[#](#animationsheetbuilder-display-sheetsize)

Package: flutter\_test Supported by Flutter Fix: yes

The `display` and `sheetSize` methods of `AnimationSheetBuilder` were deprecated in v2.3. The replacement is the `collate` method.

`AnimationSheetBuilder`'s output step previously required these two methods to be called, but is now streamlined through a single call to `collate`.

The `collate` function directly puts the images together and asynchronously returns an image. It requires less boilerplate, and outputs smaller images without any compromise to quality.

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/animation-sheet-builder-display)

Code before migration:

dart

```
final AnimationSheetBuilder animationSheet = AnimationSheetBuilder(
    frameSize: const Size(40, 40)
);

await tester.pumpFrames(animationSheet.record(
  const Directionality(
    textDirection: TextDirection.ltr,
    child: Padding(
      padding: EdgeInsets.all(4),
      child: CircularProgressIndicator(),
    ),
  ),
), const Duration(seconds: 2));

tester.binding.setSurfaceSize(animationSheet.sheetSize());

final Widget display = await animationSheet.display();
await tester.pumpWidget(display);

await expectLater(
  find.byWidget(display),
  matchesGoldenFile('material.circular_progress_indicator.indeterminate.png'),
);
```

Code after migration:

dart

```
final AnimationSheetBuilder animationSheet = AnimationSheetBuilder(
    frameSize: const Size(40, 40)
);

await tester.pumpFrames(animationSheet.record(
  const Directionality(
    textDirection: TextDirection.ltr,
    child: Padding(
      padding: EdgeInsets.all(4),
      child: CircularProgressIndicator(),
    ),
  ),
), const Duration(seconds: 2));

await expectLater(
  animationSheet.collate(20),
  matchesGoldenFile('material.circular_progress_indicator.indeterminate.png'),
);
```

**References**

API documentation:

* [`AnimationSheetBuilder`](https://api.flutter.dev/flutter/flutter_test/AnimationSheetBuilder-class.html)

Relevant PRs:

* Deprecated in [#83337](https://github.com/flutter/flutter/pull/83337)* Removed in [#129657](https://github.com/flutter/flutter/pull/129657)

### flutter\_test timeout logic

[#](#flutter_test-timeout-logic)

Package: flutter\_test Supported by Flutter Fix: no

The following APIs related to timeout logic in tests were deprecated in v2.6. There are no replacements, and references should be removed, except for the `initialTimeout` parameter of `testWidgets`, which is replaced by using `timeout`.

* `TestWidgetsFlutterBinding.addTime`* `TestWidgetsFlutterBinding.runAsync` method - `additionalTime` parameter* `TestWidgetsFlutterBinding.runTest` method - `timeout` parameter* `AutomatedTestWidgetsFlutterBinding.runTest` method - `timeout` parameter* `LiveTestWidgetsFlutterBinding.runTest` method - `timeout` parameter* `testWidgets` method - `initialTime` parameter

These were found to cause flakiness in testing, and were not in use by tested customers.

Since being deprecated, use of these parameters have had no effect on tests, so removing references should have no effect on existing code bases.

**Migration guide**

Code before migration:

dart

```
testWidgets('Test', (_) {}, initialTimeout:  Duration(seconds: 5));
```

Code after migration:

dart

```
testWidgets('Test', (_) {}, timeout:  Timeout(Duration(seconds: 5)));
```

**References**

API documentation:

* [`testWidgets`](https://api.flutter.dev/flutter/flutter_test/testWidgets.html)* [`TestWidgetsFlutterBinding`](https://api.flutter.dev/flutter/flutter_test/TestWidgetsFlutterBinding-class.html)* [`AutomatedTestWidgetsFlutterBinding`](https://api.flutter.dev/flutter/flutter_test/AutomatedTestWidgetsFlutterBinding-class.html)* [`LiveTestWidgetsFlutterBinding`](https://api.flutter.dev/flutter/flutter_test/LiveTestWidgetsFlutterBinding-class.html)

Relevant PRs:

* Deprecated in [#89952](https://github.com/flutter/flutter/pull/89952)* Removed in [#129663](https://github.com/flutter/flutter/pull/129663)

---

Timeline
--------

[#](#timeline)

In stable release: 3.13.0

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-10-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-10-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-10-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-10-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-10-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-10-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-10-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   