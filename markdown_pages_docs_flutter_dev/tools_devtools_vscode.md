Run DevTools from VS Code
=========================

1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [Run DevTools from VS Code](/tools/devtools/vscode)

Add the VS Code extensions
--------------------------

[#](#add-the-vs-code-extensions)

To use the DevTools from VS Code, you need the [Dart extension](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code). If you're debugging Flutter applications, you should also install the [Flutter extension](https://marketplace.visualstudio.com/items?itemName=Dart-Code.flutter).

Start an application to debug
-----------------------------

[#](#run-and-debug)

Start a debug session for your application by opening the root folder of your project (the one containing `pubspec.yaml`) in VS Code and clicking **Run > Start Debugging** (`F5`).

Launch DevTools
---------------

[#](#launch-devtools)

Once the debug session is active and the application has started, the **Open DevTools** commands become available in the VS Code command palette (`F1`):

![Screenshot showing Open DevTools commands](/assets/images/docs/tools/vs-code/vscode_command.png)

The chosen tool will be opened embedded inside VS Code.

![Screenshot showing DevTools embedded in VS Code](/assets/images/docs/tools/vs-code/vscode_embedded.png)

You can choose to have DevTools always opened in a browser with the `dart.embedDevTools` setting, and control whether it opens as a full window or in a new column next to your current editor with the `dart.devToolsLocation` setting.

A full list of Dart/Flutter settings are available on [dartcode.org](https://dartcode.org/docs/settings/) or in the [VS Code settings editor](https://code.visualstudio.com/docs/getstarted/settings#_settings-editor). Some recommendation settings for Dart/Flutter in VS Code can also be found on [dartcode.org](https://dartcode.org/docs/recommended-settings/).

You can also see whether DevTools is running and launch it in a browser from the language status area (the `{}` icon next to **Dart** in the status bar).

![Screenshot showing DevTools in the VS Code language status area](/assets/images/docs/tools/vs-code/vscode_status_bar.png)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/vscode/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/vscode.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/vscode/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/vscode.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-06-28. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/vscode.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/vscode/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/vscode.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   