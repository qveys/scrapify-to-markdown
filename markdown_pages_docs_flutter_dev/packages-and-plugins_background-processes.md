Background processes
====================

1. [Packages & plugins](/packages-and-plugins) chevron\_right- [Background processes](/packages-and-plugins/background-processes)

Have you ever wanted to execute Dart code in the background—even if your app wasn't the currently active app? Perhaps you wanted to implement a process that watches the time, or that catches camera movement. In Flutter, you can execute Dart code in the background.

The mechanism for this feature involves setting up an isolate. *Isolates* are Dart's model for multithreading, though an isolate differs from a conventional thread in that it doesn't share memory with the main program. You'll set up your isolate for background execution using callbacks and a callback dispatcher.

Additionally, the [WorkManager](https://pub.dev/packages/workmanager) plugin enables persistent background processing that keeps tasks scheduled through app restarts and system reboots.

For more information and a geofencing example that uses background execution of Dart code, see the Medium article by Ben Konyi, [Executing Dart in the Background with Flutter Plugins and Geofencing](https://blog.flutter.dev/executing-dart-in-the-background-with-flutter-plugins-and-geofencing-2b3e40a1a124). At the end of this article, you'll find links to example code, and relevant documentation for Dart, iOS, and Android.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/background-processes/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/background-processes.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/background-processes/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/background-processes.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/background-processes.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/background-processes/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/background-processes.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   