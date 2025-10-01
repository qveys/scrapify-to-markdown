Route transition record and transition delegate updates
=======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Route transition record and transition delegate updates](/release/breaking-changes/route-transition-record-and-transition-delegate)

Summary
-------

[#](#summary)

A new boolean getter `isWaitingForExitingDecision` was added to the route transition record and the `isEntering` getter was renamed to `isWaitingForEnteringDecision`. In the `resolve()` method for the transition delegate, use the `isWaitingForExitingDecision` to check if an exiting route actually needs an explicit decision on how to transition off the screen. If you try to make a decision for an existing route that *isn't* waiting for a decision, Flutter throws an assertion error.

Context
-------

[#](#context)

When the navigator receives a new list of pages, it tries to update its current routes stack to match the list. However, it requires explicit decisions on how to transition the route on and off the screen. Previously, routes that were not in the new list required decisions on how to transition off the screen. However, we later found out this is not always true. If a route is popped, but is still waiting for the popping animation to finish, this route would sit in the navigator routes stack until the animation was done. If a page update occurred during this time, this route exits but doesn't require a decision on how to transition off the screen. Therefore, `isWaitingForExitingDecision` was added to cover that case.

The `isEntering` getter is also renamed to `isWaitingForEnteringDecision` to be more descriptive, and also to make the naming more consistent.

Migration guide
---------------

[#](#migration-guide)

If you implement your own transition delegate, you need to check the exiting routes using the getter `isWaitingForExitingDecision` before you call `markForPop`, `markForComplete`, or `markForRemove` on them. You also need to rename all the references from `isEntering` to `isWaitingForEnteringDecision`.

Code before migration:

dart

```
import 'package:flutter/widgets.dart';

class NoAnimationTransitionDelegate extends TransitionDelegate<void> {
  @override
  Iterable<RouteTransitionRecord> resolve({
    List<RouteTransitionRecord> newPageRouteHistory,
    Map<RouteTransitionRecord, RouteTransitionRecord> locationToExitingPageRoute,
    Map<RouteTransitionRecord, List<RouteTransitionRecord>> pageRouteToPagelessRoutes,
  }) {
    final List<RouteTransitionRecord> results = <RouteTransitionRecord>[];

    for (final RouteTransitionRecord pageRoute in newPageRouteHistory) {
      if (pageRoute.isEntering) {
        pageRoute.markForAdd();
      }
      results.add(pageRoute);

    }
    for (final RouteTransitionRecord exitingPageRoute in locationToExitingPageRoute.values) {
      exitingPageRoute.markForRemove();
      final List<RouteTransitionRecord> pagelessRoutes = pageRouteToPagelessRoutes[exitingPageRoute];
      if (pagelessRoutes != null) {
        for (final RouteTransitionRecord pagelessRoute in pagelessRoutes) {
          pagelessRoute.markForRemove();
        }
      }
      results.add(exitingPageRoute);

    }
    return results;
  }
}
```

Code after migration:

dart

```
import 'package:flutter/widgets.dart';

class NoAnimationTransitionDelegate extends TransitionDelegate<void> {
  @override
  Iterable<RouteTransitionRecord> resolve({
    List<RouteTransitionRecord> newPageRouteHistory,
    Map<RouteTransitionRecord, RouteTransitionRecord> locationToExitingPageRoute,
    Map<RouteTransitionRecord, List<RouteTransitionRecord>> pageRouteToPagelessRoutes,
  }) {
    final List<RouteTransitionRecord> results = <RouteTransitionRecord>[];

    for (final RouteTransitionRecord pageRoute in newPageRouteHistory) {
      // Renames isEntering to isWaitingForEnteringDecision.
      if (pageRoute.isWaitingForEnteringDecision) {
        pageRoute.markForAdd();
      }
      results.add(pageRoute);

    }
    for (final RouteTransitionRecord exitingPageRoute in locationToExitingPageRoute.values) {
      // Checks the isWaitingForExitingDecision before calling the markFor methods.
      if (exitingPageRoute.isWaitingForExitingDecision) {
        exitingPageRoute.markForRemove();
        final List<RouteTransitionRecord> pagelessRoutes = pageRouteToPagelessRoutes[exitingPageRoute];
        if (pagelessRoutes != null) {
          for (final RouteTransitionRecord pagelessRoute in pagelessRoutes) {
            pagelessRoute.markForRemove();
          }
        }
      }
      results.add(exitingPageRoute);

    }
    return results;
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.18.0  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html)* [`TransitionDelegate`](https://api.flutter.dev/flutter/widgets/TransitionDelegate-class.html)* [`RouteTransitionRecord`](https://api.flutter.dev/flutter/widgets/RouteTransitionRecord-class.html)

Relevant issue:

* [Issue 45938: Navigator 2.0](https://github.com/flutter/flutter/issues/45938)

Relevant PR:

* [PR 55998](https://github.com/flutter/flutter/pull/55998): Fixes the navigator pages update crash when there is still a route waiting

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-transition-record-and-transition-delegate/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-transition-record-and-transition-delegate.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-transition-record-and-transition-delegate/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-transition-record-and-transition-delegate.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-transition-record-and-transition-delegate.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-transition-record-and-transition-delegate/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-transition-record-and-transition-delegate.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   