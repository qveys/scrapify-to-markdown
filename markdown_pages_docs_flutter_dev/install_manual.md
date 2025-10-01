Install Flutter manually
========================

1. [Install](/install) chevron\_right- [Manually](/install/manual)

Learn how to install and manually set up your Flutter development environment.

*lightbulb* Tip

If you've never set up or developed an app with Flutter before, follow [Get started with Flutter](/get-started) instead.

If you're just looking to quickly install Flutter, consider [installing Flutter with VS Code](/install/with-vs-code) for a streamlined setup experience.

Choose your development platform
--------------------------------

[#](#dev-platform)

The instructions on this page are configured to cover installing Flutter on a **Windows** device.

If you'd like to follow the instructions for a different OS, please select one of the following.

![Windows logo](/assets/images/docs/brand-svg/windows.svg)

Windows

 

![macOS logo](/assets/images/docs/brand-svg/macos.svg)

macOS

 

![Linux logo](/assets/images/docs/brand-svg/linux.svg)

Linux

 

![ChromeOS logo](/assets/images/docs/brand-svg/chromeos.svg)

ChromeOS

Download prerequisite software
------------------------------

[#](#download-prerequisites)

Before installing the Flutter SDK, first complete the following setup.

1. ### Install Git for Windows

   Download and install the latest version of [Git for Windows](https://git-scm.com/downloads/win).

   For help installing or troubleshooting Git, reference the [Git documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).- ### Set up an editor or IDE

     For the best experience developing Flutter apps, consider installing and setting up an [editor or IDE with Flutter support](/tools/editors).

1. ### Install the Xcode command-line tools

   Download the Xcode command-line tools to get access to the command-line tools that Flutter relies on, including Git.

   To download the tools, run the following command in your preferred terminal:

   ```
   xcode-select --install
   ```

   If you haven't installed the tools already, a dialog should open that confirms you'd like to install them. Click **Install**, then once the installation is complete, click **Done**.- ### Set up an editor or IDE

     For the best experience developing Flutter apps, consider installing and setting up an [editor or IDE with Flutter support](/tools/editors).

1. ### Download and install prerequisite packages

   Using your preferred package manager or mechanism, install the latest versions of the following packages:
   * `curl`* `git`* `unzip`* `xz-utils`* `zip`* `libglu1-mesa`

   On Debian-based distros with `apt-get`, such as Ubuntu, install these packages using the following commands:

   ```
   sudo apt-get update -y && sudo apt-get upgrade -y
   sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa
   ```

   - ### Set up an editor or IDE

     For the best experience developing Flutter apps, consider installing and setting up an [editor or IDE with Flutter support](/tools/editors).

1. ### Set up Linux support

   If you haven't set up Linux support on your Chromebook before, [Turn on Linux support](https://support.google.com/chromebook/answer/9145439).

   If you've already turned on Linux support, ensure it's up to date following the [Fix problems with Linux](https://support.google.com/chromebook/answer/9145439?hl=en#:~:text=Fix%20problems%20with%20Linux) instructions.- ### Download and install prerequisite packages

     Using `apt-get` or your preferred installation mechanism, install the latest versions of the following packages:
     * `curl`* `git`* `unzip`* `xz-utils`* `zip`* `libglu1-mesa`

     If you want to use `apt-get`, install these packages using the following commands:

     ```
     sudo apt-get update -y && sudo apt-get upgrade -y
     sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa
     ```

     - ### Set up an editor or IDE

       For the best experience developing Flutter apps, consider installing and setting up an [editor or IDE with Flutter support](/tools/editors).

Install and set up Flutter
--------------------------

[#](#install-flutter)

To install the Flutter SDK, download the latest bundle from the SDK archive, then extract the SDK to where you want it stored.

1. ### Download the Flutter SDK bundle

   Download the following installation bundle to get the latest stable release of the Flutter SDK.

   [(loading...)](#)- ### Create a folder to store the SDK

     Create or find a folder to store the extracted SDK in. Consider creating and using a directory at `%USERPROFILE%\develop` (`C:\Users\{username}\develop`).

     *info* Note

     Select a location that doesn't have special characters or spaces in its path and doesn't require elevated privileges.

     - ### Extract the SDK

       Extract the SDK bundle you downloaded into the directory you want to store the Flutter SDK in.
       1. Copy the following command.- Replace `<sdk_zip_path>` with the path to the bundle you downloaded.- Replace `<destination_directory_path>` with the path to the folder you want the extracted SDK to be in.- Run the edited command in your preferred terminal.

       ```
       Expand-Archive –Path <sdk_zip_path> -Destination <destination_directory_path>
       ```

       For example, if you downloaded the bundle for Flutter 3.29.3 into the `%USERPROFILE%\Downloads` directory and want to store the extracted SDK in the `%USERPROFILE%\develop` directory:

       ```
       Expand-Archive `
         -Path $env:USERPROFILE\Downloads\flutter_windows_3.29.3-stable.zip `
         -Destination $env:USERPROFILE\develop\
       ```

1. ### Download the Flutter SDK bundle

   Depending on your macOS device's cpu architecture, download one of the following installation bundles to get the latest stable release of the Flutter SDK.

   |  |  |  |  |
   | --- | --- | --- | --- |
   | Apple Silicon (ARM64) Intel (x64)|  |  | | --- | --- | | [(loading...)](#) [(loading...)](#) | | | |

   - ### Create a folder to store the SDK

     Create or find a folder to store the extracted SDK in. Consider creating and using a directory at `~/develop/`.- ### Extract the SDK

       Extract the SDK bundle you downloaded into the directory you want to store the Flutter SDK in.
       1. Copy the following command.- Replace `<sdk_zip_path>` with the path to the bundle you downloaded.- Replace `<destination_directory_path>` with the path to the folder you want the extracted SDK to be in.- Run the edited command in your preferred terminal.

       ```
       unzip <sdk_zip_path> -d <destination_directory_path>
       ```

       For example, if you downloaded the bundle for Flutter 3.29.3 into the `~/Downloads` directory and want to store the extracted SDK in the `~/develop` directory:

       ```
       unzip ~/Downloads/flutter_macos_3.29.3-stable.zip -d ~/develop/
       ```

1. ### Download the Flutter SDK bundle

   Download the following installation bundle to get the latest stable release of the Flutter SDK.

   [(loading...)](#)- ### Create a folder to store the SDK

     Create or find a folder to store the extracted SDK in. Consider creating and using a directory at `~/develop/`.- ### Extract the SDK

       Extract the SDK bundle you downloaded into the directory you want to store the Flutter SDK in.
       1. Copy the following command.- Replace `<sdk_zip_path>` with the path to the bundle you downloaded.- Replace `<destination_directory_path>` with the path to the folder you want the extracted SDK to be in.- Run the edited command in your preferred terminal.

       ```
       tar -xf <sdk_zip_path> -C <destination_directory_path>
       ```

       For example, if you downloaded the bundle for Flutter 3.29.3 into the `~/Downloads` directory and want to store the extracted SDK in the `~/develop` directory:

       ```
       tar -xf ~/Downloads/flutter_linux_3.29.3-stable.tar.xz -C ~/develop/
       ```

Add Flutter to your PATH
------------------------

[#](#add-to-path)

Now that you've downloaded the SDK, add the Flutter SDK's `bin` directory to your `PATH` environment variable. Adding Flutter to your `PATH` allows you to use the `flutter` and `dart` command-line tools in terminals and IDEs.

1. ### Determine your Flutter SDK installation location

   Copy the absolute path to the directory that you downloaded and extracted the Flutter SDK into.- ### Navigate to the environment variables settings

     1. Press `Windows` + `Pause`.

        If your keyboard lacks a `Pause` key, try `Windows` + `Fn` + `B`.

        The **System > About** dialog opens.- Click **Advanced System Settings** > **Advanced** > **Environment Variables...**.

          The **Environment Variables** dialog opens.- ### Add the Flutter SDK bin to your path

       1. In the **User variables for (username)** section of the **Environment Variables** dialog, look for the **Path** entry.- If the **Path** entry exists, double-click it.

            The **Edit Environment Variable** dialog should open.
            1. Double-click inside an empty row.- Type the path to the `bin` directory of your Flutter installation.

                 For example, if you downloaded Flutter into a `develop\flutter` folder inside your user directory, you'd type the following:

                 ```
                 %USERPROFILE%\develop\flutter\bin
                 ```

                 - Click the Flutter entry you added to select it.- Click **Move Up** until the Flutter entry sits at the top of the list.- To confirm your changes, click **OK** three times.- If the entry doesn't exist, click **New...**.

              The **Edit Environment Variable** dialog should open.
              1. In the **Variable Name** box, type `Path`.- In the **Variable Value** box, type the path to the `bin` directory of your Flutter installation.

                   For example, if you downloaded Flutter into a `develop\flutter` folder inside your user directory, you'd type the following:

                   ```
                   %USERPROFILE%\develop\flutter\bin
                   ```

                   - To confirm your changes, click **OK** three times.- ### Apply your changes

         To apply this change and get access to the `flutter` tool, close and reopen all open command prompts, sessions in your terminal apps, and IDEs.- ### Validate your setup

           To ensure you successfully added the SDK to your `PATH`, open command prompt or your preferred terminal app, then try running the `flutter` and `dart` tools.

           ```
           flutter --version
           dart --version
           ```

           If either command isn't found, check out [Flutter installation troubleshooting](/install/troubleshoot).

*info* Note

The following steps assume you're using the [default shell](https://support.apple.com/en-us/102360) on macOS, Zsh. Zsh uses the `.zshenv` file for configuring [environment variables](https://zsh.sourceforge.io/Intro/intro_3.html).

If you use another shell besides Zsh, check out [this tutorial on setting your PATH](https://www.cyberciti.biz/faq/unix-linux-adding-path/).

1. ### Determine your Flutter SDK installation location

   Copy the absolute path to the directory that you downloaded and extracted the Flutter SDK into.- ### Open or create the Zsh environment variable file

     If it exists, open the Zsh environment variable file `~/.zshenv` in your preferred text editor. If it doesn't exist, create the `~/.zshenv` file.- ### Add the Flutter SDK bin to your path

       At the end of your `~/.zshenv` file, use the built-in `export` command to update the `PATH` variable to include the `bin` directory of your Flutter installation.

       Replace `<path-to-sdk>` with the path to your Flutter SDK install.

       bash

       ```
       export PATH="<path-to-sdk>/bin:$PATH"
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd add the following to the file:

       bash

       ```
       export PATH="$HOME/development/flutter/bin:$PATH"
       ```

       - ### Save your changes

         Save, then close, the `~/.zshenv` file you edited.- ### Apply your changes

           To apply this change and get access to the `flutter` tool, close and reopen all open Zsh sessions in your terminal apps and IDEs.- ### Validate your setup

             To ensure you successfully added the SDK to your `PATH`, open a Zsh session in your preferred terminal, then try running the `flutter` and `dart` tools.

             ```
             flutter --version
             dart --version
             ```

             If either command isn't found, check out [Flutter installation troubleshooting](/install/troubleshoot).

1. ### Determine your Flutter SDK installation location

   Copy the absolute path to the directory that you downloaded and extracted the Flutter SDK into.- ### Determine your default shell

     If you don't know what shell you use, check which shell starts when you open a new console window.

     ```
     echo $SHELL
     ```

     - ### Add the Flutter SDK bin to your path

       To add the `bin` directory of your Flutter installation to your `PATH`:
       1. Expand the instructions for your default shell.- Copy the provided command.- Replace `<path-to-sdk>` with the path to your Flutter SDK install.- Run the edited command in your preferred terminal with that shell.

       ---

       Expand for `bash` instructions

       ```
       echo 'export PATH="<path-to-sdk>:$PATH"' >> ~/.bash_profile
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

       ```
       echo 'export PATH="$HOME/development/flutter/bin:$PATH"' >> ~/.bash_profile
       ```

       Expand for `zsh` instructions

       ```
       echo 'export PATH="<path-to-sdk>/bin:$PATH"' >> ~/.zshenv
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

       ```
       echo 'export PATH="$HOME/development/flutter/bin:$PATH"' >> ~/.zshenv
       ```

       Expand for `fish` instructions

       ```
       fish_add_path -g -p <path-to-sdk>/bin
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

       ```
       fish_add_path -g -p ~/development/flutter/bin
       ```

       Expand for `csh` instructions

       ```
       echo 'setenv PATH "<path-to-sdk>/bin:$PATH"' >> ~/.cshrc
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

       ```
       echo 'setenv PATH "$HOME/development/flutter/bin:$PATH"' >> ~/.cshrc
       ```

       Expand for `tcsh` instructions

       ```
       echo 'setenv PATH "<path-to-sdk>/bin:$PATH"' >> ~/.tcshrc
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

       ```
       echo 'setenv PATH "$HOME/development/flutter/bin:$PATH"' >> ~/.tcshrc
       ```

       Expand for `ksh` instructions

       ```
       echo 'export PATH="<path-to-sdk>/bin:$PATH"' >> ~/.profile
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

       ```
       echo 'export PATH="$HOME/development/flutter/bin:$PATH"' >> ~/.profile
       ```

       Expand for `sh` instructions

       ```
       echo 'export PATH="<path-to-sdk>/bin:$PATH"' >> ~/.profile
       ```

       For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

       ```
       echo 'export PATH="$HOME/development/flutter/bin:$PATH"' >> ~/.profile
       ```

       - ### Apply your changes

         To apply this change and get access to the `flutter` tool, close and reopen all open shell sessions in your terminal apps and IDEs.- ### Validate your setup

           To ensure you successfully added the SDK to your `PATH`, open your preferred terminal with your default shell, then try running the `flutter` and `dart` tools.

           ```
           flutter --version
           dart --version
           ```

           If either command isn't found, check out [Flutter installation troubleshooting](/install/troubleshoot).

*info* Note

The following steps assume you've already [turned on Linux support](https://support.google.com/chromebook/answer/9145439) and that you're using Bash or the default shell on ChromeOS.

If you're using a different shell besides the default or Bash, follow the [add to path instructions for Linux](/install/add-to-path#linux) instead.

1. ### Determine your Flutter SDK installation location

   Copy the absolute path to the directory that you downloaded and extracted the Flutter SDK into.- ### Add the Flutter SDK bin to your path

     To add the `bin` directory of your Flutter installation to your `PATH`:
     1. Copy the following command.- Replace `<path-to-sdk>` with the path to your Flutter SDK install.- Run the edited command in your preferred terminal.

     ```
     echo 'export PATH="<path-to-sdk>:$PATH"' >> ~/.bash_profile
     ```

     For example, if you downloaded Flutter into a `development/flutter` folder inside your user directory, you'd run the following:

     ```
     echo 'export PATH="$HOME/development/flutter/bin:$PATH"' >> ~/.bash_profile
     ```

     - ### Apply your changes

       To apply this change and get access to the `flutter` tool, close and reopen all open Zsh sessions in your terminal apps and IDEs.- ### Validate your setup

         To ensure you successfully added the SDK to your `PATH`, open a Zsh session in your preferred terminal, then try running the `flutter` and `dart` tools.

         ```
         flutter --version
         dart --version
         ```

         If either command isn't found, check out [Flutter installation troubleshooting](/install/troubleshoot).

Continue your Flutter journey
-----------------------------

[#](#next-steps)

Now that you've successfully installed Flutter, set up development for at least one target platform to continue your journey with Flutter.

*bolt* Recommended

If you don't yet have a preferred platform to target during development, the Flutter team recommends you first try out [developing on the web](/platform-integration/web/setup)!

![A representation of Flutter on multiple devices.](/assets/images/decorative/flutter-on-phone.svg)

Set up a target platform

* [Target the web](/platform-integration/web/setup)* [Target Android](/platform-integration/android/setup)* [Target iOS](/platform-integration/ios/setup)* [Target macOS](/platform-integration/macos/setup)* [Target Windows](/platform-integration/windows/setup)* [Target Linux](/platform-integration/linux/setup)

![Dash helping you explore Flutter learning resources.](/assets/images/decorative/pointing-the-way.png)

Learn Flutter development

* [Write your first app](/get-started/codelab)* [Learn the fundamentals](/get-started/fundamentals)* [Explore Flutter widgets](https://www.youtube.com/watch?v=b_sQ9bMltGU&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG)

![Keep up to date with Flutter](/assets/images/decorative/up-to-date.png)

Stay up to date with Flutter

* [Update Flutter](/install/upgrade)* [Find out what's new](/release/release-notes)* [Subscribe on YouTube](https://www.youtube.com/@flutterdev)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/manual/&page-source=https://github.com/flutter/website/tree/main/src/content/install/manual.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/manual/&page-source=https://github.com/flutter/website/tree/main/src/content/install/manual.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-25. [View source](https://github.com/flutter/website/tree/main/src/content/install/manual.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/manual/&page-source=https://github.com/flutter/website/tree/main/src/content/install/manual.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   