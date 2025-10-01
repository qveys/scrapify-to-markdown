Insert content text input client
================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Insert content text input client](/release/breaking-changes/insert-content-text-input-client)

Summary
-------

[#](#summary)

Added an `insertContent` method to the `TextInputClient` interface to allow Android's image keyboard feature to insert content into a Flutter `TextField`.

Context
-------

[#](#context)

As of Android 7.1, IMEs (input method editors or virtual keyboards) can send images and rich content into a text editor. This allows users to insert gifs, stickers, or context-aware rich content into a text field.

Description of change
---------------------

[#](#description-of-change)

When the user inserts rich content in the IME, the platform sends a `TextInputClient.commitContent` channel message, notifying the Dart code that the IME inserted rich content. The channel message contains the mime type, URI, and bytedata for the inserted content in JSON form.

Migration guide
---------------

[#](#migration-guide)

If you implemented the `TextInputClient` interface earlier, override `insertContent` to either support rich content insertion or provide an empty implementation.

To migrate, implement `insertContent`.

Code before migration:

dart

```
class MyCustomTextInputClient implements TextInputClient {
  // ...
}
```

Code after migration:

dart

```
class MyCustomTextInputClient implements TextInputClient {
  // ...
  @override
  void insertContent() {
    // ...
  }
  // ...
}
```

Your implementation of `TextInputClient` might not require the ability to receive rich content inserted from the IME. In that case, you can leave the implementation of `insertContent` empty with no consequences.

dart

```
class MyCustomTextInputClient implements TextInputClient {
  // ...
  @override
  void insertContent() {}
  // ...
}
```

As an alternative, you can use a similar implementation to the default `TextInputClient`. To learn how to do this, check out the [insertContent implementation](https://api.flutter.dev/flutter/services/TextInputClient/insertContent.html).

To prevent breaking changes to an interface, use `with TextInputClient` rather than `implements TextInputClient`.

Timeline
--------

[#](#timeline)

Landed in version: 3.8.0-1.0.pre  
 In stable release: 3.10.0

References
----------

[#](#references)

API documentation:

* [`TextInputClient`](https://api.flutter.dev/flutter/services/TextInputClient-class.html)

Relevant issue:

* [Issue 20796](https://github.com/flutter/flutter/issues/20796)

Relevant PRs:

* [24224: Support Image Insertion on Android (engine)](https://github.com/flutter/engine/pull/35619)* [97437: Support Image Insertion on Android](https://github.com/flutter/flutter/pull/110052)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/insert-content-text-input-client/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/insert-content-text-input-client.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/insert-content-text-input-client/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/insert-content-text-input-client.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/insert-content-text-input-client.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/insert-content-text-input-client/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/insert-content-text-input-client.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   