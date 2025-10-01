Remove invalid parameters for `InputDecoration.collapsed`
=========================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Remove invalid parameters for `InputDecoration.collapsed`](/release/breaking-changes/input-decoration-collapsed)

Summary
-------

[#](#summary)

`InputDecoration.collapsed` invalid parameters `floatingLabelBehavior` and `floatingLabelAlignment` are deprecated.

Background
----------

[#](#background)

`InputDecoration.collapsed` constructor is used to create a minimal decoration without a label.

The parameters `floatingLabelAlignment` and `floatingLabelBehavior` have no effect because an input decoration created using `InputDecoration.collapsed` has no label.

Migration guide
---------------

[#](#migration-guide)

To migrate, remove usage of `floatingLabelBehavior` and `floatingLabelAlignment` parameters when calling the `InputDecoration.collapsed` constructor. Those parameters had no effect.

Code before migration:

dart

```
InputDecoration.collapsed(
  hintText: 'Hint',
  floatingLabelAlignment: FloatingLabelAlignment.center,
  floatingLabelBehavior: FloatingLabelBehavior.auto,
),
```

Code after migration:

dart

```
InputDecoration.collapsed(
  hintText: 'Hint',
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.24.0-0.1.pre  
 In stable release: 3.27.0

References
----------

[#](#references)

API documentation:

* [`InputDecoration.collapsed`](https://api.flutter.dev/flutter/material/InputDecoration/InputDecoration.collapsed.html)* [`InputDecoration.floatingLabelAlignment`](https://api.flutter.dev/flutter/material/InputDecoration/floatingLabelAlignment.html)* [`InputDecoration.floatingLabelBehavior`](https://api.flutter.dev/flutter/material/InputDecoration/floatingLabelBehavior.html)

Relevant issues:

* [Add prefixIcon and suffixIcon parameters to InputDecoration.collapsed](https://github.com/flutter/flutter/issues/61331)

Relevant PRs:

* [Deprecate invalid InputDecoration.collapsed parameters](https://github.com/flutter/flutter/pull/152486)* [Cleanup InputDecoration.collapsed constructor](https://github.com/flutter/flutter/pull/152165)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/input-decoration-collapsed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/input-decoration-collapsed.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/input-decoration-collapsed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/input-decoration-collapsed.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-12-16. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/input-decoration-collapsed.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/input-decoration-collapsed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/input-decoration-collapsed.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   