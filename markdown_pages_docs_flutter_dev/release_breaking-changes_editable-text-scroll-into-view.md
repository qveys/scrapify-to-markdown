Updated EditableText scroll into view behavior
==============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Updated EditableText scroll into view behavior](/release/breaking-changes/editable-text-scroll-into-view)

Summary
-------

[#](#summary)

The `Editable.onCaretChanged` callback is removed. With this change, `EditableText` behavior for scrolling the selection into view changes.

Context
-------

[#](#context)

Previously, upon scrolling into view to show user updates, `EditableText` used multiple mechanisms to determine the extent of the selection or the caret location.

Description of change
---------------------

[#](#description-of-change)

By removing the `Editable.onCaretChanged` callback, `EditableText` will always use the most up-to-date selection extent location when scrolling to show it. Specifically, this improves scroll into view behavior after changing selection from collapsed to non-collapsed using `userUpdateTextEditingValue()`.

Timeline
--------

[#](#timeline)

Landed in version: 3.12.0-4.0.pre  
 In stable release: 3.13.0

References
----------

[#](#references)

API documentation:

* [`EditableText`](https://api.flutter.dev/flutter/widgets/EditableText-class.html)

Relevant PRs:

* [109114: Remove Editable.onCaretChanged callback](https://github.com/flutter/flutter/pull/109114)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/editable-text-scroll-into-view/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/editable-text-scroll-into-view.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/editable-text-scroll-into-view/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/editable-text-scroll-into-view.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/editable-text-scroll-into-view.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/editable-text-scroll-into-view/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/editable-text-scroll-into-view.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   