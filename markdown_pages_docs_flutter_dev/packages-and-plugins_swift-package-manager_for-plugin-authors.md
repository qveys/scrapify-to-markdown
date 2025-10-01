Swift Package Manager for plugin authors
========================================

1. [Packages & plugins](/packages-and-plugins) chevron\_right- [Swift Package Manager for Flutter](/packages-and-plugins/swift-package-manager) chevron\_right- [Swift Package Manager for plugin authors](/packages-and-plugins/swift-package-manager/for-plugin-authors)

*warning* Warning

Flutter is migrating to [Swift Package Manager](https://www.swift.org/documentation/package-manager/) to manage iOS and macOS native dependencies. Flutter's support of Swift Package Manager is under development. If you find a bug in Flutter's Swift Package Manager support, [open an issue](https://github.com/flutter/flutter/issues/new?template=2_bug.yml). Swift Package Manager support is [off by default](#how-to-turn-on-swift-package-manager). Flutter continues to support CocoaPods.

Flutter's Swift Package Manager integration has several benefits:

1. **Provides access to the Swift package ecosystem**. Flutter plugins can use the growing ecosystem of [Swift packages](https://swiftpackageindex.com/)!- **Simplifies Flutter installation**. Swift Package Manager is bundled with Xcode. In the future, you won’t need to install Ruby and CocoaPods to target iOS or macOS.

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

How to add Swift Package Manager support to an existing Flutter plugin
----------------------------------------------------------------------

[#](#how-to-add-swift-package-manager-support-to-an-existing-flutter-plugin)

This guide shows how to add Swift Package Manager support to a plugin that already supports CocoaPods. This ensures the plugin is usable by all Flutter projects.

Flutter plugins should support *both* Swift Package Manager and CocoaPods until further notice.

Swift Package Manager adoption will be gradual. Plugins that don't support CocoaPods won't be usable by projects that haven't migrated to Swift Package Manager yet. Plugins that don't support Swift Package Manager can cause problems for projects that have migrated.

* [Swift plugin](#35-tab-panel)* [Objective-C plugin](#36-tab-panel)

Replace `plugin_name` throughout this guide with the name of your plugin. The example below uses `ios`, replace `ios` with `macos`/`darwin` as applicable.

1. [Turn on the Swift Package Manager feature](/packages-and-plugins/swift-package-manager/for-plugin-authors#how-to-turn-on-swift-package-manager).- Start by creating a directory under the `ios`, `macos`, and/or `darwin` directories. Name this new directory the name of the platform package.

     ```
     plugin_name/ios/
     ├── ...
     └── plugin_name/
     ```

     - Within this new directory, create the following files/directories:
       * `Package.swift` (file)* `Sources` (directory)* `Sources/plugin_name` (directory)

       Your plugin should look like:

       ```
       plugin_name/ios/
       ├── ...
       └── plugin_name/
          ├── Package.swift
          └── Sources/plugin_name/
       ```

       - Use the following template in the `Package.swift` file:

         Package.swift

         swift

         ```
         // swift-tools-version: 5.9
         // The swift-tools-version declares the minimum version of Swift required to build this package.

         import PackageDescription

         let package = Package(
             // TODO: Update your plugin name.
             name: "plugin_name",
             platforms: [
                 // TODO: Update the platforms your plugin supports.
                 // If your plugin only supports iOS, remove `.macOS(...)`.
                 // If your plugin only supports macOS, remove `.iOS(...)`.
                 .iOS("13.0"),
                 .macOS("10.15")
             ],
             products: [
                 // TODO: Update your library and target names.
                 // If the plugin name contains "_", replace with "-" for the library name.
                 .library(name: "plugin-name", targets: ["plugin_name"])
             ],
             dependencies: [],
             targets: [
                 .target(
                     // TODO: Update your target name.
                     name: "plugin_name",
                     dependencies: [],
                     resources: [
                         // TODO: If your plugin requires a privacy manifest
                         // (e.g. if it uses any required reason APIs), update the PrivacyInfo.xcprivacy file
                         // to describe your plugin's privacy impact, and then uncomment this line.
                         // For more information, see:
                         // https://developer.apple.com/documentation/bundleresources/privacy_manifest_files
                         // .process("PrivacyInfo.xcprivacy"),

                         // TODO: If you have other resources that need to be bundled with your plugin, refer to
                         // the following instructions to add them:
                         // https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package
                     ]
                 )
             ]
         )
         ```

         - Update the [supported platforms](https://developer.apple.com/documentation/packagedescription/supportedplatform) in your `Package.swift` file.

           Package.swift

           swift

           ```
               platforms: [
                   // TODO: Update the platforms your plugin supports.
                   // If your plugin only supports iOS, remove `.macOS(...)`.
                   // If your plugin only supports macOS, remove `.iOS(...)`.
                   .iOS("13.0"),
                   .macOS("10.15")
               ],
           ```

           - Update the package, library, and target names in your `Package.swift` file.

             Package.swift

             swift

             ```
             let package = Package(
                 // TODO: Update your plugin name.
                 name: "plugin_name",
                 platforms: [
                     .iOS("13.0"),
                     .macOS("10.15")
                 ],
                 products: [
                     // TODO: Update your library and target names.
                     // If the plugin name contains "_", replace with "-" for the library name
                     .library(name: "plugin-name", targets: ["plugin_name"])
                 ],
                 dependencies: [],
                 targets: [
                     .target(
                         // TODO: Update your target name.
                         name: "plugin_name",
                         dependencies: [],
                         resources: [
                             // TODO: If your plugin requires a privacy manifest
                             // (e.g. if it uses any required reason APIs), update the PrivacyInfo.xcprivacy file
                             // to describe your plugin's privacy impact, and then uncomment this line.
                             // For more information, see:
                             // https://developer.apple.com/documentation/bundleresources/privacy_manifest_files
                             // .process("PrivacyInfo.xcprivacy"),

                             // TODO: If you have other resources that need to be bundled with your plugin, refer to
                             // the following instructions to add them:
                             // https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package
                         ]
                     )
                 ]
             )
             ```

             *info* Note

             If the plugin name contains `_`, the library name must be a `-` separated version of the plugin name.

             - If your plugin has a [`PrivacyInfo.xcprivacy` file](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files), move it to `ios/plugin_name/Sources/plugin_name/PrivacyInfo.xcprivacy` and uncomment the resource in the `Package.swift` file.

               Package.swift

               swift

               ```
                           resources: [
                               // TODO: If your plugin requires a privacy manifest
                               // (e.g. if it uses any required reason APIs), update the PrivacyInfo.xcprivacy file
                               // to describe your plugin's privacy impact, and then uncomment this line.
                               // For more information, see:
                               // https://developer.apple.com/documentation/bundleresources/privacy_manifest_files
                               .process("PrivacyInfo.xcprivacy"),

                               // TODO: If you have other resources that need to be bundled with your plugin, refer to
                               // the following instructions to add them:
                               // https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package
                           ],
               ```

               - Move any resource files from `ios/Assets` to `ios/plugin_name/Sources/plugin_name` (or a subdirectory). Add the resource files to your `Package.swift` file, if applicable. For more instructions, see <https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package>.- Move all files from `ios/Classes` to `ios/plugin_name/Sources/plugin_name`.- The `ios/Assets`, `ios/Resources`, and `ios/Classes` directories should now be empty and can be deleted.- If your plugin uses [Pigeon](https://pub.dev/packages/pigeon), update your Pigeon input file.

                       pigeons/messages.dart

                       dart

                       ```
                       kotlinOptions: KotlinOptions(),
                       javaOut: 'android/app/src/main/java/io/flutter/plugins/Messages.java',
                       javaOptions: JavaOptions(),
                       swiftOut: 'ios/Classes/messages.g.swift',
                       swiftOut: 'ios/plugin_name/Sources/plugin_name/messages.g.swift',
                       swiftOptions: SwiftOptions(),
                       ```

                       - Update your `Package.swift` file with any customizations you might need.
                         1. Open the `ios/plugin_name/` directory in Xcode.- In Xcode, open your `Package.swift` file. Verify Xcode doesn't produce any warnings or errors for this file.

                              *lightbulb* Tip

                              If Xcode doesn't show any files, quit Xcode (**Xcode > Quit Xcode**) and reopen.

                              If Xcode doesn't update after you make a change, try clicking **File > Packages > Reset Package Caches**.

                              - If your `ios/plugin_name.podspec` file has [CocoaPods `dependency`](https://guides.cocoapods.org/syntax/podspec.html#dependency)s, add the corresponding [Swift Package Manager dependencies](https://developer.apple.com/documentation/packagedescription/package/dependency) to your `Package.swift` file.- If your package must be linked explicitly `static` or `dynamic` ([not recommended by Apple](https://developer.apple.com/documentation/packagedescription/product/library(name:type:targets:))), update the [Product](https://developer.apple.com/documentation/packagedescription/product) to define the type:

                                  Package.swift

                                  swift

                                  ```
                                  products: [
                                      .library(name: "plugin-name", type: .static, targets: ["plugin_name"])
                                  ],
                                  ```

                                  - Make any other customizations. For more information on how to write a `Package.swift` file, see <https://developer.apple.com/documentation/packagedescription>.

                                    *lightbulb* Tip

                                    If you add targets to your `Package.swift` file, use unique names. This avoids conflicts with targets from other packages.- Update your `ios/plugin_name.podspec` to point to new paths.

                           ios/plugin\_name.podspec

                           ruby

                           ```
                           s.source_files = 'Classes/**/*.swift'
                           s.resource_bundles = {'plugin_name_privacy' => ['Resources/PrivacyInfo.xcprivacy']}
                           s.source_files = 'plugin_name/Sources/plugin_name/**/*.swift'
                           s.resource_bundles = {'plugin_name_privacy' => ['plugin_name/Sources/plugin_name/PrivacyInfo.xcprivacy']}
                           ```

                           - Update loading of resources from bundle to use [`Bundle.module`](https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package#Access-a-resource-in-code).

                             swift

                             ```
                             #if SWIFT_PACKAGE
                                  let settingsURL = Bundle.module.url(forResource: "image", withExtension: "jpg")
                             #else
                                  let settingsURL = Bundle(for: Self.self).url(forResource: "image", withExtension: "jpg")
                             #endif
                             ```

                             *info* Note

                             `Bundle.module` only works if there are resources [defined in the `Package.swift` file](https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package#Explicitly-declare-or-exclude-resources) or [automatically included by Xcode](https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package#:~:text=Xcode%20detects%20common%20resource%20types%20for%20Apple%20platforms%20and%20treats%20them%20as%20a%20resource%20automatically)). Otherwise, using `Bundle.module` results in an error.

                             - If your `.gitignore` doesn't include `.build/` and `.swiftpm/` directories, you'll want to update your `.gitignore` to include:

                               .gitignore

                               text

                               ```
                               .build/
                               .swiftpm/
                               ```

                               Commit your plugin's changes to your version control system.- Verify the plugin still works with CocoaPods.
                                 1. Turn off Swift Package Manager.

                                    sh

                                    ```
                                    flutter config --no-enable-swift-package-manager
                                    ```

                                    - Navigate to the plugin's example app.

                                      sh

                                      ```
                                      cd path/to/plugin/example/
                                      ```

                                      - Ensure the plugin's example app builds and runs.

                                        sh

                                        ```
                                        flutter run
                                        ```

                                        - Navigate to the plugin's top-level directory.

                                          sh

                                          ```
                                          cd path/to/plugin/
                                          ```

                                          - Run CocoaPods validation lints.

                                            sh

                                            ```
                                            pod lib lint ios/plugin_name.podspec  --configuration=Debug --skip-tests --use-modular-headers --use-libraries
                                            ```

                                            sh

                                            ```
                                            pod lib lint ios/plugin_name.podspec  --configuration=Debug --skip-tests --use-modular-headers
                                            ```- Verify the plugin works with Swift Package Manager.
                                   1. Turn on Swift Package Manager.

                                      sh

                                      ```
                                      flutter config --enable-swift-package-manager
                                      ```

                                      - Navigate to the plugin's example app.

                                        sh

                                        ```
                                        cd path/to/plugin/example/
                                        ```

                                        - Ensure the plugin's example app builds and runs.

                                          sh

                                          ```
                                          flutter run
                                          ```

                                          *info* Note

                                          Using the Flutter CLI to run the plugin's example app with the Swift Package Manager feature turned on migrates the project to add Swift Package Manager integration.

                                          This raises the example app's Flutter SDK requirement to version 3.24 or higher.

                                          If you'd like to run the example app using an older Flutter SDK version, do not commit the migration's changes to your version control system. If needed, you can always [undo the Swift Package Manager migration](/packages-and-plugins/swift-package-manager/for-app-developers#how-to-remove-swift-package-manager-integration).

                                          - Open the plugin's example app in Xcode. Ensure that **Package Dependencies** shows in the left **Project Navigator**.- Verify tests pass.
                                     * **If your plugin has native unit tests (XCTest), make sure you also [update unit tests in the plugin's example app](/packages-and-plugins/swift-package-manager/for-plugin-authors/#how-to-update-unit-tests-in-a-plugins-example-app).*** Follow instructions for [testing plugins](https://docs.flutter.dev/testing/testing-plugins).

Replace `plugin_name` throughout this guide with the name of your plugin. The example below uses `ios`, replace `ios` with `macos`/`darwin` as applicable.

1. [Turn on the Swift Package Manager feature](/packages-and-plugins/swift-package-manager/for-plugin-authors#how-to-turn-on-swift-package-manager).- Start by creating a directory under the `ios`, `macos`, and/or `darwin` directories. Name this new directory the name of the platform package.

     ```
     plugin_name/ios/
     ├── ...
     └── plugin_name/
     ```

     - Within this new directory, create the following files/directories:
       * `Package.swift` (file)* `Sources` (directory)* `Sources/plugin_name` (directory)* `Sources/plugin_name/include` (directory)* `Sources/plugin_name/include/plugin_name` (directory)* `Sources/plugin_name/include/plugin_name/.gitkeep` (file)
                   + This file ensures the directory is committed. You can remove the `.gitkeep` file if other files are added to the directory.

       Your plugin should look like:

       ```
       plugin_name/ios/
       ├── ...
       └── plugin_name/
          ├── Package.swift
          └── Sources/plugin_name/include/plugin_name/
             └── .gitkeep
       ```

       - Use the following template in the `Package.swift` file:

         Package.swift

         swift

         ```
         // swift-tools-version: 5.9
         // The swift-tools-version declares the minimum version of Swift required to build this package.

         import PackageDescription

         let package = Package(
             // TODO: Update your plugin name.
             name: "plugin_name",
             platforms: [
                 // TODO: Update the platforms your plugin supports.
                 // If your plugin only supports iOS, remove `.macOS(...)`.
                 // If your plugin only supports macOS, remove `.iOS(...)`.
                 .iOS("13.0"),
                 .macOS("10.15")
             ],
             products: [
                 // TODO: Update your library and target names.
                 // If the plugin name contains "_", replace with "-" for the library name
                 .library(name: "plugin-name", targets: ["plugin_name"])
             ],
             dependencies: [],
             targets: [
                 .target(
                     // TODO: Update your target name.
                     name: "plugin_name",
                     dependencies: [],
                     resources: [
                         // TODO: If your plugin requires a privacy manifest
                         // (e.g. if it uses any required reason APIs), update the PrivacyInfo.xcprivacy file
                         // to describe your plugin's privacy impact, and then uncomment this line.
                         // For more information, see:
                         // https://developer.apple.com/documentation/bundleresources/privacy_manifest_files
                         // .process("PrivacyInfo.xcprivacy"),

                         // TODO: If you have other resources that need to be bundled with your plugin, refer to
                         // the following instructions to add them:
                         // https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package
                     ],
                     cSettings: [
                         // TODO: Update your plugin name.
                         .headerSearchPath("include/plugin_name")
                     ]
                 )
             ]
         )
         ```

         - Update the [supported platforms](https://developer.apple.com/documentation/packagedescription/supportedplatform) in your `Package.swift` file.

           Package.swift

           swift

           ```
               platforms: [
                   // TODO: Update the platforms your plugin supports.
                   // If your plugin only supports iOS, remove `.macOS(...)`.
                   // If your plugin only supports macOS, remove `.iOS(...)`.
                   .iOS("13.0"),
                   .macOS("10.15")
               ],
           ```

           - Update the package, library, and target names in your `Package.swift` file.

             Package.swift

             swift

             ```
             let package = Package(
                 // TODO: Update your plugin name.
                 name: "plugin_name",
                 platforms: [
                     .iOS("13.0"),
                     .macOS("10.15")
                 ],
                 products: [
                     // TODO: Update your library and target names.
                     // If the plugin name contains "_", replace with "-" for the library name
                     .library(name: "plugin-name", targets: ["plugin_name"])
                 ],
                 dependencies: [],
                 targets: [
                     .target(
                         // TODO: Update your target name.
                         name: "plugin_name",
                         dependencies: [],
                         resources: [
                             // TODO: If your plugin requires a privacy manifest
                             // (e.g. if it uses any required reason APIs), update the PrivacyInfo.xcprivacy file
                             // to describe your plugin's privacy impact, and then uncomment this line.
                             // For more information, see:
                             // https://developer.apple.com/documentation/bundleresources/privacy_manifest_files
                             // .process("PrivacyInfo.xcprivacy"),

                             // TODO: If you have other resources that need to be bundled with your plugin, refer to
                             // the following instructions to add them:
                             // https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package
                         ],
                         cSettings: [
                             // TODO: Update your plugin name.
                             .headerSearchPath("include/plugin_name")
                         ]
                     )
                 ]
             )
             ```

             *info* Note

             If the plugin name contains `_`, the library name must be a `-` separated version of the plugin name.

             - If your plugin has a [`PrivacyInfo.xcprivacy` file](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files), move it to `ios/plugin_name/Sources/plugin_name/PrivacyInfo.xcprivacy` and uncomment the resource in the `Package.swift` file.

               Package.swift

               swift

               ```
                           resources: [
                               // TODO: If your plugin requires a privacy manifest
                               // (e.g. if it uses any required reason APIs), update the PrivacyInfo.xcprivacy file
                               // to describe your plugin's privacy impact, and then uncomment this line.
                               // For more information, see:
                               // https://developer.apple.com/documentation/bundleresources/privacy_manifest_files
                               .process("PrivacyInfo.xcprivacy"),

                               // TODO: If you have other resources that need to be bundled with your plugin, refer to
                               // the following instructions to add them:
                               // https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package
                           ],
               ```

               - Move any resource files from `ios/Assets` to `ios/plugin_name/Sources/plugin_name` (or a subdirectory). Add the resource files to your `Package.swift` file, if applicable. For more instructions, see <https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package>.- Move any public headers from `ios/Classes` to `ios/plugin_name/Sources/plugin_name/include/plugin_name`.
                   * If you're unsure which headers are public, check your `podspec` file's [`public_header_files`](https://guides.cocoapods.org/syntax/podspec.html#public_header_files) attribute. If this attribute isn't specified, all of your headers were public. You should consider whether you want all of your headers to be public.* The `pluginClass` defined in your `pubspec.yaml` file must be public and within this directory.- Handling `modulemap`.

                     Skip this step if your plugin does not have a `modulemap`.

                     If you're using a `modulemap` for CocoaPods to create a Test submodule, consider removing it for Swift Package Manager. Note that this makes all public headers available through the module.

                     To remove the `modulemap` for Swift Package Manager but keep it for CocoaPods, exclude the `modulemap` and umbrella header in the plugin's `Package.swift` file.

                     The example below assumes the `modulemap` and umbrella header are located in the `ios/plugin_name/Sources/plugin_name/include` directory.

                     Package.swift

                     swift

                     ```
                     .target(
                         name: "plugin_name",
                         dependencies: [],
                         exclude: ["include/cocoapods_plugin_name.modulemap", "include/plugin_name-umbrella.h"],
                     ```

                     If you want to keep your unit tests compatible with both CocoaPods and Swift Package Manager, you can try the following:

                     Tests/TestFile.m

                     objc

                     ```
                     @import plugin_name;
                     @import plugin_name.Test;
                     #if __has_include(<plugin_name plugin_name-umbrella.h="">)
                       @import plugin_name.Test;
                     #endif
                     ```

                     If you would like to use a custom `modulemap` with your Swift package, refer to [Swift Package Manager's documentation](https://github.com/apple/swift-package-manager/blob/main/Documentation/Usage.md#creating-c-language-targets).- Move all remaining files from `ios/Classes` to `ios/plugin_name/Sources/plugin_name`.- The `ios/Assets`, `ios/Resources`, and `ios/Classes` directories should now be empty and can be deleted.- If your header files are no longer in the same directory as your implementation files, you should update your import statements.

                           For example, imagine the following migration:
                           * Before:

                             ```
                             ios/Classes/
                             ├── PublicHeaderFile.h
                             └── ImplementationFile.m
                             ```

                             * After:

                               ```
                               ios/plugin_name/Sources/plugin_name/
                               └── include/plugin_name/
                                  └── PublicHeaderFile.h
                               └── ImplementationFile.m
                               ```

                           In this example, the import statements in `ImplementationFile.m` should be updated:

                           Sources/plugin\_name/ImplementationFile.m

                           objc

                           ```
                           #import "PublicHeaderFile.h"
                           #import "./include/plugin_name/PublicHeaderFile.h"
                           ```

                           - If your plugin uses [Pigeon](https://pub.dev/packages/pigeon), update your Pigeon input file.

                             pigeons/messages.dart

                             dart

                             ```
                             javaOptions: JavaOptions(),
                             objcHeaderOut: 'ios/Classes/messages.g.h',
                             objcSourceOut: 'ios/Classes/messages.g.m',
                             objcHeaderOut: 'ios/plugin_name/Sources/plugin_name/messages.g.h',
                             objcSourceOut: 'ios/plugin_name/Sources/plugin_name/messages.g.m',
                             copyrightHeader: 'pigeons/copyright.txt',
                             ```

                             If your `objcHeaderOut` file is no longer within the same directory as the `objcSourceOut`, you can change the `#import` using `ObjcOptions.headerIncludePath`:

                             pigeons/messages.dart

                             dart

                             ```
                             javaOptions: JavaOptions(),
                             objcHeaderOut: 'ios/Classes/messages.g.h',
                             objcSourceOut: 'ios/Classes/messages.g.m',
                             objcHeaderOut: 'ios/plugin_name/Sources/plugin_name/include/plugin_name/messages.g.h',
                             objcSourceOut: 'ios/plugin_name/Sources/plugin_name/messages.g.m',
                             objcOptions: ObjcOptions(
                               headerIncludePath: './include/plugin_name/messages.g.h',
                             ),
                             copyrightHeader: 'pigeons/copyright.txt',
                             ```

                             Run Pigeon to re-generate its code with the latest configuration.- Update your `Package.swift` file with any customizations you might need.
                               1. Open the `ios/plugin_name/` directory in Xcode.- In Xcode, open your `Package.swift` file. Verify Xcode doesn't produce any warnings or errors for this file.

                                    *lightbulb* Tip

                                    If Xcode doesn't show any files, quit Xcode (**Xcode > Quit Xcode**) and reopen.

                                    If Xcode doesn't update after you make a change, try clicking **File > Packages > Reset Package Caches**.

                                    - If your `ios/plugin_name.podspec` file has [CocoaPods `dependency`](https://guides.cocoapods.org/syntax/podspec.html#dependency)s, add the corresponding [Swift Package Manager dependencies](https://developer.apple.com/documentation/packagedescription/package/dependency) to your `Package.swift` file.- If your package must be linked explicitly `static` or `dynamic` ([not recommended by Apple](https://developer.apple.com/documentation/packagedescription/product/library(name:type:targets:))), update the [Product](https://developer.apple.com/documentation/packagedescription/product) to define the type:

                                        Package.swift

                                        swift

                                        ```
                                        products: [
                                            .library(name: "plugin-name", type: .static, targets: ["plugin_name"])
                                        ],
                                        ```

                                        - Make any other customizations. For more information on how to write a `Package.swift` file, see <https://developer.apple.com/documentation/packagedescription>.

                                          *lightbulb* Tip

                                          If you add targets to your `Package.swift` file, use unique names. This avoids conflicts with targets from other packages.- Update your `ios/plugin_name.podspec` to point to new paths.

                                 ios/plugin\_name.podspec

                                 ruby

                                 ```
                                 s.source_files = 'Classes/**/*.{h,m}'
                                 s.public_header_files = 'Classes/**/*.h'
                                 s.module_map = 'Classes/cocoapods_plugin_name.modulemap'
                                 s.resource_bundles = {'plugin_name_privacy' => ['Resources/PrivacyInfo.xcprivacy']}
                                 s.source_files = 'plugin_name/Sources/plugin_name/**/*.{h,m}'
                                 s.public_header_files = 'plugin_name/Sources/plugin_name/include/**/*.h'
                                 s.module_map = 'plugin_name/Sources/plugin_name/include/cocoapods_plugin_name.modulemap'
                                 s.resource_bundles = {'plugin_name_privacy' => ['plugin_name/Sources/plugin_name/PrivacyInfo.xcprivacy']}
                                 ```

                                 - Update loading of resources from bundle to use `SWIFTPM_MODULE_BUNDLE`:

                                   objc

                                   ```
                                   #if SWIFT_PACKAGE
                                      NSBundle *bundle = SWIFTPM_MODULE_BUNDLE;
                                    #else
                                      NSBundle *bundle = [NSBundle bundleForClass:[self class]];
                                    #endif
                                    NSURL *imageURL = [bundle URLForResource:@"image" withExtension:@"jpg"];
                                   ```

                                   *info* Note

                                   `SWIFTPM_MODULE_BUNDLE` only works if there are actual resources (either [defined in the `Package.swift` file](https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package#Explicitly-declare-or-exclude-resources) or [automatically included by Xcode](https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package#:~:text=Xcode%20detects%20common%20resource%20types%20for%20Apple%20platforms%20and%20treats%20them%20as%20a%20resource%20automatically)). Otherwise, using `SWIFTPM_MODULE_BUNDLE` results in an error.

                                   - If your `ios/plugin_name/Sources/plugin_name/include` directory only contains a `.gitkeep`, you'll want update your `.gitignore` to include the following:

                                     .gitignore

                                     text

                                     ```
                                     !.gitkeep
                                     ```

                                     Run `flutter pub publish --dry-run` to ensure the `include` directory is published.- Commit your plugin's changes to your version control system.- Verify the plugin still works with CocoaPods.
                                         1. Turn off Swift Package Manager:

                                            sh

                                            ```
                                            flutter config --no-enable-swift-package-manager
                                            ```

                                            - Navigate to the plugin's example app.

                                              sh

                                              ```
                                              cd path/to/plugin/example/
                                              ```

                                              - Ensure the plugin's example app builds and runs.

                                                sh

                                                ```
                                                flutter run
                                                ```

                                                - Navigate to the plugin's top-level directory.

                                                  sh

                                                  ```
                                                  cd path/to/plugin/
                                                  ```

                                                  - Run CocoaPods validation lints:

                                                    sh

                                                    ```
                                                    pod lib lint ios/plugin_name.podspec  --configuration=Debug --skip-tests --use-modular-headers --use-libraries
                                                    ```

                                                    sh

                                                    ```
                                                    pod lib lint ios/plugin_name.podspec  --configuration=Debug --skip-tests --use-modular-headers
                                                    ```- Verify the plugin works with Swift Package Manager.
                                           1. Turn on Swift Package Manager:

                                              sh

                                              ```
                                              flutter config --enable-swift-package-manager
                                              ```

                                              - Navigate to the plugin's example app.

                                                sh

                                                ```
                                                cd path/to/plugin/example/
                                                ```

                                                - Ensure the plugin's example app builds and runs.

                                                  sh

                                                  ```
                                                  flutter run
                                                  ```

                                                  *info* Note

                                                  Using the Flutter CLI to run the plugin's example app with the Swift Package Manager feature turned on migrates the project to add Swift Package Manager integration.

                                                  This raises the example app's Flutter SDK requirement to version 3.24 or higher.

                                                  If you'd like to run the example app using an older Flutter SDK version, do not commit the migration's changes to your version control system. If needed, you can always [undo the Swift Package Manager migration](/packages-and-plugins/swift-package-manager/for-app-developers#how-to-remove-swift-package-manager-integration).

                                                  - Open the plugin's example app in Xcode. Ensure that **Package Dependencies** shows in the left **Project Navigator**.- Verify tests pass.
                                             * **If your plugin has native unit tests (XCTest), make sure you also [update unit tests in the plugin's example app](/packages-and-plugins/swift-package-manager/for-plugin-authors/#how-to-update-unit-tests-in-a-plugins-example-app).*** Follow instructions for [testing plugins](https://docs.flutter.dev/testing/testing-plugins).

</plugin\_name>

How to update unit tests in a plugin's example app
--------------------------------------------------

[#](#how-to-update-unit-tests-in-a-plugins-example-app)

If your plugin has native XCTests, you might need to update them to work with Swift Package Manager if one of the following is true:

* You're using a CocoaPod dependency for the test.* Your plugin is explicitly set to `type: .dynamic` in its `Package.swift` file.

To update your unit tests:

1. Open your `example/ios/Runner.xcworkspace` in Xcode.- If you were using a CocoaPod dependency for tests, such as `OCMock`, you'll want to remove it from your `Podfile` file.

     ios/Podfile

     ruby

     ```
     target 'RunnerTests' do
       inherit! :search_paths

       pod 'OCMock', '3.5'
     end
     ```

     Then in the terminal, run `pod install` in the `plugin_name_ios/example/ios` directory.- Navigate to **Package Dependencies** for the project.

       ![The project's package dependencies](/assets/images/docs/development/packages-and-plugins/swift-package-manager/package-dependencies.png)The project's package dependencies- Click the **+** button and add any test-only dependencies by searching for them in the top right search bar.

         ![Search for test-only dependencies](/assets/images/docs/development/packages-and-plugins/swift-package-manager/search-for-ocmock.png)Search for test-only dependencies

         *info* Note

         OCMock uses unsafe build flags and can only be used if targeted by commit. `fe1661a3efed11831a6452f4b1a0c5e6ddc08c3d` is the commit for the 3.9.3 version.

         - Ensure the dependency is added to the `RunnerTests` Target.

           ![Ensure the dependency is added to the `RunnerTests` target](/assets/images/docs/development/packages-and-plugins/swift-package-manager/choose-package-products-test.png)Ensure the dependency is added to the `RunnerTests` target- Click the **Add Package** button.- If you've explicitly set your plugin's library type to `.dynamic` in its `Package.swift` file ([not recommended by Apple](https://developer.apple.com/documentation/packagedescription/product/library(name:type:targets:))), you'll also need to add it as a dependency to the `RunnerTests` target.
               1. Ensure `RunnerTests` **Build Phases** has a **Link Binary With Libraries** build phase:

                  ![The `Link Binary With Libraries` Build Phase in the `RunnerTests` target](/assets/images/docs/development/packages-and-plugins/swift-package-manager/runner-tests-link-binary-with-libraries.png)The `Link Binary With Libraries` Build Phase in the `RunnerTests` target

                  If the build phase doesn't exist already, create one. Click the add and then click **New Link Binary With Libraries Phase**.

                  ![Add `Link Binary With Libraries` Build Phase](/assets/images/docs/development/packages-and-plugins/swift-package-manager/add-runner-tests-link-binary-with-libraries.png)Add `Link Binary With Libraries` Build Phase- Navigate to **Package Dependencies** for the project.- Click add.- In the dialog that opens, click the **Add Local...** button.- Navigate to `plugin_name/plugin_name_ios/ios/plugin_name_ios` and click the **Add Package** button.- Ensure that it's added to the `RunnerTests` target and click the **Add Package** button.- Ensure tests pass **Product > Test**.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/swift-package-manager/for-plugin-authors/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-plugin-authors.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/swift-package-manager/for-plugin-authors/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-plugin-authors.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-22. [View source](https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-plugin-authors.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/packages-and-plugins/swift-package-manager/for-plugin-authors/&page-source=https://github.com/flutter/website/tree/main/src/content/packages-and-plugins/swift-package-manager/for-plugin-authors.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   