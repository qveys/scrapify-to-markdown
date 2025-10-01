At least one clipboard data variant must be provided
====================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [At least one clipboard data variant must be provided](/release/breaking-changes/clipboard-data-required)

Summary
-------

[#](#summary)

The [`ClipboardData constructor`](https://api.flutter.dev/flutter/services/ClipboardData/ClipboardData.html)'s `text` argument is no longer nullable. Code that provides `null` to the `text` argument must be migrated to provide an empty string `''`.

Context
-------

[#](#context)

In preparation for supporting multiple clipboard data variants, the `ClipboardData` constructor now requires that at least one data variant is provided.

Previously, platforms were inconsistent in how they handled `null`. The behavior is now consistent across platforms. If you are interested in the low-level details, see [PR 122446](https://github.com/flutter/flutter/pull/122446).

Description of change
---------------------

[#](#description-of-change)

The [`ClipboardData constructor`](https://api.flutter.dev/flutter/services/ClipboardData/ClipboardData.html)'s `text` argument is no longer nullable.

Migration guide
---------------

[#](#migration-guide)

To reset the text clipboard, use an empty string `''` instead of `null`.

Code before migration:

dart

```
void resetClipboard() {
  Clipboard.setData(ClipboardData(text: null));
}
```

Code after migration:

dart

```
void resetClipboard() {
  Clipboard.setData(ClipboardData(text: ''));
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.10.0-9.0.pre  
 In stable release: 3.10.0

References
----------

[#](#references)

API documentation:

* [`Clipboard.setData`](https://api.flutter.dev/flutter/services/Clipboard/setData.html)* [`ClipboardData constructor`](https://api.flutter.dev/flutter/services/ClipboardData/ClipboardData.html)

Relevant PRs:

* [Assert at least one clipboard data variant is provided](https://github.com/flutter/flutter/pull/122446)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/clipboard-data-required/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clipboard-data-required.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/clipboard-data-required/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clipboard-data-required.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clipboard-data-required.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/clipboard-data-required/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clipboard-data-required.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   