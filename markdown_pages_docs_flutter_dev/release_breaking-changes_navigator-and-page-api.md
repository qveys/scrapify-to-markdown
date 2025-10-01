Navigator's page APIs breaking change
=====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Navigator's page APIs breaking change](/release/breaking-changes/navigator-and-page-api)

Summary
-------

[#](#summary)

The [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html) page APIs are refactored so that they can integrate with Flutter's other pop mechanisms.

Context
-------

[#](#context)

The `onPopPage` property was added for cleaning up pages after a page is about to be popped. To veto pop, you'd return `false` in the callback. This did not work well with other popping mechanisms in the framework, such as [`PopScope`](https://api.flutter.dev/flutter/widgets/PopScope-class.html) and iOS back gestures.

To integrate the framework's pop mechanisms together, the page APIs needed to be refactored.

Description of change
---------------------

[#](#description-of-change)

The `onDidRemovePage` property replaces the `onPopPage` property. You can no longer veto a pop in the `onDidRemovePage` property. Instead, you are only responsible for updating the [`pages`](https://api.flutter.dev/flutter/widgets/Navigator/pages.html).

The veto mechanism is now managed with the `Page.canPop` and `Page.onPopInvoked` properties. These function similar to how you use the `PopScope` widget.

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
import 'package:flutter/material.dart';

final MaterialPage<void> page1 = MaterialPage<void>(child: Placeholder());
final MaterialPage<void> page2 = MaterialPage<void>(child: Placeholder());
final MaterialPage<void> page3 = MaterialPage<void>(child: Placeholder());

void main() {
  final List<Page<void>> pages = <Page<void>>[page1, page2, page3];
  runApp(
    MaterialApp(
      home: Navigator(
        pages: pages,
        onPopPage: (Route<Object?> route, Object? result) {
          if (route.settings == page2) {
            return false;
          }
          if (route.didPop) {
            pages.remove(route.settings);
            return true;
          }
          return false;
        },
      ),
    ),
  );
}
```

Code after migration:

dart

```
import 'package:flutter/material.dart';

final MaterialPage<void> page1 = MaterialPage<void>(child: Placeholder());
final MaterialPage<void> page2 = MaterialPage<void>(canPop: false, child: Placeholder());
final MaterialPage<void> page3 = MaterialPage<void>(child: Placeholder());

void main() {
  final List<Page<void>> pages = <Page<void>>[page1, page2, page3];
  runApp(
    MaterialApp(
      home: Navigator(
        pages: pages,
        onDidRemovePage: (Page<Object?> page) {
          pages.remove(page);
        },
      ),
    ),
  );
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.22.0-32.0.pre  
 In stable release: 3.24.0

References
----------

[#](#references)

API documentation:

* [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html)* [`PopScope`](https://api.flutter.dev/flutter/widgets/PopScope-class.html)

Relevant issue:

* [Issue 137458](https://github.com/flutter/flutter/issues/137458)

Relevant PR:

* [Refactors page API](https://github.com/flutter/flutter/pull/137792)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/navigator-and-page-api/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-and-page-api.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/navigator-and-page-api/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-and-page-api.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-08-08. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-and-page-api.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/navigator-and-page-api/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-and-page-api.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   