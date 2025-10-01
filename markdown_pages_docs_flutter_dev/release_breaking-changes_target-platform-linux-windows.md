Adding 'linux' and 'windows' to TargetPlatform enum
===================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Adding 'linux' and 'windows' to TargetPlatform enum](/release/breaking-changes/target-platform-linux-windows)

Summary
-------

[#](#summary)

Two new values were added to the [`TargetPlatform`](https://api.flutter.dev/flutter/foundation/TargetPlatform-class.html) enum that could require additional cases in switch statements that switch on a `TargetPlatform` and don't include a `default:` case.

Context
-------

[#](#context)

Prior to this change, the `TargetPlatform` enum only contained four values, and was defined like this:

dart

```
enum TargetPlatform {
  android,
  fuchsia,
  iOS,
  macOS,
}
```

A `switch` statement only needed to handle these cases, and desktop applications that wanted to run on Linux or Windows usually had a test like this in their `main()` method:

dart

```
// Sets a platform override for desktop to avoid exceptions. See
// https://docs.flutter.dev/desktop#target-platform-override for more info.
void _enablePlatformOverrideForDesktop() {
  if (!kIsWeb && (Platform.isWindows || Platform.isLinux)) {
    debugDefaultTargetPlatformOverride = TargetPlatform.fuchsia;
  }
}

void main() {
  _enablePlatformOverrideForDesktop();
  runApp(MyApp());
}
```

Description of change
---------------------

[#](#description-of-change)

The `TargetPlatform` enum is now defined as:

dart

```
enum TargetPlatform {
  android,
  fuchsia,
  iOS,
  linux, // new value
  macOS,
  windows, // new value
}
```

And the platform test setting [`debugDefaultTargetPlatformOverride`](https://api.flutter.dev/flutter/foundation/debugDefaultTargetPlatformOverride.html) in `main()` is no longer required on Linux and Windows.

This can cause the Dart analyzer to give the [`missing_enum_constant_in_switch`](https://dart.dev/tools/diagnostic-messages#missing_enum_constant_in_switch) warning for switch statements that don't include a `default` case. Writing a switch without a `default:` case is the recommended way to handle enums, since the analyzer can then help you find any cases that aren't handled.

Migration guide
---------------

[#](#migration-guide)

In order to migrate to the new enum, and avoid the analyzer's `missing_enum_constant_in_switch` error, which looks like:

```
warning: Missing case clause for 'linux'. (missing_enum_constant_in_switch at [package] path/to/file.dart:111)
```

or:

```
warning: Missing case clause for 'windows'. (missing_enum_constant_in_switch at [package] path/to/file.dart:111)
```

Modify your code as follows:

Code before migration:

dart

```
void dance(TargetPlatform platform) {
  switch (platform) {
    case TargetPlatform.android:
      // Do Android dance.
      break;
    case TargetPlatform.fuchsia:
      // Do Fuchsia dance.
      break;
    case TargetPlatform.iOS:
      // Do iOS dance.
      break;
    case TargetPlatform.macOS:
      // Do macOS dance.
      break;
  }
}
```

Code after migration:

dart

```
void dance(TargetPlatform platform) {
  switch (platform) {
    case TargetPlatform.android:
      // Do Android dance.
      break;
    case TargetPlatform.fuchsia:
      // Do Fuchsia dance.
      break;
    case TargetPlatform.iOS:
      // Do iOS dance.
      break;
    case TargetPlatform.linux: // new case
      // Do Linux dance.
      break;
    case TargetPlatform.macOS:
      // Do macOS dance.
      break;
    case TargetPlatform.windows: // new case
      // Do Windows dance.
      break;
  }
}
```

Having `default:` cases in such switch statements isn't recommended, because then the analyzer can't help you find all the cases that need to be handled.

Also, any tests like the one referenced above that set the `debugDefaultTargetPlatformOverride` are no longer needed for Linux and Windows applications.

Timeline
--------

[#](#timeline)

Landed in version: 1.15.4  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`TargetPlatform`](https://api.flutter.dev/flutter/foundation/TargetPlatform-class.html)

Relevant issues:

* [Issue #31366](https://github.com/flutter/flutter/issues/31366)

Relevant PR:

* [Add Windows, and Linux as TargetPlatforms](https://github.com/flutter/flutter/pull/51519)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/target-platform-linux-windows/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/target-platform-linux-windows.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/target-platform-linux-windows/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/target-platform-linux-windows.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/target-platform-linux-windows.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/target-platform-linux-windows/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/target-platform-linux-windows.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   