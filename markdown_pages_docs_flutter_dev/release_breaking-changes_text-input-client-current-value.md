TextInputClient currentTextEditingValue
=======================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [TextInputClient currentTextEditingValue](/release/breaking-changes/text-input-client-current-value)

Summary
-------

[#](#summary)

Add a field, `currentTextEditingValue`, to the `TextInputClient` interface to get the current value of an editable text field from a platform client.

Context
-------

[#](#context)

The `TextInputClient` class is used by the Flutter framework to communicate with platform code about the current state of text input widgets like `EditableText`.

The platform side can lose its state when an Android app moves to the background. As of this change, the app can ask the framework for the last known state. In order to obtain this information, the `TextEditingValue` was surfaced for the `TextInputClient`.

Description of change
---------------------

[#](#description-of-change)

On some supported platforms, the application can be moved into the background where it is expected to consume fewer resources. For example, a backgrounded application on Android should avoid consuming unnecessary memory and has no need to retain references to views. Before this change, the Android-specific platform code could lose state information about editable text fields when the app moved back to the foreground. This is seen, for example, when text entered in a `TextField` widget is lost to the Java code, but is still remembered in the Dart code.

As of this change, the platform side now sends a `textInput` channel message called `TextInput.requestExistingState`. This notifies the Dart code that, when the app wakes up, it should re-establish any text input connections and notify the platform of its most recently known editing state.

The `TextInput` class interacts with client widgets using the `TextInputClient` interface. This interface previously provided no insight into the current value that a client had. To allow the `TextInput` class to appropriately respond to `TextInput.requestExistingState`, a new getter was added to `TextInputClient` called `currentTextEditingValue`. You cannot safely use the last value passed to `TextInputConnection.setEditingState`, since the client only calls that method under specific circumstances, such as when Dart code directly modifies the value of a `TextEditingController` in a way that does not directly mirror the platform's native handling of a response to a key input event. This is how a `TextInputFormatter` generally works, or what happens when Dart code directly sets `TextEditingController.value`.

Migration guide
---------------

[#](#migration-guide)

If you previously implemented or extended `TextEditingClient`, you must now add the appropriate override for `currentTextEditingValue`.

This value may be null.

If you want to migrate *before* this change lands, you can add a class to your class similar to the following:

dart

```
abstract class _TemporaryTextEditingClient {
  TextEditingValue get currentTextEditingValue;
}
```

This allows you to add the new member with an `@override` annotation before the change lands in the framework. Later, you can remove the temporary interface definition.

Code before migration:

dart

```
class _MyCustomTextWidgetState extends State<MyCustomWidget> implements TextEditingClient {
  ...

  @override
  void updateEditingValue(TextEditingValue value) {
    ...
  }

  @override
  void performAction(TextInputAction action) {
    ...
  }

  @override
  void updateFloatingCursor(RawFloatingCursorPoint point) {
    ...
  }
}
```

Code after migration:

dart

```
class _MyCustomTextWidgetState extends State<MyCustomWidget> implements TextEditingClient {
  ...

  @override
  TextEditingValue get currentTextEditingValue => widget.textEditingController.value;

  @override
  void updateEditingValue(TextEditingValue value) {
    ...
  }

  @override
  void performAction(TextInputAction action) {
    ...
  }

  @override
  void updateFloatingCursor(RawFloatingCursorPoint point) {
    ...
  }
}
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

* [`TextInput`](https://api.flutter.dev/flutter/services/TextInput-class.html)* [`TextInputClient`](https://api.flutter.dev/flutter/services/TextInputClient-class.html)* [`EditableText`](https://api.flutter.dev/flutter/widgets/EditableText-class.html)* [`SystemChannels.textInput`](https://api.flutter.dev/flutter/services/SystemChannels/textInput-constant.html)

Relevant issue:

* [Issue 47137](https://github.com/flutter/flutter/issues/47137)

Relevant PR:

* [Fix requestExistingInputState response](https://github.com/flutter/flutter/pull/47472)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-input-client-current-value/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-input-client-current-value.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-input-client-current-value/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-input-client-current-value.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-input-client-current-value.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-input-client-current-value/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-input-client-current-value.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   