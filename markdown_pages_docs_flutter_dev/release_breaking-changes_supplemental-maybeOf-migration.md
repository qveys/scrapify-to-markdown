Migrate `of` to non-nullable return values, and add `maybeOf`
=============================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migrate `of` to non-nullable return values, and add `maybeOf`](/release/breaking-changes/supplemental-maybeOf-migration)

Summary
-------

[#](#summary)

This migration guide describes conversion of code that uses various static `of` functions to retrieve information from a context that used to return nullable values, but now return non-nullable values.

Context
-------

[#](#context)

Flutter has a common pattern of allowing lookup of some types of widgets (typically [`InheritedWidget`](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html)s, but also others) using static member functions that are typically called `of`.

When non-nullability was made the default, it was then desirable to have the most commonly used APIs return a non-nullable value. This is because saying `Scrollable.of(context)` and then still requiring an `!` operator or `?` and a fallback value after that call felt awkward, and was not idiomatic for non-nullable Dart code.

A lot of this migration was performed when we eliminated `nullOk` parameters in a [previous migration](/release/breaking-changes/eliminating-nullok-parameters), but some `of` methods were missed in that migration, and some were subsequently added with nullable return types, counter to our common pattern.

In this migration, the affected `of` accessors were split into two calls: one that returned a non-nullable value and threw an exception when the sought-after value was not present (still called `of`), and one that returned a nullable value that didn't throw an exception, and returned null if the value was not present (a new method called `maybeOf`).

Description of change
---------------------

[#](#description-of-change)

The change modified these static `of` APIs to return non-nullable values. If a value is not found, they will also now assert in debug mode, and throw an exception in release mode.

* [`AutofillGroup.of`](https://api.flutter.dev/flutter/widgets/AutofillGroup/of.html)* [`DefaultTabController.of`](https://api.flutter.dev/flutter/material/DefaultTabController/of.html)* [`DefaultTextHeightBehavior.of`](https://api.flutter.dev/flutter/widgets/DefaultTextHeightBehavior/of.html)* [`Form.of`](https://api.flutter.dev/flutter/widgets/Form/of.html)* [`HeroControllerScope.of`](https://api.flutter.dev/flutter/widgets/HeroControllerScope/of.html)* [`Material.of`](https://api.flutter.dev/flutter/material/Material/of.html)* [`Overlay.of`](https://api.flutter.dev/flutter/widgets/Overlay/of.html)* [`PageStorage.of`](https://api.flutter.dev/flutter/widgets/PageStorage/of.html)* [`PrimaryScrollController.of`](https://api.flutter.dev/flutter/widgets/PrimaryScrollController/of.html)* [`RenderAbstractViewport.of`](https://api.flutter.dev/flutter/rendering/RenderAbstractViewport/of.html)* [`RestorationScope.of`](https://api.flutter.dev/flutter/widgets/RestorationScope/of.html)* [`Scrollable.of`](https://api.flutter.dev/flutter/widgets/Scrollable/of.html)* [`ScrollNotificationObserver.of`](https://api.flutter.dev/flutter/widgets/ScrollNotificationObserver/of.html)

This change also introduced new static `maybeOf` APIs alongside the above functions, which return a nullable version of the same value, and simply return null if the value is not found, without throwing any exceptions.

* [`AutofillGroup.maybeOf`](https://api.flutter.dev/flutter/widgets/AutofillGroup/maybeOf.html)* [`DefaultTabController.maybeOf`](https://api.flutter.dev/flutter/material/DefaultTabController/maybeOf.html)* [`DefaultTextHeightBehavior.maybeOf`](https://api.flutter.dev/flutter/widgets/DefaultTextHeightBehavior/maybeOf.html)* [`Form.maybeOf`](https://api.flutter.dev/flutter/widgets/Form/maybeOf.html)* [`HeroControllerScope.maybeOf`](https://api.flutter.dev/flutter/widgets/HeroControllerScope/maybeOf.html)* [`Material.maybeOf`](https://api.flutter.dev/flutter/material/Material/maybeOf.html)* [`Overlay.maybeOf`](https://api.flutter.dev/flutter/widgets/Overlay/maybeOf.html)* [`PageStorage.maybeOf`](https://api.flutter.dev/flutter/widgets/PageStorage/maybeOf.html)* [`PrimaryScrollController.maybeOf`](https://api.flutter.dev/flutter/widgets/PrimaryScrollController/maybeOf.html)* [`RenderAbstractViewport.maybeOf`](https://api.flutter.dev/flutter/rendering/RenderAbstractViewport/maybeOf.html)* [`RestorationScope.maybeOf`](https://api.flutter.dev/flutter/widgets/RestorationScope/maybeOf.html)* [`Scrollable.maybeOf`](https://api.flutter.dev/flutter/widgets/Scrollable/maybeOf.html)* [`ScrollNotificationObserver.maybeOf`](https://api.flutter.dev/flutter/widgets/ScrollNotificationObserver/maybeOf.html)

Migration guide
---------------

[#](#migration-guide)

To modify your code to use the new form of the APIs, first convert all instances of the original static `of` functions (where its nullability is important) to use the `maybeOf` form instead.

Code before migration:

dart

```
ScrollController? controller = Scrollable.of(context);
```

Code after migration:

dart

```
ScrollController? controller = Scrollable.maybeOf(context);
```

Then, for instances where the code calls the `of` API followed by an exclamation point, just remove the exclamation point: it can no longer return a nullable value.

Code before migration:

dart

```
ScrollController controller = Scrollable.of(context)!;
```

Code after migration:

dart

```
ScrollController controller = Scrollable.of(context);
```

The following can also be helpful:

* [`unnecessary_non_null_assertion`](https://dart.dev/tools/diagnostic-messages#unnecessary_non_null_assertion) (linter message) identifies places where an `!` operator should be removed* [`unnecessary_null_checks`](https://dart.dev/tools/linter-rules#unnecessary_null_checks) (analysis option) identifies places where the `?` operator isn't needed* [`unnecessary_null_in_if_null_operators`](https://dart.dev/tools/linter-rules#unnecessary_null_in_if_null_operators) identifies places where a `??` operator isn't needed* [`unnecessary_nullable_for_final_variable_declarations`](https://dart.dev/tools/linter-rules#unnecessary_nullable_for_final_variable_declarations) (analysis option) finds unnecessary question mark operators on `final` and `const` variables

Timeline
--------

[#](#timeline)

In stable release: 3.7

References
----------

[#](#references)

API documentation:

* [`Material.of`](https://api.flutter.dev/flutter/material/Material/of.html)

Relevant PRs:

* [Add `maybeOf` for all the cases when `of` returns nullable](https://github.com/flutter/flutter/pull/114120)* [Add `Overlay.maybeOf`, make `Overlay.of` return a non-nullable instance](https://github.com/flutter/flutter/pull/110811)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/supplemental-maybeOf-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/supplemental-maybeOf-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/supplemental-maybeOf-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/supplemental-maybeOf-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/supplemental-maybeOf-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/supplemental-maybeOf-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/supplemental-maybeOf-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   