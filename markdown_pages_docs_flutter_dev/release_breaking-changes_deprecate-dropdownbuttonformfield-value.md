Deprecated the 'value' parameter of the 'DropdownButtonFormField' constructor
=============================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated the 'value' parameter of the 'DropdownButtonFormField' constructor](/release/breaking-changes/deprecate-dropdownbuttonformfield-value)

Summary
-------

[#](#summary)

The `value` parameter of the [`DropdownButtonFormField`](https://api.flutter.dev/flutter/material/DropdownButtonFormField/DropdownButtonFormField.html) constructor was deprecated in favor of the `initialValue` parameter.

Context
-------

[#](#context)

The `value` parameter of the [`DropdownButtonFormField`](https://api.flutter.dev/flutter/material/DropdownButtonFormField/DropdownButtonFormField.html) constructor was used to initialize [`DropdownButtonFormField.initialValue`](https://main-api.flutter.dev/flutter/widgets/FormField/initialValue.html). Not using the same name was confusing. For example, developers falsely assumed that setting `value` would change the current selected value. This was not the case—it only set the initial value or when the field is reset.

Description of change
---------------------

[#](#description-of-change)

The `value` parameter of the [`DropdownButtonFormField`](https://api.flutter.dev/flutter/material/DropdownButtonFormField/DropdownButtonFormField.html) constructor is deprecated in favor of the parameter named `initialValue`.

Migration guide
---------------

[#](#migration-guide)

Replace the `value` parameter of the [`DropdownButtonFormField`](https://api.flutter.dev/flutter/material/DropdownButtonFormField/DropdownButtonFormField.html) constructor with the `initialValue` parameter to initialize [`DropdownButtonFormField.initialValue`](https://main-api.flutter.dev/flutter/widgets/FormField/initialValue.html).

Code before migration:

dart

```
DropdownButtonFormField(
  value: 'Yellow',
),
```

Code after migration:

dart

```
DropdownButtonFormField(
  initialValue: 'Yellow',
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.35.0-0.0.pre  
 In stable release: 3.35

References
----------

[#](#references)

API documentation:

* [`DropdownButtonFormField`](https://api.flutter.dev/flutter/material/DropdownButtonFormField/DropdownButtonFormField.html)* [`DropdownButtonFormField.initialValue`](https://main-api.flutter.dev/flutter/widgets/FormField/initialValue.html)

Relevant issues:

* [Issue #169983](https://github.com/flutter/flutter/issues/169983)

Relevant PRs:

* [Deprecate `DropdownButtonFormField` `value` parameter in favor of `initialValue`](https://github.com/flutter/flutter/pull/170805)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-dropdownbuttonformfield-value/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-dropdownbuttonformfield-value.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-dropdownbuttonformfield-value/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-dropdownbuttonformfield-value.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-dropdownbuttonformfield-value.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-dropdownbuttonformfield-value/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-dropdownbuttonformfield-value.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   