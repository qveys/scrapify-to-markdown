Flutter fix
===========

1. [Tools](/tools) chevron\_right- [Flutter fix](/tools/flutter-fix)

As Flutter continues to evolve, we provide a tool to help you clean up deprecated APIs from your codebase. The tool ships as part of Flutter, and suggests changes that you might want to make to your code. The tool is available from the command line, and is also integrated into the IDE plugins for Android Studio and Visual Studio Code.

*lightbulb* Tip

These automated updates are called *quick-fixes* in IntelliJ and Android Studio, and *code actions* in VS Code.

Applying individual fixes
-------------------------

[#](#applying-individual-fixes)

You can use any supported IDE to apply a single fix at a time.

### IntelliJ and Android Studio

[#](#intellij-and-android-studio)

When the analyzer detects a deprecated API, a light bulb appears on that line of code. Clicking the light bulb displays the suggested fix that updates that code to the new API. Clicking the suggested fix performs the update.

![Screenshot showing suggested change in IntelliJ](/assets/images/docs/development/tools/flutter-fix-suggestion-intellij.png)  
 A sample quick-fix in IntelliJ

### VS Code

[#](#vs-code)

When the analyzer detects a deprecated API, it presents an error. You can do any of the following:

* Hover over the error and then click the **Quick Fix** link. This presents a filtered list showing *only* fixes.* Put the caret in the code with the error and click the light bulb icon that appears. This shows a list of all actions, including refactors.* Put the caret in the code with the error and press the shortcut (**Command+.** on macOS, **Control+.** elsewhere) This shows a list of all actions, including refactors.

![Screenshot showing suggested change in VS Code](/assets/images/docs/development/tools/flutter-fix-suggestion-vscode.png)  
 A sample code action in VS Code

Applying project-wide fixes
---------------------------

[#](#applying-project-wide-fixes)

[dart fix Decoding Flutter](https://www.youtube.com/watch?v=OBIuSrg_Quo)

To see or apply changes to an entire project, you can use the command-line tool, [`dart fix`](https://dart.dev/tools/dart-fix).

This tool has two options:

* To see a full list of available changes, run the following command:

  ```
  dart fix --dry-run
  ```

  * To apply all changes in bulk, run the following command:

    ```
    dart fix --apply
    ```

For more information on Flutter deprecations, see [Deprecation lifetime in Flutter](https://blog.flutter.dev/deprecation-lifetime-in-flutter-e4d76ee738ad), a free article on Flutter's Medium publication.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/flutter-fix/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/flutter-fix.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/flutter-fix/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/flutter-fix.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/tools/flutter-fix.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/flutter-fix/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/flutter-fix.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   