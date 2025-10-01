Web-specific golden comparisons are no longer supported
=======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Web-specific golden comparisons are no longer supported](/release/breaking-changes/web-golden-comparator)

Summary
-------

[#](#summary)

The `flutter_test` package and `flutter` tool will no longer use the [`webGoldenComparator`](https://api.flutter.dev/flutter/flutter_test/webGoldenComparator.html) top-level variable, and instead use the original [`goldenFileComparator`](https://api.flutter.dev/flutter/flutter_test/goldenFileComparator.html) top-level variable (like the non-web platforms).

For *users* of `flutter_test`, these changes will be made automatically.

Background
----------

[#](#background)

Originally, [`WebGoldenComparator`](https://api.flutter.dev/flutter/flutter_test/WebGoldenComparator-class.html) was added for the HTML-backend of Flutter web, as it was not possible to create an encoded PNG (byte buffer), and a new API was needed. As [the HTML backend is being deprecated and removed](https://github.com/flutter/flutter/issues/145954), this separate API is no longer necessary.

Migration guide
---------------

[#](#migration-guide)

For most users, no changes are required (other than migrating off the HTML backend, which is not covered here), the `flutter` tool will automatically configure [`goldenFileComparator`](https://api.flutter.dev/flutter/flutter_test/goldenFileComparator.html) and use it (when using a non-HTML web backend).

For users that implement a custom [`WebGoldenComparator`](https://api.flutter.dev/flutter/flutter_test/webGoldenComparator.html), you will migrate the implemenation to [`GoldenFileComparator`](https://api.flutter.dev/flutter/flutter_test/goldenFileComparator.html). Fortunately the Canvas Kit and SkWasm backends already required similar methods (`compareButes` and `updateBytes`).

For example:

dart

```
// Before
class MyWebGoldenComparator extends WebGoldenComparator {
  @override
  Future<bool> compare(double width, double height, Uri golden) {
    // will be removed in the migration
  }

  @override
  Future<bool> update(double width, double height, Uri golden) {
    // will be removed in the migration
  }

  @override
  Future<bool> compareBytes(Uint8List bytes, Uri golden) {
    // will be renamed "compare"
  }

  @override
  Future<bool> updateBytes(Uint8List bytes, Uri golden) {
    // will be renamed "update" and the parameter orders swapped
  }
}

// After
class MyGenericGoldenComparator extends GoldenFileComparator {
  @override
  Future<bool> compare(Uint8List bytes, Uri golden) {
    // used to be "compareBytes"
  }

  @override
  Future<bool> update(Uri golden, Uint8List bytes) {
    // used to be "updateBytes"
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.29.0-0.0.pre  
 In stable release: 3.29

References
----------

[#](#references)

Relevant Issues:

* [Issue 145954](https://github.com/flutter/flutter/issues/145954), where the HTML renderer was deprecated.* [Issue 160261](https://github.com/flutter/flutter/issues/160261), where it was proposed to consolidate `GoldenFileComparator` and `WebGoldenComparator`.

Relevant PRs:

* [PR 161196](https://github.com/flutter/flutter/pull/161196), where `WebGoldenComparator` was deprecated and the `flutter` CLI started using `goldenFileComparator`.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/web-golden-comparator/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/web-golden-comparator.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/web-golden-comparator/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/web-golden-comparator.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/web-golden-comparator.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/web-golden-comparator/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/web-golden-comparator.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   