Deprecate `InputDecoration.maintainHintHeight` in favor of `InputDecoration.maintainHintSize`
=============================================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecate `InputDecoration.maintainHintHeight` in favor of `InputDecoration.maintainHintSize`](/release/breaking-changes/deprecate-inputdecoration-maintainhintheight)

Summary
-------

[#](#summary)

The [`InputDecoration.maintainHintHeight`](https://api.flutter.dev/flutter/material/InputDecoration/maintainHintHeight.html) parameter was deprecated in favor of the [`InputDecoration.maintainHintSize`](https://main-api.flutter.dev/flutter/material/InputDecoration/maintainHintSize.html) parameter.

Context
-------

[#](#context)

The default intrinsic size of an input decorator depends on the hint size. The [`InputDecoration.maintainHintSize`](https://main-api.flutter.dev/flutter/material/InputDecoration/maintainHintSize.html) parameter can be set to `false` to make the intrinsic size ignores the hint size when the hint isn't visible. Previously, the `InputDecoration.maintainHintHeight` parameter was used to override the default intrinsic height and had no impact on the intrinsic width.

Description of change
---------------------

[#](#description-of-change)

The [`InputDecoration.maintainHintHeight`](https://api.flutter.dev/flutter/material/InputDecoration/maintainHintHeight.html) is deprecated in favor of [`InputDecoration.maintainHintSize`](https://main-api.flutter.dev/flutter/material/InputDecoration/maintainHintSize.html) which makes both the intrinsic width and height depend on the hint dimensions.

Migration guide
---------------

[#](#migration-guide)

Replace [`InputDecoration.maintainHintHeight`](https://api.flutter.dev/flutter/material/InputDecoration/maintainHintHeight.html) with [`InputDecoration.maintainHintSize`](https://main-api.flutter.dev/flutter/material/InputDecoration/maintainHintSize.html) to override the default intrinsic size computation.

Code before migration:

dart

```
TextField(
  indicator: InputDecoration(
    maintainHintHeight: false,
  ),
),
```

Code after migration:

dart

```
TextField(
  indicator: InputDecoration(
    maintainHintSize: false,
  ),
),
```

Timeline
--------

[#](#timeline)

Landed in version: 3.30.0-0.0.pre  
 In stable release: 3.32

References
----------

[#](#references)

API documentation:

* [`InputDecoration.maintainHintHeight`](https://api.flutter.dev/flutter/material/InputDecoration/maintainHintHeight.html)* [`InputDecoration.maintainHintSize`](https://main-api.flutter.dev/flutter/material/InputDecoration/maintainHintSize.html)

Relevant issues:

* [Issue #93337](https://github.com/flutter/flutter/issues/93337)

Relevant PRs:

* [Fix TextField intrinsic width when hint is not visible](https://github.com/flutter/flutter/pull/161235)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-inputdecoration-maintainhintheight/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-inputdecoration-maintainhintheight.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-inputdecoration-maintainhintheight/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-inputdecoration-maintainhintheight.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-inputdecoration-maintainhintheight.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-inputdecoration-maintainhintheight/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-inputdecoration-maintainhintheight.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   