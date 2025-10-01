Create with AI
==============

1. [Create with AI](/ai/create-with-ai)

This guide covers how you can leverage AI tools to build AI-powered features for your Flutter apps and streamline your Flutter and Dart development.

Overview
--------

[#](#overview)

AI can be used for building AI-powered apps with Flutter and for accelerating your development workflow. You can integrate AI-powered features like natural language understanding and content generation directly into your Flutter app using powerful SDKs, like the Firebase SDK for Generative AI. You can also use AI tools, such as Gemini Code Assist and Gemini CLI, to help with code generation and scaffolding. These tools are powered by the Dart and Flutter MCP Server, which provides AI with a rich context about your codebase. Additionally, rules files help fine-tune the AI's behavior and enforce project-specific best practices.

Build AI-powered experiences with Flutter
-----------------------------------------

[#](#build-ai-powered-experiences-with-flutter)

Using AI in your Flutter app unlocks new user experiences that allow your app to support natural language understanding and content generation.

To get started building AI-powered experiences in Flutter, check out these resources:

* [Firebase AI Logic](https://firebase.google.com/docs/ai-logic) - The official Firebase SDK for using generative AI features directly in Flutter. Compatible with the Gemini Developer API or Vertex AI. To get started, check out the [official documentation](https://firebase.google.com/docs/ai-logic/get-started).* [Flutter AI Toolkit](https://docs.flutter.dev/ai-toolkit) - A sample app with pre-built widgets to help you build AI-powered features in Flutter

AI development tools
--------------------

[#](#ai-development-tools)

AI can not only be a feature in your app, but also a powerful assistant in your development workflow. Tools like Gemini Code Assist and the Gemini CLI can help you write code faster, understand complex concepts, and reduce boilerplate.

### Gemini Code Assist

[#](#gemini-code-assist)

[Gemini Code Assist](https://codeassist.google/) is an AI-powered collaborator available in Visual Studio Code and JetBrains IDEs (including Android Studio). It has a deep understanding of your project's codebase and can help you with:

* **Code completion and generation**: It suggests and generates entire blocks of code based on the context of what you're writing.* **In-editor chat**: You can ask questions about your code, Flutter concepts, or best practices directly within your IDE.* **Debugging and explanation**: If you encounter an error, you can ask Gemini Code Assist to explain it and suggest a fix, and [Dart and Flutter MCP Server](#dart-and-flutter-mcp-server)

### Gemini CLI

[#](#gemini-cli)

The [Gemini CLI](https://github.com/google-gemini/gemini-cli) is a command-line AI workflow tool. It allows you to interact with Gemini models for a variety of tasks without leaving your development environment. You can use it to:

* Quickly scaffold a new Flutter widget, Dart function, or a complete app.* Use MCP server tools, such as the Dart and Flutter MCP server* Automate tasks like committing and pushing changes to a Git repository

To get started, visit the [Gemini CLI](https://github.com/google-gemini/gemini-cli) website, or try this [Gemini CLI codelab](https://codelabs.developers.google.com/gemini-cli-hands-on).

Dart and Flutter MCP Server
---------------------------

[#](#dart-and-flutter-mcp-server)

To provide assistance during Flutter development, AI tools such as Gemini Code Assist and Gemini CLI need to communicate with Dart and Flutter's developer tools. The Dart and Flutter MCP Server facilitates this communication. MCP (model context protocol) is a specification that outlines how development tools can share the context of a user's code with an AI model, which allows the AI to better understand and interact with the code.

The Dart and Flutter MCP server provides a growing list of tools to analyze and fix errors, hot reload, get the selected widget, and more. This bridges the gap between the AI's natural language understanding, and Dart and Flutter's suite of developer tools.

To get started, check out the official documentation for the [Dart and Flutter MCP server](https://dart.dev/tools/mcp-server) on dart.dev and the [Dart and Flutter MCP repository](https://github.com/dart-lang/ai/tree/main/pkgs/dart_mcp_server).

Rules for Flutter and Dart
--------------------------

[#](#rules-for-flutter-and-dart)

You can use a rules file with AI-powered editors to provide context and instructions to an underlying LLM. To get started, see the [AI rules for Flutter and Dart](/ai/ai-rules) guide.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ai/create-with-ai/&page-source=https://github.com/flutter/website/tree/main/src/content/ai/create-with-ai.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ai/create-with-ai/&page-source=https://github.com/flutter/website/tree/main/src/content/ai/create-with-ai.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/ai/create-with-ai.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ai/create-with-ai/&page-source=https://github.com/flutter/website/tree/main/src/content/ai/create-with-ai.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   