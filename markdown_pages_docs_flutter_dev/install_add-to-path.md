Add Flutter to your PATH
========================

1. [Install](/install) chevron\_right- [Add to PATH](/install/add-to-path)

Learn how to add Flutter to your `PATH` environment variable after downloading the SDK. Adding Flutter to your `PATH` allows you to use the `flutter` and `dart` command-line tools in terminals and IDEs.

*lightbulb* Tip

If you haven't downloaded Flutter yet, follow [Set up and test drive Flutter](/get-started/quick) instead.

[Windows

Add Flutter to your path on Windows.](#windows)[macOS

Add Flutter to your path on macOS.](#macos)[Linux

Add Flutter to your path on Linux.](#linux)[ChromeOS

Add Flutter to your path on ChromeOS.](#chromeos)

Windows
-------

[#](#windows)

To run `flutter` and `dart` commands in a terminal on Windows, add the Flutter SDK's `bin` directory to the `Path` environment variable.

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

macOS
-----

[#](#macos)

To run `flutter` and `dart` commands in a terminal on macOS, add the Flutter SDK's `bin` directory to the `PATH` environment variable.

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

Linux
-----

[#](#linux)

To run `flutter` and `dart` commands in a terminal on Linux, add the Flutter SDK's `bin` directory to the `PATH` environment variable.

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

ChromeOS
--------

[#](#chromeos)

To run `flutter` and `dart` commands in a terminal on chromeOS, add the Flutter SDK's `bin` directory to the `PATH` environment variable.

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

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/add-to-path/&page-source=https://github.com/flutter/website/tree/main/src/content/install/add-to-path.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/add-to-path/&page-source=https://github.com/flutter/website/tree/main/src/content/install/add-to-path.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/install/add-to-path.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/add-to-path/&page-source=https://github.com/flutter/website/tree/main/src/content/install/add-to-path.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   