Protect your app's sensitive content
====================================

1. [Platform integration](/platform-integration) chevron\_right- [Android](/platform-integration/android) chevron\_right- [Sensitive content](/platform-integration/android/sensitive-content)

This feature is available on Android API 35+, and you can try it out by using the [`SensitiveContent`](https://api.flutter.dev/flutter/widgets/SensitiveContent-class.html) widget. See the guide below for details.

About the `SensitiveContent` widget
-----------------------------------

[#](#about-the-sensitivecontent-widget)

You can use the `SensitiveContent` widget in your app to set the content sensitivity of a child `Widget` to one of the following [`ContentSensitivity`](https://api.flutter.dev/flutter/services/ContentSensitivity.html) values: `notSensitive`, `sensitive`, or `autoSensitive`. The mode that you choose helps to determine if the device screen should be obscured (blacked out) during media projection to protect users’ sensitive data.

You can have as many `SensitiveContent` widgets in your app as you wish, but if *any* one of those widgets has a `sensitive` content value, then the screen will be obscured during media projection. Thus, for most use cases, using multiple `SensitiveContent` widgets provides no advantage over having one `SensitiveContent` widget in your app’s widget tree. This feature is available on Android API 35+ and has no effect on lower API versions and other platforms.

*info* Note

The `autoSensitive` value isn't supported as of Flutter 3.35 and behaves the same as `notSensitive`. See the [Issue #160879](https://github.com/flutter/flutter/issues/160879) for more information.

Using the `SensitiveContent` widget
-----------------------------------

[#](#using-the-sensitivecontent-widget)

Given some content that you want to protect from media screen share (for example, a `MySensitiveContent()` widget), you can wrap it with the `SensitiveContent` widget as shown in the following example:

dart

```
class MyWidget extends StatelessWidget {
  ...
  Widget build(BuildContext context) {
    return SensitiveContent(
      sensitivity: ContentSensitivity.sensitive,
      child: MySensitiveContent(),
    );
  }
}
```

When running on Android API 34 and below, the screen will not be obscured during media projection. The widget will exist in the tree but has no other effect, and you do not need to avoid usages of `SensitiveContent` on platforms that do not support this feature.

For more information
--------------------

[#](#for-more-information)

For more information, visit the [`SensitiveContent`](https://api.flutter.dev/flutter/widgets/SensitiveContent-class.html) and [`ContentSensitivity`](https://api.flutter.dev/flutter/services/ContentSensitivity.html) API docs.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/sensitive-content/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/sensitive-content.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/sensitive-content/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/sensitive-content.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/android/sensitive-content.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/sensitive-content/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/sensitive-content.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   