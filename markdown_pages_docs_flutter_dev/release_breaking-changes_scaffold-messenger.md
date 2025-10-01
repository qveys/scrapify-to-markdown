SnackBars managed by the ScaffoldMessenger
==========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [SnackBars managed by the ScaffoldMessenger](/release/breaking-changes/scaffold-messenger)

Summary
-------

[#](#summary)

The `SnackBar` API within the `Scaffold` is now handled by the `ScaffoldMessenger`, one of which is available by default within the context of a `MaterialApp`.

Context
-------

[#](#context)

Prior to this change, `SnackBar`s would be shown by calling on the `Scaffold` within the current `BuildContext`. By calling `Scaffold.of(context).showSnackBar`, the current `Scaffold` would animate a `SnackBar` into view. This would only apply to the current `Scaffold`, and would not persist across routes if they were changed in the course of the `SnackBar`s presentation. This would also lead to errors if `showSnackBar` would be called in the course of executing an asynchronous event, and the `BuildContext` became invalidated by the route changing and the `Scaffold` being disposed of.

The `ScaffoldMessenger` now handles `SnackBar`s in order to persist across routes and always be displayed on the current `Scaffold`. By default, a root `ScaffoldMessenger` is included in the `MaterialApp`, but you can create your own controlled scope for the `ScaffoldMessenger` to further control *which* `Scaffold`s receive your `SnackBar`s.

Description of change
---------------------

[#](#description-of-change)

The previous approach called upon the `Scaffold` to show a `SnackBar`.

dart

```
Scaffold(
  key: scaffoldKey,
  body: Builder(
    builder: (BuildContext context) {
      return GestureDetector(
        onTap: () {
          Scaffold.of(context).showSnackBar(SnackBar(
            content: const Text('snack'),
            duration: const Duration(seconds: 1),
            action: SnackBarAction(
              label: 'ACTION',
              onPressed: () { },
            ),
          ));
        },
        child: const Text('SHOW SNACK'),
      );
    },
  )
);
```

The new approach calls on the `ScaffoldMessenger` to show the `SnackBar`. In this case, the `Builder` is no longer required to provide a new scope with a `BuildContext` that is "under" the `Scaffold`.

dart

```
Scaffold(
  key: scaffoldKey,
  body: GestureDetector(
    onTap: () {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: const Text('snack'),
        duration: const Duration(seconds: 1),
        action: SnackBarAction(
          label: 'ACTION',
          onPressed: () { },
        ),
      ));
    },
    child: const Text('SHOW SNACK'),
  ),
);
```

When presenting a `SnackBar` during a transition, the `SnackBar` completes a `Hero` animation, moving smoothly to the next page.

The `ScaffoldMessenger` creates a scope in which all descendant `Scaffold`s register to receive `SnackBar`s, which is how they persist across these transitions. When using the root `ScaffoldMessenger` provided by the `MaterialApp`, all descendant `Scaffold`s receive `SnackBar`s, unless a new `ScaffoldMessenger` scope is created further down the tree. By instantiating your own `ScaffoldMessenger`, you can control which `Scaffold`s receive `SnackBar`s, and which are not, based on the context of your application.

The method `debugCheckHasScaffoldMessenger` is available to assert that a given context has a `ScaffoldMessenger` ancestor. Trying to present a `SnackBar` without a `ScaffoldMessenger` ancestor present results in an assertion such as the following:

```
No ScaffoldMessenger widget found.
Scaffold widgets require a ScaffoldMessenger widget ancestor.
Typically, the ScaffoldMessenger widget is introduced by the MaterialApp
at the top of your application widget tree.
```

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
// The ScaffoldState of the current context was used for managing SnackBars.
Scaffold.of(context).showSnackBar(mySnackBar);
Scaffold.of(context).hideCurrentSnackBar(mySnackBar);
Scaffold.of(context).removeCurrentSnackBar(mySnackBar);

// If a Scaffold.key is specified, the ScaffoldState can be directly
// accessed without first obtaining it from a BuildContext via
// Scaffold.of. From the key, use the GlobalKey.currentState
// getter. This was previously used to manage SnackBars.
final GlobalKey<ScaffoldState> scaffoldKey = GlobalKey<ScaffoldState>();
Scaffold(
  key: scaffoldKey,
  body: ...,
);

scaffoldKey.currentState.showSnackBar(mySnackBar);
scaffoldKey.currentState.hideCurrentSnackBar(mySnackBar);
scaffoldKey.currentState.removeCurrentSnackBar(mySnackBar);
```

Code after migration:

dart

```
// The ScaffoldMessengerState of the current context is used for managing SnackBars.
ScaffoldMessenger.of(context).showSnackBar(mySnackBar);
ScaffoldMessenger.of(context).hideCurrentSnackBar(mySnackBar);
ScaffoldMessenger.of(context).removeCurrentSnackBar(mySnackBar);

// If a ScaffoldMessenger.key is specified, the ScaffoldMessengerState can be directly
// accessed without first obtaining it from a BuildContext via
// ScaffoldMessenger.of. From the key, use the GlobalKey.currentState
// getter. This is used to manage SnackBars.
final GlobalKey<ScaffoldMessengerState> scaffoldMessengerKey = GlobalKey<ScaffoldMessengerState>();
ScaffoldMessenger(
  key: scaffoldMessengerKey,
  child: ...
)

scaffoldMessengerKey.currentState.showSnackBar(mySnackBar);
scaffoldMessengerKey.currentState.hideCurrentSnackBar(mySnackBar);
scaffoldMessengerKey.currentState.removeCurrentSnackBar(mySnackBar);

// The root ScaffoldMessenger can also be accessed by providing a key to 
// MaterialApp.scaffoldMessengerKey. This way, the ScaffoldMessengerState can be directly accessed
// without first obtaining it from a BuildContext via ScaffoldMessenger.of. From the key, use
// the GlobalKey.currentState getter.
final GlobalKey<ScaffoldMessengerState> rootScaffoldMessengerKey = GlobalKey<ScaffoldMessengerState>();
MaterialApp(
  scaffoldMessengerKey: rootScaffoldMessengerKey,
  home: ...
)

rootScaffoldMessengerKey.currentState.showSnackBar(mySnackBar);
rootScaffoldMessengerKey.currentState.hideCurrentSnackBar(mySnackBar);
rootScaffoldMessengerKey.currentState.removeCurrentSnackBar(mySnackBar);
```

Timeline
--------

[#](#timeline)

Landed in version: 1.23.0-13.0.pre  
 In stable release: 2.0.0

References
----------

[#](#references)

API documentation:

* [`Scaffold`](https://api.flutter.dev/flutter/material/Scaffold-class.html)* [`ScaffoldMessenger`](https://api.flutter.dev/flutter/material/ScaffoldMessenger-class.html)* [`SnackBar`](https://api.flutter.dev/flutter/material/SnackBar-class.html)* [`MaterialApp`](https://api.flutter.dev/flutter/material/MaterialApp-class.html)

Relevant issues:

* [Issue #57218](https://github.com/flutter/flutter/issues/57218)* [Issue #62921](https://github.com/flutter/flutter/issues/62921)

Relevant PRs:

* [ScaffoldMessenger](https://github.com/flutter/flutter/pull/64101)* [ScaffoldMessenger Migration](https://github.com/flutter/flutter/pull/64170)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scaffold-messenger/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scaffold-messenger.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scaffold-messenger/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scaffold-messenger.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scaffold-messenger.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scaffold-messenger/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scaffold-messenger.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   