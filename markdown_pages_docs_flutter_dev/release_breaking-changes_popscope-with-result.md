Generic types in PopScope
=========================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Generic types in PopScope](/release/breaking-changes/popscope-with-result)

Summary
-------

[#](#summary)

Added a generic type to the [`PopScope`](https://api.flutter.dev/flutter/widgets/PopScope-class.html) class and replaced the [`onPopInvoked`](https://api.flutter.dev/flutter/widgets/PopScope/onPopInvoked.html) with a new method [`onPopInvokedWithResult`](https://api.flutter.dev/flutter/widgets/PopScope/onPopInvokedWithResult.html). The new method takes a boolean `didPop` and a `result` as position parameters.

Also replaced the [`Form.onPopInvoked`](https://api.flutter.dev/flutter/widgets/Form/onPopInvoked.html) with [`Form.onPopInvokedWithResult`](https://api.flutter.dev/flutter/widgets/Form/onPopInvokedWithResult.html) for the same reason.

Context
-------

[#](#context)

Previously, `PopScope` didn't have a way to access the pop result when `onPopInvoked` was called. The generic type is added to the `PopScope` class so that the new method `onPopInvokedWithResult` can access the type-safe result.

Description of change
---------------------

[#](#description-of-change)

Added a generic type (`<T>`) to the `PopScope` class and a new method `onPopInvokedWithResult`. The `onPopInvoked` property was deprecated in favor of `onPopInvokedWithResult`.

Also added a new method `onPopInvokedWithResult` to `Form` to replace `onPopInvoked`.

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      navigatorKey: nav,
      home: Column(
        children: [
          Form(
            canPop: false,
            onPopInvoked: (bool didPop) {
              if (didPop) {
                return;
              }
              launchConfirmationDialog();
            },
            child: MyWidget(),
          ),
          PopScope(
            canPop: false,
            onPopInvoked: (bool didPop) {
              if (didPop) {
                return;
              }
              launchConfirmationDialog();
            },
            child: MyWidget(),
          ),
        ],
      ),
    ),
  );
}
```

Code after migration:

dart

```
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      navigatorKey: nav,
      home: Column(
        children: [
          Form(
            canPop: false,
            onPopInvokedWithResult: (bool didPop, Object? result) {
              if (didPop) {
                return;
              }
              launchConfirmationDialog();
            },
            child: MyWidget(),
          ),
          PopScope<Object?>(
            canPop: false,
            onPopInvokedWithResult: (bool didPop, Object? result) {
              if (didPop) {
                return;
              }
              launchConfirmationDialog();
            },
            child: MyWidget(),
          ),
        ],
      ),
    ),
  );
}
```

The generic type should match the generic type of the [`Route`](https://api.flutter.dev/flutter/widgets/Route-class.html) that the `PopScope` is in. For example, if the route uses `int` as its generic type, consider using `PopScope<int>`.

If the `PopScope` widgets are shared across multiple routes with different types, you can use `PopScope<Object?>` to catch all possible types.

Timeline
--------

[#](#timeline)

Landed in version: 3.22.0-26.0.pre  
 In stable release: 3.24.0

References
----------

[#](#references)

API documentation:

* [`PopScope`](https://api.flutter.dev/flutter/widgets/PopScope-class.html)* [`onPopInvoked`](https://api.flutter.dev/flutter/widgets/PopScope/onPopInvoked.html)* [`Route`](https://api.flutter.dev/flutter/widgets/Route-class.html)* [`onPopInvokedWithResult`](https://api.flutter.dev/flutter/widgets/PopScope/onPopInvokedWithResult.html)* [`Form.onPopInvoked`](https://api.flutter.dev/flutter/widgets/Form/onPopInvoked.html)* [`Form.onPopInvokedWithResult`](https://api.flutter.dev/flutter/widgets/Form/onPopInvokedWithResult.html)

Relevant issue:

* [Issue 137458](https://github.com/flutter/flutter/issues/137458)

Relevant PR:

* [Add generic type for result in PopScope](https://github.com/flutter/flutter/pull/139164) *(reverted)** [Reapply new PopScope API](https://github.com/flutter/flutter/pull/147607) *(final reland)*

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/popscope-with-result/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/popscope-with-result.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/popscope-with-result/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/popscope-with-result.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-08-06. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/popscope-with-result.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/popscope-with-result/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/popscope-with-result.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   