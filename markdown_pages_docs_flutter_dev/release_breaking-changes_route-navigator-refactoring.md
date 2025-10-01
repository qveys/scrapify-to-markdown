Route and Navigator Refactoring
===============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Route and Navigator Refactoring](/release/breaking-changes/route-navigator-refactoring)

Summary
-------

[#](#summary)

The `Route` class no longer manages its overlay entries in overlay, and its `install()` method no longer has an `insertionPoint` parameter. The `isInitialRoute` property in `RouteSetting` has been deprecated, and `Navigator.pop()` no longer returns a value.

Context
-------

[#](#context)

We refactored the navigator APIs to prepare for the new page API and the introduction of the `Router` widget as outlined in the [Router](/go/navigator-with-router) design document. This refactoring introduced some function signature changes in order to make the existing navigator APIs continue to work with the new page API.

Description of change
---------------------

[#](#description-of-change)

The boolean return value of `Navigator.pop()` was not well defined, and the user could achieve the same result by calling `Navigator.canPop()`. Since the API for `Navigator.canPop()` was better defined, we simplified `Navigator.pop()` to not return a boolean value.

On the other hand, the navigator requires the ability to manually rearrange entries in the overlay to allow the user to change the route history in the new API. We changed it so that the route only creates and destroys its overlay entries, while the navigator inserts or removes overlay entries from the overlay. We also removed the `insertionPoint` argument of `Route.install()` because it was obsolete after the change.

Finally, we removed the `isInitialRoute` property from `RouteSetting` as part of refactoring, and provided the `onGenerateInitialRoutes` API for full control of initial routes generation.

Migration guide
---------------

[#](#migration-guide)

Case 1: An app depends on `pop()` returning a boolean value.

dart

```
TextField(
  onTap: () {
    if (Navigator.pop(context))
      print('There still is at least one route after pop');
    else
      print('Oops! No more routes.');
  }
)
```

You could use `Navigator.canPop()` in combination with `Navigator.pop()` to achieve the same result.

dart

```
TextField(
  onTap: () {
    if (Navigator.canPop(context))
      print('There still is at least one route after pop');
    else
      print('Oops! No more routes.');
    // Our navigator pops the route anyway.
    Navigator.pop(context);
  }
)
```

Case 2: An app generates routes based on `isInitialRoute`.

dart

```
MaterialApp(
  onGenerateRoute: (RouteSetting setting) {
    if (setting.isInitialRoute)
      return FakeSplashRoute();
    else
      return RealRoute(setting);
  }
)
```

There are different ways to migrate this change. One way is to set an explicit value for `MaterialApp.initialRoute`. You can then test for this value in place of `isInitialRoute`. As `initialRoute` inherits its default value outside of Flutter's scope, you must set an explicit value for it.

dart

```
MaterialApp(
  initialRoute: '/', // Set this value explicitly. Default might be altered.
  onGenerateRoute: (RouteSetting setting) {
    if (setting.name == '/')
      return FakeSplashRoute();
    else
      return RealRoute(setting);
  }
)
```

If there is a more complicated use case, you can use the new API, `onGenerateInitialRoutes`, in `MaterialApp` or `CupertinoApp`.

dart

```
MaterialApp(
  onGenerateRoute: (RouteSetting setting) {
    return RealRoute(setting);
  },
  onGenerateInitialRoutes: (String initialRouteName) {
    return <Route>[FakeSplashRoute()];
  }
)
```

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

Design doc:

* [Router](/go/navigator-with-router)

API documentation:

* [`Route`](https://api.flutter.dev/flutter/widgets/Route-class.html)* [`Route.install`](https://api.flutter.dev/flutter/widgets/Route/install.html)* [`RouteSetting.isInitialRoute`](https://api.flutter.dev/flutter/widgets/RouteSettings/isInitialRoute.html)* [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html)* [`Navigator.pop`](https://api.flutter.dev/flutter/widgets/Navigator/pop.html)* [`Navigator.canPop`](https://api.flutter.dev/flutter/widgets/Navigator/canPop.html)

Relevant issue:

* [Issue 45938: Router](https://github.com/flutter/flutter/issues/45938)

Relevant PR:

* [PR 44930](https://github.com/flutter/flutter/pull/44930) - Refactor the imperative api to continue working in the new navigation system

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-navigator-refactoring/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-navigator-refactoring.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-navigator-refactoring/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-navigator-refactoring.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-navigator-refactoring.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-navigator-refactoring/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-navigator-refactoring.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   