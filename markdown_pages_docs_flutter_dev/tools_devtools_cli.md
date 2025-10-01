Run DevTools from the command line
==================================

1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [Run DevTools from the command line](/tools/devtools/cli)

To run DevTools from the CLI, you must have `dart` on your path. Then to launch DevTools, run the `dart devtools` command.

To upgrade DevTools, upgrade Flutter. If a newer Dart SDK (which is included in the Flutter SDK) has a newer version of DevTools, running `dart devtools` automatically launches this version. If `which dart` points to a Dart SDK *not* included in your Flutter SDK, updating that Dart SDK won't update the Flutter version.

When you run DevTools from the command line, you should see output that looks something like:

```
Serving DevTools at http://127.0.0.1:9100
```

Start an application to debug
-----------------------------

[#](#start-an-application-to-debug)

Next, start an app to connect to. This can be either a Flutter application or a Dart command-line application. The command below specifies a Flutter app:

```
cd path/to/flutter/app
flutter run
```

You need to have a device connected, or a simulator open, for `flutter run` to work. Once the app starts, you'll see a message in your terminal that looks like the following:

```
A Dart VM Service on macOS is available at:
http://127.0.0.1:51830/u37pq71Re0k=/
The Flutter DevTools debugger and profiler on macOS
is available at:
http://127.0.0.1:9100?uri=http://127.0.0.1:51830/u37pq71Re0k=/
```

Open the DevTools instance connected to your app by opening the second link in Chrome.

This URL contains a security token, so it's different for each run of your app. This means that if you stop your application and re-run it, you need to connect to DevTools again with the new URL.

Connect to a new app instance
-----------------------------

[#](#connect-to-a-new-app-instance)

If your app stops running or you opened DevTools manually, you should see a **Connect** dialog:

![Screenshot of the DevTools connect dialog](/assets/images/docs/tools/devtools/connect_dialog.png)

You can manually connect DevTools to a new app instance by copying the link you got from running your app, such as  `http://127.0.0.1:51830/u37pq71Re0k=/`

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/cli/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/cli.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/cli/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/cli.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-19. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/cli.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/cli/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/cli.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   