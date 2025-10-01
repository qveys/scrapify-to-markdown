TestTextInput state reset
=========================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [TestTextInput state reset](/release/breaking-changes/test-text-input)

Summary
-------

[#](#summary)

The state of a `TestTextInput` instance, a stub for the system's onscreen keyboard, is now reset between tests.

Context
-------

[#](#context)

The Flutter test framework uses a class called `TestTextInput` to track and manipulate editing state in a widgets test. Individual tests can make calls that modify the internal state of this object, sometimes indirectly (such as by setting their own handlers on `SystemChannels.textInput`). Subsequent tests might then check the state of `WidgetTester.testTextInput` and get unexpected values.

Description of change
---------------------

[#](#description-of-change)

The state of `WidgetTester.testTextInput` is now reset before running a `testWidgets` test.

Migration guide
---------------

[#](#migration-guide)

Tests that relied on dirty state from a previously run test must be updated. For example, the following test, from `packages/flutter/test/material/text_field_test.dart` in the `'Controller can update server'` test, previously passed because of a combination of dirty state from previous tests and a failure to actually set state in cases where it should have been set.

Code before migration:

In a `widgetsTest`, before actually changing text on a text editing widget, this call might have succeeded:

dart

```
    expect(tester.testTextInput.editingState['text'], isEmpty);
```

Code after migration:

Either remove the call entirely, or consider using the following to assert that the state hasn't been modified yet:

dart

```
    expect(tester.testTextInput.editingState, isNull);
```

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`TestTextInput`](https://api.flutter.dev/flutter/flutter_test/TestTextInput-class.html)* [`WidgetTester`](https://api.flutter.dev/flutter/flutter_test/WidgetTester-class.html)

Relevant issue:

* [Randomize test order to avoid global state](https://github.com/flutter/flutter/issues/47233)

Relevant PR:

* [Reset state between tests](https://github.com/flutter/flutter/pull/47464)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/test-text-input/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-text-input.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/test-text-input/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-text-input.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-text-input.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/test-text-input/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/test-text-input.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   