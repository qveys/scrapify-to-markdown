Deprecated API removed after v2.10
==================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v2.10](/release/breaking-changes/2-10-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 2.10 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. A [quick reference sheet](/go/deprecations-removed-after-2-10) is available as well.

Changes
-------

[#](#changes)

This section lists the deprecations by affected class.

---

### `maxLengthEnforced` of `TextField` & related classes

[#](#maxlengthenforced-of-textfield-related-classes)

Supported by Flutter Fix: yes

`maxLengthEnforced` was deprecated in v1.25.

Use `maxLengthEnforcement` instead. Where `maxLengthEnforced` was true, replace with `MaxLengthEnforcement.enforce`. Where `maxLengthEnforced` was false, replace with `MaxLengthEnforcement.none`. This change allows more behaviors to be specified beyond the original binary choice, adding `MaxLengthEnforcement.truncateAfterCompositionEnds` as an additional option.

The following classes all have the same change of API:

* `TextField`* `TextFormField`* `CupertinoTextField`

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/use-maxLengthEnforcement-instead-of-maxLengthEnforced)

Code before migration:

dart

```
const TextField textField = TextField(maxLengthEnforced: true);
const TextField textField = TextField(maxLengthEnforced: false);
final lengthEnforced = textField.maxLengthEnforced;

const TextFormField textFormField = TextFormField(maxLengthEnforced: true);
const TextFormField textFormField = TextFormField(maxLengthEnforced: false);
final lengthEnforced = textFormField.maxLengthEnforced;

const CupertinoTextField cupertinoTextField = CupertinoTextField(maxLengthEnforced: true);
const CupertinoTextField cupertinoTextField = CupertinoTextField(maxLengthEnforced: false);
final lengthEnforced = cupertinoTextField.maxLengthEnforced;
```

Code after migration:

dart

```
const TextField textField = TextField(maxLengthEnforcement: MaxLengthEnforcement.enforce);
const TextField textField = TextField(maxLengthEnforcement: MaxLengthEnforcement.none);
final lengthEnforced = textField.maxLengthEnforcement;

const TextFormField textFormField = TextFormField(maxLengthEnforcement: MaxLengthEnforcement.enforce);
const TextFormField textFormField = TextFormField(maxLengthEnforcement: MaxLengthEnforcement.none);
final lengthEnforced = textFormField.maxLengthEnforcement;

const CupertinoTextField cupertinoTextField = CupertinoTextField(maxLengthEnforcement: MaxLengthEnforcement.enforce);
const CupertinoTextField cupertinoTextField = CupertinoTextField(maxLengthEnforcement: MaxLengthEnforcement.none);
final lengthEnforced = cupertinoTextField.maxLengthEnforcement;
```

**References**

API documentation:

* [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html)* [`TextFormField`](https://api.flutter.dev/flutter/material/TextFormField-class.html)* [`CupertinoTextField`](https://api.flutter.dev/flutter/cupertino/CupertinoTextField-class.html)

Relevant issues:

* [Issue 67898](https://github.com/flutter/flutter/issues/67898)

Relevant PRs:

* Deprecated in [#68086](https://github.com/flutter/flutter/pull/68086)* Removed in [#98539](https://github.com/flutter/flutter/pull/98539)

---

### `VelocityTracker` constructor

[#](#velocitytracker-constructor)

Supported by Flutter Fix: yes

The default constructor for `VelocityTracker`was deprecated in v1.22.

The `VelocityTracker.withKind()` should be used instead. This allows for a `PointerDeviceKind` to be specified for the tracker. The previous default for `VelocityTracker.kind` was `PointerDeviceKind.touch`.

**Migration guide**

Code before migration:

dart

```
final VelocityTracker tracker = VelocityTracker();
```

Code after migration:

dart

```
final VelocityTracker tracker = VelocityTracker.withKind(PointerDeviceKind.touch);
```

**References**

API documentation:

* [`VelocityTracker`](https://api.flutter.dev/flutter/gestures/VelocityTracker-class.html)* [`PointerDeviceKind`](https://api.flutter.dev/flutter/dart-ui/PointerDeviceKind.html)

Relevant PRs:

* Deprecated in [#66043](https://github.com/flutter/flutter/pull/66043)* Removed in [#98541](https://github.com/flutter/flutter/pull/98541)

---

### `DayPicker` & `MonthPicker`

[#](#daypicker-monthpicker)

Supported by Flutter Fix: no

The `DayPicker` and `MonthPicker` widgets were first deprecated in v1.15, and then extended in v1.26.

They have been replaced by one comprehensive widget, `CalendarDatePicker`.

These widgets were displayed using the `showDatePicker` method. This method was migrated to present the new `CalendarDatePicker` before this release, and so their final removal should not necessitate further action.

**References**

Design document:

* [Material Date Picker Redesign](/go/material-date-picker-redesign)

API documentation:

* [`CalendarDatePicker`](https://api.flutter.dev/flutter/material/CalendarDatePicker-class.html)* [`showDatePicker`](https://api.flutter.dev/flutter/material/showDatePicker.html)

Relevant issues:

* [Issue 50133](https://github.com/flutter/flutter/issues/50133)

Relevant PRs:

* Deprecated in [#50546](https://github.com/flutter/flutter/issues/50546)* Removed in [#98543](https://github.com/flutter/flutter/issues/98543)

---

### `FlatButton`, `RaisedButton`, & `OutlineButton`

[#](#flatbutton-raisedbutton-outlinebutton)

Supported by Flutter Fix: no

The `FlatButton`, `RaisedButton`, and `OutlineButton` widgets were first deprecated in v1.20, and then extended in v1.26.

They are replaced by new buttons, `TextButton`, `ElevatedButton`, and `OutlinedButton`. These new widgets also use new associated themes, rather than the generic `ButtonTheme`.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Old Widget Old Theme New Widget New Theme|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `FlatButton` `ButtonTheme` `TextButton` `TextButtonTheme`| `RaisedButton` `ButtonTheme` `ElevatedButton` `ElevatedButtonTheme`| `OutlineButton` `ButtonTheme` `OutlinedButton` `OutlinedButtonTheme` | | | | | | | | | | | | | | | |

**Migration guide**

[In-depth migration guide available for detailed styling](/release/breaking-changes/buttons)

Code before migration:

dart

```
FlatButton(
  onPressed: onPressed,
  child: Text('Button'),
  // ...
);

RaisedButton(
  onPressed: onPressed,
  child: Text('Button'),
  // ...
);

OutlineButton(
  onPressed: onPressed,
  child: Text('Button'),
  // ...
);
```

Code after migration:

dart

```
TextButton(
  onPressed: onPressed,
  child: Text('Button'),
  // ...
);

ElevatedButton(
  onPressed: onPressed,
  child: Text('Button'),
  // ...
);

OutlinedButton(
  onPressed: onPressed,
  child: Text('Button'),
  // ...
);
```

**References**

Design document:

* [New Material buttons and themes](/go/material-button-migration-guide)

API documentation:

* [`ButtonStyle`](https://api.flutter.dev/flutter/material/ButtonStyle-class.html)* [`ButtonStyleButton`](https://api.flutter.dev/flutter/material/ButtonStyleButton-class.html)* [`ElevatedButton`](https://api.flutter.dev/flutter/material/ElevatedButton-class.html)* [`ElevatedButtonTheme`](https://api.flutter.dev/flutter/material/ElevatedButtonTheme-class.html)* [`ElevatedButtonThemeData`](https://api.flutter.dev/flutter/material/ElevatedButtonThemeData-class.html)* [`OutlinedButton`](https://api.flutter.dev/flutter/material/OutlinedButton-class.html)* [`OutlinedButtonTheme`](https://api.flutter.dev/flutter/material/OutlinedButtonTheme-class.html)* [`OutlinedButtonThemeData`](https://api.flutter.dev/flutter/material/OutlinedButtonThemeData-class.html)* [`TextButton`](https://api.flutter.dev/flutter/material/TextButton-class.html)* [`TextButtonTheme`](https://api.flutter.dev/flutter/material/TextButtonTheme-class.html)* [`TextButtonThemeData`](https://api.flutter.dev/flutter/material/TextButtonThemeData-class.html)

Relevant PRs:

* New API added in [#59702](https://github.com/flutter/flutter/issues/59702)* Deprecated in [#73352](https://github.com/flutter/flutter/issues/73352)* Removed in [#98546](https://github.com/flutter/flutter/issues/98546)

---

### `Scaffold` `SnackBar` methods

[#](#scaffold-snackbar-methods)

Supported by Flutter Fix: no

The following `Scaffold` `SnackBar` methods were deprecated in v1.23.

* `showSnackBar`* `removeCurrentSnackBar`* `hideCurrentSnackBar`

The same named methods of the `ScaffoldMessenger` should be used instead. A default `ScaffoldMessenger` is already created in every `MaterialApp`.

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/use-maxLengthEnforcement-instead-of-maxLengthEnforced)

Code before migration:

dart

```
Scaffold.of(context).showSnackBar(mySnackBar);
Scaffold.of(context).removeCurrentSnackBar(mySnackBar);
Scaffold.of(context).hideCurrentSnackBar(mySnackBar);
```

Code after migration:

dart

```
ScaffoldMessenger.of(context).showSnackBar(mySnackBar);
ScaffoldMessenger.of(context).removeCurrentSnackBar(mySnackBar);
ScaffoldMessenger.of(context).hideCurrentSnackBar(mySnackBar);
```

**References**

Design document:

* [ScaffoldMessenger Design](/go/scaffold-messenger)

Video content:

* [SnackBar Delivery](https://youtu.be/sYG7HAGu_Eg?t=10271)* [Widget of the Week](https://youtu.be/lytQi-slT5Y)

API documentation:

* [`ScaffoldMessenger`](https://api.flutter.dev/flutter/material/ScaffoldMessenger-class.html)* [`SnackBar`](https://api.flutter.dev/flutter/material/SnackBar-class.html)

Relevant issues:

* [Issue 57218](https://github.com/flutter/flutter/issues/57218)* [Issue 62921](https://github.com/flutter/flutter/issues/62921)

Relevant PRs:

* New API added in [#64101](https://github.com/flutter/flutter/issues/64101)* Deprecated in [#67947](https://github.com/flutter/flutter/issues/67947)* Removed in [#98549](https://github.com/flutter/flutter/issues/98549)

---

### `RectangularSliderTrackShape.disabledThumbGapWidth`

[#](#rectangularslidertrackshape-disabledthumbgapwidth)

Supported by Flutter Fix: yes

The `RectangularSliderTrackShape.disabledThumbGapWidth` was first deprecated in v1.5, and then extended in v1.26.

This was no longer used by the framework, as the animation of the slider thumb no longer occurs when disabled.

**Migration guide**

Code before migration:

dart

```
RectangularSliderTrackShape(disabledThumbGapWidth: 2.0);
```

Code after migration:

dart

```
RectangularSliderTrackShape();
```

**References**

API documentation:

* [`RectangularSliderTrackShape`](https://api.flutter.dev/flutter/material/RectangularSliderTrackShape-class.html)

Relevant PRs:

* Animation changed in [#30390](https://github.com/flutter/flutter/issues/30390)* Deprecated in [#65246](https://github.com/flutter/flutter/issues/65246)* Removed in [#98613](https://github.com/flutter/flutter/issues/98613)

---

### Text selection of `ThemeData` to `TextSelectionThemeData`

[#](#text-selection-of-themedata-to-textselectionthemedata)

Supported by Flutter Fix: yes

The following `ThemeData` members were first deprecated in v1.23, and extended in v1.26.

* `useTextSelectionTheme`* `textSelectionColor`* `cursorColor`* `textSelectionHandleColor`

These should be replaced by a more comprehensive `TextSelectionThemeData`, which is now specified in `ThemeData` itself.

The `useTextSelectionTheme` flag served as a temporary migration flag to distinguish the two APIs, it can be removed now.

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/use-maxLengthEnforcement-instead-of-maxLengthEnforced)

Code before migration:

dart

```
ThemeData(
  useTextSelectionTheme: false,
  textSelectionColor: Colors.blue,
  cursorColor: Colors.green,
  textSelectionHandleColor: Colors.red,
);
```

Code after migration:

dart

```
ThemeData(
  textSelectionTheme: TextSelectionThemeData(
    selectionColor: Colors.blue,
    cursorColor: Colors.green,
    selectionHandleColor: Colors.red,
  ),
);
```

**References**

Design document:

* [Text Selection Theme](/go/text-selection-theme)

API documentation:

* [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html)* [`TextSelectionThemeData`](https://api.flutter.dev/flutter/material/TextSelectionThemeData-class.html)

Relevant issues:

* [Issue 17635](https://github.com/flutter/flutter/issues/17635)* [Issue 56082](https://github.com/flutter/flutter/issues/56082)* [Issue 61227](https://github.com/flutter/flutter/issues/61227)

Relevant PRs:

* New API added in [#62014](https://github.com/flutter/flutter/issues/62014)* Deprecated in [#66485](https://github.com/flutter/flutter/issues/66482)* Removed in [#98578](https://github.com/flutter/flutter/issues/98578)

---

### `RenderEditable.onSelectionChanged` to `TextSelectionDelegate.textEditingValue`

[#](#rendereditable-onselectionchanged-to-textselectiondelegate-texteditingvalue)

Supported by Flutter Fix: no

`RenderEditable.onSelectionChanged` and `TextSelectionDelegate.textEditingValue` were deprecated in v1.26.

Instead of calling one or both of these methods, call `TextSelectionDelegate.userUpdateTextEditingValue`. This fixed a bug where the `TextInputFormatter` would receive the wrong selection value.

**Migration guide**

Code before migration:

dart

```
renderEditable.onSelectionChanged(selection, renderObject, cause);
textSelectionDelegate.textEditingValue = value;
```

Code after migration:

dart

```
textSelectionDelegate.userUpdateTextEditingValue(value, cause);
```

**References**

API documentation:

* [`RenderEditable`](https://api.flutter.dev/flutter/rendering/RenderEditable-class.html)* [`TextSelectionDelegate`](https://api.flutter.dev/flutter/services/TextSelectionDelegate-mixin.html)

Relevant issues:

* Resolved [#75505](https://github.com/flutter/flutter/issues/75502)

Relevant PRs:

* Deprecated in [#75541](https://github.com/flutter/flutter/issues/75541)* Removed in [#98582](https://github.com/flutter/flutter/issues/98582)

---

### `Stack.overflow`

[#](#stack-overflow)

Supported by Flutter Fix: yes

`Stack.overflow`, as well as the `Overflow` enum were deprecated in v1.22.

The replacement is `Stack.clipBehavior`, a change made as part of unifying clip behaviors and semantics across the framework. Where `Overflow.visible` was used, use `Clip.none`. Where `Overflow.clip` was used, use `Clip.hardEdge`.

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/use-maxLengthEnforcement-instead-of-maxLengthEnforced)

Code before migration:

dart

```
const Stack stack = Stack(overflow: Overflow.visible);
const Stack stack = Stack(overflow: Overflow.clip);
```

Code after migration:

dart

```
const Stack stack = Stack(clipBehavior: Clip.none);
const Stack stack = Stack(clipBehavior: Clip.hardEdge);
```

**References**

API documentation:

* [`Stack`](https://api.flutter.dev/flutter/widgets/Stack-class.html)* [`Clip`](https://api.flutter.dev/flutter/dart-ui/Clip.html)

Relevant issues:

* Resolved [#66030](https://github.com/flutter/flutter/issues/66030)

Relevant PRs:

* Deprecated in [#66305](https://github.com/flutter/flutter/issues/66305)* Removed in [#98583](https://github.com/flutter/flutter/issues/98583)

---

### `UpdateLiveRegionEvent`

[#](#updateliveregionevent)

Supported by Flutter Fix: no

The `SemanticsEvent` `UpdateLiveRegionEvent`, was first deprecated in v1.12, and then extended in v1.26.

This was never implemented by the framework, and any references should be removed.

**References**

API documentation:

* [`SemanticsEvent`](https://api.flutter.dev/flutter/semantics/SemanticsEvent-class.html)

Relevant PRs:

* Deprecated in [#45940](https://github.com/flutter/flutter/issues/45940)* Removed in [#98615](https://github.com/flutter/flutter/issues/98615)

---

### `RenderObjectElement` methods

[#](#renderobjectelement-methods)

Supported by Flutter Fix: yes

The following `RenderObjectElement` methods were deprecated in v1.21.

* `insertChildRenderObject`* `moveChildRenderObject`* `removeChildRenderObject`

These methods are replaced, respectively, by:

* `insertRenderObjectChild`* `moveRenderObjectChild`* `removeRenderObjectChild`

These changes were made as a soft breaking deprecation in order to change the function signature.

**Migration guide**

Code before migration:

dart

```
element.insertChildRenderObject(child, slot);
element.moveChildRenderObject(child, slot);
element.removeChildRenderObject(child);
```

Code after migration:

dart

```
element.insertRenderObjectChild(child, slot);
element.moveRenderObjectChild(child, oldSlot, newSlot);
element.removeRenderObjectChild(child, slot);
```

**References**

API documentation:

* [`RenderObjectElement`](https://api.flutter.dev/flutter/widgets/RenderObjectElement-class.html)

Relevant issues:

* [Issue 63269](https://github.com/flutter/flutter/issues/63269)

Relevant PRs:

* Deprecated in [#64254](https://github.com/flutter/flutter/issues/64254)* Removed in [#98616](https://github.com/flutter/flutter/issues/98616)

---

Timeline
--------

[#](#timeline)

In stable release: 3.0.0

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-10-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-10-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-10-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-10-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-10-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-10-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-10-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   