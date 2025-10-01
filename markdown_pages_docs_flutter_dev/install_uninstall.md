Uninstall Flutter
=================

1. [Install](/install) chevron\_right- [Uninstall](/install/uninstall)

To remove the Flutter SDK from your development machine, delete the directories that store Flutter and its configuration files.

Choose your development platform
--------------------------------

[#](#dev-platform)

The instructions on this page are configured to cover uninstall Flutter on a **Windows** device.

If you'd like to follow the instructions for a different OS, please select one of the following.

![Windows logo](/assets/images/docs/brand-svg/windows.svg)

Windows

 

![macOS logo](/assets/images/docs/brand-svg/macos.svg)

macOS

 

![Linux logo](/assets/images/docs/brand-svg/linux.svg)

Linux

 

![ChromeOS logo](/assets/images/docs/brand-svg/chromeos.svg)

ChromeOS

Uninstall the Flutter SDK
-------------------------

[#](#uninstall)

1. ### Determine your Flutter SDK installation location

   Copy the absolute path to the directory that you downloaded and extracted the Flutter SDK into.- ### Remove the installation directory

     To uninstall the Flutter SDK, delete the `flutter` directory you installed Flutter to.

     For example, if you downloaded Flutter into a `develop\flutter` folder inside your user directory, run the following command to delete the SDK:

     ```
     Remove-Item -Recurse -Force -Path (Join-Path $env:USERPROFILE "develop\flutter")
     ```

1. ### Determine your Flutter SDK installation location

   Copy the absolute path to the directory that you downloaded and extracted the Flutter SDK into.- ### Remove the installation directory

     To uninstall the Flutter SDK, delete the `flutter` directory you installed Flutter to.

     For example, if you downloaded Flutter into a `develop/flutter` folder inside your user directory, run the following command to delete the SDK:

     ```
     rm -rf ~/develop/flutter
     ```

Clean up installation and configuration files
---------------------------------------------

[#](#cleanup)

Flutter and Dart add to additional directories in your home directory. These contain configuration files and package downloads. The following cleanup is optional.

1. ### Remove Flutter configuration directories

   If you don't want to preserve your Flutter tooling configuration, remove the following directories from your device.

   * `%APPDATA%\.flutter-devtools`

   To remove these directories, run the following command:

   ```
   Remove-Item -Recurse -Force -Path (Join-Path $env:APPDATA ".flutter-devtools")
   ```

   * `~/.flutter`* `~/.flutter-devtools`* `~/.flutter_settings`

   To remove these directories, run the following command:

   ```
   rm -rf  ~/.flutter ~/.flutter-devtools ~/.flutter_settings
   ```

   - ### Remove Dart configuration directories

     If you don't want to preserve your Dart tooling configuration, remove the following directories from your device.

     * `%APPDATA%\.dart`* `%APPDATA%\.dart-tool`* `%LOCALAPPDATA%\.dartServer`

     To remove these directories, run the following command:

     ```
     Remove-Item -Recurse -Force -Path (Join-Path $env:APPDATA ".dart"), (Join-Path $env:APPDATA ".dart-tool"), (Join-Path $env:LOCALAPPDATA ".dartServer")
     ```

     * `~/.dart`* `~/.dart-tool`* `~/.dartServer`

     To remove these directories, run the following command:

     ```
     rm -rf  ~/.dart ~/.dart-tool ~/.dartServer
     ```

     - ### Remove pub package directories

       If you don't want to preserve your locally installed pub packages, remove the [pub system cache](https://dart.dev/tools/pub/glossary#system-cache) directory from your device.

       If you didn't change the location of the pub system cache, run the following command to delete the `%LOCALAPPDATA%\Pub\Cache` directory:

       ```
       Remove-Item -Recurse -Force -Path (Join-Path $env:LOCALAPPDATA "Pub\Cache")
       ```

       If you didn't change the location of the pub system cache, run the following command to delete the `~/.pub-cache` directory:

       ```
       rm -rf ~/.pub-cache
       ```

Reinstall Flutter
-----------------

[#](#reinstall)

You can [reinstall Flutter](/install) or [just Dart](https://dart.dev/get-dart) at any time. If you removed any configuration directories, reinstalling Flutter restores them to default settings.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/uninstall/&page-source=https://github.com/flutter/website/tree/main/src/content/install/uninstall.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/uninstall/&page-source=https://github.com/flutter/website/tree/main/src/content/install/uninstall.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/install/uninstall.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/uninstall/&page-source=https://github.com/flutter/website/tree/main/src/content/install/uninstall.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   