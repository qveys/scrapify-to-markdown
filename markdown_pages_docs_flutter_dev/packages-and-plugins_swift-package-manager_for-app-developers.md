Swift Package Manager for app developers
========================================

1. [Packages & plugins](/packages-and-plugins) chevron\_right- [Swift Package Manager for Flutter](/packages-and-plugins/swift-package-manager) chevron\_right- [Swift Package Manager for app developers](/packages-and-plugins/swift-package-manager/for-app-developers)

*warning* Warning

Flutter is migrating to [Swift Package Manager](https://www.swift.org/documentation/package-manager/) to manage iOS and macOS native dependencies. Flutter's support of Swift Package Manager is under development. If you find a bug in Flutter's Swift Package Manager support, [open an issue](https://github.com/flutter/flutter/issues/new?template=2_bug.yml). Swift Package Manager support is [off by default](#how-to-turn-on-swift-package-manager). Flutter continues to support CocoaPods.

Flutter's Swift Package Manager integration has several benefits:

1. **Provides access to the Swift package ecosystem**. Flutter plugins can use the growing ecosystem of [Swift packages](https://swiftpackageindex.com/).- **Simplifies Flutter installation**. Xcode includes Swift Package Manager. You don't need to install Ruby and CocoaPods if your project uses Swift Package Manager.

How to turn on Swift Package Manager
------------------------------------

[#](#how-to-turn-on-swift-package-manager)

Flutter's Swift Package Manager support is turned off by default. To turn it on:

1. Upgrade to the latest Flutter SDK:

   sh

   ```
   flutter upgrade
   ```

   - Turn on the Swift Package Manager feature:

     sh

     ```
     flutter config --enable-swift-package-manager
     ```

Using the Flutter CLI to run an app [migrates the project](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-add-swift-package-manager-integration) to add Swift Package Manager integration. This makes your project download the Swift packages that your Flutter plugins depend on. An app with Swift Package Manager integration requires Flutter version 3.24 or higher. To use an older Flutter version, you will need to [remove Swift Package Manager integration](/packages-and-plugins/swift-package-manager/for-app-developers#how-to-remove-swift-package-manager-integration) from the app.

Flutter falls back to CocoaPods for dependencies that do not support Swift Package Manager yet.

How to turn off Swift Package Manager
-------------------------------------

[#](#how-to-turn-off-swift-package-manager)

Plugin authors

Plugin authors need to turn on and off Flutter's Swift Package Manager support for testing. App developers do not need to disable Swift Package Manager support, unless they are running into issues.

If you find a bug in Flutter's Swift Package Manager support, [open an issue](https://github.com/flutter/flutter/issues/new?template=2_bug.yml).

Disabling Swift Package Manager causes Flutter to use CocoaPods for all dependencies. However, Swift Package Manager remains integrated with your project. To remove Swift Package Manager integration completely from your project, follow the [How to remove Swift Package Manager integration](/packages-and-plugins/swift-package-manager/for-app-developers#how-to-remove-swift-package-manager-integration) instructions.

### Turn off for a single project

[#](#turn-off-for-a-single-project)

In the project's `pubspec.yaml` file, under the `flutter` section, add `disable-swift-package-manager: true`.

pubspec.yaml

yaml

```
# The following section is specific to Flutter packages.
flutter:
  disable-swift-package-manager: true
```

This turns off Swift Package Manager for all contributors to this project.

### Turn off globally for all projects

[#](#turn-off-globally-for-all-projects)

Run the following command:

sh

```
flutter config --no-enable-swift-package-manager
```

This turns off Swift Package Manager for the current user.

If a project is incompatible with Swift Package Manager, all contributors need to run this command.

How to add Swift Package Manager integration
--------------------------------------------

[#](#how-to-add-swift-package-manager-integration)

### Add to a Flutter app

[#](#add-to-a-flutter-app)

* [iOS project](#37-tab-panel)* [macOS project](#38-tab-panel)

Once you [turn on Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-turn-on-swift-package-manager), the Flutter CLI tries to migrate your project the next time you run your app using the CLI. This migration updates your Xcode project to use Swift Package Manager to add Flutter plugin dependencies.

To migrate your project:

1. [Turn on Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-turn-on-swift-package-manager).- Run the iOS app using the Flutter CLI.

     If your iOS project doesn't have Swift Package Manager integration yet, the Flutter CLI tries to migrate your project and outputs something like:

     ```
     flutter run
     Adding Swift Package Manager integration...
     ```

     The automatic iOS migration modifies the `ios/Runner.xcodeproj/project.pbxproj` and `ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme` files.- If the Flutter CLI's automatic migration fails, follow the steps in [add Swift Package Manager integration manually](/packages-and-plugins/swift-package-manager/for-app-developers/#add-to-a-flutter-app-manually).

[Optional] To check if your project is migrated:

1. Run the app in Xcode.- Ensure that **Run Prepare Flutter Framework Script** runs as a pre-action and that `FlutterGeneratedPluginSwiftPackage` is a target dependency.

     ![Ensure **Run Prepare Flutter Framework Script** runs as a pre-action](/assets/images/docs/development/packages-and-plugins/swift-package-manager/flutter-pre-action-build-log.png)Ensure **Run Prepare Flutter Framework Script** runs as a pre-action

Once you [turn on Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-turn-on-swift-package-manager), the Flutter CLI tries to migrate your project the next time you run your app using the CLI. This migration updates your Xcode project to use Swift Package Manager to add Flutter plugin dependencies.

To migrate your project:

1. [Turn on Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-turn-on-swift-package-manager).- Run the macOS app using the Flutter CLI.

     If your macOS project doesn't have Swift Package Manager integration yet, the Flutter CLI tries to migrate your project and outputs something like:

     ```
     flutter run -d macos
     Adding Swift Package Manager integration...
     ```

     The automatic iOS migration modifies the `macos/Runner.xcodeproj/project.pbxproj` and `macos/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme` files.- If the Flutter CLI's automatic migration fails, follow the steps in [add Swift Package Manager integration manually](/packages-and-plugins/swift-package-manager/for-app-developers/#add-to-a-flutter-app-manually).

[Optional] To check if your project is migrated:

1. Run the app in Xcode.- Ensure that **Run Prepare Flutter Framework Script** runs as a pre-action and that `FlutterGeneratedPluginSwiftPackage` is a target dependency.

     ![Ensure **Run Prepare Flutter Framework Script** runs as a pre-action](/assets/images/docs/development/packages-and-plugins/swift-package-manager/flutter-pre-action-build-log.png)Ensure **Run Prepare Flutter Framework Script** runs as a pre-action

### Add to a Flutter app *manually*

[#](#add-to-a-flutter-app-manually)

* [iOS project](#39-tab-panel)* [macOS project](#40-tab-panel)

Once you [turn on Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-turn-on-swift-package-manager), the Flutter CLI tries to migrate your project to use Swift Package Manager the next time you run your app using the CLI.

However, the Flutter CLI tool might be unable to migrate your project automatically if there are unexpected modifications.

If the automatic migration fails, use the steps below to add Swift Package Manager integration to a project manually.

Before migrating manually, [file an issue](https://github.com/flutter/flutter/issues/new?template=2_bug.yml); this helps the Flutter team improve the automatic migration process. Include the error message and, if possible, include a copy of the following files in your issue:

* `ios/Runner.xcodeproj/project.pbxproj`* `ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme` (or the xcsheme for the flavor used)

### Step 1: Add FlutterGeneratedPluginSwiftPackage Package Dependency

[#](#step-1-add-fluttergeneratedpluginswiftpackage-package-dependency)

1. Open your app (`ios/Runner.xcworkspace`) in Xcode.- Navigate to **Package Dependencies** for the project.

     ![The project's package dependencies](/assets/images/docs/development/packages-and-plugins/swift-package-manager/package-dependencies.png)The project's package dependencies- Click add.- In the dialog that opens, click **Add Local...**.- Navigate to `ios/Flutter/ephemeral/Packages/FlutterGeneratedPluginSwiftPackage` and click **Add Package**.- Ensure that it's added to the `Runner` target and click **Add Package**.

             ![Ensure that the package is added to the `Runner` target](/assets/images/docs/development/packages-and-plugins/swift-package-manager/choose-package-products.png)Ensure that the package is added to the `Runner` target- Ensure that `FlutterGeneratedPluginSwiftPackage` was added to **Frameworks, Libraries, and Embedded Content**.

               ![Ensure that `FlutterGeneratedPluginSwiftPackage` was added to **Frameworks, Libraries, and Embedded Content**](/assets/images/docs/development/packages-and-plugins/swift-package-manager/add-generated-framework.png)Ensure that `FlutterGeneratedPluginSwiftPackage` was added to **Frameworks, Libraries, and Embedded Content**

### Step 2: Add Run Prepare Flutter Framework Script Pre-Action

[#](#step-2-add-run-prepare-flutter-framework-script-pre-action)

**The following steps must be completed for each flavor.**

1. Go to **Product > Scheme > Edit Scheme**.- Expand the **Build** section in the left side bar.- Click **Pre-actions**.- Click add and select **New Run Script Action** from the menu.- Click the **Run Script** title and change it to:

           ```
           Run Prepare Flutter Framework Script
           ```

           - Change the **Provide build settings from** to the `Runner` app.- Input the following in the text box:

               sh

               ```
               "$FLUTTER_ROOT/packages/flutter_tools/bin/xcode_backend.sh" prepare
               ```

               ![Add **Run Prepare Flutter Framework Script** build pre-action](/assets/images/docs/development/packages-and-plugins/swift-package-manager/add-flutter-pre-action.png)Add **Run Prepare Flutter Framework Script** build pre-action

### Step 3: Run app

[#](#step-3-run-app)

1. Run the app in Xcode.- Ensure that **Run Prepare Flutter Framework Script** runs as a pre-action and that `FlutterGeneratedPluginSwiftPackage` is a target dependency.

     ![Ensure **Run Prepare Flutter Framework Script** runs as a pre-action](/assets/images/docs/development/packages-and-plugins/swift-package-manager/flutter-pre-action-build-log.png)Ensure **Run Prepare Flutter Framework Script** runs as a pre-action- Ensure that the app runs on the command line with `flutter run`.

Once you [turn on Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-turn-on-swift-package-manager), the Flutter CLI tries to migrate your project to use Swift Package Manager the next time you run your app using the CLI.

However, the Flutter CLI tool might be unable to migrate your project automatically if there are unexpected modifications.

If the automatic migration fails, use the steps below to add Swift Package Manager integration to a project manually.

Before migrating manually, [file an issue](https://github.com/flutter/flutter/issues/new?template=2_bug.yml); this helps the Flutter team improve the automatic migration process. Include the error message and, if possible, include a copy of the following files in your issue:

* `macos/Runner.xcodeproj/project.pbxproj`* `macos/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme` (or the xcscheme for the flavor used)

### Step 1: Add FlutterGeneratedPluginSwiftPackage Package Dependency

[#](#step-1-add-fluttergeneratedpluginswiftpackage-package-dependency-1)

1. Open your app (`macos/Runner.xcworkspace`) in Xcode.- Navigate to **Package Dependencies** for the project.

     ![The project's package dependencies](/assets/images/docs/development/packages-and-plugins/swift-package-manager/package-dependencies.png)The project's package dependencies- Click add.- In the dialog that opens, click the **Add Local...**.- Navigate to `macos/Flutter/ephemeral/Packages/FlutterGeneratedPluginSwiftPackage` and click the **Add Package**.- Ensure that it's added to the Runner Target and click **Add Package**.

             ![Ensure that the package is added to the `Runner` target](/assets/images/docs/development/packages-and-plugins/swift-package-manager/choose-package-products.png)Ensure that the package is added to the `Runner` target- Ensure that `FlutterGeneratedPluginSwiftPackage` was added to **Frameworks, Libraries, and Embedded Content**.

               ![Ensure that `FlutterGeneratedPluginSwiftPackage` was added to **Frameworks, Libraries, and Embedded Content**](/assets/images/docs/development/packages-and-plugins/swift-package-manager/add-generated-framework.png)Ensure that `FlutterGeneratedPluginSwiftPackage` was added to **Frameworks, Libraries, and Embedded Content**

### Step 2: Add Run Prepare Flutter Framework Script Pre-Action

[#](#step-2-add-run-prepare-flutter-framework-script-pre-action-1)

**The following steps must be completed for each flavor.**

1. Go to **Product > Scheme > Edit Scheme**.- Expand the **Build** section in the left side bar.- Click **Pre-actions**.- Click the add button and select **New Run Script Action** from the menu.- Click the **Run Script** title and change it to:

           ```
           Run Prepare Flutter Framework Script
           ```

           - Change the **Provide build settings from** to the `Runner` target.- Input the following in the text box:

               sh

               ```
               "$FLUTTER_ROOT"/packages/flutter_tools/bin/macos_assemble.sh prepare
               ```

               ![Add **Run Prepare Flutter Framework Script** build pre-action](/assets/images/docs/development/packages-and-plugins/swift-package-manager/add-flutter-pre-action.png)Add **Run Prepare Flutter Framework Script** build pre-action

### Step 3: Run app

[#](#step-3-run-app-1)

1. Run the app in Xcode.- Ensure that **Run Prepare Flutter Framework Script** runs as a pre-action and that `FlutterGeneratedPluginSwiftPackage` is a target dependency.

     ![Ensure `Run Prepare Flutter Framework Script` runs as a pre-action](/assets/images/docs/development/packages-and-plugins/swift-package-manager/flutter-pre-action-build-log.png)Ensure `Run Prepare Flutter Framework Script` runs as a pre-action- Ensure that the app runs on the command line with `flutter run`.

### Add to an existing app (add-to-app)

[#](#add-to-an-existing-app-add-to-app)

Flutter's Swift Package Manager support doesn't work with add-to-app scenarios.

To keep current on status updates, consult [flutter#146957](https://github.com/flutter/flutter/issues/146957).

### Add to a custom Xcode target

[#](#add-to-a-custom-xcode-target)

Your Flutter Xcode project can have custom [Xcode targets](https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project) to build additional products, like frameworks or unit tests. You can add Swift Package Manager integration to these custom Xcode targets.

Follow the steps in [How to add Swift Package Manager integration to a project *manually*](/packages-and-plugins/swift-package-manager/for-app-developers/#add-to-a-flutter-app-manually).

In [Step 1](/packages-and-plugins/swift-package-manager/for-app-developers/#step-1-add-fluttergeneratedpluginswiftpackage-package-dependency), list item 6 use your custom target instead of the `Flutter` target.

In [Step 2](/packages-and-plugins/swift-package-manager/for-app-developers/#step-2-add-run-prepare-flutter-framework-script-pre-action), list item 6 use your custom target instead of the `Flutter` target.

How to remove Swift Package Manager integration
-----------------------------------------------

[#](#how-to-remove-swift-package-manager-integration)

To add Swift Package Manager integration, the Flutter CLI migrates your project. This migration updates your Xcode project to add Flutter plugin dependencies.

To undo this migration:

1. [Turn off Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers/#how-to-turn-off-swift-package-manager).- Clean your project:

     sh

     ```
     flutter clean
     ```

     - Open your app (`ios/Runner.xcworkspace` or `macos/Runner.xcworkspace`) in Xcode.- Navigate to **Package Dependencies** for the project.- Click the `FlutterGeneratedPluginSwiftPackage` package, then click remove.

           ![The `FlutterGeneratedPluginSwiftPackage` to remove](/assets/images/docs/development/packages-and-plugins/swift-package-manager/remove-generated-package.png)The `FlutterGeneratedPluginSwiftPackage` to remove- Navigate to **Frameworks, Libraries, and Embedded Content** for the `Runner` target.- Click `FlutterGeneratedPluginSwiftPackage`, then click the remove.

               ![The `FlutterGeneratedPluginSwiftPackage` to remove](/assets/images/docs/development/packages-and-plugins/swift-package-manager/remove-generated-framework.png)The `FlutterGeneratedPluginSwiftPackage` to remove- Go to **Product > Scheme > Edit Scheme**.- Expand the **Build** section in the left side bar.- Click **Pre-actions**.- Expand **Run Prepare Flutter Framework Script**.- Click **delete**.

                         ![The build pre-action to remove](/assets/images/docs/development/packages-and-plugins/swift-package-manager/remove-flutter-pre-action.png)The build pre-action to remove

How to use a Swift Package Manager Flutter plugin that requires a higher OS version
-----------------------------------------------------------------------------------

[#](#how-to-use-a-swift-package-manager-flutter-plugin-that-requires-a-higher-os-version)

If a Swift Package Flutter Manager plugin requires a higher OS version than the project, you might get an error like this:

```
Target Integrity (Xcode): The package product 'plugin_name_ios' requires minimum platform version 14.0 for the iOS platform, but this target supports 12.0
```

To use the plugin:

1. Open your app (`ios/Runner.xcworkspace` or `macos/Runner.xcworkspace`) in Xcode.- Increase your app's target **Minimum Deployments**.

     ![The target's **Minimum Deployments** setting](/assets/images/docs/development/packages-and-plugins/swift-package-manager/minimum-deployments.png)The target's **Minimum Deployments** setting- If you updated your iOS app's **Minimum Deployments**, regenerate the iOS project's configuration files:

       sh

       ```
       flutter build ios --config-only
       ```

       - If you updated your macOS app's **Minimum Deployments**, regenerate the macOS project's configuration files:

         sh

         ```
         flutter build macos --config-only
         ```

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/swift-package-manager/for-app-developers/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-app-developers.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/swift-package-manager/for-app-developers/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-app-developers.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-22. [View source](https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-app-developers.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/swift-package-manager/for-app-developers/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-app-developers.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   