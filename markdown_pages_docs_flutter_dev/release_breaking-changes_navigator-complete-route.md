When a route is removed from the stack, associated futures must complete
========================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [When a route is removed from the stack, associated futures must complete](/release/breaking-changes/navigator-complete-route)

Summary
-------

[#](#summary)

When routes are pushed, developers can await them to be notified when they are popped. However, this didn't work when they were removed because the associated future was never completed.

Context
-------

[#](#context)

All Navigator methods that call `remove` had this issue. By using `complete`, the issue is properly resolved, allowing developers to pass a result.

Description of change
---------------------

[#](#description-of-change)

All Navigator methods have been updated to no longer call `remove` but instead use `complete`. Context menus are now built from the `contextMenuBuilder` parameter.

All methods that directly use `complete` now accept an optional `result` parameter to return it to the associated future. Other methods that indirectly use `remove` currently return `null`. In the future, we might extend these methods with an optional callback function to allow developers to handle pop logic in indirect scenarios (such as `removeUntil`).

Before this PR, the methods below can't return a result:

dart

```
Navigator.of(context).removeRoute(route);
Navigator.of(context).removeRouteBelow(route);
```

After this PR, methods can return a result:

dart

```
Navigator.of(context).removeRoute(route, result);
Navigator.of(context).removeRouteBelow(route, result);
```

Migration guide
---------------

[#](#migration-guide)

If you implemented `RouteTransitionRecord` and used `markForRemove`, you need to use `markForComplete` instead. `markForRemove` is now deprecated.

For other developers, no changes are required. The navigator continues to work as expected with new capabilities.

Timeline
--------

[#](#timeline)

Landed in version: 3.31.0-0.0.pre  
 In stable release: 3.32

References
----------

[#](#references)

### API documentation:

[#](#api-documentation)

* [`RouteTransitionRecord`](https://api.flutter.dev/flutter/widgets/RouteTransitionRecord-class.html)* [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html)

### Relevant issues:

[#](#relevant-issues)

* [removeRoute unresolved future](https://github.com/flutter/flutter/issues/157505)

### Relevant PRs:

[#](#relevant-prs)

* [feat: removeRoute now calls didComplete](https://github.com/flutter/flutter/pull/157725)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/navigator-complete-route/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-complete-route.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/navigator-complete-route/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-complete-route.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-complete-route.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/navigator-complete-route/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/navigator-complete-route.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   