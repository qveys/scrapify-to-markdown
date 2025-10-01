showAutocorrectionPromptRect method added to TextInputClient
============================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [showAutocorrectionPromptRect method added to TextInputClient](/release/breaking-changes/add-showAutocorrectionPromptRect)

Summary
-------

[#](#summary)

A new method,`void showAutocorrectionPromptRect(int start, int end)`, was added to the `TextInputClient` interface.

Context
-------

[#](#context)

In order to display the iOS autocorrection highlight, the iOS text input plugin needed a way to inform the Flutter framework of the highlight's start and end position.

Description of change
---------------------

[#](#description-of-change)

A new method, `void showAutocorrectionPromptRect(int start, int end)`, was added to the `TextInputClient` interface. iOS calls this method when it finds a new potential autocorrect candidate in the current user input, or when the range of a previously highlighted candidate changes.

Migration guide
---------------

[#](#migration-guide)

If your application doesn't implement or subclass `TextInputClient`, no migration is needed. If your application doesn't target iOS, or the class that implemented the `textInputClient` interface doesn't support autocorrect, you only need to add an empty implementation for the new method:

dart

```
class CustomTextInputClient implements TextInputClient {
  void showAutocorrectionPromptRect(int start, int end) {}
}
```

Otherwise, if your app targets iOS and supports autocorrect on iOS, we recommend that you add a sensible implementation of `void showAutocorrectionPromptRect(int start, int end)` to your `TextInputClient` subclass.

Code after migration:

dart

```
// Assume your `TextInputClient` is a `State` subclass, and it has a variable 
// `_currentPromptRectRange` that controls the autocorrection highlight.
class CustomTextInputClient extends State<...> implements TextInputClient {
  @override
  void updateEditingValue(TextEditingValue value) {
    // When the text changes, the highlight needs to be dismissed.
    if (value.text != _value.text) {
      setState(() {
        _currentPromptRectRange = null;
      });
    }
  }

  void _handleFocusChanged() {
    // When this text input loses focus, the autocorrection highlight needs
    // to be dismissed.
    if (!_hasFocus) {
      setState(() {
        _currentPromptRectRange = null;
      });
    }
  }

  @override
  void showAutocorrectionPromptRect(int start, int end) {
    // Updates the range of the highlight, as iOS requested.
    // This method isn't called when iOS decides to
    // dismiss the highlight.
    setState(() {
      _currentPromptRectRange = TextRange(start: start, end: end);
    });
  }
}
```

Timeline
--------

[#](#timeline)

In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`TextInputClient`](https://api.flutter.dev/flutter/services/TextInputClient-class.html)

Relevant issue:

* [Issue 12920](https://github.com/flutter/flutter/issues/12920)

Relevant PR:

* [iOS UITextInput autocorrection prompt](https://github.com/flutter/flutter/pull/54119/)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-showAutocorrectionPromptRect/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-showAutocorrectionPromptRect.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-showAutocorrectionPromptRect/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-showAutocorrectionPromptRect.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-showAutocorrectionPromptRect.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-showAutocorrectionPromptRect/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-showAutocorrectionPromptRect.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   