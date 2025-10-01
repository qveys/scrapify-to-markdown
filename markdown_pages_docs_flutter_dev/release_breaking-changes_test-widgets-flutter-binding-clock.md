TestWidgetsFlutterBinding.clock change
======================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [TestWidgetsFlutterBinding.clock change](/release/breaking-changes/test-widgets-flutter-binding-clock)

Summary
-------

[#](#summary)

The `TestWidgetsFlutterBinding.clock` now comes from `package:clock` and not `package:quiver`.

Context
-------

[#](#context)

The `flutter_test` package is removing its dependency on the heavier weight `quiver` package in favor of a dependency on two more targeted and lighter weight packages, `clock` and `fake_async`.

This can affect user code which grabs the clock from a `TestWidgetsFlutterBinding` and passes that to an API that expects a `Clock` from `package:quiver`, for example some code like this:

dart

```
testWidgets('some test', (WidgetTester tester) {
  someApiThatWantsAQuiverClock(tester.binding.clock);
});
```

Migration guide
---------------

[#](#migration-guide)

The error you might see after this change looks something like this:

```
Error: The argument type 'Clock/*1*/' can't be assigned to the parameter type 'Clock/*2*/'.
 - 'Clock/*1*/' is from 'package:clock/src/clock.dart' ('<pub-cache>/clock/lib/src/clock.dart').
 - 'Clock/*2*/' is from 'package:quiver/time.dart' ('<pub-cache>/quiver/lib/time.dart').
```

### Option #1: Create a package:quiver Clock from a package:clock Clock

[#](#option-1-create-a-package-quiver-clock-from-a-package-clock-clock)

The easiest migration is to create a `package:quiver` clock from the `package:clock` clock, which can be done by passing the `.now` function tearoff to the `Clock` constructor:

Code before migration:

dart

```
testWidgets('some test', (WidgetTester tester) {
  someApiThatWantsAQuiverClock(tester.binding.clock);
});
```

Code after migration:

dart

```
testWidgets('some test', (WidgetTester tester) {
  someApiThatWantsAQuiverClock(Clock(tester.binding.clock.now));
});
```

### Option #2: Change the api to accept a package:clock Clock

[#](#option-2-change-the-api-to-accept-a-package-clock-clock)

If you own the api you are calling, you may want to change it to accept a `Clock` from `package:clock`. This is a judgement call based on how many places are calling this API with something other than a clock retrieved from a `TestWidgetsFlutterBinding`.

If you go this route, your call sites that are passing `tester.binding.clock` won't need to be modified, but other call sites will.

### Option #3: Change the API to accept a `DateTime function()`

[#](#option-3-change-the-api-to-accept-a-datetime-function)

If you only use the `Clock` for its `now` function, and you control the API, then you can also change it to accept that function directly instead of a `Clock`. This makes it easily callable with either type of `Clock`, by passing a tearoff of the `now` method from either type of clock:

Calling code before migration:

dart

```
testWidgets('some test', (WidgetTester tester) {
  someApiThatWantsAQuiverClock(tester.binding.clock);
});
```

Calling code after migration:

dart

```
testWidgets('some test', (WidgetTester tester) {
  modifiedApiThatTakesANowFunction(tester.binding.clock.now);
});
```

Timeline
--------

[#](#timeline)

Landed in version: 1.18.0  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`TestWidgetsFlutterBinding`](https://api.flutter.dev/flutter/flutter_test/TestWidgetsFlutterBinding-class.html)

Relevant PRs:

* [PR 54125](https://github.com/flutter/flutter/pull/54125): remove flutter\_test quiver dep, use fake\_async and clock instead

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/test-widgets-flutter-binding-clock/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-widgets-flutter-binding-clock.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/test-widgets-flutter-binding-clock/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-widgets-flutter-binding-clock.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-widgets-flutter-binding-clock.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/test-widgets-flutter-binding-clock/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-widgets-flutter-binding-clock.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   