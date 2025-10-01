Adaptive and responsive design in Flutter
=========================================

1. [UI](/ui) chevron\_right- [Adaptive design](/ui/adaptive-responsive)

![List of supported platforms](/assets/images/docs/ui/adaptive-responsive/platforms.png)

One of Flutter's primary goals is to create a framework that allows you to develop apps from a single codebase that look and feel great on any platform.

This means that your app might appear on screens of many different sizes, from a watch, to a foldable phone with two screens, to a high definition monitor. And your input device might be a physical or virtual keyboard, a mouse, a touchscreen, or any number of other devices.

Two terms that describe these design concepts are *adaptive* and *responsive*. Ideally, you'd want your app to be *both* but what, exactly, does this mean?

What is responsive vs adaptive?
-------------------------------

[#](#what-is-responsive-vs-adaptive)

An easy way to think about it is that responsive design is about fitting the UI *into* the space and adaptive design is about the UI being *usable* in the space.

So, a responsive app adjusts the placement of design elements to *fit* the available space. And an adaptive app selects the appropriate layout and input devices to be usable *in* the available space. For example, should a tablet UI use bottom navigation or side-panel navigation?

*info* Note

Often adaptive and responsive concepts are collapsed into a single term. Most often, *adaptive design* is used to refer to both adaptive and responsive.

This section covers various aspects of adaptive and responsive design:

* [General approach](/ui/adaptive-responsive/general)* [SafeArea & MediaQuery](/ui/adaptive-responsive/safearea-mediaquery)* [Large screens & foldables](/ui/adaptive-responsive/large-screens)* [User input & accessibility](/ui/adaptive-responsive/input)* [Capabilities & policies](/ui/adaptive-responsive/capabilities)* [Best practices for adaptive apps](/ui/adaptive-responsive/best-practices)* [Additional resources](/ui/adaptive-responsive/more-info)

*info* Note

You might also check out the Google I/O 2024 talk about this subject.

[Watch on YouTube in a new tab: "How to build adaptive UI with Flutter"](https://www.youtube.com/watch/LeKLGzpsz9I)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/adaptive-responsive/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/adaptive-responsive/index.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/adaptive-responsive/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/adaptive-responsive/index.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/ui/adaptive-responsive/index.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/adaptive-responsive/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/adaptive-responsive/index.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   