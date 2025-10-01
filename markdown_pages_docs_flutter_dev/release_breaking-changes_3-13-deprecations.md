Deprecated API removed after v3.13
==================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v3.13](/release/breaking-changes/3-13-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 3.13 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. To further aid your migration, check out this [quick reference sheet](/go/deprecations-removed-after-3-13).

Changes
-------

[#](#changes)

This section lists the deprecations by the package and affected class.

### Chip classes' useDeleteButtonTooltip

[#](#chip-classes-usedeletebuttontooltip)

Package: flutter Supported by Flutter Fix: yes

The `useDeleteButtonTooltip` property of the following classes was deprecated in v2.10:

* `DeletableChipAttributes`* `Chip`* `RawChip`* `InputChip`

`deleteButtonTooltipMessage` replaces `useDeleteButtonTooltip`. This change simplified the API, as providing an empty String to `deleteButtonTooltipMessage` achieves the same result as setting the original property `useDeleteButtonTooltip` to false. When `deleteButtonTooltipMessage` is unset, the `MaterialLocalizations.deleteButtonTooltip` is used by default.

The [Deprecate `useDeleteButtonTooltip` for Chips](https://docs.google.com/document/d/1wc9ot7T2E7hJubYxEWMX230a79wYSiFey4BHxnEzHtw/edit?usp=sharing&resourcekey=0-Bo7KPqEtkWgZcSuRCqwQ5w) design document covers this update to chips and tooltips in greater depth. To learn more, check out the [chips and tooltips migration guide](/release/breaking-changes/chip-usedeletebuttontooltip-migration).

**Migration guide**

Code before migration:

dart

```
Chip(useDeleteButtonTooltip: false);
InputChip(useDeleteButtonTooltip: true);
RawChip rawChip = RawChip();
rawChip.useDeleteButtonTooltip;
```

Code after migration:

dart

```
Chip(deleteButtonTooltipMessage: '');
InputChip();
RawChip rawChip = RawChip();
rawChip.deleteButtonTooltipMessage;
```

**References**

API documentation:

* [`DeletableChipAttributes`](https://api.flutter.dev/flutter/material/DeletableChipAttributes-class.html)* [`Chip`](https://api.flutter.dev/flutter/material/Chip-class.html)* [`RawChip`](https://api.flutter.dev/flutter/material/RawChip-class.html)* [`InputChip`](https://api.flutter.dev/flutter/material/InputChip-class.html)* [`MaterialLocalizations.deleteButtonTooltip`](https://api.flutter.dev/flutter/material/MaterialLocalizations/deleteButtonTooltip.html)

Relevant PRs:

* Deprecated in [#96174](https://github.com/flutter/flutter/pull/96174)* Removed in [#134486](https://github.com/flutter/flutter/pull/134486)

---

### MaterialButtonWithIconMixin

[#](#materialbuttonwithiconmixin)

Package: flutter Supported by Flutter Fix: no

The `MaterialButtonWithIconMixin` property was deprecated in v2.11.

With the introduction of new button classes `TextButton`, `OutlinedButton` and `ElevatedButton`, this mixin is no longer used. An earlier release removed old button classes that used this mixin. As a result, this mixin no longer affects any classes that might mix it in.

**Migration guide**

Code before migration:

dart

```
class MyButtonClass extends StatelessWidget with MaterialButtonWithIconMixin {
  // ...
}
```

Code after migration:

dart

```
class MyButtonClass extends StatelessWidget {
  // ...
}
```

**References**

Relevant PRs:

* Deprecated in [#99088](https://github.com/flutter/flutter/pull/99088)* Removed in [#133173](https://github.com/flutter/flutter/pull/133173)

---

### PlatformsViewsService.synchronizeToNativeViewHierarchy

[#](#platformsviewsservice-synchronizetonativeviewhierarchy)

Package: flutter Supported by Flutter Fix: no

The static method `synchronizeToNativeViewHierarchy` of `PlatformsViewsService` was deprecated in v2.11.

During the deprecation period, the method was a no-op function as it was no longer required to call for performance improvements. References to the method should be removed and won't impact the application.

**Migration guide**

Code before migration:

dart

```
await PlatformsViewsService.synchronizeToNativeViewHierarchy(false);
```

Code after migration:

dart

**References**

API documentation:

* [`PlatformViewsService`](https://api.flutter.dev/flutter/services/PlatformViewsService-class.html)

Relevant PRs:

* Deprecated in [#100990](https://github.com/flutter/flutter/pull/100990)* Removed in [#133175](https://github.com/flutter/flutter/pull/133175)

---

### TextSelectionOverlay.fadeDuration

[#](#textselectionoverlay-fadeduration)

Package: flutter Supported by Flutter Fix: yes

The static `fadeDuration` property of `TextSelectionOverlay` was deprecated in v2.12.

The `SelectionOverlay.fadeDuration` property replaces `TextSelectionOverlay.fadeDuration`. With the `TextSelectionOverlay` refactor, `SelectionOverlay` was added as a more generic widget without the specific dependency on `RenderEditable`.

**Migration guide**

Code before migration:

dart

```
TextSelectionOverlay.fadeDuration;
```

Code after migration:

dart

```
SelectionOverlay.fadeDuration;
```

**References**

API documentation:

* [`TextSelectionOverlay`](https://api.flutter.dev/flutter/widgets/TextSelectionOverlay-class.html)* [`SelectionOverlay`](https://api.flutter.dev/flutter/widgets/SelectionOverlay-class.html)

Relevant PRs:

* Deprecated in [#100381](https://github.com/flutter/flutter/pull/100381)* Removed in [#134485](https://github.com/flutter/flutter/pull/134485)

---

### androidOverscrollIndicator

[#](#androidoverscrollindicator)

Package: flutter Supported by Flutter Fix: no

The `androidOverscrollIndicator` property of the following classes was deprecated in v2.13:

* `ScrollBehavior`* `MaterialScrollBehavior`* `ThemeData`

This flag was introduced to allow users to configure scrolling widgets to use the `GlowingOverscrollIndicator` or the `StretchingOvercrollIndicator`. It was deprecated in favor of the `ThemeData.useMaterial3` flag as the framework introduced more support for Material 3-styled widgets.

Since `ThemeData.useMaterial3` is `true` by default, the `StretchingOverscrollIndicator` is applied by default. Setting this value to `false` will apply a `GlowingOverscrollIndicator` instead.

Alternatively, the `buildOverscrollIndicator` method of `ScrollBehavior` or `MaterialScrollBehavior` can be overridden to further alter the appearance of overscroll indicators.

**Migration guide**

Code before migration:

dart

```
MaterialApp(
  scrollBehavior: MaterialScrollBehavior(
    androidOverscrollIndicator: AndroidOverscrollIndicator.glow,
  ),
  //...
);

MaterialApp(
  scrollBehavior: ScrollBehavior(
    androidOverscrollIndicator: AndroidOverscrollIndicator.glow,
  ),
  //...
);

MaterialApp(
  theme: Theme.light().copyWith(
    androidOverscrollIndicator: AndroidOverscrollIndicator.glow,
  ),
  //...
);
```

Code after migration:

dart

```
MaterialApp(
  theme: Theme.light().copyWith(
    // defaults to true and stretching indicator,
    // false results in glowing indicator
    useMaterial3: false,
  ),
  //...
);
```

**References**

API documentation:

* [`ScrollBehavior`](https://api.flutter.dev/flutter/widgets/ScrollBehavior-class.html)* [`MaterialScrollBehavior`](https://api.flutter.dev/flutter/material/MaterialScrollBehavior-class.html)* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)* [`GlowingOverscrollIndicator`](https://api.flutter.dev/flutter/widgets/GlowingOverscrollIndicator-class.html)* [`StretchingOverscrollIndicator`](https://api.flutter.dev/flutter/widgets/StretchingOverscrollIndicator-class.html)

Relevant PRs:

* Deprecated in [#100234](https://github.com/flutter/flutter/pull/100234)* Removed in [#133181](https://github.com/flutter/flutter/pull/133181)

---

### Updates to ImageProvider and PaintingBinding

[#](#updates-to-imageprovider-and-paintingbinding)

Package: flutter Supported by Flutter Fix: no

The `instantiateImageCodec` method of `PaintingBinding`, as well as the `load` method of `ImageProvider` and the associated `DecoderCallback` were all deprecated in v2.13.

The respective replacements are:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Deprecated Method Current Method|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `PaintingBinding.instantiateImageCodec` `PaintingBinding.instantiateImageCodecFromBuffer`| `ImageProvider.load` `ImageProvider.loadBuffer`| `DecoderCallback` `DecoderBufferCallback` | | | | | | | |

This change enabled faster performance in image loading by using a buffer.

**Migration guide**

Code before migration:

dart

```
PaintingBinding.instance.instantiateImageCodec
```

Code after migration:

dart

```
PaintingBinding.instance.instantiateImageCodecFromBuffer
```

**References**

API documentation:

* [`PaintingBinding`](https://api.flutter.dev/flutter/painting/PaintingBinding-mixin.html)* [`ImageProvider`](https://api.flutter.dev/flutter/painting/ImageProvider-class.html)* [`DecoderBufferCallback`](https://api.flutter.dev/flutter/painting/DecoderBufferCallback.html)

Relevant PRs:

* Deprecated in [#103496](https://github.com/flutter/flutter/pull/103496)* Removed in [#132679](https://github.com/flutter/flutter/pull/132679)

---

### TestWindow properties

[#](#testwindow-properties)

Package: flutter\_test Supported by Flutter Fix: no

To prepare for multi-window support, many deprecated properties of `TestWindow` have been removed. While `TestWindow` has been deprecated, it does not qualify for removal at this time. Migrating the expired properties now will help in migrating from `TestWindow`.

The following properties were removed:

* `localeTestValue`* `clearLocaleTestValue`* `localesTestValue`* `clearLocalesTestValue`* `initialLifecycleStateTestValue`* `textScaleFactorTestValue`* `clearTextScaleFactorTestValue`* `platformBrightnessTestValue`* `clearPlatformBrightnessTestValue`* `alwaysUse24HourFormatTestValue`* `clearAlwaysUse24HourTestValue`* `brieflyShowPasswordTestValue`* `defaultRouteNameTestValue`* `clearDefaultRouteNameTestValue`* `semanticsEnabledTestValue`* `clearSemanticsEnabledTestValue`* `accessibilityFeaturesTestValue`* `clearAccessibilityFeaturesTestValue`

To learn more about this `TestWindow` update, check out [`TestWindow` migration guide](/release/breaking-changes/window-singleton).

**Migration guide**

Code before migration:

dart

```
testWidgets('My test', (WidgetTester tester) aysnc {
  // For all instances, replace window with platformDispatcher
  tester.binding.window.textScaleFactorTestValue = 42;
  addTearDown(tester.binding.window.clearTextScaleFactorTestValue);
  // ...
});
```

Code after migration:

dart

```
testWidgets('My test', (WidgetTester tester) aysnc {
  // For all instances, replace window with platformDispatcher
  tester.binding.platformDispatcher.textScaleFactorTestValue = 42;
  addTearDown(tester.binding.platformDispatcher.clearTextScaleFactorTestValue);
  // ...
});
```

**References**

API documentation:

* [`WidgetTester`](https://api.flutter.dev/flutter/flutter_test/WidgetTester-class.html)* [`TestWidgetsFlutterBinding`](https://api.flutter.dev/flutter/flutter_test/TestWidgetsFlutterBinding-class.html)* [`TestPlatformDispatcher`](https://api.flutter.dev/flutter/flutter_test/TestPlatformDispatcher-class.html)

Relevant PRs:

* Deprecated in [#99443](https://github.com/flutter/flutter/pull/99443)* Removed in [#131098](https://github.com/flutter/flutter/pull/131098)

---

Timeline
--------

[#](#timeline)

In stable release: 3.16

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-13-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-13-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-13-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-13-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-13-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-13-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-13-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   