Scribble Text Input Client
==========================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Scribble Text Input Client](/release/breaking-changes/scribble-text-input-client)

Summary
-------

[#](#summary)

Adds three methods, `showToolbar`, `insertTextPlaceholder`, and `removeTextPlaceholder` to the `TextInputClient` interface to allow the iOS 14 Scribble feature to insert and remove text placeholders and show the toolbar.

Context
-------

[#](#context)

As of iOS 14, iPads support the Scribble feature when using the Apple Pencil. This feature allows users to use the pencil to interact with text fields to add, delete, select, and modify text.

Description of change
---------------------

[#](#description-of-change)

In native text widgets, the text toolbar is shown when a user uses the pencil to select text on an iPad running iOS 14 or higher. To replicate this behavior, the platform sends a `textInput` channel message called `TextInputClient.showToolbar`. This notifies the Dart code that the toolbar should be shown.

When a user holds the pencil down, a visual gap in the text is shown to allow the user extra space to write. To replicate this behavior, the platform sends `textInput` channel messages called `TextInputClient.insertTextPlaceholder` and `TextInputClient.removeTextPlaceholder`. Multiline text inputs should have placeholders that provide vertical space, while single line inputs should provide horizontal space.

Migration guide
---------------

[#](#migration-guide)

If you previously implemented `TextEditingClient`, you must override `showToolbar`, `insertTextPlaceholder`, and `removeTextPlaceholder` to either support these Scribble features or provide an empty implementation.

To migrate, implement `showToolbar`, `insertTextPlaceholder`, and `removeTextPlaceholder`.

Code before migration:

dart

```
class MyCustomTextInputClient implements TextInputClient {
  ...
}
```

Code after migration:

dart

```
class MyCustomTextInputClient implements TextInputClient {
  ...
  @override
  void showToolbar() {
    ...
  }
  
  @override
  void insertTextPlaceholder(Size size) {
    ...
  }
  
  @override
  void removeTextPlaceholder() {
    ...
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 2.9.0-1.0.pre  
 In stable release: 2.10

References
----------

[#](#references)

API documentation:

* [`TextInputClient`](https://api.flutter.dev/flutter/services/TextInputClient-class.html)

Relevant issues:

* [Issue 61278](https://github.com/flutter/flutter/issues/61278)

Relevant PRs:

* [24224: Support Scribble Handwriting (engine)](https://github.com/flutter/engine/pull/24224)* [75472: Support Scribble Handwriting](https://github.com/flutter/flutter/pull/75472)* [97437: Re-land Support Scribble Handwriting](https://github.com/flutter/flutter/pull/97437)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scribble-text-input-client/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scribble-text-input-client.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scribble-text-input-client/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scribble-text-input-client.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scribble-text-input-client.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scribble-text-input-client/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scribble-text-input-client.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   