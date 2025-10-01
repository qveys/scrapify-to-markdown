Deprecated API removed after v1.22
==================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v1.22](/release/breaking-changes/1-22-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 1.22 stable release have been removed. This is the first time that deprecated APIs have been removed from Flutter, and some of these deprecations predate our migration guide policy.

All affected APIs have been compiled into this primary source to aid in migration. A [quick reference sheet](/go/deprecations-removed-after-1-22) is available as well.

A [design document](/go/deprecation-lifetime) and [article](https://blog.flutter.dev/deprecation-lifetime-in-flutter-e4d76ee738ad) are available for more context on Flutter's deprecation policy.

Changes
-------

[#](#changes)

This section lists the deprecations, listed by the affected class.

### `CupertinoDialog`

[#](#cupertinodialog)

Supported by fix tool: IDE fix only.

`CupertinoDialog` was deprecated in v0.2.3. Use `CupertinoAlertDialog` or `CupertinoPopupSurface` instead.

**Migration guide**

*CupertinoAlertDialog*

Code before migration:

dart

```
CupertinoDialog(child: myWidget);
```

Code after migration:

dart

```
CupertinoAlertDialog(content: myWidget);
```

*CupertinoPopupSurface*

Code before migration:

dart

```
CupertinoDialog(child: myWidget);
```

Code after migration:

dart

```
CupertinoPopupSurface(child: myWidget);
```

**References**

API documentation:

* [`CupertinoAlertDialog`](https://api.flutter.dev/flutter/cupertino/CupertinoAlertDialog-class.html)* [`CupertinoPopupSurface`](https://api.flutter.dev/flutter/cupertino/CupertinoPopupSurface-class.html)

Relevant issues:

* [Deprecate CupertinoDialog class](https://github.com/flutter/flutter/issues/20397)

Relevant PRs:

* Deprecated in [#20649](https://github.com/flutter/flutter/pull/20649)* Removed in [#73604](https://github.com/flutter/flutter/pull/73604)

---

### Cupertino navigation bars' `actionsForegroundColor`

[#](#cupertino-navigation-bars-actionsforegroundcolor)

Supported by fix tool: No

`CupertinoNavigationBar.actionsForegroundColor` and `CupertinoSliverNavigationBar.actionsForegroundColor` were deprecated in v1.1.2. Setting `primaryColor` in your `CupertinoTheme` propagates this instead. To access the `primaryColor`, call `CupertinoTheme.of(context).primaryColor`.

**Migration guide**

Code before migration:

dart

```
CupertinoNavigationBar(
  actionsForegroundColor: CupertinoColors.systemBlue,
);
CupertinoSliverNavigationBar(
  actionsForegroundColor: CupertinoColors.systemBlue,
);
```

Code after migration:

dart

```
CupertinoTheme(
  data: CupertinoThemeData(
    primaryColor: CupertinoColors.systemBlue
  ),
  child: ...
);

// To access the color from the `CupertinoTheme`
CupertinoTheme.of(context).primaryColor;
```

**References**

API documentation:

* [`CupertinoNavigationBar`](https://api.flutter.dev/flutter/cupertino/CupertinoNavigationBar-class.html)* [`CupertinoSliverNavigationBar`](https://api.flutter.dev/flutter/cupertino/CupertinoSliverNavigationBar-class.html)* [`CupertinoTheme`](https://api.flutter.dev/flutter/cupertino/CupertinoTheme-class.html)* [`CupertinoThemeData`](https://api.flutter.dev/flutter/cupertino/CupertinoThemeData-class.html)

Relevant issues:

* [Create a CupertinoApp and a CupertinoTheme](https://github.com/flutter/flutter/issues/18037)

Relevant PRs:

* Deprecated in [#23759](https://github.com/flutter/flutter/pull/23759)* Removed in [#73745](https://github.com/flutter/flutter/pull/73745)

---

### `CupertinoTextThemeData.brightness`

[#](#cupertinotextthemedata-brightness)

Supported by fix tool: Yes

`CupertinoTextThemeData.brightness` was deprecated in v1.10.14. This field member was made ineffective at the time of deprecation. There is no replacement for this parameter, references should be removed.

**Migration guide**

Code before migration:

dart

```
const CupertinoTextThemeData themeData = CupertinoTextThemeData(brightness: Brightness.dark);
themeData.copyWith(brightness: Brightness.light);
```

Code after migration:

dart

```
const CupertinoTextThemeData themeData = CupertinoTextThemeData();
themeData.copyWith();
```

**References**

API documentation:

* [`CupertinoTextThemeData`](https://api.flutter.dev/flutter/cupertino/CupertinoTextThemeData-class.html)

Relevant issues:

* [Revise CupertinoColors and CupertinoTheme for dynamic colors](https://github.com/flutter/flutter/issues/35541)

Relevant PRs:

* Deprecated in [#41859](https://github.com/flutter/flutter/pull/41859)* Removed in [#72017](https://github.com/flutter/flutter/pull/72017)

---

### Pointer events constructed `fromHoverEvent`

[#](#pointer-events-constructed-fromhoverevent)

Supported by fix tool: Yes

The `fromHoverEvent` constructors for `PointerEnterEvent` and `PointerExitEvent` were deprecated in v1.4.3. The `fromMouseEvent` constructor should be used instead.

**Migration guide**

Code before migration:

dart

```
final PointerEnterEvent enterEvent = PointerEnterEvent.fromHoverEvent(PointerHoverEvent());
final PointerExitEvent exitEvent = PointerExitEvent.fromHoverEvent(PointerHoverEvent());
```

Code after migration:

dart

```
final PointerEnterEvent enterEvent = PointerEnterEvent.fromMouseEvent(PointerHoverEvent());
final PointerExitEvent exitEvent = PointerExitEvent.fromMouseEvent(PointerHoverEvent());
```

**References**

API documentation:

* [`PointerEnterEvent`](https://api.flutter.dev/flutter/gestures/PointerEnterEvent-class.html)* [`PointerExitEvent`](https://api.flutter.dev/flutter/gestures/PointerExitEvent-class.html)

Relevant issues:

* [PointerEnterEvent and PointerExitEvent can only be created from hover events](https://github.com/flutter/flutter/issues/29696)

Relevant PRs:

* Deprecated in [#28602](https://github.com/flutter/flutter/pull/28602)* Removed in [#72395](https://github.com/flutter/flutter/pull/72395)

---

### `showDialog` uses `builder`

[#](#showdialog-uses-builder)

Supported by fix tool: Yes

The `child` parameter of `showDialog` was deprecated in v0.2.3. The `builder` parameter should be used instead.

**Migration guide**

Code before migration:

dart

```
showDialog(child: myWidget);
```

Code after migration:

dart

```
showDialog(builder: (context) => myWidget);
```

**References**

API documentation:

* [`showDialog`](https://api.flutter.dev/flutter/material/showDialog.html)

Relevant issues:

* [showDialog should take a builder rather than a child](https://github.com/flutter/flutter/issues/14341)

Relevant PRs:

* Deprecated in [#15303](https://github.com/flutter/flutter/pull/15303)* Removed in [#72532](https://github.com/flutter/flutter/pull/72532)

---

### `Scaffold.resizeToAvoidBottomPadding`

[#](#scaffold-resizetoavoidbottompadding)

Supported by fix tool: Yes

The `resizeToAvoidBottomPadding` parameter of `Scaffold` was deprecated in v1.1.9. The `resizeToAvoidBottomInset` parameter should be used instead.

**Migration guide**

Code before migration:

dart

```
Scaffold(resizeToAvoidBottomPadding: true);
```

Code after migration:

dart

```
Scaffold(resizeToAvoidBottomInset: true);
```

**References**

API documentation:

* [`Scaffold`](https://api.flutter.dev/flutter/material/Scaffold-class.html)

Relevant issues:

* [Show warning when nesting Scaffolds](https://github.com/flutter/flutter/issues/23106)* [SafeArea with keyboard](https://github.com/flutter/flutter/issues/25758)* [Double stacked material scaffolds shouldn't double resizeToAvoidBottomPadding](https://github.com/flutter/flutter/issues/12084)* [viewInsets and padding on Window and MediaQueryData should define how they interact](https://github.com/flutter/flutter/issues/15424)* [bottom overflow issue, when using textfields inside tabbarview](https://github.com/flutter/flutter/issues/20295)

Relevant PRs:

* Deprecated in [#26259](https://github.com/flutter/flutter/pull/26259)* Removed in [#72890](https://github.com/flutter/flutter/pull/72890)

---

### `ButtonTheme.bar`

[#](#buttontheme-bar)

Supported by fix tool: No

The `bar` constructor of `ButtonTheme` was deprecated in v1.9.1. `ButtonBarTheme` can be used instead for `ButtonBar`s, or use another constructor of `ButtonTheme` if the use is not specific to `ButtonBar`.

Button-specific theming is also available with the `TextButtonTheme`, `ElevatedButtonTheme`, and `OutlinedButtonTheme` classes, each corresponding with the appropriate button class, `TextButton`, `ElevatedButton` and `OutlinedButton`.

**Migration guide**

Code before migration:

dart

```
ButtonTheme.bar(
  minWidth: 10.0,
  alignedDropdown: true,
  height: 40.0,
);
```

Code after migration, using `ButtonTheme`:

dart

```
ButtonTheme(
  minWidth: 10.0,
  alignedDropdown: true,
  height: 40.0,
);
```

Code after migration, using `ButtonBarTheme`:

dart

```
ButtonBarTheme(
  data: ButtonBarThemeData(
    buttonMinWidth: 10.0,
    buttonAlignedDropdown: true,
    buttonHeight: 40.0,
  )
);
```

**References**

API documentation:

* [`ButtonTheme`](https://api.flutter.dev/flutter/material/ButtonTheme-class.html)* [`ButtonBarTheme`](https://api.flutter.dev/flutter/material/ButtonBarTheme-class.html)* [`ButtonBar`](https://api.flutter.dev/flutter/material/ButtonBar-class.html)* [`TextButtonTheme`](https://api.flutter.dev/flutter/material/TextButtonTheme-class.html)* [`TextButton`](https://api.flutter.dev/flutter/material/TextButton-class.html)* [`ElevatedButtonTheme`](https://api.flutter.dev/flutter/material/ElevatedButtonTheme-class.html)* [`ElevatedButton`](https://api.flutter.dev/flutter/material/ElevatedButton-class.html)* [`OutlinedButtonTheme`](https://api.flutter.dev/flutter/material/OutlinedButtonTheme-class.html)* [`OutlinedButton`](https://api.flutter.dev/flutter/material/OutlinedButton-class.html)

Relevant issues:

* [ButtonTheme.bar uses accent color when it should be using primary color](https://github.com/flutter/flutter/issues/31333)* [ThemeData.accentColor has insufficient contrast for text](https://github.com/flutter/flutter/issues/19946)* [Increased height as a result of changes to materialTapTargetSize affecting AlertDialog/ButtonBar heights](https://github.com/flutter/flutter/issues/20585)

Relevant PRs:

* Deprecated in [#37544](https://github.com/flutter/flutter/pull/37544)* Removed in [#73746](https://github.com/flutter/flutter/pull/73746)

---

### `InlineSpan`, `TextSpan`, `PlaceholderSpan`

[#](#inlinespan-textspan-placeholderspan)

Supported by fix tool: No

The following methods were deprecated in the `InlineSpan`, `TextSpan` and `PlaceholderSpan` in order to enable embedding widgets inline into paragraphs, like images.

**Migration guide**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Code before migration Code after migration|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `InlineSpan.text` `TextSpan.text`| `InlineSpan.children` `TextSpan.children`| `InlineSpan.visitTextSpan` `InlineSpan.visitChildren`| `InlineSpan.recognizer` `TextSpan.recognizer`| `InlineSpan.describeSemantics` `InlineSpan.computeSemanticsInformation`| `PlaceholderSpan.visitTextSpan` `PlaceHolderSpan.visitChildren`| `TextSpan.visitTextSpan` `TextSpan.visitChildren` | | | | | | | | | | | | | | | |

**References**

API documentation:

* [`InlineSpan`](https://api.flutter.dev/flutter/painting/InlineSpan-class.html)* [`TextSpan`](https://api.flutter.dev/flutter/painting/TextSpan-class.html)* [`PlaceholderSpan`](https://api.flutter.dev/flutter/painting/PlaceholderSpan-class.html)* [`WidgetSpan`](https://api.flutter.dev/flutter/widgets/WidgetSpan-class.html)

Relevant issues:

* [Text: support inline images](https://github.com/flutter/flutter/issues/2022)

Relevant PRs:

* Development history:
  + [#30069](https://github.com/flutter/flutter/pull/30069)+ [#33946](https://github.com/flutter/flutter/pull/33946)+ [#33794](https://github.com/flutter/flutter/pull/33794)* Deprecated in [#34051](https://github.com/flutter/flutter/pull/34051)* Removed in [#73747](https://github.com/flutter/flutter/pull/73747)

---

### `RenderView.scheduleInitialFrame`

[#](#renderview-scheduleinitialframe)

Supported by fix tool: No

The `RenderView.scheduleInitialFrame` method was deprecated and removed in order to prevent splash screens from being taken down too early, resulting in a black screen. This would happen when `WidgetsFlutterBinding.ensureInitialized` was called. Instead, replace calls to this method with `RenderView.prepareInitialFrame`, followed by `RenderView.owner.requestVisualUpdate`.

**Migration guide**

Code before migration:

dart

```
scheduleInitialFrame();
```

Code after migration:

dart

```
prepareInitialFrame();
owner.requestVisualUpdate();
```

**References**

API documentation:

* [`RenderView`](https://api.flutter.dev/flutter/rendering/RenderView-class.html)* [`WidgetsFlutterBinding`](https://api.flutter.dev/flutter/widgets/WidgetsFlutterBinding-class.html)

Relevant issues:

* [WidgetsFlutterBinding.ensureInitialized() takes down splash screen too early](https://github.com/flutter/flutter/issues/39494)

Relevant PRs:

* Deprecated in [#39535](https://github.com/flutter/flutter/pull/39535)* Removed in [#73748](https://github.com/flutter/flutter/pull/73748)

---

### `Layer.findAll`

[#](#layer-findall)

Supported by fix tool: No

The `Layer.findAll` method was deprecated with the introduction of `Layer.findAnnotations` in order to unify the implementations of `find` and `findAll`. To migrate affected code, call `findAllAnnotations` instead. This method returns an `AnnotationResult`, containing the former return value of `findAll` in `AnnotationResult.annotations`.

**Migration guide**

Code before migration:

dart

```
findAll(offset);
```

Code after migration:

dart

```
findAllAnnotations(offset).annotations;
```

**References**

API documentation:

* [`Layer`](https://api.flutter.dev/flutter/rendering/Layer-class.html)* [`MouseRegion`](https://api.flutter.dev/flutter/widgets/MouseRegion-class.html)* [`RenderMouseRegion`](https://api.flutter.dev/flutter/rendering/RenderMouseRegion-class.html)* [`AnnotatedRegionLayer`](https://api.flutter.dev/flutter/rendering/AnnotatedRegionLayer-class.html)* [`AnnotationResult`](https://api.flutter.dev/flutter/rendering/AnnotationResult-class.html)

Relevant issues:

* [Breaking Proposal: MouseRegion defaults to opaque; Layers are required to implement findAnnotations](https://github.com/flutter/flutter/issues/38488)

Relevant PRs:

* Initially changed in [#37896](https://github.com/flutter/flutter/pull/37896)* Deprecated in [#42953](https://github.com/flutter/flutter/pull/42953)* Removed in [#73749](https://github.com/flutter/flutter/pull/73749)

---

### `BinaryMessages`

[#](#binarymessages)

Supported by fix tool: No

The `BinaryMessages` class, its associated static methods and the `defaultBinaryMessenger` getter were deprecated and removed. The `defaultBinaryMessenger` instance was moved to `ServicesBinding`. This made it possible to register a different default `BinaryMessenger` under testing environment, by creating a `ServicesBinding` subclass for testing. Doing so allows you to track the number of pending platform messages for synchronization purposes.

**Migration guide**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Code before migration: Code after migration:|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `defaultBinaryMessenger` `ServicesBinding.instance.defaultBinaryMessenger`| `BinaryMessages` `BinaryMessenger`| `BinaryMessages.handlePlatformMessage` `ServicesBinding.instance.defaultBinaryMessenger.handlePlatformMessage`| `BinaryMessages.send` `ServicesBinding.instance.defaultBinaryMessenger.send`| `BinaryMessages.setMessageHandler` `ServicesBinding.instance.defaultBinaryMessenger.setMessageHandler`| `BinaryMessages.setMockMessageHandler` `ServicesBinding.instance.defaultBinaryMessenger.setMockMessageHandler` | | | | | | | | | | | | | |

**References**

API documentation:

* [`ServicesBinding`](https://api.flutter.dev/flutter/services/ServicesBinding-mixin.html)* [`BinaryMessenger`](https://api.flutter.dev/flutter/services/BinaryMessenger-class.html)

Relevant issues:

* [Flutter synchronization support for Espresso/EarlGrey](https://github.com/flutter/flutter/issues/37409)

Relevant PRs:

* Initially changed in [#37489](https://github.com/flutter/flutter/pull/37489)* Deprecated in [#38464](https://github.com/flutter/flutter/pull/38464)* Removed in [#73750](https://github.com/flutter/flutter/pull/73750)

---

### Generic methods for `BuildContext`

[#](#generic-methods-for-buildcontext)

Supported by fix tool: Yes

Several methods in `BuildContext` were using `Type` to search for ancestors. Most of those methods implied a cast at call site because their return type was a parent type. Moreover the type provided was not checked at analysis time even if the type is actually constrained. Making these methods generics improves type safety and requires less code.

These method changes affect the `BuildContext`, `Element`, and `StatefulElement` classes. The `TypeMatcher` class was also removed.

**Migration guide**

Code before migration:

dart

```
ComplexLayoutState state = context.ancestorStateOfType(const TypeMatcher<ComplexLayoutState>()) as ComplexLayoutState;
```

Code after migration:

dart

```
ComplexLayoutState state = context.ancestorStateOfType<ComplexLayoutState>();
```

`BuildContext`

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Code before migration: Code after migration:|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `inheritFromElement` `dependOnInheritedElement`| `inheritFromWidgetOfExactType` `dependOnInheritedWidgetOfExactType`| `ancestorInheritedElementForWidgetOfExactType` `getElementForInheritedWidgetOfExactType`| `ancestorWidgetOfExactType` `findAncestorWidgetOfExactType`| `ancestorStateOfType` `findAncestorStateOfType`| `rootAncestorStateOfType` `findRootAncestorStateOfType`| `ancestorRenderObjectOfType` `findAncestorRenderObjectOfType` | | | | | | | | | | | | | | | |

`Element`

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Code before migration: Code after migration:|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `inheritFromElement` `dependOnInheritedElement`| `inheritFromWidgetOfExactType` `dependOnInheritedWidgetOfExactType`| `ancestorInheritedElementForWidgetOfExactType` `getElementForInheritedWidgetOfExactType`| `ancestorWidgetOfExactType` `findAncestorWidgetOfExactType`| `ancestorStateOfType` `findAncestorStateOfType`| `rootAncestorStateOfType` `findRootAncestorStateOfType`| `ancestorRenderObjectOfType` `findAncestorRenderObjectOfType` | | | | | | | | | | | | | | | |

`StatefulElement`

|  |  |  |  |
| --- | --- | --- | --- |
| Code before migration: Code after migration:|  |  | | --- | --- | | `inheritFromElement` `dependOnInheritedElement` | | | |

**References**

API documentation:

* [`Type`](https://api.flutter.dev/flutter/dart-core/Type-class.html)* [`BuildContext`](https://api.flutter.dev/flutter/widgets/BuildContext-class.html)* [`Element`](https://api.flutter.dev/flutter/widgets/Element-class.html)* [`StatefulElement`](https://api.flutter.dev/flutter/widgets/StatefulElement-class.html)

Relevant PRs:

* Deprecated in [#44189](https://github.com/flutter/flutter/pull/44189)* Removed in:
    + [#69620](https://github.com/flutter/flutter/pull/69620)+ [#72903](https://github.com/flutter/flutter/pull/72903)+ [#72901](https://github.com/flutter/flutter/pull/72901)+ [#73751](https://github.com/flutter/flutter/pull/73751)

---

### `WidgetsBinding.deferFirstFrameReport` & `WidgetsBinding.allowFirstFrameReport`

[#](#widgetsbinding-deferfirstframereport-widgetsbinding-allowfirstframereport)

Supported by fix tool: Yes

The `deferFirstFrameReport` and `allowFirstFrameReport` methods of `WidgetsBinding` were deprecated and removed in order to provide the option to delay rendering the first frame. This is useful for widgets that need to obtain initialization information asynchronously and while they are waiting for that information no frame should render as that would take down the splash screen pre-maturely. The `deferFirstFrame` and `allowFirstFrame` methods should be used respectively instead.

**Migration guide**

Code before migration:

dart

```
final WidgetsBinding binding = WidgetsBinding.instance;
binding.deferFirstFrameReport();
binding.allowFirstFrameReport();
```

Code after migration:

dart

```
final WidgetsBinding binding = WidgetsBinding.instance;
binding.deferFirstFrame();
binding.allowFirstFrame();
```

**References**

API documentation:

* [`WidgetsBinding`](https://api.flutter.dev/flutter/widgets/WidgetsBinding-mixin.html)

Relevant PRs:

* Initially changed in
  + [#45135](https://github.com/flutter/flutter/pull/45135)+ [#45588](https://github.com/flutter/flutter/pull/45588)* Deprecated in [#45941](https://github.com/flutter/flutter/pull/45941)* Removed in [#72893](https://github.com/flutter/flutter/pull/72893)

---

### `WaitUntilNoTransientCallbacks`, `WaitUntilNoPendingFrame`, & `WaitUntilFirstFrameRasterized`

[#](#waituntilnotransientcallbacks-waituntilnopendingframe-waituntilfirstframerasterized)

Supported by fix tool: No

The `WaitUntilNoTransientCallbacks`, `WaitUntilNoPendingFrame`, and `WaitUntilFirstFrameRasterized` methods from the `flutter_driver` packages were deprecated and removed in order to provide a more composable `waitForCondition` API that can be used to compose conditions that the client would like to wait for.

**Migration guide**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Code before migration: Code after migration:|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `WaitUntilNoTransientCallbacks` `WaitForCondition(NoTransientCallbacks())`| `WaitUntilNoPendingFrame` `WaitForCondition(NoPendingFrame())`| `WaitUntilFirstFrameRasterized` `WaitForCondition(FirstFrameRasterized))` | | | | | | | |

**References**

API documentation:

* [`WaitForCondition`](https://api.flutter.dev/flutter/flutter_driver/WaitForCondition-class.html)

Relevant issues:

* [Flutter synchronization support for Espresso/EarlGrey](https://github.com/flutter/flutter/issues/37409)

Relevant PRs:

* Initially changed in [#37736](https://github.com/flutter/flutter/pull/37736)* Deprecated in [#38836](https://github.com/flutter/flutter/pull/38836)* Removed in [#73754](https://github.com/flutter/flutter/pull/73754)

---

Timeline
--------

[#](#timeline)

In stable release: 2.0.0

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/1-22-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/1-22-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/1-22-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/1-22-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/1-22-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/1-22-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/1-22-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   