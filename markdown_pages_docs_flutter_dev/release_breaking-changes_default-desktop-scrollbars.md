Default Scrollbars on Desktop
=============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Default Scrollbars on Desktop](/release/breaking-changes/default-desktop-scrollbars)

Summary
-------

[#](#summary)

`ScrollBehavior`s now automatically apply `Scrollbar`s to scrolling widgets on desktop platforms - Mac, Windows and Linux.

Context
-------

[#](#context)

Prior to this change, `Scrollbar`s were applied to scrolling widgets manually by the developer across all platforms. This did not match developer expectations when executing Flutter applications on desktop platforms.

Now, the inherited `ScrollBehavior` applies a `Scrollbar` automatically to most scrolling widgets. This is similar to how `GlowingOverscrollIndicator` is created by `ScrollBehavior`. The few widgets that are exempt from this behavior are listed below.

To provide better management and control of this feature, `ScrollBehavior` has also been updated. The `buildViewportChrome` method, which applied a `GlowingOverscrollIndicator`, has been deprecated. Instead, `ScrollBehavior` now supports individual methods for decorating the viewport, `buildScrollbar` and `buildOverscrollIndicator`. These methods can be overridden to control what is built around the scrollable.

Furthermore, `ScrollBehavior` subclasses `MaterialScrollBehavior` and `CupertinoScrollBehavior` have been made public, allowing developers to extend and build upon the other existing `ScrollBehavior`s in the framework. These subclasses were previously private.

Description of change
---------------------

[#](#description-of-change)

The previous approach called on developers to create their own `Scrollbar`s on all platforms. In some use cases, a `ScrollController` would need to be provided to the `Scrollbar` and the scrollable widget.

dart

```
final ScrollController controller = ScrollController();
Scrollbar(
  controller: controller,
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
      return Text('Item $index');
    }
  )
);
```

The `ScrollBehavior` now applies the `Scrollbar` automatically when executing on desktop, and handles providing the `ScrollController` to the `Scrollbar` for you.

dart

```
final ScrollController controller = ScrollController();
ListView.builder(
  controller: controller,
  itemBuilder: (BuildContext context, int index) {
   return Text('Item $index');
 }
);
```

Some widgets in the framework are exempt from this automatic `Scrollbar` application. They are:

* `EditableText`, when `maxLines` is 1.* `ListWheelScrollView`* `PageView`* `NestedScrollView`

Since these widgets manually override the inherited `ScrollBehavior` to remove `Scrollbar`s, all of these widgets now have a `scrollBehavior` parameter so that one can be provided to use instead of the override.

This change did not cause any test failures, crashes, or error messages in the course of development, but it may result in two `Scrollbar`s being rendered in your application if you are manually adding `Scrollbar`s on desktop platforms.

If you are seeing this in your application, there are several ways to control and configure this feature.

* Remove the manually applied `Scrollbar`s in your application when running on desktop.* Extend `ScrollBehavior`, `MaterialScrollBehavior`, or `CupertinoScrollBehavior` to modify the default behavior.
    + With your own `ScrollBehavior`, you can apply it app-wide by setting `MaterialApp.scrollBehavior` or `CupertinoApp.scrollBehavior`.+ Or, if you wish to only apply it to specific widgets, add a `ScrollConfiguration` above the widget in question with your custom `ScrollBehavior`.

Your scrollable widgets then inherits this and reflects this behavior.

* Instead of creating your own `ScrollBehavior`, another option for changing the default behavior is to copy the existing `ScrollBehavior`, and toggle the desired feature.
  + Create a `ScrollConfiguration` in your widget tree, and provide a modified copy of the existing `ScrollBehavior` in the current context using `copyWith`.

Migration guide
---------------

[#](#migration-guide)

### Removing manual `Scrollbar`s on desktop

[#](#removing-manual-scrollbars-on-desktop)

Code before migration:

dart

```
final ScrollController controller = ScrollController();
Scrollbar(
  controller: controller,
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
      return Text('Item $index');
    }
  )
);
```

Code after migration:

dart

```
final ScrollController controller = ScrollController();
final Widget child = ListView.builder(
  controller: controller,
  itemBuilder: (BuildContext context, int index) {
    return Text('Item $index');
  }
);
// Only manually add a `Scrollbar` when not on desktop platforms.
// Or, see other migrations for changing `ScrollBehavior`.
switch (currentPlatform) {
  case TargetPlatform.linux:
  case TargetPlatform.macOS:
  case TargetPlatform.windows:
    return child;
  case TargetPlatform.android:
  case TargetPlatform.fuchsia:
  case TargetPlatform.iOS:
    return Scrollbar(
      controller: controller,
      child: child;
    );
}
```

### Setting a custom `ScrollBehavior` for your application

[#](#setting-a-custom-scrollbehavior-for-your-application)

Code before migration:

dart

```
// MaterialApps previously had a private ScrollBehavior.
MaterialApp(
  // ...
);
```

Code after migration:

dart

```
// MaterialApps previously had a private ScrollBehavior.
// This is available to extend now.
class MyCustomScrollBehavior extends MaterialScrollBehavior {
  // Override behavior methods like buildOverscrollIndicator and buildScrollbar
}

// ScrollBehavior can now be configured for an entire application.
MaterialApp(
  scrollBehavior: MyCustomScrollBehavior(),
  // ...
);
```

### Setting a custom `ScrollBehavior` for a specific widget

[#](#setting-a-custom-scrollbehavior-for-a-specific-widget)

Code before migration:

dart

```
final ScrollController controller = ScrollController();
ListView.builder(
  controller: controller,
  itemBuilder: (BuildContext context, int index) {
   return Text('Item $index');
 }
);
```

Code after migration:

dart

```
// MaterialApps previously had a private ScrollBehavior.
// This is available to extend now.
class MyCustomScrollBehavior extends MaterialScrollBehavior {
  // Override behavior methods like buildOverscrollIndicator and buildScrollbar
}

// ScrollBehavior can be set for a specific widget.
final ScrollController controller = ScrollController();
ScrollConfiguration(
  behavior: MyCustomScrollBehavior(),
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
     return Text('Item $index');
    }
  ),
);
```

### Copy and modify existing `ScrollBehavior`

[#](#copy-and-modify-existing-scrollbehavior)

Code before migration:

dart

```
final ScrollController controller = ScrollController();
ListView.builder(
  controller: controller,
  itemBuilder: (BuildContext context, int index) {
   return Text('Item $index');
 }
);
```

Code after migration:

dart

```
// ScrollBehavior can be copied and adjusted.
final ScrollController controller = ScrollController();
ScrollConfiguration(
  behavior: ScrollConfiguration.of(context).copyWith(scrollbars: false),
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
     return Text('Item $index');
    }
  ),
);
```

Timeline
--------

[#](#timeline)

Landed in version: 2.2.0-10.0.pre  
 In stable release: 2.2.0

References
----------

[#](#references)

API documentation:

* [`ScrollConfiguration`](https://api.flutter.dev/flutter/widgets/ScrollConfiguration-class.html)* [`ScrollBehavior`](https://api.flutter.dev/flutter/widgets/ScrollBehavior-class.html)* [`MaterialScrollBehavior`](https://api.flutter.dev/flutter/material/MaterialScrollBehavior-class.html)* [`CupertinoScrollBehavior`](https://api.flutter.dev/flutter/cupertino/CupertinoScrollBehavior-class.html)* [`Scrollbar`](https://api.flutter.dev/flutter/material/Scrollbar-class.html)* [`CupertinoScrollbar`](https://api.flutter.dev/flutter/cupertino/CupertinoScrollbar-class.html)

Relevant issues:

* [Issue #40107](https://github.com/flutter/flutter/issues/40107)* [Issue #70866](https://github.com/flutter/flutter/issues/70866)

Relevant PRs:

* [Exposing ScrollBehaviors for app-wide settings](https://github.com/flutter/flutter/pull/76739)* [Automatically applying Scrollbars on desktop platforms with configurable ScrollBehaviors](https://github.com/flutter/flutter/pull/78588)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-desktop-scrollbars/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-desktop-scrollbars.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-desktop-scrollbars/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-desktop-scrollbars.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-desktop-scrollbars.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-desktop-scrollbars/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-desktop-scrollbars.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   