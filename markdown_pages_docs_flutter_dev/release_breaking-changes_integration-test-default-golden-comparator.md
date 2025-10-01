Integration test default golden-file comparators changed on Android and iOS.
============================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Integration test default golden-file comparators changed on Android and iOS.](/release/breaking-changes/integration-test-default-golden-comparator)

Summary
-------

[#](#summary)

Unless a user-defined [`goldenFileComparator`](https://api.flutter.dev/flutter/flutter_test/goldenFileComparator.html) is set, either manually in a test, or using a `flutter_test_config.dart` file, Android and iOS devices and emulators/simulators have a new default that proxies to the local host filesystem, fixing a long-standing bug ([#143299](https://github.com/flutter/flutter/issues/143299)).

Background
----------

[#](#background)

The package [`integration_test`](https://api.flutter.dev/flutter/package-integration_test_integration_test/), and its integration with [`flutter_test`](https://api.flutter.dev/flutter/flutter_test) has historically had a bug where using [`matchesGoldenFile`](https://api.flutter.dev/flutter/flutter_test/MatchesGoldenFile-class.html) or similar APIs where a `FileSystemException` was thrown.

Some users may have worked around this issue by writing and using a custom [`goldenFileComparator`](https://api.flutter.dev/flutter/flutter_test/goldenFileComparator.html):

dart

```
import 'package:integration_test/integration_test.dart';
import 'package:my_integration_test/custom_golden_file_comparator.dart';

void main() {
  goldenFileComparator = CustomGoldenFileComparatorThatWorks();

  // ...
}
```

Such workarounds are no longer necessary, and if type checking the default, will no longer work as before:

dart

```
if (goldenFileComparator is ...) {
  // The new default is a new (hidden) type that has not existed before.
}
```

Migration guide
---------------

[#](#migration-guide)

In most cases, we expect users to have to do nothing - this will be in a sense *new* functionality that replaced functionality that did not work and caused an unhandled exception which would fail a test.

In cases where users wrote custom test infrastructure and comparators, consider instead removing the [`goldenFileComparator`](https://api.flutter.dev/flutter/flutter_test/goldenFileComparator.html) overrides, and instead rely on the (new) default which should work as expected:

```
import 'package:integration_test/integration_test.dart';
-import 'package:my_integration_test/custom_golden_file_comparator.dart';

void main() {
-  goldenFileComparator = CustomGoldenFileComparatorThatWorks();

  // ...
}
```

*Fun fact*: The existing code that was used for the *web* platform was [reused](https://github.com/flutter/flutter/pull/160484).

Timeline
--------

[#](#timeline)

Landed in version: 3.29.0-0.0.pre  
 Stable release: 3.32

References
----------

[#](#references)

Relevant APIs:

* [`flutter_test`](https://api.flutter.dev/flutter/flutter_test), which talks about `flutter_test_config.dart` and its capabilities.* [`goldenFileComparator`](https://api.flutter.dev/flutter/flutter_test/goldenFileComparator.html), which implements comparison, and is user-configurable.

Relevant Issues:

* [Issue 143299](https://github.com/flutter/flutter/issues/143299), one of many user reports about the long-standing bug.* [Issue 160043](https://github.com/flutter/flutter/issues/160043), which explains in technical detail why [`matchesGoldenFile`](https://api.flutter.dev/flutter/flutter_test/MatchesGoldenFile-class.html) failed.

Relevant PRs:

* [PR 160215](https://github.com/flutter/flutter/pull/160215), where the web tool implementation was refactored to make it generic.* [PR 160484](https://github.com/flutter/flutter/pull/160484), which uses the Dart VM service protocol to proxy between device and host.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/integration-test-default-golden-comparator/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/integration-test-default-golden-comparator.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/integration-test-default-golden-comparator/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/integration-test-default-golden-comparator.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/integration-test-default-golden-comparator.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/integration-test-default-golden-comparator/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/integration-test-default-golden-comparator.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   