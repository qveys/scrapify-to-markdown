Added missing `dispose()` for some disposable objects in Flutter
================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Added missing `dispose()` for some disposable objects in Flutter](/release/breaking-changes/dispose)

Summary
-------

[#](#summary)

Missing calls to 'dispose()' are added for some disposable objects. For example, ContextMenuController did not dispose OverlayEntry, and EditableTextState did not dispose TextSelectionOverlay.

If some other code also invokes 'dispose()' for the object, and the object is protected from double disposal, the second 'dispose()' fails with the following error message:

`Once you have called dispose() on a <class name>, it can no longer be used.`

Background
----------

[#](#background)

The convention is that the owner of an object should dispose of it.

This convention was broken in some places: owners were not disposing the disposable objects. The issue was fixed by adding a call to `dispose()`. However, if the object is protected from double disposal, this can cause failures when running in debug mode and `dispose()` is called elsewhere on the object.

Migration guide
---------------

[#](#migration-guide)

If you encounter the following error, update your code to call `dispose()` only in cases when your code created the object.

```
Once you have called dispose() on a <class name>, it can no longer be used.
```

Code before migration:

dart

```
x.dispose();
```

Code after migration:

dart

```
if (xIsCreatedByMe) {
  x.dispose();
}
```

To locate the incorrect disposal, check the call stack of the error. If the call stack points to `dispose` in your code, this disposal is incorrect and should be fixed.

If the error occurs in Flutter code, `dispose()` was called incorrectly the first time.

You can locate the incorrect call by temporary calling `print(StackTrace.current)` in the body of the failed method `dispose`.

Timeline
--------

[#](#timeline)

See the progress and status [in the tracking issue](https://github.com/flutter/flutter/issues/134787).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/dispose/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dispose.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/dispose/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dispose.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dispose.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/dispose/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dispose.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   