Updated `Checkbox.fillColor` behavior
=====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Updated `Checkbox.fillColor` behavior](/release/breaking-changes/checkbox-fillColor)

Summary
-------

[#](#summary)

The `Checkbox.fillColor` is now applied to the checkbox's background when the checkbox is unselected.

Context
-------

[#](#context)

Previously, the `Checkbox.fillColor` was applied to the checkbox's border when the checkbox was unselected and its background was transparent. With this change, the `Checkbox.fillColor` is applied to the checkbox's background and the border uses the `Checkbox.side` color when the checkbox is unselected.

Description of change
---------------------

[#](#description-of-change)

The `Checkbox.fillColor` is now applied to the checkbox's background when the checkbox is unselected instead of being used as the border color.

Migration guide
---------------

[#](#migration-guide)

The updated `Checkbox.fillColor` behavior applies the fill color to the checkbox's background in the unselected state. To get the previous behavior, set `Checbox.fillColor` to `Colors.transparent` in the unselected state and set `Checkbox.side` to the desired color.

If you use the `Checkbox.fillColor` property to customize the checkbox.

Code before migration:

dart

```
Checkbox(
  fillColor: MaterialStateProperty.resolveWith((states) {
    if (!states.contains(MaterialState.selected)) {
      return Colors.red;
    }
    return null;
  }),
  value: _checked,
  onChanged: _enabled
    ? (bool? value) {
        setState(() {
          _checked = value!;
        });
      }
    : null,
),
```

Code after migration:

dart

```
Checkbox(
  fillColor: MaterialStateProperty.resolveWith((states) {
    if (!states.contains(MaterialState.selected)) {
      return Colors.transparent;
    }
    return null;
  }),
  side: const BorderSide(color: Colors.red, width: 2),
  value: _checked,
  onChanged: _enabled
    ? (bool? value) {
        setState(() {
          _checked = value!;
        });
      }
    : null,
),
```

If you use the `CheckboxThemeData.fillColor` property to customize the checkbox.

Code before migration:

dart

```
checkboxTheme: CheckboxThemeData(
  fillColor: MaterialStateProperty.resolveWith((states) {
    if (!states.contains(MaterialState.selected)) {
      return Colors.red;
    }
    return null;
  }),
),
```

Code after migration:

dart

```
checkboxTheme: CheckboxThemeData(
  fillColor: MaterialStateProperty.resolveWith((states) {
    if (!states.contains(MaterialState.selected)) {
      return Colors.transparent;
    }
    return null;
  }),
  side: const BorderSide(color: Colors.red, width: 2),
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.10.0-17.0.pre  
 In stable release: 3.13.0

References
----------

[#](#references)

API documentation:

* [`Checkbox.fillColor`](https://api.flutter.dev/flutter/material/Checkbox/fillColor.html)

Relevant issues:

* [Add `backgroundColor` to `Checkbox` and `CheckboxThemeData`](https://github.com/flutter/flutter/issues/123386)

Relevant PRs:

* [`Checkbox.fillColor` should be applied to checkbox's background color when it is unchecked.](https://github.com/flutter/flutter/pull/125643)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/checkbox-fillColor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/checkbox-fillColor.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/checkbox-fillColor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/checkbox-fillColor.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/checkbox-fillColor.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/checkbox-fillColor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/checkbox-fillColor.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   