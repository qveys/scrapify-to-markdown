Set up Android development
==========================

1. [Platform integration](/platform-integration) chevron\_right- [Android](/platform-integration/android) chevron\_right- [Set up Android development](/platform-integration/android/setup)

Learn how to set up your development environment to run, build, and deploy Flutter apps for Android devices.

*info* Note

If you haven't set up Flutter already, visit and follow the [Get started with Flutter](/get-started) guide first.

If you've already installed Flutter, ensure that it's [up to date](/install/upgrade).

Choose your development platform
--------------------------------

[#](#dev-platform)

The instructions on this page are configured to cover setting up Android development on a **Windows** device.

If you'd like to follow the instructions for a different OS, please select one of the following.

![Windows logo](/assets/images/docs/brand-svg/windows.svg)

Windows

 

![macOS logo](/assets/images/docs/brand-svg/macos.svg)

macOS

 

![Linux logo](/assets/images/docs/brand-svg/linux.svg)

Linux

 

![ChromeOS logo](/assets/images/docs/brand-svg/chromeos.svg)

ChromeOS

Set up Android tooling
----------------------

[#](#set-up-tooling)

With Android Studio, you can run Flutter apps on a physical Android device or an Android Emulator.

If you haven't done so already, install and set up the latest stable version of [Android Studio](https://developer.android.com/studio).

1. ### Install prerequisites libraries

   If you're developing on Linux, first install the [prerequisite collection of 32-bit libraries](https://developer.android.com/studio/install#64bit-libs) that Android Studio requires.- ### Install Android Studio

     If you haven't done so already, [install and set up](https://developer.android.com/studio/install) the latest stable version of [Android Studio](https://developer.android.com/studio).

     If you already have Android Studio installed, ensure that it's [up to date](https://developer.android.com/studio/intro/update).- ### Install Android SDK and tools

       1. Launch **Android Studio**.- Open the **SDK Manager** settings dialog.
            1. If the **Welcome to Android Studio** dialog is open, click the **More Actions** button that follows the **New Project** and **Open** buttons, then click **SDK Manager** from the dropdown menu.- If you have a project open, go to **Tools** > **SDK Manager**.- If the **SDK Platforms** tab is not open, switch to it.- Verify that the first entry with an **API Level** of **36** has been selected.

                If the **Status** column displays **Update available** or **Not installed**:
                1. Select the checkbox for that entry or row.- Click **Apply**.- When the **Confirm Change** dialog displays, click **OK**.

                       The **SDK Component Installer** dialog displays with a progress indicator.- When the installation finishes, click **Finish**.- Switch to the **SDK Tools** tab.- Verify that the following SDK Tools have been selected:
                    * **Android SDK Build-Tools*** **Android SDK Command-line Tools*** **Android Emulator*** **Android SDK Platform-Tools**- If the **Status** column for any of the preceding tools displays **Update available** or **Not installed**:
                      1. Select the checkbox for the necessary tools.- Click **Apply**.- When the **Confirm Change** dialog displays, click **OK**.

                             The **SDK Component Installer** dialog displays with a progress indicator.- When the installation finishes, click **Finish**.- ### Agree to the Android licenses

         Before you can use Flutter and after you install all prerequisites, agree to the licenses of the Android SDK platform.
         1. Open your preferred terminal.- Run the following command to review and sign the SDK licenses.

              ```
              flutter doctor --android-licenses
              ```

              - Read and accept any necessary licenses.

                If you haven't accepted each of the SDK licenses previously, you'll need to review and agree to them before developing for Android.

                Before agreeing to the terms of each license, read each with care.

                Once you've accepted all the necessary licenses successfully, you should see output similar to the following:

                ```
                All SDK package licenses accepted.
                ```

Set up an Android device
------------------------

[#](#set-up-devices)

You can debug Flutter apps on physical Android devices or by running them on an Android emulator.

* [Android emulator](#31-tab-panel)* [Physical device](#32-tab-panel)

To set up your development environment to run a Flutter app on an Android emulator, follow these steps:

1. ### Set up your development device

   Enable [VM acceleration](https://developer.android.com/studio/run/emulator-acceleration#accel-vm) on your development computer.- ### Set up a new emulator

     1. Start **Android Studio**.- Open the **Device Manager** settings dialog.
          1. If the **Welcome to Android Studio** dialog is open, click the **More Actions** button that follows the **New Project** and **Open** buttons, then select **Virtual Device Manager** from the dropdown menu.- If you have a project open, go to **Tools** > **Device Manager**.- Click the **Create Virtual Device** button that appears as a `+` icon.

            The **Virtual Device Configuration** dialog displays.- Select either **Phone** or **Tablet** under **Form Factor**.- Select a device definition. You can browse or search for the device.- Click **Next**.- If the option is provided, select either **x86 Images** or **ARM Images** depending on if your development computer is an x64 or Arm64 device.- Select one system image for the Android version you want to emulate.
                      1. If the desired image has a **Download** icon to the left of the system image name, click it.

                         The **SDK Component Installer** dialog displays with a progress indicator.- When the download completes, click **Finish**.- Click **Additional settings** in the top tab bar and scroll to **Emulated Performance**.- From the **Graphics acceleration** dropdown menu, select an option that mentions **Hardware**.

                          This enables [hardware acceleration](https://developer.android.com/studio/run/emulator-acceleration), improving render performance.- Verify your virtual device configuration. If it is correct, click **Finish**.

                            To learn more about virtual devices, check out [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds).- ### Try running the emulator

       In the **Device Manager** dialog, click the **Run** icon to the right of your desired virtual device.

       The emulator should start up and display the default canvas for your selected Android OS version and device.

To set up your development environment to run a Flutter app on a physical Android device, follow these steps:

1. ### Configure your device

   Enable **Developer options** and **USB debugging** on your device as described in [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options).- ### Enable wireless debugging

     To leverage wireless debugging, enable **Wireless debugging** on your device as described in [Connect to your device using Wi-Fi](https://developer.android.com/studio/run/device#wireless).- ### Install platform prerequisites

       If you're developing on Windows, first install the necessary USB driver for your particular device as described in [Install OEM USB drivers](https://developer.android.com/studio/run/oem-usb).- ### Connect your device

         Plug your device into your computer. If your device prompts you, authorize your computer to access your Android device.- ### Verify the device connection

           To verify that Flutter recognizes your connected Android device, run `flutter devices` in your preferred terminal:

           ```
           flutter devices
           ```

           Your device should be found and show up as a connected device.

Validate your setup
-------------------

[#](#validate-setup)

1. ### Check for toolchain issues

   To check for any issues with your Android development setup, run the `flutter doctor` command in your preferred terminal:

   ```
   flutter doctor
   ```

   If you see any errors or tasks to complete under the **Android toolchain** or **Android Studio** sections,

   Complete any mentioned tasks and then run `flutter doctor` again to verify any changes.- ### Check for Android devices

     To ensure you set up your emulator and/or physical Android device correctly, run `flutter emulators` and `flutter devices` in your preferred terminal:

     ```
     flutter emulators && flutter devices
     ```

     Depending on if you set up an emulator or a device, at least one should output an entry with the platform marked as **android**.- ### Troubleshoot setup issues

       If you need help resolving any setup issues, check out [Install and setup troubleshooting](/install/troubleshoot#android-setup).

       If you still have issues or questions, reach out on one of the Flutter [community](https://flutter.dev/community) channels.

Start developing for Android
----------------------------

[#](#start-developing)

Congratulations! Now that you've set up Android development for Flutter, you can continue your Flutter learning journey while testing on Android or begin improving integration with Android.

![Dash helping you explore Flutter learning resources.](/assets/images/decorative/pointing-the-way.png)

Continue learning Flutter

* [Write your first app](/get-started/codelab)* [Learn the fundamentals](/get-started/fundamentals)* [Explore Flutter widgets](https://www.youtube.com/watch?v=b_sQ9bMltGU&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG)* [Check out samples](/reference/learning-resources)* [Learn about Dart](/resources/bootstrap-into-dart)

![A representation of Flutter on multiple devices.](/assets/images/decorative/flutter-on-phone.svg)

Build for Android

* [Build and deploy to Android](/deployment/android)* [Bind to native Android code](/platform-integration/android/c-interop)* [Add a splash screen](/platform-integration/android/splash-screen)* [Embed native Android views](/platform-integration/android/platform-views)* [Support predictive back](/platform-integration/android/predictive-back)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/setup.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/setup.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-25. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/android/setup.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/setup.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   