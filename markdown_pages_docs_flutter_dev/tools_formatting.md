Code formatting
===============

1. [Tools](/tools) chevron\_right- [Code formatting](/tools/formatting)

While your code might follow any preferred style—in our experience—teams of developers might find it more productive to:

* Have a single, shared style, and* Enforce this style through automatic formatting.

The alternative is often tiring formatting debates during code reviews, where time might be better spent on code behavior rather than code style.

Automatically formatting code in VS Code
----------------------------------------

[#](#automatically-formatting-code-in-vs-code)

Install the `Flutter` extension (see [VS Code setup](/tools/vs-code#setup)) to get automatic formatting of code in VS Code.

To automatically format the code in the current source code window, right-click in the code window and select `Format Document`. You can add a keyboard shortcut to this VS Code **Preferences**.

To automatically format code whenever you save a file, set the `editor.formatOnSave` setting to `true`.

Automatically formatting code in Android Studio and IntelliJ
------------------------------------------------------------

[#](#automatically-formatting-code-in-android-studio-and-intellij)

Install the `Dart` plugin (see [Android Studio and IntelliJ setup](/tools/android-studio#setup)) to get automatic formatting of code in Android Studio and IntelliJ. To format your code in the current source code window:

* On macOS, press `Cmd` + `Option` + `L`.* On Windows and Linux, press `Ctrl` + `Alt` + `L`.

Android Studio and IntelliJ also provide a checkbox named **Format code on save** on the Flutter page in **Preferences** on macOS or **Settings** on Windows and Linux. This option corrects formatting in the current file when you save it.

Automatically formatting code with the `dart` command
-----------------------------------------------------

[#](#automatically-formatting-code-with-the-dart-command)

To correct code formatting in the command line interface (CLI), run the `dart format` command:

```
dart format path1 path2 [...]
```

To learn more about the Dart formatter, check out the dart.dev docs on [`dart format`](https://dart.dev/tools/dart-format).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/formatting/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/formatting.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/formatting/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/formatting.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-29. [View source](https://github.com/flutter/website/tree/main/src/content/tools/formatting.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/formatting/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/formatting.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   