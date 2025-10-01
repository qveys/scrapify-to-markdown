Set up Windows development
==========================

1. [Platform integration](/platform-integration) chevron\_right- [Windows](/platform-integration/windows) chevron\_right- [Set up Windows development](/platform-integration/windows/setup)

Learn how to set up your development environment to run, build, and deploy Flutter apps for the Windows desktop platform.

*info* Note

If you haven't set up Flutter already, visit and follow the [Get started with Flutter](/get-started) guide first.

If you've already installed Flutter, ensure that it's [up to date](/install/upgrade).

Set up tooling
--------------

[#](#set-up-tooling)

With [Visual Studio](https://visualstudio.microsoft.com/), you can run Flutter apps on Windows as well as compile and debug native C and C++ code.

Note that **Visual Studio** is an IDE separate from **Visual Studio *Code*** and only supported on Windows.

1. ### Install Visual Studio

   If you haven't done so already, follow the Microsoft guide to [install and set up Visual Studio](https://visualstudio.microsoft.com/).

   If you've already installed Visual Studio, [update it to the latest version](https://learn.microsoft.com/en-us/visualstudio/install/update-visual-studio).- ### Set up Visual Studio workloads

     When the Visual Studio installer prompts you to choose workloads, select and install the **Desktop development with C++** workload.

     If you already installed Visual Studio, follow the Microsoft guide to [Modify Visual Studio workloads](https://learn.microsoft.com/en-us/visualstudio/install/modify-visual-studio).

     *lightbulb* Tip

     If installing with the command line, the ID of the **Desktop development with C++** workload is `Microsoft.VisualStudio.Workload.NativeDesktop`.

Validate your setup
-------------------

[#](#validate-setup)

1. ### Check for toolchain issues

   To check for any issues with your Windows development setup, run the `flutter doctor` command in your preferred terminal:

   ```
   flutter doctor -v
   ```

   If you see any errors or tasks to complete under the **Windows version** and **Visual Studio - develop Windows apps** sections, complete and resolve them, then run `flutter doctor -v` again to verify any changes.- ### Check for Windows devices

     To ensure Flutter can find and connect to your Windows device correctly, run `flutter devices` in your preferred terminal:

     ```
     flutter devices
     ```

     If you've set everything up correctly, there should be at least one entry with the platform marked as **windows**.- ### Troubleshoot setup issues

       If you need help resolving any setup issues, check out [installation and setup troubleshooting](/install/troubleshoot). Depending on your issue, also check out Microsoft's guide on [Visual Studio troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/developer/visualstudio/installation/troubleshoot-installation-issues).

       If you still have issues or questions, reach out on one of the Flutter [community](https://flutter.dev/community) channels.

Start developing for Windows
----------------------------

[#](#start-developing)

Congratulations! Now that you've set up Windows desktop development for Flutter, you can continue your Flutter learning journey while testing on Windows or begin expanding integration with Windows.

![Dash helping you explore Flutter learning resources.](/assets/images/decorative/pointing-the-way.png)

Continue learning Flutter

* [Write your first app](/get-started/codelab)* [Learn the fundamentals](/get-started/fundamentals)* [Explore Flutter widgets](https://www.youtube.com/watch?v=b_sQ9bMltGU&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG)* [Check out samples](/reference/learning-resources)* [Learn about Dart](/resources/bootstrap-into-dart)

![An outline of Flutter desktop support.](/assets/images/decorative/flutter-on-desktop.svg)

Build for Windows

* [Build a Windows app](/platform-integration/windows/building)* [Deploy to windows](/deployment/windows)* [Write Windows-specific code](/platform-integration/platform-channels)* [Customize the app window](/platform-integration/windows/building#customizing-the-windows-host-application)* [Access Win32 APIs with Dart](https://pub.dev/packages/win32)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/windows/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/windows/setup.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/windows/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/windows/setup.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-25. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/windows/setup.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/windows/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/windows/setup.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   