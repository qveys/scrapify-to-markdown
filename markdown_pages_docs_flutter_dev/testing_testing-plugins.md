Testing plugins
===============

1. [Testing & debugging](/testing) chevron\_right- [Testing plugins](/testing/testing-plugins)

All of the [usual types of Flutter tests](/testing/overview) apply to plugin packages as well, but because plugins contain native code they often also require other kinds of tests to test all of their functionality.

*info* Note

To learn how to test your plugin code, read on. To learn how to avoid crashes from a plugin when testing your Flutter app, check out [Plugins in Flutter tests](/testing/plugins-in-tests).

Types of plugin tests
---------------------

[#](#types-of-plugin-tests)

To see examples of each of these types of tests, you can [create a new plugin from the plugin template](/packages-and-plugins/developing-packages#step-1-create-the-package-1) and look in the indicated directories.

* **Dart [unit tests](/cookbook/testing/unit/introduction) and [widget tests](/cookbook/testing/widget/introduction)**. These tests allow you to test the Dart portion of your plugin just as you would test the Dart code of a non-plugin package. However, the plugin's native code [won't be loaded](/testing/plugins-in-tests), so any calls to platform channels need to be [mocked in tests](/testing/plugins-in-tests#mock-the-platform-channel).

  See the `test` directory for an example.* **Dart [integration tests](/cookbook/testing/integration/introduction)**. Since integration tests run in the context of a Flutter application (the example app), they can test both the Dart and native code, as well as the interaction between them. They are also useful for unit testing web implementation code that needs to run in a browser.

    These are often the most important tests for a plugin. However, Dart integration tests can't interact with native UI, such as native dialogs or the contents of platform views.

    See the `example/integration_test` directory for an example.* **Native unit tests.** Just as Dart unit tests can test the Dart portions of a plugin in isolation, native unit tests can test the native parts in isolation. Each platform has its own native unit test system, and the tests are written in the same native languages as the code it is testing.

      Native unit tests can be especially valuable if you need to mock out APIs wrapped by your plugin code, which isn't possible in a Dart integration test.

      You can set up and use any native test frameworks you are familiar with for each platform, but the following are already configured in the plugin template:
      + **Android**: [JUnit](https://github.com/junit-team/junit4/wiki/Getting-started) tests can be found in `android/src/test/`.+ **iOS** and **macOS**: [XCTest](https://developer.apple.com/documentation/xctest) tests can be found in `example/ios/RunnerTests/` and `example/macos/RunnerTests/` respectively. These are in the example directory, not the top-level package directory, because they are run via the example app's project.+ **Linux** and **Windows**: [GoogleTest](https://github.com/google/googletest) tests can be found in `linux/test/` and `windows/test/`, respectively.

Other types of tests, which aren't currently pre-configured in the template, are **native UI tests**. Running your application under a native UI testing framework, such as [Espresso](https://github.com/flutter/packages/tree/main/packages/espresso) or [XCUITest](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/09-ui_testing.html), enables tests that interact with both native and Flutter UI elements, so can be useful if your plugin can't be tested without native UI interactions.

Running tests
-------------

[#](#running-tests)

### Dart unit tests

[#](#dart-unit-tests)

These can be run like any other Flutter unit tests, either from your preferred Flutter IDE, or using `flutter test`.

### Integration tests

[#](#integration-tests)

For information on running this type of test, check out the [integration test documentation](/cookbook/testing/integration/introduction). The commands must be run in the `example` directory.

### Native unit tests

[#](#native-unit-tests)

For all platforms, you need to build the example application at least once before running the unit tests, to ensure that all of the platform-specific build files have been created.

**Android JUnit**  

If you have the example opened as an Android project in Android Studio, you can run the unit tests using the [Android Studio test UI](https://developer.android.com/studio/test/test-in-android-studio).

To run the tests from the command line, use the following command in the `example/android` directory:

sh

```
./gradlew testDebugUnitTest
```

**iOS and macOS XCTest**  

If you have the example app opened in Xcode, you can run the unit tests using the [Xcode Test UI](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/05-running_tests.html).

To run the tests from the command line, use the following command in the `example/ios` (for iOS) or `example/macos` (for macOS) directory:

sh

```
xcodebuild test -workspace Runner.xcworkspace -scheme Runner -configuration Debug
```

For iOS tests, you might need to first open `Runner.xcworkspace` in Xcode to configure code signing.

**Linux GoogleTest**  

To run the tests from the command line, use the following command in the example directory, replacing "my\_plugin" with your plugin project name:

sh

```
build/linux/plugins/x64/debug/my_plugin/my_plugin_test
```

If you built the example app in release mode rather than debug, replace "debug" with "release".

**Windows GoogleTest**  

If you have the example app opened in Visual Studio, you can run the unit tests using the [Visual Studio test UI](https://learn.microsoft.com/en-us/visualstudio/test/getting-started-with-unit-testing?view=vs-2022&tabs=dotnet%2Cmstest#run-unit-tests).

To run the tests from the command line, use the following command in the example directory, replacing "my\_plugin" with your plugin project name:

sh

```
build/windows/plugins/my_plugin/Debug/my_plugin_test.exe
```

If you built the example app in release mode rather than debug, replace "Debug" with "Release".

What types of tests to add
--------------------------

[#](#what-types-of-tests-to-add)

The [general advice for testing Flutter projects](/testing/overview) applies to plugins as well. Some extra considerations for plugin testing:

* Since only integration tests can test the communication between Dart and the native languages, try to have at least one integration test of each platform channel call.* If some flows can't be tested using integration tests—for example if they require interacting with native UI or mocking device state—consider writing "end to end" tests of the two halves using unit tests:
    + Native unit tests that set up the necessary mocks, then call into the method channel entry point with a synthesized call and validate the method response.+ Dart unit tests that mock the platform channel, then call the plugin's public API and validate the results.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/testing-plugins/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/testing-plugins.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/testing-plugins/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/testing-plugins.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/testing/testing-plugins.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/testing-plugins/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/testing-plugins.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   