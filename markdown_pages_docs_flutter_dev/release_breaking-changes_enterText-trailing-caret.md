Change the enterText method to move the caret to the end of the input text
==========================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Change the enterText method to move the caret to the end of the input text](/release/breaking-changes/enterText-trailing-caret)

Summary
-------

[#](#summary)

The `WidgetTester.enterText` and `TestTextInput.enterText` methods now move the caret to the end of the input text.

Context
-------

[#](#context)

The caret indicates the insertion point within the current text in an active input field. Typically, when a new character is entered, the caret stays immediately after it. In Flutter the caret position is represented by a collapsed selection. When the selection is invalid, usually the user won't be able to modify or add text until they change the selection to a valid value.

`WidgetTester.enterText` and `TestTextInput.enterText` are 2 methods used in tests to replace the content of the target text field. Prior to this change, `WidgetTester.enterText` and `TestTextInput.enterText` set the selection to an invalid range (-1, -1), indicating there's no selection or caret. This contradicts the typical behavior of an input field.

Description of change
---------------------

[#](#description-of-change)

In addition to replacing the text with the supplied text, `WidgetTester.enterText` and `TestTextInput.enterText` now set the selection to `TextSelection.collapsed(offset: text.length)`, instead of `TextSelection.collapsed(offset: -1)`.

Migration guide
---------------

[#](#migration-guide)

It should be very uncommon for tests to have to rely on the previous behavior of `enterText`, since usually the selection should not be invalid. **Consider changing the expected values of your tests to adopt the `enterText` change.**

Common test failures this change may introduce includes:

* Golden test failures:

  The caret appears at the end of the text, as opposed to before the text prior to the change.* Different `TextEditingValue.selection` after calling `enterText`:

    The text field's `TextEditingValue` now has a collapsed selection with a non-negative offset, as opposed to `TextSelection.collapsed(offset: -1)` prior to the change. For instance, you may see `expect(controller.value.selection.baseOffset, -1);` failing after `enterText` calls.

If your tests have to rely on setting the selection to invalid, the previous behavior can be achieved using`updateEditingValue`:

### `TestTextInput.enterText`

[#](#testtextinput-entertext)

Code before migration:

dart

```
await testTextInput.enterText(text);
```

Code after migration:

dart

```
await testTextInput.updateEditingValue(TextEditingValue(
  text: text,
));
```

### `WidgetTester.enterText`

[#](#widgettester-entertext)

Code before migration:

dart

```
await tester.enterText(finder, text);
```

Code after migration:

dart

```
await tester.showKeyboard(finder);
await tester.updateEditingValue(TextEditingValue(
  text: text,
));
await tester.idle();
```

Timeline
--------

[#](#timeline)

Landed in version: 2.1.0-13.0.pre  
 In stable release: 2.5

References
----------

[#](#references)

API documentation:

* [`WidgetTester.enterText`](https://api.flutter.dev/flutter/flutter_test/WidgetTester/enterText.html)* [`TestTextInput.enterText`](https://api.flutter.dev/flutter/flutter_test/TestTextInput/enterText.html)

Relevant issues:

* [Issue 79494](https://github.com/flutter/flutter/issues/79494)

Relevant PR:

* [enterText to move the caret to the end](https://github.com/flutter/flutter/pull/79506)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/enterText-trailing-caret/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/enterText-trailing-caret.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/enterText-trailing-caret/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/enterText-trailing-caret.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/enterText-trailing-caret.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/enterText-trailing-caret/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/enterText-trailing-caret.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   