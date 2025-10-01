Testing Flutter apps
====================

1. [Testing & debugging](/testing) chevron\_right- [Testing Flutter apps](/testing/overview)

The more features your app has, the harder it is to test manually. Automated tests help ensure that your app performs correctly before you publish it, while retaining your feature and bug fix velocity.

*info* Note

For hands-on practice of testing Flutter apps, see the [How to test a Flutter app](https://codelabs.developers.google.com/codelabs/flutter-app-testing) codelab.

Automated testing falls into a few categories:

* A [*unit test*](#unit-tests) tests a single function, method, or class.* A [*widget test*](#widget-tests) (in other UI frameworks referred to as *component test*) tests a single widget.* An [*integration test*](#integration-tests) tests a complete app or a large part of an app.

Generally speaking, a well-tested app has many unit and widget tests, tracked by [code coverage](https://en.wikipedia.org/wiki/Code_coverage), plus enough integration tests to cover all the important use cases. This advice is based on the fact that there are trade-offs between different kinds of testing, seen below.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tradeoff Unit Widget Integration|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Confidence** Low Higher Highest|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Maintenance cost** Low Higher Highest|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | **Dependencies** Few More Most|  |  |  |  | | --- | --- | --- | --- | | **Execution speed** Quick Quick Slow | | | | | | | | | | | | | | | | | | | |

Unit tests
----------

[#](#unit-tests)

A *unit test* tests a single function, method, or class. The goal of a unit test is to verify the correctness of a unit of logic under a variety of conditions. External dependencies of the unit under test are generally [mocked out](/cookbook/testing/unit/mocking). Unit tests generally don't read from or write to disk, render to screen, or receive user actions from outside the process running the test. For more information regarding unit tests, you can view the following recipes or run `flutter test --help` in your terminal.

*info* Note

If you're writing unit tests for code that uses plugins and you want to avoid crashes, check out [Plugins in Flutter tests](/testing/plugins-in-tests). If you want to test your Flutter plugin, check out [Testing plugins](/testing/testing-plugins).

### Recipes

[#](#recipes)

* [An introduction to unit testing](/cookbook/testing/unit/introduction/)* [Mock dependencies using Mockito](/cookbook/testing/unit/mocking/)

Widget tests
------------

[#](#widget-tests)

A *widget test* (in other UI frameworks referred to as *component test*) tests a single widget. The goal of a widget test is to verify that the widget's UI looks and interacts as expected. Testing a widget involves multiple classes and requires a test environment that provides the appropriate widget lifecycle context.

For example, the Widget being tested should be able to receive and respond to user actions and events, perform layout, and instantiate child widgets. A widget test is therefore more comprehensive than a unit test. However, like a unit test, a widget test's environment is replaced with an implementation much simpler than a full-blown UI system.

### Recipes

[#](#recipes-1)

* [Handle scrolling](/cookbook/testing/widget/scrolling/)* [Test orientation](/cookbook/testing/widget/orientation/)* [Find widgets](/cookbook/testing/widget/finders/)* [An introduction to widget testing](/cookbook/testing/widget/introduction/)* [Tap, drag, and enter text](/cookbook/testing/widget/tap-drag/)

Integration tests
-----------------

[#](#integration-tests)

An *integration test* tests a complete app or a large part of an app. The goal of an integration test is to verify that all the widgets and services being tested work together as expected. Furthermore, you can use integration tests to verify your app's performance.

Generally, an *integration test* runs on a real device or an OS emulator, such as iOS Simulator or Android Emulator. The app under test is typically isolated from the test driver code to avoid skewing the results.

For more information on how to write integration tests, see the [integration testing page](/testing/integration-tests).

### Recipes

[#](#recipes-2)

* [Measure performance with an integration test](/cookbook/testing/integration/profiling/)* [Integration testing concepts](/cookbook/testing/integration/introduction/)

Continuous integration services
-------------------------------

[#](#continuous-integration-services)

Continuous integration (CI) services allow you to run your tests automatically when pushing new code changes. This provides timely feedback on whether the code changes work as expected and do not introduce bugs.

For information on running tests on various continuous integration services, see the following:

* [Continuous delivery using fastlane with Flutter](/deployment/cd#fastlane)* [Test Flutter apps on Appcircle](https://blog.appcircle.io/article/flutter-ci-cd-github-ios-android-web#)* [Test Flutter apps on Travis](https://blog.flutter.dev/test-flutter-apps-on-travis-3fd5142ecd8c)* [Test Flutter apps on Cirrus](https://cirrus-ci.org/examples/#flutter)* [Codemagic CI/CD for Flutter](https://blog.codemagic.io/getting-started-with-codemagic/)* [Flutter CI/CD with Bitrise](https://devcenter.bitrise.io/en/getting-started/quick-start-guides/getting-started-with-flutter-apps)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/overview/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/overview.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/overview/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/overview.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-07-07. [View source](https://github.com/flutter/website/tree/main/src/content/testing/overview.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/overview/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/overview.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   