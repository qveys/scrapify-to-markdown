Build Linux apps with Flutter
=============================

1. [Platform integration](/platform-integration) chevron\_right- [Linux](/platform-integration/linux) chevron\_right- [Linux development](/platform-integration/linux/building)

This page discusses considerations unique to building Linux apps with Flutter, including shell integration and preparation of apps for distribution.

Integrate with Linux
--------------------

[#](#integrate-with-linux)

The Linux programming interface, comprising library functions and system calls, is designed around the C language and ABI. Fortunately, Dart provides the `dart:ffi` package, which enables Dart programs to call into C libraries.

Foreign Function Interfaces (FFI) allow Flutter apps to perform the following with native libraries:

* allocate native memory with `malloc` or `calloc`* support pointers, structs, and callbacks* support Application Binary Interface (ABI) types like `long` and `size_t`

To learn more about calling C libraries from Flutter, consult [C interop using `dart:ffi`](https://dart.dev/guides/libraries/c-interop).

Many apps benefit from using a package that wraps the underlying library calls in a more convenient, idiomatic Dart API. [Canonical has built a series of packages](https://pub.dev/publishers/canonical.com/packages) with a focus on enabling Dart and Flutter on Linux, including support for desktop notifications, dbus, network management, and Bluetooth.

In general, many other [packages support creating Linux apps](https://pub.dev/packages?q=platform%3Alinux), including common packages such as [`url_launcher`](https://pub.dev/packages/url_launcher), [`shared_preferences`](https://pub.dev/packages/shared_preferences), [`file_selector`](https://pub.dev/packages/file_selector), and [`path_provider`](https://pub.dev/packages/path_provider).

Prepare Linux apps for distribution
-----------------------------------

[#](#prepare-linux-apps-for-distribution)

The executable binary can be found in your project under `build/linux/x64/<build mode>/bundle/`. Alongside your executable binary in the `bundle` directory, you can find two directories:

* `lib` contains the required `.so` library files* `data` contains the application's data assets, such as fonts or images

In addition to these files, your application also relies on various operating system libraries against which it's been compiled. To see the full list of libraries, use the `ldd` command on your application's directory.

For example, assume you have a Flutter desktop application called `linux_desktop_test`. To inspect the its system library dependencies, use the following commands:

```
flutter build linux --release
ldd build/linux/x64/release/bundle/linux_desktop_test
```

To wrap up this application for distribution, include everything in the `bundle` directory and verify the target Linux system has all required system libraries.

This might only require using the following command.

```
sudo apt-get install libgtk-3-0 libblkid1 liblzma5
```

To learn how to publish a Linux application to the [Snap Store](https://snapcraft.io/store), consult [Build and release a Linux application to the Snap Store](/deployment/linux).

Additional resources
--------------------

[#](#additional-resources)

To learn how to create Linux Debian (`.deb`) and RPM (`.rpm`) builds of your Flutter desktop app, consult the step-by-step [Linux packaging guide](https://medium.com/@fluttergems/packaging-and-distributing-flutter-desktop-apps-the-missing-guide-part-3-linux-24ef8d30a5b4).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/linux/building/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/building.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/linux/building/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/building.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/building.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/linux/building/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/linux/building.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   