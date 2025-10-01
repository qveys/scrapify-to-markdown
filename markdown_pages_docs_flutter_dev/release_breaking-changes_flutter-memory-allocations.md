Deprecate MemoryAllocations in favor of FlutterMemoryAllocations
================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecate MemoryAllocations in favor of FlutterMemoryAllocations](/release/breaking-changes/flutter-memory-allocations)

Summary
-------

[#](#summary)

Disposables in pure Dart projects can't use `MemoryAllocations` in Flutter. So, to be leak-trackable they need a Dart-only class. `MemoryAllocations` in Flutter is renamed to make the name available to a non-Flutter, Dart project.

Migration guide
---------------

[#](#migration-guide)

Before:

dart

```
if (kFlutterMemoryAllocationsEnabled) {
  MemoryAllocations.instance.dispatchObjectCreated(
    library: 'package:flutter/gestures.dart',
    className: '$MultiDragPointerState',
    object: this,
  );
}
```

After:

dart

```
if (kFlutterMemoryAllocationsEnabled) {
  FlutterMemoryAllocations.instance.dispatchObjectCreated(
    library: 'package:flutter/gestures.dart',
    className: '$MultiDragPointerState',
    object: this,
  );
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.19.0-2.0.pre  
 Landed in stable: 3.22.0

References
----------

[#](#references)

Relevant issues:

* [Rename MemoryAllocations to FlutterMemoryAllocations (Issue 140622)](https://github.com/flutter/flutter/issues/140622)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-memory-allocations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-memory-allocations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-memory-allocations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-memory-allocations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-05-14. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-memory-allocations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-memory-allocations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-memory-allocations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   