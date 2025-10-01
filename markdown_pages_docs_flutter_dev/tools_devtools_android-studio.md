Run DevTools from Android Studio
================================

1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [Run DevTools from Android Studio](/tools/devtools/android-studio)

Install the Flutter plugin
--------------------------

[#](#install-the-flutter-plugin)

Add the Flutter plugin if you don't already have it installed. This can be done using the normal **Plugins** page in the IntelliJ and Android Studio settings. Once that page is open, you can search the marketplace for the Flutter plugin.

Start an app to debug
---------------------

[#](#run-and-debug)

To open DevTools, you first need to run a Flutter app. This can be accomplished by opening a Flutter project, ensuring that you have a device connected, and clicking the **Run** or **Debug** toolbar buttons.

Launch DevTools from the toolbar/menu
-------------------------------------

[#](#launch-devtools-from-the-toolbarmenu)

Once an app is running, you can start DevTools using one of the following techniques:

* Select the **Open DevTools** toolbar action in the Run view.* Select the **Open DevTools** toolbar action in the Debug view. (if debugging)* Select the **Open DevTools** action from the **More Actions** menu in the Flutter Inspector view.

![screenshot of Open DevTools button](/assets/images/docs/tools/devtools/android_studio_open_devtools.png)

Launch DevTools from an action
------------------------------

[#](#launch-devtools-from-an-action)

You can also open DevTools from an IntelliJ action. Open the **Find Action...** dialog (on macOS, press `Cmd` + `Shift` + `A`), and search for the **Open DevTools** action. When you select that action, the DevTools server launches and a browser instance opens pointing to the DevTools app.

When opened with an IntelliJ action, DevTools is not connected to a Flutter app. You'll need to provide a service protocol port for a currently running app. You can do this using the inline **Connect to a running app** dialog.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/android-studio/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/android-studio.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/android-studio/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/android-studio.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-15. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/android-studio.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/android-studio/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/android-studio.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   