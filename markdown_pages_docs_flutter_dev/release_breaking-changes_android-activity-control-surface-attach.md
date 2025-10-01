Android ActivityControlSurface attachToActivity signature change
================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Android ActivityControlSurface attachToActivity signature change](/release/breaking-changes/android-activity-control-surface-attach)

Summary
-------

[#](#summary)

*info* Note

If you use standard Android embedding Java classes like [`FlutterActivity`](https://api.flutter.dev/javadoc/io/flutter/embedding/android/FlutterActivity.html) or [`FlutterFragment`](https://api.flutter.dev/javadoc/io/flutter/embedding/android/FlutterFragment.html), and don't manually embed a [`FlutterView`](https://api.flutter.dev/javadoc/io/flutter/view/FlutterView.html) inside your own custom `Activity` (this should be uncommon), you can stop reading.

A new [`ActivityControlSurface`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/plugins/activity/ActivityControlSurface.html) method:

java

```
void attachToActivity(
    @NonNull ExclusiveAppComponent<Activity> exclusiveActivity,
    @NonNull Lifecycle lifecycle);
```

is replacing the now deprecated method:

java

```
void attachToActivity(@NonNull Activity activity, @NonNull Lifecycle lifecycle);
```

The existing deprecated method with the `Activity` parameter was removed in Flutter 2.

Context
-------

[#](#context)

In order for custom Activities to also supply the `Activity` lifecycle events Flutter plugins expect using the [`ActivityAware`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/plugins/activity/ActivityAware.html) interface, the [`FlutterEngine`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html) exposed a [`getActivityControlSurface()`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html#getActivityControlSurface--) API.

This allows custom Activities to signal to the engine (with which it has a `(0|1):1` relationship) that it was being attached or detached from the engine.

*info* Note

This lifecycle signaling is done automatically when you use the engine's bundled [`FlutterActivity`](https://api.flutter.dev/javadoc/io/flutter/embedding/android/FlutterActivity.html) or [`FlutterFragment`](https://api.flutter.dev/javadoc/io/flutter/embedding/android/FlutterFragment.html), which should be the most common case.

However, the previous API had the flaw that it didn't enforce exclusion between activities connecting to the engine, thus enabling `n:1` relationships between the activity and the engine, causing lifecycle cross-talk issues.

Description of change
---------------------

[#](#description-of-change)

After [Issue #21272](https://github.com/flutter/engine/pull/21272), instead of attaching your activity to the [`FlutterEngine`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html) by using the:

java

```
void attachToActivity(@NonNull Activity activity, @NonNull Lifecycle lifecycle);
```

API, which is now deprecated, instead use:

java

```
void attachToActivity(
    @NonNull ExclusiveAppComponent<Activity> exclusiveActivity,
    @NonNull Lifecycle lifecycle);
```

An `ExclusiveAppComponent<Activity>` interface is now expected instead of an `Activity`. The `ExclusiveAppComponent<Activity>` provides a callback in case your exclusive activity is being replaced by another activity attaching itself to the `FlutterEngine`.

java

```
void detachFromActivity();
```

API remains unchanged and you're still expected to call it when your custom activity is being destroyed naturally.

Migration guide
---------------

[#](#migration-guide)

If you have your own activity holding a [`FlutterView`](https://api.flutter.dev/javadoc/io/flutter/view/FlutterView.html), replace calls to:

java

```
void attachToActivity(@NonNull Activity activity, @NonNull Lifecycle lifecycle);
```

with calls to:

java

```
void attachToActivity(
    @NonNull ExclusiveAppComponent<Activity> exclusiveActivity,
    @NonNull Lifecycle lifecycle);
```

on the [`ActivityControlSurface`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/plugins/activity/ActivityControlSurface.html) that you obtained by calling [`getActivityControlSurface()`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html#getActivityControlSurface--) on the [`FlutterEngine`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html).

Wrap your activity with an `ExclusiveAppComponent<Activity>` and implement the callback method:

java

```
void detachFromFlutterEngine();
```

to handle your activity being replaced by another activity being attached to the [`FlutterEngine`](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html). Generally, you want to perform the same detaching operations as performed when the activity is being naturally destroyed.

Timeline
--------

[#](#timeline)

Landed in version: 1.23.0-7.0.pre  
 In stable release: 2.0.0

References
----------

[#](#references)

Motivating bug: [Issue #66192](https://github.com/flutter/flutter/issues/66192.)—Non exclusive UI components attached to the FlutterEngine causes event crosstalk

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-activity-control-surface-attach/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-activity-control-surface-attach.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-activity-control-surface-attach/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-activity-control-surface-attach.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-activity-control-surface-attach.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-activity-control-surface-attach/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-activity-control-surface-attach.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   