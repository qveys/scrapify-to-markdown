Set up Linux development
========================

1. [Platform integration](/platform-integration) chevron\_right- [Linux](/platform-integration/linux) chevron\_right- [Set up Linux development](/platform-integration/linux/setup)

Learn how to set up your development environment to run, build, and deploy Flutter apps for the Linux desktop platform.

*info* Note

If you haven't set up Flutter already, visit and follow the [Get started with Flutter](/get-started) guide first.

If you've already installed Flutter, ensure that it's [up to date](/install/upgrade).

Set up tooling
--------------

[#](#set-up-tooling)

To run and debug desktop Flutter apps on Linux, download and install the prerequisite packages.

Using your preferred package manager or mechanism, install the latest versions of the following packages:

* `clang`* `cmake`* `ninja-build`* `pkg-config`* `libgtk-3-dev`* `libstdc++-12-dev`

On Debian-based distros with `apt-get`, such as Ubuntu, install these packages using the following commands:

```
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y clang cmake ninja-build pkg-config libgtk-3-dev libstdc++-12-dev
```

Validate your setup
-------------------

[#](#validate-setup)

1. ### Check for toolchain issues

   To check for any issues with your Linux development setup, run the `flutter doctor` command in your preferred terminal:

   ```
   flutter doctor -v
   ```

   If you see any errors or tasks to complete under the **Linux toolchain** section, complete and resolve them, then run `flutter doctor -v` again to verify any changes.- ### Check for Linux devices

     To ensure Flutter can find and connect to your Linux device correctly, run `flutter devices` in your preferred terminal:

     ```
     flutter devices
     ```

     If you set everything up correctly, there should be at least one entry with the platform marked as **linux**.- ### Troubleshoot setup issues

       If you need help resolving any setup issues, check out [Install and setup troubleshooting](/install/troubleshoot).

       If you still have issues or questions, reach out on one of the Flutter [community](https://flutter.dev/community) channels.

Start developing for Linux
--------------------------

[#](#start-developing)

Congratulations! Now that you've set up Linux desktop development for Flutter, you can continue your Flutter learning journey while testing on Linux or begin expanding integration with Linux.

![Dash helping you explore Flutter learning resources.](/assets/images/decorative/pointing-the-way.png)

Continue learning Flutter

* [Write your first app](/get-started/codelab)* [Learn the fundamentals](/get-started/fundamentals)* [Explore Flutter widgets](https://www.youtube.com/watch?v=b_sQ9bMltGU&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG)* [Check out samples](/reference/learning-resources)* [Learn about Dart](/resources/bootstrap-into-dart)

![An outline of Flutter desktop support.](/assets/images/decorative/flutter-on-desktop.svg)

Build for Linux

* [Build a Linux app](/platform-integration/linux/building)* [Release a Linux app](/deployment/linux)* [Write Linux-specific code](/platform-integration/platform-channels)* [Flutter plugins for Linux](https://pub.dev/packages?q=platform%3Alinux+is%3Aplugin)* [Design Ubuntu-themed apps](https://github.com/ubuntu-flutter-community/yaru_tutorial)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/linux/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/setup.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/linux/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/setup.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-25. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/setup.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/linux/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/setup.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   