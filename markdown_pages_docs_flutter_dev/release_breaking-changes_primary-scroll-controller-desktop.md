Default `PrimaryScrollController` on Desktop
============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Default `PrimaryScrollController` on Desktop](/release/breaking-changes/primary-scroll-controller-desktop)

Summary
-------

[#](#summary)

The `PrimaryScrollController` API has been updated to no longer automatically attach to vertical `ScrollView`s on desktop platforms.

Context
-------

[#](#context)

Prior to this change, `ScrollView.primary` would default to true if a `ScrollView` had an `Axis.vertical` scroll direction and a `ScrollController` had not already been provided. This allowed for common UI patterns, like the scroll-to-top function on iOS to work out of the box for Flutter apps. On desktop however, this default would often cause the following assertion error:

```
ScrollController attached to multiple ScrollViews.
```

While it is common for a mobile application to display one `ScrollView` at a time, desktop UI patterns are more likely to display multiple `ScrollView`s side-by-side. The prior implementation of `PrimaryScrollController` conflicted with this pattern, resulting in an often unhelpful error message. To remedy this, the `PrimaryScrollController` has been updated with additional parameters as well as better error messaging across multiple widgets that depend on it.

Description of change
---------------------

[#](#description-of-change)

The previous implementation of `ScrollView` resulted in `primary` being true by default for all vertical `ScrollView`s that did not already have a `ScrollController`, on all platforms. This default behavior was not always clear, particularly because it is separate from the `PrimaryScrollController` itself.

dart

```
// Previously, this ListView would always result in primary being true,
// and attached to the PrimaryScrollController on all platforms.
Scaffold(
  body: ListView.builder(
    itemBuilder: (BuildContext context, int index) {
      return Text('Item $index');
    }
  ),
);
```

The implementation changes `ScrollView.primary` to be nullable, with the fallback decision-making being relocated to the `PrimaryScrollController`. When `primary` is null, and no `ScrollController` has been provided, the `ScrollView` will look up the `PrimaryScrollController` and instead call `shouldInherit` to determine if the given `ScrollView` should use the `PrimaryScrollController`.

The new members of the `PrimaryScrollController` class, `automaticallyInheritForPlatforms` and `scrollDirection`, are evaluated in `shouldInherit`, allowing users clarity and control over the `PrimaryScrollController`'s behavior.

By default, backwards compatibility is maintained for mobile platforms. `PrimaryScrollController.shouldInherit` returns true for vertical `ScrollView`s. On desktop, this returns false by default.

dart

```
// Only on mobile platforms will this attach to the PrimaryScrollController by
// default.
Scaffold(
  body: ListView.builder(
    itemBuilder: (BuildContext context, int index) {
      return Text('Item $index');
    }
  ),
);
```

To change the default, users can set `ScrollView.primary` true or false to explicitly manage the `PrimaryScrollController` for an individual `ScrollView`. For behavior across multiple `ScrollView`s, the `PrimaryScrollController` is now configurable by setting the specific platform, as well as the scroll direction that is preferred for inheritance.

Widgets that use the `PrimaryScrollController`, such as `NestedScrollView`, `Scrollbar`, and `DropdownMenuButton` will experience no change to existing functionality. Features like the iOS scroll-to-top will also continue to work as expected without any migration.

`ScrollAction`s, and `ScrollIntent`s on desktop are the only classes affected by this change, requiring migration. By default, the `PrimaryScrollController` is used to execute fallback keyboard scrolling `Shortcuts` if the current `Focus` is contained within a `Scrollable`. Since displaying more than one `ScrollView` side-by-side is common on desktop platforms, it isn't possible for Flutter to decide "Which `ScrollView` should be primary in this view and receive the keyboard scroll action?"

If more than one `ScrollView` was present previous to this change, the same assertion (`ScrollController attached to multiple ScrollViews.`) would be thrown. Now, on desktop platforms, users need to specify `primary: true` to designate which `ScrollView` is the fallback to receive unhandled keyboard `Shortcuts`.

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
// These side-by-side ListViews would throw errors from Scrollbars and
// ScrollActions previously due to the PrimaryScrollController.
Scaffold(
  body: LayoutBuilder(
    builder: (context, constraints) {
      return Row(
        children: [
          SizedBox(
            height: constraints.maxHeight,
            width: constraints.maxWidth / 2,
            child: ListView.builder(
              itemBuilder: (BuildContext context, int index) {
                return Text('List 1 - Item $index');
              }
            ),
          ),
          SizedBox(
            height: constraints.maxHeight,
            width: constraints.maxWidth / 2,
            child: ListView.builder(
              itemBuilder: (BuildContext context, int index) {
                return Text('List 2 - Item $index');
              }
            ),
          ),
        ]
      );
    },
  ),
);
```

Code after migration:

dart

```
// These side-by-side ListViews will no longer throw errors, but for
// default ScrollActions, one will need to be designated as primary.
Scaffold(
  body: LayoutBuilder(
    builder: (context, constraints) {
      return Row(
        children: [
          SizedBox(
            height: constraints.maxHeight,
            width: constraints.maxWidth / 2,
            child: ListView.builder(
              // This ScrollView will use the PrimaryScrollController
              primary: true,
              itemBuilder: (BuildContext context, int index) {
                return Text('List 1 - Item $index');
              }
            ),
          ),
          SizedBox(
            height: constraints.maxHeight,
            width: constraints.maxWidth / 2,
            child: ListView.builder(
              itemBuilder: (BuildContext context, int index) {
                return Text('List 2 - Item $index');
              }
            ),
          ),
        ]
      );
    },
  ),
);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.3.0-0.0.pre  
 In stable release: 3.3

References
----------

[#](#references)

API documentation:

* [`PrimaryScrollController`](https://api.flutter.dev/flutter/widgets/PrimaryScrollController-class.html)* [`ScrollView`](https://api.flutter.dev/flutter/widgets/ScrollView-class.html)* [`ScrollAction`](https://api.flutter.dev/flutter/widgets/ScrollAction-class.html)* [`ScrollIntent`](https://api.flutter.dev/flutter/widgets/ScrollIntent-class.html)* [`Scrollbar`](https://api.flutter.dev/flutter/material/Scrollbar-class.html)

Design document:

* [Updating PrimaryScrollController](https://docs.google.com/document/d/12OQx7h8UQzzAi0Kxh-saDC2dg7h2fghCCzwJ0ysPmZE/edit?usp=sharing&resourcekey=0-ATO-1Er3HO2HITm59I0IdA)

Relevant issues:

* [Issue #100264](https://github.com/flutter/flutter/issues/100264)

Relevant PRs:

* [Updating PrimaryScrollController for Desktop](https://github.com/flutter/flutter/pull/102099)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/primary-scroll-controller-desktop/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/primary-scroll-controller-desktop.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/primary-scroll-controller-desktop/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/primary-scroll-controller-desktop.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-05-14. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/primary-scroll-controller-desktop.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/primary-scroll-controller-desktop/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/primary-scroll-controller-desktop.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   