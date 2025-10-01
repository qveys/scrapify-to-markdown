Eliminating nullOk Parameters
=============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Eliminating nullOk Parameters](/release/breaking-changes/eliminating-nullok-parameters)

Summary
-------

[#](#summary)

This migration guide describes conversion of code that uses the `nullOk` parameter on multiple `of` static accessors and related accessors to use alternate APIs with nullable return values.

Context
-------

[#](#context)

Flutter has a common pattern of allowing lookup of some types of widgets ([`InheritedWidget`](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html)s) using static member functions that are typically called `of`, and take a `BuildContext`.

Before non-nullability was the default, it was useful to have a toggle on these APIs that swapped between throwing an exception if the widget was not present in the widget tree and returning null if it was not found. It was useful, and wasn't confusing, since every variable was nullable.

When non-nullability was made the default, it was then desirable to have the most commonly used APIs return a non-nullable value. This is because saying `MediaQuery.of(context, nullOk: false)` and then still requiring an `!` operator or `?` and a fallback value after that call felt awkward.

The `nullOk` parameter was a cheap form of providing a null safety toggle, which in the face of true language support for non-nullability, was then supplying redundant, and perhaps contradictory signals to the developer.

To solve this, the `of` accessors (and some related accessors that also used `nullOk`) were split into two calls: one that returned a non-nullable value and threw an exception when the sought-after widget was not present, and one that returned a nullable value that didn't throw an exception, and returned null if the widget was not present.

The design document for this change is [Eliminating nullOk parameters](/go/eliminating-nullok-parameters).

Description of change
---------------------

[#](#description-of-change)

The actual change modified these APIs to not have a `nullOk` parameter, and to return a non-nullable value:

* [`MediaQuery.of`](https://api.flutter.dev/flutter/widgets/MediaQuery/of.html)* [`Navigator.of`](https://api.flutter.dev/flutter/widgets/Navigator/of.html)* [`ScaffoldMessenger.of`](https://api.flutter.dev/flutter/material/ScaffoldMessenger/of.html)* [`Scaffold.of`](https://api.flutter.dev/flutter/material/Scaffold/of.html)* [`Router.of`](https://api.flutter.dev/flutter/widgets/Router/of.html)* [`Localizations.localeOf`](https://api.flutter.dev/flutter/widgets/Localizations/localeOf.html)* [`FocusTraversalOrder.of`](https://api.flutter.dev/flutter/widgets/FocusTraversalOrder/of.html)* [`FocusTraversalGroup.of`](https://api.flutter.dev/flutter/widgets/FocusTraversalGroup/of.html)* [`Focus.of`](https://api.flutter.dev/flutter/widgets/Focus/of.html)* `Shortcuts.of`* [`Actions.handler`](https://api.flutter.dev/flutter/widgets/Actions/handler.html)* [`Actions.find`](https://api.flutter.dev/flutter/widgets/Actions/find.html)* [`Actions.invoke`](https://api.flutter.dev/flutter/widgets/Actions/invoke.html)* [`AnimatedList.of`](https://api.flutter.dev/flutter/widgets/AnimatedList/of.html)* [`SliverAnimatedList.of`](https://api.flutter.dev/flutter/widgets/SliverAnimatedList/of.html)* [`CupertinoDynamicColor.resolve`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/resolve.html)* [`CupertinoDynamicColor.resolveFrom`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/resolveFrom.html)* [`CupertinoUserInterfaceLevel.of`](https://api.flutter.dev/flutter/cupertino/CupertinoUserInterfaceLevel/of.html)* [`CupertinoTheme.brightnessOf`](https://api.flutter.dev/flutter/cupertino/CupertinoTheme/brightnessOf.html)* [`CupertinoThemeData.resolveFrom`](https://api.flutter.dev/flutter/cupertino/CupertinoThemeData/resolveFrom.html)* [`NoDefaultCupertinoThemeData.resolveFrom`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/resolveFrom.html)* [`CupertinoTextThemeData.resolveFrom`](https://api.flutter.dev/flutter/cupertino/CupertinoTextThemeData/resolveFrom.html)* [`MaterialBasedCupertinoThemeData.resolveFrom`](https://api.flutter.dev/flutter/material/MaterialBasedCupertinoThemeData/resolveFrom.html)

And introduced these new APIs alongside those, to return a nullable value:

* [`MediaQuery.maybeOf`](https://api.flutter.dev/flutter/widgets/MediaQuery/maybeOf.html)* [`Navigator.maybeOf`](https://api.flutter.dev/flutter/widgets/Navigator/maybeOf.html)* [`ScaffoldMessenger.maybeOf`](https://api.flutter.dev/flutter/material/ScaffoldMessenger/maybeOf.html)* [`Scaffold.maybeOf`](https://api.flutter.dev/flutter/material/Scaffold/maybeOf.html)* [`Router.maybeOf`](https://api.flutter.dev/flutter/widgets/Router/maybeOf.html)* [`Localizations.maybeLocaleOf`](https://api.flutter.dev/flutter/widgets/Localizations/maybeLocaleOf.html)* [`FocusTraversalOrder.maybeOf`](https://api.flutter.dev/flutter/widgets/FocusTraversalOrder/maybeOf.html)* [`FocusTraversalGroup.maybeOf`](https://api.flutter.dev/flutter/widgets/FocusTraversalGroup/maybeOf.html)* [`Focus.maybeOf`](https://api.flutter.dev/flutter/widgets/Focus/maybeOf.html)* `Shortcuts.maybeOf`* [`Actions.maybeFind`](https://api.flutter.dev/flutter/widgets/Actions/maybeFind.html)* [`Actions.maybeInvoke`](https://api.flutter.dev/flutter/widgets/Actions/maybeInvoke.html)* [`AnimatedList.maybeOf`](https://api.flutter.dev/flutter/widgets/AnimatedList/maybeOf.html)* [`SliverAnimatedList.maybeOf`](https://api.flutter.dev/flutter/widgets/SliverAnimatedList/maybeOf.html)* [`CupertinoDynamicColor.maybeResolve`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/maybeResolve.html)* [`CupertinoUserInterfaceLevel.maybeOf`](https://api.flutter.dev/flutter/cupertino/CupertinoUserInterfaceLevel/maybeOf.html)* [`CupertinoTheme.maybeBrightnessOf`](https://api.flutter.dev/flutter/cupertino/CupertinoTheme/maybeBrightnessOf.html)

Migration guide
---------------

[#](#migration-guide)

In order to modify your code to use the new form of the APIs, convert all instances of calls that include `nullOk = true` as a parameter to use the `maybe` form of the API instead.

So this:

dart

```
MediaQueryData? data = MediaQuery.of(context, nullOk: true);
```

becomes:

dart

```
MediaQueryData? data = MediaQuery.maybeOf(context);
```

You also need to modify all instances of calling the API with `nullOk = false` (often the default), to accept non-nullable return values, or remove any `!` operators:

So either of:

dart

```
MediaQueryData data = MediaQuery.of(context)!; // nullOk false by default.
MediaQueryData? data = MediaQuery.of(context); // nullOk false by default.
```

both become:

dart

```
MediaQueryData data = MediaQuery.of(context); // No ! or ? operator here now.
```

The `unnecessary_non_null_assertion` analysis option can be quite helpful in finding the places where the `!` operator should be removed, and the `unnecessary_nullable_for_final_variable_declarations` analysis option can be helpful in finding unnecessary question mark operators on `final` and `const` variables.

Timeline
--------

[#](#timeline)

Landed in version: 1.24.0  
 In stable release: 2.0.0

References
----------

[#](#references)

API documentation:

* [`MediaQuery.of`](https://api.flutter.dev/flutter/widgets/MediaQuery/of.html)* [`Navigator.of`](https://api.flutter.dev/flutter/widgets/Navigator/of.html)* [`ScaffoldMessenger.of`](https://api.flutter.dev/flutter/material/ScaffoldMessenger/of.html)* [`Scaffold.of`](https://api.flutter.dev/flutter/material/Scaffold/of.html)* [`Router.of`](https://api.flutter.dev/flutter/widgets/Router/of.html)* [`Localizations.localeOf`](https://api.flutter.dev/flutter/widgets/Localizations/localeOf.html)* [`FocusTraversalOrder.of`](https://api.flutter.dev/flutter/widgets/FocusTraversalOrder/of.html)* [`FocusTraversalGroup.of`](https://api.flutter.dev/flutter/widgets/FocusTraversalGroup/of.html)* [`Focus.of`](https://api.flutter.dev/flutter/widgets/Focus/of.html)* `Shortcuts.of`* [`Actions.handler`](https://api.flutter.dev/flutter/widgets/Actions/handler.html)* [`Actions.find`](https://api.flutter.dev/flutter/widgets/Actions/find.html)* [`Actions.invoke`](https://api.flutter.dev/flutter/widgets/Actions/invoke.html)* [`AnimatedList.of`](https://api.flutter.dev/flutter/widgets/AnimatedList/of.html)* [`SliverAnimatedList.of`](https://api.flutter.dev/flutter/widgets/SliverAnimatedList/of.html)* [`CupertinoDynamicColor.resolve`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/resolve.html)* [`CupertinoDynamicColor.resolveFrom`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/resolveFrom.html)* [`CupertinoUserInterfaceLevel.of`](https://api.flutter.dev/flutter/cupertino/CupertinoUserInterfaceLevel/of.html)* [`CupertinoTheme.brightnessOf`](https://api.flutter.dev/flutter/cupertino/CupertinoTheme/brightnessOf.html)* [`CupertinoThemeData.resolveFrom`](https://api.flutter.dev/flutter/cupertino/CupertinoThemeData/resolveFrom.html)* [`NoDefaultCupertinoThemeData.resolveFrom`](https://api.flutter.dev/flutter/cupertino/NoDefaultCupertinoThemeData/resolveFrom.html)* [`CupertinoTextThemeData.resolveFrom`](https://api.flutter.dev/flutter/cupertino/CupertinoTextThemeData/resolveFrom.html)* [`MaterialBasedCupertinoThemeData.resolveFrom`](https://api.flutter.dev/flutter/material/MaterialBasedCupertinoThemeData/resolveFrom.html)* [`MediaQuery.maybeOf`](https://api.flutter.dev/flutter/widgets/MediaQuery/maybeOf.html)* [`Navigator.maybeOf`](https://api.flutter.dev/flutter/widgets/Navigator/maybeOf.html)* [`ScaffoldMessenger.maybeOf`](https://api.flutter.dev/flutter/material/ScaffoldMessenger/maybeOf.html)* [`Scaffold.maybeOf`](https://api.flutter.dev/flutter/material/Scaffold/maybeOf.html)* [`Router.maybeOf`](https://api.flutter.dev/flutter/widgets/Router/maybeOf.html)* [`Localizations.maybeLocaleOf`](https://api.flutter.dev/flutter/widgets/Localizations/maybeLocaleOf.html)* [`FocusTraversalOrder.maybeOf`](https://api.flutter.dev/flutter/widgets/FocusTraversalOrder/maybeOf.html)* [`FocusTraversalGroup.maybeOf`](https://api.flutter.dev/flutter/widgets/FocusTraversalGroup/maybeOf.html)* [`Focus.maybeOf`](https://api.flutter.dev/flutter/widgets/Focus/maybeOf.html)* `Shortcuts.maybeOf`* [`Actions.maybeFind`](https://api.flutter.dev/flutter/widgets/Actions/maybeFind.html)* [`Actions.maybeInvoke`](https://api.flutter.dev/flutter/widgets/Actions/maybeInvoke.html)* [`AnimatedList.maybeOf`](https://api.flutter.dev/flutter/widgets/AnimatedList/maybeOf.html)* [`SliverAnimatedList.maybeOf`](https://api.flutter.dev/flutter/widgets/SliverAnimatedList/maybeOf.html)* [`CupertinoDynamicColor.maybeResolve`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/maybeResolve.html)* [`CupertinoUserInterfaceLevel.maybeOf`](https://api.flutter.dev/flutter/cupertino/CupertinoUserInterfaceLevel/maybeOf.html)* [`CupertinoTheme.maybeBrightnessOf`](https://api.flutter.dev/flutter/cupertino/CupertinoTheme/maybeBrightnessOf.html)

Relevant issue:

* [Issue 68637](https://github.com/flutter/flutter/issues/68637)

Relevant PRs:

* [Remove `nullOk` in `MediaQuery.of`](https://github.com/flutter/flutter/pull/68736)* [Remove `nullOk` in `Navigator.of`](https://github.com/flutter/flutter/pull/70726)* [Remove `nullOk` parameter from `AnimatedList.of` and `SliverAnimatedList.of`](https://github.com/flutter/flutter/pull/68925)* [Remove `nullOk` parameter from `Shortcuts.of`, `Actions.find`, and `Actions.handler`](https://github.com/flutter/flutter/pull/68921)* [Remove `nullOk` parameter from `Focus.of`, `FocusTraversalOrder.of`, and `FocusTraversalGroup.of`](https://github.com/flutter/flutter/pull/68917)* [Remove `nullOk` parameter from `Localizations.localeOf`](https://github.com/flutter/flutter/pull/68911)* [Remove `nullOk` parameter from `Router.of`](https://github.com/flutter/flutter/pull/68910)* [Remove `nullOk` from `Scaffold.of` and `ScaffoldMessenger.of`](https://github.com/flutter/flutter/pull/68908)* [Remove `nullOk` parameter from Cupertino color resolution APIs](https://github.com/flutter/flutter/pull/68905)* [Remove vestigial `nullOk` parameter from `Localizations.localeOf`](https://github.com/flutter/flutter/pull/74657)* [Remove `nullOk` from `Actions.invoke`, add `Actions.maybeInvoke`](https://github.com/flutter/flutter/pull/74680)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/eliminating-nullok-parameters/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/eliminating-nullok-parameters.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/eliminating-nullok-parameters/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/eliminating-nullok-parameters.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/eliminating-nullok-parameters.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/eliminating-nullok-parameters/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/eliminating-nullok-parameters.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   