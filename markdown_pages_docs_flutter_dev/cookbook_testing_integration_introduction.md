Integration testing concepts
============================

1. [Cookbook](/cookbook) chevron\_right- [Testing](/cookbook/testing) chevron\_right- [Integration](/cookbook/testing/integration) chevron\_right- [Introduction](/cookbook/testing/integration/introduction)

Unit tests and widget tests validate individual classes, functions, or widgets. They don't validate how individual pieces work together in whole or capture the performance of an app running on a real device. To perform these tasks, use *integration tests*.

Integration tests verify the behavior of the complete app. This test can also be called end-to-end testing or GUI testing.

The Flutter SDK includes the [integration\_test](https://github.com/flutter/flutter/tree/main/packages/integration_test) package.

Terminology
-----------

[#](#terminology)

**host machine**: The system on which you develop your app, like a desktop computer. **target device**: The mobile device, browser, or desktop application that runs your Flutter app. If you run your app in a web browser or as a desktop application, the host machine and the target device are the same.

Dependent package
-----------------

[#](#dependent-package)

To run integration tests, add the `integration_test` package as a dependency for your Flutter app test file.

To migrate existing projects that use `flutter_driver`, consult the [Migrating from flutter\_driver](/release/breaking-changes/flutter-driver-migration) guide.

Tests written with the `integration_test` package can perform the following tasks.

* Run on the target device. To test multiple Android or iOS devices, use Firebase Test Lab.* Run from the host machine with `flutter test integration_test`.* Use `flutter_test` APIs. This makes integration tests similar to writing [widget tests](/testing/overview#widget-tests).

Use cases for integration testing
---------------------------------

[#](#use-cases-for-integration-testing)

The other guides in this section explain how to use integration tests to validate [functionality](/testing/integration-tests/) and [performance](/cookbook/testing/integration/profiling/).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/integration/introduction/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/introduction.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/integration/introduction/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/introduction.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/introduction.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/integration/introduction/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/introduction.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   