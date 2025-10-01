Rename MaterialState to WidgetState
===================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Rename MaterialState to WidgetState](/release/breaking-changes/material-state)

Summary
-------

[#](#summary)

`MaterialState`, and its related APIs, have been moved out of the Material library and renamed to `WidgetState`.

Background
----------

[#](#background)

Previously, `MaterialState` provided logic for handling multiple different states a widget could have, like "hovered", "focused", and "disabled". Because this functionality is useful outside the Material library, namely for the base Widgets layer and Cupertino, it was decided to move it outside of Material. As part of the move, and to avoid future confusion, the different `MaterialState` classes have been renamed to `WidgetState`. The behavior of the two are the same.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Before Now|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `MaterialState` `WidgetState`| `MaterialStatePropertyResolver` `WidgetStatePropertyResolver`| `MaterialStateColor` `WidgetStateColor`| `MaterialStateMouseCursor` `WidgetStateColorMouseCursor`| `MaterialStateBorderSide` `WidgetStateBorderSide`| `MaterialStateOutlinedBorder` `WidgetStateOutlinedBorder`| `MaterialStateTextStyle` `WidgetStateTextStyle`| `MaterialStateProperty` `WidgetStateProperty`| `MaterialStatePropertyAll` `WidgetStatePropertyAll`| `MaterialStatesController` `WidgetStatesController` | | | | | | | | | | | | | | | | | | | | | |

The classes `MaterialStateOutlineInputBorder` and `MaterialStateUnderlineInputBorder` were left in the Material library with no `WidgetState` equivalent, as they are specific to Material design.

Migration guide
---------------

[#](#migration-guide)

A [Flutter fix](/tools/flutter-fix) is available to help migrate the `MaterialState` classes to `WidgetState`.

To migrate, replace `MaterialState` with `WidgetState`.

Code before migration:

dart

```
MaterialState selected = MaterialState.selected;

final MaterialStateProperty<Color> backgroundColor;

class _MouseCursor extends MaterialStateMouseCursor{
  const _MouseCursor(this.resolveCallback);

  final MaterialPropertyResolver<MouseCursor?> resolveCallback;

  @override
  MouseCursor resolve(Set<MaterialState> states) => resolveCallback(states) ?? MouseCursor.uncontrolled;
}

BorderSide side = MaterialStateBorderSide.resolveWith((Set<MaterialState> states) {
  if (states.contains(MaterialState.selected)) {
    return const BorderSide(color: Colors.red);
  }
  return null;
});
```

Code after migration:

dart

```
WidgetState selected = WidgetState.selected;

final WidgetStateProperty<Color> backgroundColor;

class _MouseCursor extends WidgetStateMouseCursor{
  const _MouseCursor(this.resolveCallback);

  final WidgetPropertyResolver<MouseCursor?> resolveCallback;

  @override
  MouseCursor resolve(Set<WidgetState> states) => resolveCallback(states) ?? MouseCursor.uncontrolled;
}

BorderSide side = WidgetStateBorderSide.resolveWith((Set<WidgetState> states) {
  if (states.contains(WidgetState.selected)) {
    return const BorderSide(color: Colors.red);
  }
  return null;
});
```

Timeline
--------

[#](#timeline)

Landed in version: 3.21.0-11.0.pre  
 In stable release: 3.22.0

References
----------

[#](#references)

Relevant issues:

* [Create widgets level support for State](https://github.com/flutter/flutter/issues/138270)

Relevant PRs:

* [Widget State Properties](https://github.com/flutter/flutter/pull/142151)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-state/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-state.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-state/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-state.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-05-14. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-state.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-state/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-state.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   