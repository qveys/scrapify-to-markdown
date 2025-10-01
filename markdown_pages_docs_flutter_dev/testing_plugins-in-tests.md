Plugins in Flutter tests
========================

1. [Testing & debugging](/testing) chevron\_right- [Plugin tests](/testing/plugins-in-tests)

*info* Note

To learn how to avoid crashes from a plugin when testing your Flutter app, read on. To learn how to test your plugin code, check out [Testing plugins](/testing/testing-plugins).

Almost all [Flutter plugins](/packages-and-plugins/using-packages) have two parts:

* Dart code, which provides the API your code calls.* Code written in a platform-specific (or "host") language, such as Kotlin or Swift, which implements those APIs.

In fact, the native (or host) language code distinguishes a plugin package from a standard package.

Building and registering the host portion of a plugin is part of the Flutter application build process, so plugins only work when your code is running in your application, such as with `flutter run` or when running [integration tests](/cookbook/testing/integration/introduction). When running [Dart unit tests](/cookbook/testing/unit/introduction) or [widget tests](https://api.flutter.dev/flutter/flutter_test/flutter_test-library.html), the host code isn't available. If the code you are testing calls any plugins, this often results in errors like the following:

```
MissingPluginException(No implementation found for method someMethodName on channel some_channel_name)
```

*info* Note

Plugin implementations that [only use Dart](/packages-and-plugins/developing-packages#dart-only-platform-implementations) will work in unit tests. This is an implementation detail of the plugin, however, so tests shouldn't rely on it.

When unit testing code that uses plugins, there are several options to avoid this exception. The following solutions are listed in order of preference.

Wrap the plugin
---------------

[#](#wrap-the-plugin)

In most cases, the best approach is to wrap plugin calls in your own API, and provide a way of [mocking](/cookbook/testing/unit/mocking) your own API in tests.

This has several advantages:

* If the plugin API changes, you won't need to update your tests.* You are only testing your own code, so your tests can't fail due to behavior of a plugin you're using.* You can use the same approach regardless of how the plugin is implemented, or even for non-plugin package dependencies.

Mock the plugin's public API
----------------------------

[#](#mock-the-plugins-public-api)

If the plugin's API is already based on class instances, you can mock it directly, with the following caveats:

* This won't work if the plugin uses non-class functions or static methods.* Tests will need to be updated when the plugin API changes.

Mock the plugin's platform interface
------------------------------------

[#](#mock-the-plugins-platform-interface)

If the plugin is a [federated plugin](/packages-and-plugins/developing-packages#federated-plugins), it will include a platform interface that allows registering implementations of its internal logic. You can register a mock of that platform interface implementation instead of the public API with the following caveats:

* This won't work if the plugin isn't federated.* Your tests will include part of the plugin's code, so plugin behavior could cause problems for your tests. For instance, if a plugin writes files as part of an internal cache, your test behavior might change based on whether you had run the test previously.* Tests might need to be updated when the platform interface changes.

An example of when this might be necessary is mocking the implementation of a plugin used by a package that you rely on, rather than your own code, so you can't change how it's called. However, if possible, you should mock the dependency that uses the plugin instead.

Mock the platform channel
-------------------------

[#](#mock-the-platform-channel)

If the plugin uses [platform channels](/platform-integration/platform-channels), you can mock the platform channels using [`TestDefaultBinaryMessenger`](https://api.flutter.dev/flutter/flutter_test/TestDefaultBinaryMessenger-class.html). This should only be used if, for some reason, none of the methods above are available, as it has several drawbacks:

* Only implementations that use platform channels can be mocked. This means that if some implementations don't use platform channels, your tests will unexpectedly use real implementations when run on some platforms.* Platform channels are usually internal implementation details of plugins. They might change substantially even in a bugfix update to a plugin, breaking your tests unexpectedly.* Platform channels might differ in each implementation of a federated plugin. For instance, you might set up mock platform channels to make tests pass on a Windows machine, then find that they fail if run on macOS or Linux.* Platform channels aren't strongly typed. For example, method channels often use dictionaries and you have to read the plugin's implementation to know what the key strings and value types are.

Because of these limitations, `TestDefaultBinaryMessenger` is mainly useful in the internal tests of plugin implementations, rather than tests of code using plugins.

You might also want to check out [Testing plugins](/testing/testing-plugins).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/plugins-in-tests/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/plugins-in-tests.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/plugins-in-tests/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/plugins-in-tests.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/testing/plugins-in-tests.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/testing/plugins-in-tests/&page-source=https://github.com/flutter/website/tree/main/src/content/testing/plugins-in-tests.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   