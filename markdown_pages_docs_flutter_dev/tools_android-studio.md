Android Studio and IntelliJ
===========================

1. [Tools](/tools) chevron\_right- [Android Studio and IntelliJ](/tools/android-studio)

* Android Studio and IntelliJ* [Visual Studio Code](/tools/vs-code)

Installation and setup
----------------------

[#](#setup)

Android Studio and IntelliJ IDEA offer a complete, IDE experience once you install the Flutter plugin.

To install the latest version of the following IDEs, follow their instructions:

* [Android Studio](https://developer.android.com/studio/install)* [IntelliJ IDEA Community](https://www.jetbrains.com/idea/download/)* [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download/)

### Install the Flutter plugin

[#](#install-plugin)

* [Windows](#131-tab-panel)* [macOS](#132-tab-panel)* [Linux](#133-tab-panel)

1. Go to **File** > **Settings**.

   You can also press `Ctrl` + `Alt` + `S`.

   The **Preferences** dialog opens.- From the list at the left, select **Plugins**.- From the top of this panel, select **Marketplace**.- Type `flutter` in the plugin search field.- Select the **Flutter** plugin.- Click **Install**.- Click **Yes** when prompted to install the plugin.- Click **Restart** when prompted.

1. Start Android Studio or IntelliJ.- From the macOS menu bar, go to **Android Studio** (or **IntelliJ**) > **Settings...**.

     You can also press `Cmd` + `,`.

     The **Preferences** dialog opens.- From the list at the left, select **Plugins**.- From the top of this panel, select **Marketplace**.- Type `flutter` in the plugin search field.- Select the **Flutter** plugin.- Click **Install**.- Click **Yes** when prompted to install the plugin.- Click **Restart** when prompted.

1. Go to **File** > **Settings**.

   You can also press `Ctrl` + `Alt` + `S`.

   The **Preferences** dialog opens.- From the list at the left, select **Plugins**.- From the top of this panel, select **Marketplace**.- Type `flutter` in the plugin search field.- Select the **Flutter** plugin.- Click **Install**.- Click **Yes** when prompted to install the plugin.- Click **Restart** when prompted.

### Updating the plugins

[#](#updating)

Updates to the plugins are shipped on a regular basis. You should be prompted in the IDE when an update is available.

To check for updates manually:

1. Open preferences (**Android Studio > Check for Updates** on macOS, **Help > Check for Updates** on Linux).- If `dart` or `flutter` are listed, update them.

Creating projects
-----------------

[#](#creating-projects)

You can create a new project in one of several ways.

### Creating a new project

[#](#creating-a-new-project)

Creating a new Flutter project from the Flutter starter app template differs between Android Studio and IntelliJ.

**In Android Studio:**

1. In the IDE, click **New Flutter Project** from the **Welcome** window or **File > New > New Flutter Project** from the main IDE window.- Specify the **Flutter SDK path** and click **Next**.- Enter your desired **Project name**, **Description**, and **Project location**.- If you might publish this app, [set the company domain](#set-the-company-domain).- Click **Finish**.

**In IntelliJ:**

1. In the IDE, click **New Project** from the **Welcome** window or **File > New > Project** from the main IDE window.- Select **Flutter** from the **Generators** list in the left panel- Specify the **Flutter SDK path** and click **Next**.- Enter your desired **Project name**, **Description**, and **Project location**.- If you might publish this app, [set the company domain](#set-the-company-domain).- Click **Finish**.

#### Set the company domain

[#](#set-the-company-domain)

When creating a new app, some Flutter IDE plugins ask for an organization name in reverse domain order, something like `com.example`. Along with the name of the app, this is used as the package name for Android, and the Bundle ID for iOS when the app is released. If you think you might ever release this app, it is better to specify these now. They cannot be changed once the app is released. Your organization name should be unique.

### Opening a project from existing source code

[#](#opening-a-project-from-existing-source-code)

To open an existing Flutter project:

1. In the IDE, click **Open** from the **Welcome** window, or **File > Open** from the main IDE window.- Browse to the directory holding your existing Flutter source code files.- Click **Open**.

       *error* Important

       Do *not* use the **New > Project from existing sources** option for Flutter projects.

Editing code and viewing issues
-------------------------------

[#](#editing-code-and-viewing-issues)

The Flutter plugin performs code analysis that enables the following:

* Syntax highlighting.* Code completions based on rich type analysis.* Navigating to type declarations (**Navigate > Declaration**), and finding type usages (**Edit > Find > Find Usages**).* Viewing all current source code problems (**View > Tool Windows > Dart Analysis**). Any analysis issues are shown in the Dart Analysis pane:  
         ![Dart Analysis pane](/assets/images/docs/tools/android-studio/dart-analysis.png)

Running and debugging
---------------------

[#](#running-and-debugging)

*info* Note

You can debug your app in a few ways.

* Using [DevTools](/tools/devtools), a suite of debugging and profiling tools that run in a browser *and include the Flutter inspector*.* Using Android Studio's (or IntelliJ's) built-in debugging features, such as the ability to set breakpoints.* Using the Flutter inspector, directly available in Android Studio and IntelliJ.

The instructions below describe features available in Android Studio and IntelliJ. For information on launching DevTools, see [Running DevTools from Android Studio](/tools/devtools/android-studio) in the [DevTools](/tools/devtools) docs.

Running and debugging are controlled from the main toolbar:

![Main IntelliJ toolbar](/assets/images/docs/tools/android-studio/main-toolbar.png)

### Selecting a target

[#](#selecting-a-target)

When a Flutter project is open in the IDE, you should see a set of Flutter-specific buttons on the right-hand side of the toolbar.

*info* Note

If the Run and Debug buttons are disabled, and no targets are listed, Flutter has not been able to discover any connected iOS or Android devices or simulators. You need to connect a device, or start a simulator, to proceed.

1. Locate the **Flutter Target Selector** drop-down button. This shows a list of available targets.- Select the target you want your app to be started on. When you connect devices, or start simulators, additional entries appear.

### Run app without breakpoints

[#](#run-app-without-breakpoints)

1. Click the **Play icon** in the toolbar, or invoke **Run > Run**. The bottom **Run** pane shows logs output.

### Run app with breakpoints

[#](#run-app-with-breakpoints)

1. If desired, set breakpoints in your source code.- Click the **Debug icon** in the toolbar, or invoke **Run > Debug**.
     * The bottom **Debugger** pane shows Stack Frames and Variables.* The bottom **Console** pane shows detailed logs output.* Debugging is based on a default launch configuration. To customize this, click the drop-down button to the right of the device selector, and select **Edit configuration**.

Fast edit and refresh development cycle
---------------------------------------

[#](#fast-edit-and-refresh-development-cycle)

Flutter offers a best-in-class developer cycle enabling you to see the effect of your changes almost instantly with the *Stateful Hot Reload* feature. To learn more, check out [Hot reload](/tools/hot-reload).

### Show performance data

[#](#show-performance-data)

*info* Note

To examine performance issues in Flutter, see the [Timeline view](/tools/devtools/performance).

To view the performance data, including the widget rebuild information, start the app in **Debug** mode, and then open the Performance tool window using **View > Tool Windows > Flutter Performance**.

![Flutter performance window](/assets/images/docs/tools/android-studio/widget-rebuild-info.png)

To see the stats about which widgets are being rebuilt, and how often, click **Show widget rebuild information** in the **Performance** pane. The exact count of the rebuilds for this frame displays in the second column from the right. For a high number of rebuilds, a yellow spinning circle displays. The column to the far right shows how many times a widget was rebuilt since entering the current screen. For widgets that aren't rebuilt, a solid grey circle displays. Otherwise, a grey spinning circle displays.

The app shown in this screenshot has been designed to deliver poor performance, and the rebuild profiler gives you a clue about what is happening in the frame that might cause poor performance. The widget rebuild profiler is not a diagnostic tool, by itself, about poor performance.

The purpose of this feature is to make you aware when widgets are rebuilding—you might not realize that this is happening when just looking at the code. If widgets are rebuilding that you didn't expect, it's probably a sign that you should refactor your code by splitting up large build methods into multiple widgets.

This tool can help you debug at least four common performance issues:

1. The whole screen (or large pieces of it) are built by a single StatefulWidget, causing unnecessary UI building. Split up the UI into smaller widgets with smaller `build()` functions.- Offscreen widgets are being rebuilt. This can happen, for example, when a ListView is nested in a tall Column that extends offscreen. Or when the RepaintBoundary is not set for a list that extends offscreen, causing the whole list to be redrawn.- The `build()` function for an AnimatedBuilder draws a subtree that does not need to be animated, causing unnecessary rebuilds of static objects.- An Opacity widget is placed unnecessarily high in the widget tree. Or, an Opacity animation is created by directly manipulating the opacity property of the Opacity widget, causing the widget itself and its subtree to rebuild.

You can click on a line in the table to navigate to the line in the source where the widget is created. As the code runs, the spinning icons also display in the code pane to help you visualize which rebuilds are happening.

Note that numerous rebuilds doesn't necessarily indicate a problem. Typically you should only worry about excessive rebuilds if you have already run the app in profile mode and verified that the performance is not what you want.

And remember, *the widget rebuild information is only available in a debug build*. Test the app's performance on a real device in a profile build, but debug performance issues in a debug build.

Editing tips for Flutter code
-----------------------------

[#](#editing-tips-for-flutter-code)

If you have additional tips we should share, [let us know](https://github.com/flutter/website/issues/new)!

### Assists & quick fixes

[#](#assists-quick-fixes)

Assists are code changes related to a certain code identifier. A number of these are available when the cursor is placed on a Flutter widget identifier, as indicated by the yellow lightbulb icon. The assist can be invoked by clicking the lightbulb, or by using the keyboard shortcut (`Alt`+`Enter` on Linux and Windows, `Option`+`Return` on macOS), as illustrated here:

![IntelliJ editing assists](/assets/images/docs/tools/android-studio/assists.webp)

Quick Fixes are similar, only they are shown with a piece of code has an error and they can assist in correcting it. They are indicated with a red lightbulb.

#### Wrap with new widget assist

[#](#wrap-with-new-widget-assist)

This can be used when you have a widget that you want to wrap in a surrounding widget, for example if you want to wrap a widget in a `Row` or `Column`.

#### Wrap widget list with new widget assist

[#](#wrap-widget-list-with-new-widget-assist)

Similar to the assist above, but for wrapping an existing list of widgets rather than an individual widget.

#### Convert child to children assist

[#](#convert-child-to-children-assist)

Changes a child argument to a children argument, and wraps the argument value in a list.

### Live templates

[#](#live-templates)

Live templates can be used to speed up entering typical code structures. They are invoked by typing their prefix, and then selecting it in the code completion window:

![IntelliJ live templates](/assets/images/docs/tools/android-studio/templates.webp)

The Flutter plugin includes the following templates:

* Prefix `stless`: Create a new subclass of `StatelessWidget`.* Prefix `stful`: Create a new subclass of `StatefulWidget` and its associated State subclass.* Prefix `stanim`: Create a new subclass of `StatefulWidget` and its associated State subclass, including a field initialized with an `AnimationController`.

You can also define custom templates in **Settings > Editor > Live Templates**.

### Keyboard shortcuts

[#](#keyboard-shortcuts)

**Hot reload**

On Linux (keymap *Default for XWin*) and Windows the keyboard shortcuts are `Control`+`Alt`+`;` and `Control`+`Backslash`.

On macOS (keymap *Mac OS X 10.5+ copy*) the keyboard shortcuts are `Command`+`Option` and `Command`+`Backslash`.

Keyboard mappings can be changed in the IDE Preferences/Settings: Select *Keymap*, then enter *flutter* into the search box in the upper right corner. Right click the binding you want to change and *Add Keyboard Shortcut*.

![IntelliJ settings keymap](/assets/images/docs/tools/android-studio/keymap-settings-flutter-plugin.png)

### Hot reload vs. hot restart

[#](#hot-reload-vs-hot-restart)

Hot reload works by injecting updated source code files into the running Dart VM (Virtual Machine). This includes not only adding new classes, but also adding methods and fields to existing classes, and changing existing functions. A few types of code changes cannot be hot reloaded though:

* Global variable initializers* Static field initializers* The `main()` method of the app

For these changes you can fully restart your application, without having to end your debugging session. To perform a hot restart, don't click the Stop button, simply re-click the Run button (if in a run session) or Debug button (if in a debug session), or shift-click the 'hot reload' button.

Editing Android code in Android Studio with full IDE support
------------------------------------------------------------

[#](#android-ide)

Opening the root directory of a Flutter project doesn't expose all the Android files to the IDE. Flutter apps contain a subdirectory named `android`. If you open this subdirectory as its own separate project in Android Studio, the IDE will be able to fully support editing and refactoring all Android files (like Gradle scripts).

If you already have the entire project opened as a Flutter app in Android Studio, there are two equivalent ways to open the Android files on their own for editing in the IDE. Before trying this, make sure that you're on the latest version of Android Studio and the Flutter plugins.

* In the ["project view"](https://developer.android.com/studio/projects/#ProjectView), you should see a subdirectory immediately under the root of your flutter app named `android`. Right click on it, then select **Flutter > Open Android module in Android Studio**.* OR, you can open any of the files under the `android` subdirectory for editing. You should then see a "Flutter commands" banner at the top of the editor with a link labeled **Open for Editing in Android Studio**. Click that link.

For both options, Android Studio gives you the option to use separate windows or to replace the existing window with the new project when opening a second project. Either option is fine.

If you don't already have the Flutter project opened in Android studio, you can open the Android files as their own project from the start:

1. Click **Open an existing Android Studio Project** on the Welcome splash screen, or **File > Open** if Android Studio is already open.- Open the `android` subdirectory immediately under the flutter app root. For example if the project is called `flutter_app`, open `flutter_app/android`.

If you haven't run your Flutter app yet, you might see Android Studio report a build error when you open the `android` project. Run `flutter pub get` in the app's root directory and rebuild the project by selecting **Build > Make** to fix it.

Editing Android code in IntelliJ IDEA
-------------------------------------

[#](#edit-android-code)

To enable editing of Android code in IntelliJ IDEA, you need to configure the location of the Android SDK:

1. In **Preferences > Plugins**, enable **Android Support** if you haven't already.- Right-click the **android** folder in the Project view, and select **Open Module Settings**.- In the **Sources** tab, locate the **Language level** field, and select level 8 or later.- In the **Dependencies** tab, locate the **Module SDK** field, and select an Android SDK. If no SDK is listed, click **New** and specify the location of the Android SDK. Make sure to select an Android SDK matching the one used by Flutter (as reported by `flutter doctor`).- Click **OK**.

Flutter Property Editor
-----------------------

[#](#property-editor)

The Flutter Property Editor is a powerful tool provided by the [Flutter plugin](https://plugins.jetbrains.com/plugin/9212-flutter) that lets you view and modify widget properties directly from its visual interface.

### How to open the Flutter Property Editor in Android Studio and IntelliJ

[#](#how-to-open-the-flutter-property-editor-in-android-studio-and-intellij)

1. Click on the Flutter Property Editor **icon** ![Flutter Property Editor Android Studio/IntelliJ icon](/assets/images/docs/tools/devtools/property-editor-icon-android-studio.png) in the Android Studio or IntelliJ sidebar.- The Flutter Property Editor will load in the side panel.- Please refer to the Flutter Property Editor [documentation](/tools/property-editor) for a detailed usage guide.

![Flutter Property Editor side panel in Android Studio/IntelliJ](/assets/images/docs/tools/devtools/property-editor-android-studio.png)

Troubleshooting
---------------

[#](#troubleshooting)

### Known issues and feedback

[#](#known-issues-and-feedback)

Important known issues that might impact your experience are documented in the [Flutter plugin README](https://github.com/flutter/flutter-intellij/blob/master/README.md) file.

All known bugs are tracked in the issue trackers:

* Flutter plugin: [GitHub issue tracker](https://github.com/flutter/flutter-intellij/issues)* Dart plugin: [JetBrains YouTrack](https://youtrack.jetbrains.com/issues?q=%23dart%20%23Unresolved)

We welcome feedback, both on bugs/issues and feature requests. Prior to filing new issues:

* Do a quick search in the issue trackers to see if the issue is already tracked.* Make sure you have [updated](#updating) to the most recent version of the plugin.

When filing new issues, include the output of [`flutter doctor`](/resources/bug-reports#provide-some-flutter-diagnostics).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/android-studio/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/android-studio.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/android-studio/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/android-studio.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-15. [View source](https://github.com/flutter/website/tree/main/src/content/tools/android-studio.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/android-studio/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/android-studio.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   