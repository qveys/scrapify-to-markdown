Deprecated API removed after v3.7
=================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v3.7](/release/breaking-changes/3-7-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 3.7 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. A [quick reference sheet](/go/deprecations-removed-after-3-7) is available as well.

Changes
-------

[#](#changes)

This section lists the deprecations, listed by the affected class.

### `GestureRecognizer.kind` & subclasses

[#](#gesturerecognizer-kind-subclasses)

Supported by Flutter Fix: yes

`GestureRecognizer.kind` was deprecated in v2.3. Use `GestureRecognizer.supportedDevices` instead.

This same change affects all subclasses of `GestureRecognizer`:

* `EagerGestureRecognizer`* `ForcePressGestureRecognizer`* `LongPressGestureRecognizer`* `DragGestureRecognizer`* `VerticalDragGestureRecognizer`* `HorizontalDragGestureRecognizer`* `MultiDragGestureRecognizer`* `ImmediateMultiDragGestureRecognizer`* `HorizontalMultiDragGestureRecognizer`* `VerticalMultiDragGestureRecognizer`* `DelayedMultiDragGestureRecognizer`* `DoubleTapGestureRecognizer`* `MultiTapGestureRecognizer`* `OneSequenceGestureRecognizer`* `PrimaryPointerGestureRecognizer`* `ScaleGestureRecognizer`

This change allowed for multiple devices to be recognized for a gesture, rather than the single option `kind` provided.

**Migration guide**

Code before migration:

dart

```
var myRecognizer = GestureRecognizer(
  kind: PointerDeviceKind.mouse,  
);
```

Code after migration:

dart

```
var myRecognizer = GestureRecognizer(
  supportedDevices: <PointerDeviceKind>[ PointerDeviceKind.mouse ],
);
```

**References**

API documentation:

* [`GestureRecognizer`](https://api.flutter.dev/flutter/gestures/GestureRecognizer-class.html)* [`EagerGestureRecognizer`](https://api.flutter.dev/flutter/gestures/EagerGestureRecognizer-class.html)* [`ForcePressGestureRecognizer`](https://api.flutter.dev/flutter/gestures/ForcePressGestureRecognizer-class.html)* [`LongPressGestureRecognizer`](https://api.flutter.dev/flutter/gestures/LongPressGestureRecognizer-class.html)* [`DragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/DragGestureRecognizer-class.html)* [`VerticalDragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/VerticalDragGestureRecognizer-class.html)* [`HorizontalDragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/HorizontalDragGestureRecognizer-class.html)* [`MultiDragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/MultiDragGestureRecognizer-class.html)* [`ImmediateMultiDragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/ImmediateMultiDragGestureRecognizer-class.html)* [`HorizontalMultiDragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/HorizontalMultiDragGestureRecognizer-class.html)* [`VerticalMultiDragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/VerticalMultiDragGestureRecognizer-class.html)* [`DelayedMultiDragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/DelayedMultiDragGestureRecognizer-class.html)* [`DoubleTapGestureRecognizer`](https://api.flutter.dev/flutter/gestures/DoubleTapGestureRecognizer-class.html)* [`MultiTapGestureRecognizer`](https://api.flutter.dev/flutter/gestures/MultiTapGestureRecognizer-class.html)* [`OneSequenceGestureRecognizer`](https://api.flutter.dev/flutter/gestures/OneSequenceGestureRecognizer-class.html)* [`PrimaryPointerGestureRecognizer`](https://api.flutter.dev/flutter/gestures/PrimaryPointerGestureRecognizer-class.html)* [`ScaleGestureRecognizer`](https://api.flutter.dev/flutter/gestures/ScaleGestureRecognizer-class.html)

Relevant PRs:

* Deprecated in [#81858](https://github.com/flutter/flutter/pull/81858)* Removed in [#119572](https://github.com/flutter/flutter/pull/119572)

---

### `ThemeData` `accentColor`, `accentColorBrightness`, `accentColorTextTheme`, `accentColorIconTheme`, and `buttonColor`

[#](#themedata-accentcolor-accentcolorbrightness-accentcolortexttheme-accentcoloricontheme-and-buttoncolor)

Supported by Flutter Fix: yes

The `accentColor`, `accentColorBrightness`, `accentColorTextTheme`, `accentColorIconTheme`, and `buttonColor` properties of `ThemeData` were deprecated in v2.3.

This change better aligned `ThemeData` with Material Design guidelines. It also created more clarity in theming by relying either on the core color scheme or individual component themes for desired styling.

The `accentColorBrightness`, `accentColorTextTheme`, `accentColorIconTheme`, and `buttonColor` are no longer used by the framework. References should be removed.

Uses of `ThemeData.accentColor` should be replaced with `ThemeData.colorScheme.secondary`.

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
var myTheme = ThemeData(
  //...
  accentColor: Colors.blue,
  //...
);
var color = myTheme.accentColor;
```

Code after migration:

dart

```
var myTheme = ThemeData(
  //...
  colorScheme: ColorScheme(
    //...
    secondary:Colors.blue,
    //...
  ),
  //...
);
var color = myTheme.colorScheme.secondary;
```

**References**

* [Accent color migration guide](/release/breaking-changes/theme-data-accent-properties)

API documentation:

* [`ThemeData`](https://api.flutter.dev/flutter/widgets/Draggable-class.html)* [`ColorScheme`](https://api.flutter.dev/flutter/widgets/LongPressDraggable-class.html)

Relevant issues:

* [#56639](https://github.com/flutter/flutter/pull/56639)* [#84748](https://github.com/flutter/flutter/pull/84748)* [#56918](https://github.com/flutter/flutter/pull/56918)* [#91772](https://github.com/flutter/flutter/pull/91772)

Relevant PRs:

Deprecated in:

* [#92822](https://github.com/flutter/flutter/pull/92822)* [#81336](https://github.com/flutter/flutter/pull/81336)* [#85144](https://github.com/flutter/flutter/pull/85144)

Removed in:

* [#118658](https://github.com/flutter/flutter/pull/118658)* [#119360](https://github.com/flutter/flutter/pull/119360)* [#120577](https://github.com/flutter/flutter/pull/120577)* [#120932](https://github.com/flutter/flutter/pull/120932)

---

### `AppBar`, `SliverAppBar`, and `AppBarTheme` updates

[#](#appbar-sliverappbar-and-appbartheme-updates)

Supported by Flutter Fix: yes

In v2.4, several changes were made ot the app bar classes and their themes to better align with Material Design. Several properties were deprecated at that time and have been removed.

For `AppBar`, `SliverAppBar` and `AppBarTheme`:

* `brightness` has been removed, and is replaced by `systemOverlayStyle`* `textTheme` has been removed, and is replaced by either `toolbarTextStyle` or `titleTextStyle`.* `backwardsCompatibility` can be removed, as it was a temporary migration flag for these properties.

Additionally, `AppBarTheme.color` was removed, with `AppBarTheme.backgroundColor` as its replacement.

**Migration guide**

Code before migration:

dart

```
var toolbarTextStyle = TextStyle(...);
var titleTextStyle = TextStyle(...);
AppBar(
  brightness: Brightness.light,
  textTheme: TextTheme(
    bodyMedium: toolbarTextStyle,
    titleLarge: titleTextStyle,
  )
  backwardsCompatibility: true,
);
AppBarTheme(color: Colors.blue);
```

Code after migration:

dart

```
var toolbarTextStyle = TextStyle(...);
var titleTextStyle = TextStyle(...);
AppBar(
  systemOverlayStyle: SystemOverlayStyle(statusBarBrightness: Brightness.light),
  toolbarTextStyle: toolbarTextStyle,
  titleTextStyle: titleTextStyle,
);
AppBarTheme(backgroundColor: Colors.blue);
```

**References**

API documentation:

* [`AppBar`](https://api.flutter.dev/flutter/material/AppBar-class.html)* [`SliverAppBar`](https://api.flutter.dev/flutter/material/SliverAppBar-class.html)* [`AppBarTheme`](https://api.flutter.dev/flutter/material/AppBarTheme-class.html)

Relevant issues:

* [#86127](https://github.com/flutter/flutter/pull/86127)* [#70645](https://github.com/flutter/flutter/pull/70645)* [#67921](https://github.com/flutter/flutter/pull/67921)* [#67497](https://github.com/flutter/flutter/pull/67497)* [#50606](https://github.com/flutter/flutter/pull/50606)* [#51820](https://github.com/flutter/flutter/pull/51820)* [#61618](https://github.com/flutter/flutter/pull/61618)

Deprecated in:

* [#86198](https://github.com/flutter/flutter/pull/86198)* [#71184](https://github.com/flutter/flutter/pull/71184)

Removed in:

* [#120618](https://github.com/flutter/flutter/pull/120618)* [#119253](https://github.com/flutter/flutter/pull/119253)* [#120575](https://github.com/flutter/flutter/pull/120575)

---

### `SystemChrome.setEnabledSystemUIOverlays`

[#](#systemchrome-setenabledsystemuioverlays)

Supported by Flutter Fix: yes

In v2.3, `SystemChrome.setEnabledSystemUIOVerlays`, the static method for setting device system level overlays like status and navigation bars, was deprecated in favor of `SystemChrome.setEnabledSystemUIMode`.

This change allowed for setting up common fullscreen modes that match native Android app designs like edge to edge.

Manually setting overlays, instead of choosing a specific mode, is still supported through `SystemUiMode.manual`, allowing developers to pass the same list of overlays as before.

**Migration guide**

Code before migration:

dart

```
SystemChrome.setEnabledSystemUIOverlays(<SystemUiOverlay>[
  SystemUiOverlay.top,
  SystemUiOverlay.bottom,
]);
```

Code after migration:

dart

```
SystemChrome.setEnabledSystemUIMode(
  SystemUiMode.manual,
  overlays: <SystemUiOverlay>[
    SystemUiOverlay.top,
    SystemUiOverlay.bottom,
  ],
);
```

**References**

API documentation:

* [`SystemChrome`](https://api.flutter.dev/flutter/services/SystemChrome-class.html)

Relevant issues:

* [#35748](https://github.com/flutter/flutter/pull/35748)* [#40974](https://github.com/flutter/flutter/pull/40974)* [#44033](https://github.com/flutter/flutter/pull/44033)* [#63761](https://github.com/flutter/flutter/pull/63761)* [#69999](https://github.com/flutter/flutter/pull/69999)

Deprecated in:

* [#81303](https://github.com/flutter/flutter/pull/81303)

Removed in:

* [#11957](https://github.com/flutter/flutter/pull/11957)

---

### `SystemNavigator.routeUpdated`

[#](#systemnavigator-routeupdated)

Supported by Flutter Fix: yes

In v2.3, `SystemNavigator.routeUpdated` was deprecated in favor of `SystemNavigator.routeInformationUpdated`.

Instead of having two ways to update the engine about the current route, the change moved everything to one API, which separately selects the single-entry history mode if a `Navigator` that reports routes is created.

**Migration guide**

Code before migration:

dart

```
SystemNavigator.routeUpdated(routeName: 'foo', previousRouteName: 'bar');
```

Code after migration:

dart

```
SystemNavigator.routeInformationUpdated(location: 'foo');
```

**References**

API documentation:

* [`SystemNavigator`](https://api.flutter.dev/flutter/services/SystemNavigator-class.html)

Relevant issues:

* [#82574](https://github.com/flutter/flutter/pull/82574)

Deprecated in:

* [#82594](https://github.com/flutter/flutter/pull/82594)

Removed in:

* [#119187](https://github.com/flutter/flutter/pull/119187)

---

### `AnimatedSize.vsync`

[#](#animatedsize-vsync)

Supported by Flutter Fix: yes

In v2.2, `AnimatedSize.vsyc` was deprecated. This property was no longer necessary after `AnimatedSize` was converted to a `StatefulWidget` whose `State` mixed in `SingleTickerProviderStateMixin`. The change was made to fix a memory leak.

Uses of `vsync` should be removed, as `AnimatedSize` now handles this property.

**Migration guide**

Code before migration:

dart

```
AnimatedSize(
  vsync: this,
  // ...
);
```

Code after migration:

dart

```
AnimatedSize(
  // ...
);
```

**References**

API documentation:

* [`AnimatedSize`](https://api.flutter.dev/flutter/widgets/AnimatedSize-class.html)

Deprecated in:

* [#80554](https://github.com/flutter/flutter/pull/80554)* [#81067](https://github.com/flutter/flutter/pull/81067)

Removed in:

* [#119186](https://github.com/flutter/flutter/pull/119186)

---

Timeline
--------

[#](#timeline)

In stable release: 3.10

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-7-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-7-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-7-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-7-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-7-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-7-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-7-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   