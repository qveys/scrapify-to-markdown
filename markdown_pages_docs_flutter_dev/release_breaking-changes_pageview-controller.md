Make PageView.controller nullable
=================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Make PageView.controller nullable](/release/breaking-changes/pageview-controller)

Summary
-------

[#](#summary)

If a controller isn't provided in the constructor, the `controller` member is `null`. This makes `PageView` and its `controller` property consistent with other widgets.

Migration guide
---------------

[#](#migration-guide)

Before:

dart

```
pageView.controller.page
```

After:

dart

```
pageView.controller!.page
```

Timeline
--------

[#](#timeline)

Landed in version: 3.19.0-12.0.pre  
 In stable release: 3.22.0

References
----------

[#](#references)

Relevant issues:

* [PageView uses global controller, that is never disposed. (Issue 141119)](https://github.com/flutter/flutter/issues/141119)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/pageview-controller/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/pageview-controller.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/pageview-controller/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/pageview-controller.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-05-14. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/pageview-controller.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/pageview-controller/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/pageview-controller.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   