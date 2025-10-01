AI rules for Flutter and Dart
=============================

1. [AI rules for Flutter and Dart](/ai/ai-rules)

This guide covers how you can leverage AI rules to streamline your Flutter and Dart development.

Overview
--------

[#](#overview)

AI-powered editors use rules files to provide context and instructions to an underlying LLM. These files help you:

* Customize AI behavior to your team's needs.* Enforce project best practices for code style and design.* Provide critical project context to the AI.

 [download Download the Flutter and Dart rules template](https://raw.githubusercontent.com/flutter/flutter/refs/heads/master/docs/rules/rules.md) 

Environments that support rules
-------------------------------

[#](#environments-that-support-rules)

Many AI environments support rules files to guide LLM behavior. Here are some common examples and their corresponding rule file names:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Environment Rules File Installation Instructions|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Copilot powered IDEs `copilot-instructions.md` [Configure .github/copilot-instructions.md](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions)| Cursor `cursor.md` [Configure cursorrules.md](https://docs.cursor.com/en/context/rules)| Firebase Studio `airules.md` [Configure airules.md](https://firebase.google.com/docs/studio/set-up-gemini#custom-instructions)| Gemini CLI `GEMINI.md` [Configure GEMINI.md](https://codelabs.developers.google.com/gemini-cli-hands-on)| JetBrains IDEs `guidelines.md` [Configure guidelines.md](https://www.jetbrains.com/help/junie/customize-guidelines.html)| VS Code `.instructions.md` [Configure .instructions.md](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions)| Windsurf `guidelines.md` [Configure guidelines.md](https://www.jetbrains.com/help/junie/customize-guidelines.html) | | | | | | | | | | | | | | | | | | | | | | | |

Create rules for your editor
----------------------------

[#](#create-rules-for-your-editor)

You can adapt our Flutter and Dart rules template for your specific environment. To do so, follow these steps:

1. Download the Flutter and Dart rules template: [rules.md](https://raw.githubusercontent.com/flutter/flutter/refs/heads/master/docs/rules/rules.md)- In an LLM like [Gemini](https://gemini.google.com/), attach the `rules.md` file that you downloaded in the last step.- Provide a prompt to reformat the file for your desired editor.

       Example prompt:

       text

       ```
       Convert the attached rules.md file
       into a guidelines.md file for Gemini CLI. Make sure
       to use the styles required for a guidelines.md file.
       ```

       - Review the LLM's output and make any necessary adjustments.- Follow your environment's instructions to add the new rules file. This may involve adding to an existing file or creating a new one.- Verify that your AI assistant is using the new rules to guide its responses.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ai/ai-rules/&page-source=https://github.com/flutter/website/tree/main/src/content/ai/ai-rules.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ai/ai-rules/&page-source=https://github.com/flutter/website/tree/main/src/content/ai/ai-rules.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-18. [View source](https://github.com/flutter/website/tree/main/src/content/ai/ai-rules.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ai/ai-rules/&page-source=https://github.com/flutter/website/tree/main/src/content/ai/ai-rules.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   