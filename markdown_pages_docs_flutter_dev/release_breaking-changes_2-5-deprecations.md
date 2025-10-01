Deprecated API removed after v2.5
=================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v2.5](/release/breaking-changes/2-5-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 2.5 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. A [quick reference sheet](/go/deprecations-removed-after-2-5) is available as well.

Changes
-------

[#](#changes)

This section lists the deprecations by affected class.

---

### `autovalidate` of `Form` & related classes

[#](#autovalidate-of-form-related-classes)

Supported by Flutter Fix: yes

`autovalidate` was deprecated in v1.19.

Use `autovalidateMode` instead. Where `autovalidate` was true, replace with `AutovalidateMode.always`. Where `autovalidate` was false, replace with `AutovalidateMode.disabled`. This change allows more behaviors to be specified beyond the original binary choice, adding `AutovalidateMode.onUserInteraction` as an additional option.

The following classes all have the same change of API:

* `Form`* `FormField`* `DropdownButtonFormField`* `TextFormField`

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/form-field-autovalidation-api)

Code before migration:

dart

```
const Form form = Form(autovalidate: true);
const Form form = Form(autovalidate: false);
final autoMode = form.autovalidate;

const FormField formField = FormField(autovalidate: true);
const FormField formField = FormField(autovalidate: false);
final autoMode = formField.autovalidate;

const TextFormField textFormField = TextFormField(autovalidate: true);
const TextFormField textFormField = TextFormField(autovalidate: false);

const DropdownButtonFormField dropDownButtonFormField = DropdownButtonFormField(autovalidate: true);
const DropdownButtonFormField dropdownButtonFormField = DropdownButtonFormField(autovalidate: false);
```

Code after migration:

dart

```
const Form form = Form(autovalidateMode: AutovalidateMode.always);
const Form form = Form(autovalidateMode: AutovalidateMode.disabled);
final autoMode = form.autovalidateMode;

const FormField formField = FormField(autovalidateMode: AutovalidateMode.always);
const FormField formField = FormField(autovalidateMode: AutovalidateMode.disabled);
final autoMode = formField.autovalidateMode;

const TextFormField textFormField = TextFormField(autovalidateMode: AutovalidateMode.always);
const TextFormField textFormField = TextFormField(autovalidateMode: AutovalidateMode.disabled);

const DropdownButtonFormField dropDownButtonFormField = DropdownButtonFormField(autovalidateMode: AutovalidateMode.always);
const DropdownButtonFormField dropdownButtonFormField = DropdownButtonFormField(autovalidateMode: AutovalidateMode.disabled);
```

**References**

API documentation:

* [`Form`](https://api.flutter.dev/flutter/widgets/Form-class.html)* [`FormField`](https://api.flutter.dev/flutter/widgets/FormField-class.html)* [`TextFormField`](https://api.flutter.dev/flutter/material/TextFormField-class.html)* [`DropdownButtonFormField`](https://api.flutter.dev/flutter/material/DropdownButtonFormField-class.html)* [`AutovalidateMode`](https://api.flutter.dev/flutter/widgets/AutovalidateMode-class.html)

Relevant issues:

* [Issue 56363](https://github.com/flutter/flutter/issues/56363)* [Issue 18885](https://github.com/flutter/flutter/issues/18885)* [Issue 15404](https://github.com/flutter/flutter/issues/15404)* [Issue 36154](https://github.com/flutter/flutter/issues/36154)* [Issue 48876](https://github.com/flutter/flutter/issues/48876)

Relevant PRs:

* Deprecated in [#59766](https://github.com/flutter/flutter/pull/59766)* Removed in [#90292](https://github.com/flutter/flutter/pull/90292)

---

### `FloatingHeaderSnapConfiguration.vsync`

[#](#floatingheadersnapconfiguration-vsync)

Supported by Flutter Fix: no

The `TickerProvider` `vsync` property of `FloatingHeaderSnapConfiguration` was deprecated in v1.19.

The `vsync` for the animation should instead be specified using `SliverPersistentHeaderDelegate.vsync`.

**Migration guide**

Code before migration:

dart

```
class MySliverPersistentHeaderDelegate extends SliverPersistentHeaderDelegate {
  FloatingHeaderSnapConfiguration? get snapConfiguration => FloatingHeaderSnapConfiguration(vsync: myTickerProvider);
}
```

Code after migration:

dart

```
class MySliverPersistentHeaderDelegate extends SliverPersistentHeaderDelegate {
  FloatingHeaderSnapConfiguration? get snapConfiguration => FloatingHeaderSnapConfiguration();
  TickerProvider? get vsync => myTickerProvider;
}
```

**References**

Design document:

* [Control SliverPersistentHeader's showOnScreen Behavior](https://docs.google.com/document/d/1BZhxy176uUnqOCnXdnHM1XetS9mw9WIyUAOE-dgVdUM/edit?usp=sharing)

API documentation:

* [`FloatingHeaderSnapConfiguration`](https://api.flutter.dev/flutter/rendering/FloatingHeaderSnapConfiguration-class.html)* [`SliverPersistentHeaderDelegate`](https://api.flutter.dev/flutter/widgets/SliverPersistentHeaderDelegate-class.html)* [`TickerProvider`](https://api.flutter.dev/flutter/scheduler/TickerProvider-class.html)

Relevant issues:

* [Issue 25507](https://github.com/flutter/flutter/issues/25507)

Relevant PRs:

* Deprecated in [#56413](https://github.com/flutter/flutter/pull/56413)* Removed in [#90293](https://github.com/flutter/flutter/pull/90293)

---

### `AndroidViewController` & subclasses' `id`

[#](#androidviewcontroller-subclasses-id)

Supported by Flutter Fix: yes

The `id` of `AndroidViewController`, `TextureAndroidViewController`, and `SurfaceAndroidViewController`, was deprecated in v1.20.

For all of these use cases, `viewId` should be used instead.

**Migration guide**

Code before migration:

dart

```
final SurfaceAndroidViewController surfaceController = SurfaceAndroidViewController(
  viewId: 10,
  viewType: 'FixTester',
  layoutDirection: TextDirection.ltr,
);
int viewId = surfaceController.id;
final SurfaceAndroidViewController surfaceController = SurfaceAndroidViewController(
  error: '',
);
final TextureAndroidViewController textureController = TextureAndroidViewController(
  error: '',
);
final TextureAndroidViewController textureController = TextureAndroidViewController(
  viewId: 10,
  viewType: 'FixTester',
  layoutDirection: TextDirection.ltr,
);
viewId = textureController.id;
```

Code after migration:

dart

```
final SurfaceAndroidViewController surfaceController = SurfaceAndroidViewController(
  viewId: 10,
  viewType: 'FixTester',
  layoutDirection: TextDirection.ltr,
);
int viewId = surfaceController.viewId;
final SurfaceAndroidViewController surfaceController = SurfaceAndroidViewController(
  error: '',
);
final TextureAndroidViewController textureController = TextureAndroidViewController(
  error: '',
);
final TextureAndroidViewController textureController = TextureAndroidViewController(
  viewId: 10,
  viewType: 'FixTester',
  layoutDirection: TextDirection.ltr,
);
viewId = textureController.viewId;
```

**References**

Design document:

* [Flutter Hybrid Composition](https://github.com/flutter/flutter/blob/main/docs/platforms/Hybrid-Composition.md)

API documentation:

* [`AndroidViewController`](https://api.flutter.dev/flutter/services/AndroidViewController-class.html)* [`TextureAndroidViewController`](https://api.flutter.dev/flutter/services/TextureAndroidViewController-class.html)* [`SurfaceAndroidViewController`](https://api.flutter.dev/flutter/services/SurfaceAndroidViewController-class.html)

Relevant issues:

* [Issue 55218](https://github.com/flutter/flutter/issues/55218)

Relevant PRs:

* Deprecated in [#60320](https://github.com/flutter/flutter/issues/60320)* Removed in [#90294](https://github.com/flutter/flutter/issues/90294)

---

### `BlacklistingTextInputFormatter` & `WhitelistingTextInputFormatter`

[#](#blacklistingtextinputformatter-whitelistingtextinputformatter)

Supported by Flutter Fix: no

The entire classes of `BlacklistingTextInputFormatter` and `WhitelistingTextInoutFormatter` were deprecated in v1.20.

Their functionality has been rewritten into a single class, `FilteringTextInputFormatter`.

**Migration guide**

Code before migration:

dart

```
formatter = BlacklistingTextInputFormatter(pattern, replacementString: 'replacedPattern');
formatter = BlacklistingTextInputFormatter.singleLineFormatter;
pattern = formatter.blacklistedPattern;
formatter = WhitelistingTextInputFormatter(pattern);
formatter = WhitelistingTextInputFormatter.digitsOnly;
pattern = formatter.whitelistedPattern;
```

Code after migration:

dart

```
formatter = FilteringTextInputFormatter.deny(pattern, replacementString: 'replacedPattern');
formatter = FilteringTextInputFormatter.singleLineFormatter;
pattern = formatter.filterPattern;
formatter = FilteringTextInputFormatter.allow(pattern);
formatter = FilteringTextInputFormatter.digitsOnly;
pattern = formatter.filterPattern;
```

**References**

API documentation:

* [`FilteringTextInputFormatter`](https://api.flutter.dev/flutter/services/FilteringTextInputFormatter-class.html)

Relevant PRs:

* Deprecated in [#59120](https://github.com/flutter/flutter/issues/59120)* Removed in [#90296](https://github.com/flutter/flutter/issues/90296)

---

### `BottomNavigationBarItem.title`

[#](#bottomnavigationbaritem-title)

Supported by Flutter Fix: yes

The `title` of `BottomNavigationBarItem` was deprecated in v1.19. The `label` property should be used instead. This migration allows for better text scaling, and presents built-in `Tooltip`s for the `BottomNavigationBarItem` in the context of a `BottomNavigationBar`.

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/form-field-autovalidation-api)

Code before migration:

dart

```
const BottomNavigationBarItem bottomNavigationBarItem = BottomNavigationBarItem(title: myTitle);
const BottomNavigationBarItem bottomNavigationBarItem = BottomNavigationBarItem();
bottomNavigationBarItem.title;
```

Code after migration:

dart

```
const BottomNavigationBarItem bottomNavigationBarItem = BottomNavigationBarItem(label: myTitle);
const BottomNavigationBarItem bottomNavigationBarItem = BottomNavigationBarItem();
bottomNavigationBarItem.label;
```

**References**

Design document:

* [BottomNavigationBarItem title](/go/bottom-navigation-bar-title-deprecation)

API documentation:

* [`BottomNavigationBarItem`](https://api.flutter.dev/flutter/widgets/BottomNavigationBarItem-class.html)* [`BottomNavigationBar`](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html)* [`Tooltip`](https://api.flutter.dev/flutter/material/Tooltip-class.html)

Relevant PRs:

* Deprecated in [#59127](https://github.com/flutter/flutter/issues/59127)* Removed in [#90295](https://github.com/flutter/flutter/issues/90295)

---

### `packageRoot` in `dart:core`, `dart:isolate`, and `package:platform`

[#](#packageroot-in-dart-core-dart-isolate-and-package-platform)

The following APIs have been removed:

* [`Platform.packageRoot`](https://api.dart.dev/stable/2.15.1/dart-io/Platform/packageRoot.html) in `dart:core`* [`Isolate.packageRoot`](https://api.dart.dev/stable/2.15.1/dart-isolate/Isolate/packageRoot.html) in `dart:isolate`* [`Platform.packageRoot`](https://api.dart.dev/stable/2.15.1/dart-io/Platform/packageRoot.html) in `package:platform`

These APIs were marked deprecated [in Dart 2.0](https://dart-review.googlesource.com/c/sdk/+/59100/16/CHANGELOG.md), and did not work correctly in any Dart 2.x release.

**Migration guide**

These `packageRoot` APIs have been replaced by a new set of `packageConfig` APIs, which you should migrate to.

* [`Platform.packageConfig`](https://api.dart.dev/stable/2.15.1/dart-io/Platform/packageConfig.html) in `dart:core`* [`Isolate.packageConfig`](https://api.dart.dev/stable/2.15.1/dart-isolate/Isolate/packageConfig.html) in `dart:isolate`* [`Platform.packageConfig`](https://api.dart.dev/stable/2.15.1/dart-io/Platform/packageConfig.html) in `package:platform`

If you are using the `package:platform` package, note that regardless of whether you are using the `packageRoot` API or not, older versions of that package are not compatible with Dart 2.16 and later, as they depend on the now removed `packageRoot` API. You may see an error like this when attempting to run your app:

```
../../.pub-cache/hosted/pub.dartlang.org/platform-3.0.0/
  lib/src/interface/local_platform.dart:46:19:
  Error: Member not found: 'packageRoot'.
      io.Platform.packageRoot; // ignore: deprecated_member_use
                  ^^^^^^^^^^^
```

To resolve that, upgrade to version `3.1.0` or later of `package:platform` by upgrading the constraint in your `pubspec.yaml` file:

yaml

```
dependencies:
  platform: ^3.1.0
```

**References**

Relevant PRs:

* Removed from the Dart libraries in [#47769](https://github.com/dart-lang/sdk/issues/47769)* Removed from `package:platform` in [PR #38](https://github.com/google/platform.dart/pull/38)* Updated Flutter to use `package:platform` 3.1.0 in [PR #94603](https://github.com/flutter/flutter/pull/94603)

---

Timeline
--------

[#](#timeline)

In stable release: 2.10

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-5-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-5-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-5-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-5-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-5-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-5-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-5-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   