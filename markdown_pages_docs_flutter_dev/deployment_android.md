Build and release an Android app
================================

1. [Deployment](/deployment) chevron\_right- [Android](/deployment/android)

To test an app, you can use `flutter run` at the command line, or the **Run** and **Debug** options in your IDE.

When you're ready to prepare a *release* version of your app, for example to [publish to the Google Play Store](https://developer.android.com/distribute), this page can help. Before publishing, you might want to put some finishing touches on your app. This guide explains how to perform the following tasks:

* [Add a launcher icon](#add-a-launcher-icon)* [Enable Material Components](#enable-material-components)* [Sign the app](#sign-the-app)* [Shrink your code with R8](#shrink-your-code-with-r8)* [Enable multidex support](#enable-multidex-support)* [Review the app manifest](#review-the-app-manifest)* [Review the build configuration](#review-the-gradle-build-configuration)* [Build the app for release](#build-the-app-for-release)* [Publish to the Google Play Store](#publish-to-the-google-play-store)* [Update the app's version number](#update-the-apps-version-number)* [Android release FAQ](#android-release-faq)

*info* Note

Throughout this page, `[project]` refers to the directory that your application is in. While following these instructions, substitute `[project]` with your app's directory.

Add a launcher icon
-------------------

[#](#add-a-launcher-icon)

When a new Flutter app is created, it has a default launcher icon. To customize this icon, you might want to check out the [flutter\_launcher\_icons](https://pub.dev/packages/flutter_launcher_icons) package.

Alternatively, you can do it manually using the following steps:

1. Review the [Material Design product icons](https://m3.material.io/styles/icons) guidelines for icon design.- In the `[project]/android/app/src/main/res/` directory, place your icon files in folders named using [configuration qualifiers](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources). The default `mipmap-` folders demonstrate the correct naming convention.- In `AndroidManifest.xml`, update the [`application`](https://developer.android.com/guide/topics/manifest/application-element) tag's `android:icon` attribute to reference icons from the previous step (for example, `<application android:icon="@mipmap/ic_launcher" ...`).- To verify that the icon has been replaced, run your app and inspect the app icon in the Launcher.

Enable Material Components
--------------------------

[#](#enable-material-components)

If your app uses [platform views](/platform-integration/android/platform-views), you might want to enable Material Components by following the steps described in the [Getting Started guide for Android](https://m3.material.io/develop/android/mdc-android).

For example:

1. Add the dependency on Android's Material in `<my-app>/android/app/build.gradle.kts`:

   groovy

   ```
   dependencies {
       // ...
       implementation("com.google.android.material:material:<version>")
       // ...
   }
   ```

   To find out the latest version, visit [Google Maven](https://maven.google.com/web/index.html#com.google.android.material:material).- Set the light theme in `<my-app>/android/app/src/main/res/values/styles.xml`:

     xml

     ```
     <style name="NormalTheme" parent="@android:style/Theme.Light.NoTitleBar">
     <style name="NormalTheme" parent="Theme.MaterialComponents.Light.NoActionBar">
     ```

     - Set the dark theme in `<my-app>/android/app/src/main/res/values-night/styles.xml`:

       xml

       ```
       <style name="NormalTheme" parent="@android:style/Theme.Black.NoTitleBar">
       <style name="NormalTheme" parent="Theme.MaterialComponents.DayNight.NoActionBar">
       ```

Sign the app
------------

[#](#sign-the-app)

To publish on the Play Store, you need to sign your app with a digital certificate.

Android uses two signing keys: *upload* and *app signing*.

* Developers upload an `.aab` or `.apk` file signed with an *upload key* to the Play Store.* The end-users download the `.apk` file signed with an *app signing key*.

To create your app signing key, use Play App Signing as described in the [official Play Store documentation](https://support.google.com/googleplay/android-developer/answer/7384423?hl=en).

To sign your app, use the following instructions.

### Create an upload keystore

[#](#create-an-upload-keystore)

If you have an existing keystore, skip to the next step. If not, create one using one of the following methods:

1. Follow the [Android Studio key generation steps](https://developer.android.com/studio/publish/app-signing#generate-key).- Run the following command at the command line:

     On macOS or Linux, use the following command:

     ```
     keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA \
             -keysize 2048 -validity 10000 -alias upload
     ```

     On Windows, use the following command in PowerShell:

     ```
     keytool -genkey -v -keystore $env:USERPROFILE\upload-keystore.jks `
             -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 `
             -alias upload
     ```

     This command stores the `upload-keystore.jks` file in your home directory. If you want to store it elsewhere, change the argument you pass to the `-keystore` parameter. **However, keep the `keystore` file private; don't check it into public source control!**

     *info* Note

     * The `keytool` command might not be in your path—it's part of Java, which is installed as part of Android Studio. For the concrete path, run `flutter doctor -v` and locate the path printed after 'Java binary at:'. Then use that fully qualified path replacing `java` (at the end) with `keytool`. If your path includes space-separated names, such as `Program Files`, use platform-appropriate notation for the names. For example, on macOS and Linux use `Program\ Files`, and on Windows use `"Program Files"`.* The `-storetype JKS` tag is only required for Java 9 or newer. As of the Java 9 release, the keystore type defaults to PKS12.

### Reference the keystore from the app

[#](#reference-the-keystore-from-the-app)

Create a file named `[project]/android/key.properties` that contains a reference to your keystore. Don't include the angle brackets (`< >`). They indicate that the text serves as a placeholder for your values.

properties

```
storePassword=<password-from-previous-step>
keyPassword=<password-from-previous-step>
keyAlias=upload
storeFile=<keystore-file-location>
```

The `storeFile` might be located at `/Users/<user name>/upload-keystore.jks` on macOS or `C:\\Users\\<user name>\\upload-keystore.jks` on Windows.

*info* Note

The Windows path to `keystore.jks` must be specified with double backslashes: `\\`.

*warning* Warning

Keep the `key.properties` file private; don't check it into public source control.

### Configure signing in Gradle

[#](#configure-signing-in-gradle)

When building your app in release mode, configure Gradle to use your upload key. To configure Gradle, edit the `<project>/android/app/build.gradle.kts` file.

1. Define and load the keystore properties file before the `android` property block.- Set the `keystoreProperties` object to load the `key.properties` file.

     [project]/android/app/build.gradle.kts

     kotlin

     ```
     import java.util.Properties
     import java.io.FileInputStream

     plugins {
        ...
     }

     val keystoreProperties = Properties()
     val keystorePropertiesFile = rootProject.file("key.properties")
     if (keystorePropertiesFile.exists()) {
         keystoreProperties.load(FileInputStream(keystorePropertiesFile))
     }

     android {
        ...
     }
     ```

     - Add the signing configuration before the `buildTypes` property block inside the `android` property block.

       [project]/android/app/build.gradle.kts

       kotlin

       ```
       android {
           // ...

           signingConfigs {
               create("release") {
                   keyAlias = keystoreProperties["keyAlias"] as String
                   keyPassword = keystoreProperties["keyPassword"] as String
                   storeFile = keystoreProperties["storeFile"]?.let { file(it) }
                   storePassword = keystoreProperties["storePassword"] as String
               }
           }
           buildTypes {
               release {
                   // TODO: Add your own signing config for the release build.
                   // Signing with the debug keys for now,
                   // so `flutter run --release` works.
                   signingConfig = signingConfigs.getByName("debug")
                   signingConfig = signingConfigs.getByName("release")
               }
           }
       ...
       }
       ```

Flutter now signs all release builds.

*info* Note

You might need to run `flutter clean` after changing the Gradle file. This prevents cached builds from affecting the signing process.

To learn more about signing your app, check out [Sign your app](https://developer.android.com/studio/publish/app-signing.html#generate-key) on the Android developer docs.

Shrink your code with R8
------------------------

[#](#shrink-your-code-with-r8)

[R8](https://developer.android.com/studio/build/shrink-code) is the new code shrinker from Google. It's enabled by default when you build a release APK or AAB. To disable R8, pass the `--no-shrink` flag to `flutter build apk` or `flutter build appbundle`.

*info* Note

Obfuscation and minification can considerably extend the compile time of an Android application.

The `--[no-]shrink` flag has no effect. Code shrinking is always enabled in release builds. To learn more, check out [Shrink, obfuscate, and optimize your app](https://developer.android.com/studio/build/shrink-code).

Enable multidex support
-----------------------

[#](#enable-multidex-support)

When writing large apps or making use of large plugins, you might encounter Android's dex limit of 64k methods when targeting a minimum API of 20 or below. This might also be encountered when running debug versions of your app using `flutter run` that doesn't have shrinking enabled.

Flutter tool supports easily enabling multidex. The simplest way is to opt into multidex support when prompted. The tool detects multidex build errors and asks before making changes to your Android project. Opting in allows Flutter to automatically depend on `androidx.multidex:multidex` and use a generated `FlutterMultiDexApplication` as the project's application.

When you try to build and run your app with the **Run** and **Debug** options in your IDE, your build might fail with the following message:

![Build failure because Multidex support is required](/assets/images/docs/deployment/android/ide-build-failure-multidex.png)

To enable multidex from the command line, run `flutter run --debug` and select an Android-powered device:

![Selecting an Android device with the flutter CLI.](/assets/images/docs/deployment/android/cli-select-device.png)

When prompted, enter `y`. The Flutter tool enables multidex support and retries the build:

![The output of a successful build after adding multidex.](/assets/images/docs/deployment/android/cli-multidex-added-build.png)

*info* Note

Multidex support is natively included when targeting Android SDK 21 or later.

You might also choose to manually support multidex by following Android's guides and modifying your project's Android directory configuration. A [multidex keep file](https://developer.android.com/studio/build/multidex#keep) must be specified to include:

```
io/flutter/embedding/engine/loader/FlutterLoader.class
io/flutter/util/PathUtils.class
```

Also, include any other classes used in app startup. For more detailed guidance on adding multidex support manually, check out the official [Android documentation](https://developer.android.com/studio/build/multidex).

Review the app manifest
-----------------------

[#](#review-the-app-manifest)

Review the default [App Manifest](https://developer.android.com/guide/topics/manifest/manifest-intro) file.

[project]/android/app/src/main/AndroidManifest.xml

xml

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application
        android:label="[project]"
        ...
    </application>
    ...
    <uses-permission android:name="android.permission.INTERNET"/>
</manifest>
```

Verify the following values:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tag Attribute Value|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [`application`](https://developer.android.com/guide/topics/manifest/application-element) Edit the `android:label` in the [`application`](https://developer.android.com/guide/topics/manifest/application-element) tag to reflect the final name of the app. |  |  |  | | --- | --- | --- | | [`uses-permission`](https://developer.android.com/guide/topics/manifest/uses-permission-element) Add the `android.permission.INTERNET` [permission](https://developer.android.com/guide/topics/manifest/uses-permission-element) value to the `android:name` attribute if your app needs Internet access. The standard template doesn't include this tag but allows Internet access during development to enable communication between Flutter tools and a running app.  | | | | | | | | |

Review or change the Gradle build configuration
-----------------------------------------------

[#](#review-the-gradle-build-configuration)

To verify the Android build configuration, review the `android` block in the default [Gradle build script](https://developer.android.com/studio/build/#module-level). The default Gradle build script is found at `[project]/android/app/build.gradle.kts`. You can change the values of any of these properties.

[project]/android/app/build.gradle.kts

kotlin

```
android {
    namespace = "com.example.[project]"
    // Any value starting with "flutter." gets its value from
    // the Flutter Gradle plugin.
    // To change from these defaults, make your changes in this file.
    compileSdk = flutter.compileSdkVersion
    ndkVersion = flutter.ndkVersion

    ...

    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId = "com.example.[project]"
        // You can update the following values to match your application needs.
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        // These two properties use values defined elsewhere in this file.
        // You can set these values in the property declaration
        // or use a variable.
        versionCode = flutterVersionCode.toInteger()
        versionName = flutterVersionName
    }

    buildTypes {
        ...
    }
}
```

### Properties to adjust in build.gradle.kts

[#](#properties-to-adjust-in-build-gradle-kts)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Property Purpose Default Value|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `compileSdk` The Android API level against which your app is compiled. This should be the highest version available. If you set this property to `31`, you run your app on a device running API `30` or earlier as long as your app makes uses no APIs specific to `31`. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `defaultConfig` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `.applicationId` The final, unique [application ID](https://developer.android.com/studio/build/application-id) that identifies your app. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `.minSdk` The [minimum Android API level](https://developer.android.com/studio/publish/versioning#minsdk) for which you designed your app to run. `flutter.minSdkVersion`| `.targetSdk` The Android API level against which you tested your app to run. Your app should run on all Android API levels up to this one. `flutter.targetSdkVersion`| `.versionCode` A positive integer that sets an [internal version number](https://developer.android.com/studio/publish/versioning). This number only determines which version is more recent than another. Greater numbers indicate more recent versions. App users never see this value. |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `.versionName` A string that your app displays as its version number. Set this property as a raw string or as a reference to a string resource. |  |  |  | | --- | --- | --- | | `.buildToolsVersion` The Gradle plugin specifies the default version of the Android build tools that your project uses. To specify a different version of the build tools, change this value.  | | | | | | | | | | | | | | | | | | | | | | | | | | |

To learn more about Gradle, check out the module-level build section in the [Gradle build file](https://developer.android.com/studio/build/#module-level).

*info* Note

If you use a recent version of the Android SDK, you might get deprecation warnings about `compileSdkVersion`, `minSdkVersion`, or `targetSdkVersion`. You can rename these properties to `compileSdk`, `minSdk`, and `targetSdk` respectively.

Build the app for release
-------------------------

[#](#build-the-app-for-release)

You have two possible release formats when publishing to the Play Store.

* App bundle (preferred)* APK

*info* Note

The Google Play Store prefers the app bundle format. To learn more, check out [About Android App Bundles](https://developer.android.com/guide/app-bundle).

### Build an app bundle

[#](#build-an-app-bundle)

This section describes how to build a release app bundle. If you completed the signing steps, the app bundle will be signed. At this point, you might consider [obfuscating your Dart code](/deployment/obfuscate) to make it more difficult to reverse engineer. Obfuscating your code involves adding flags to your build command and maintaining additional files to de-obfuscate stack traces.

From the command line:

1. Enter `cd [project]`  
   - Run `flutter build appbundle`  
      (Running `flutter build` defaults to a release build.)

The release bundle for your app is created at `[project]/build/app/outputs/bundle/release/app.aab`.

By default, the app bundle contains your Dart code and the Flutter runtime compiled for [armeabi-v7a](https://developer.android.com/ndk/guides/abis#v7a) (ARM 32-bit), [arm64-v8a](https://developer.android.com/ndk/guides/abis#arm64-v8a) (ARM 64-bit), and [x86-64](https://developer.android.com/ndk/guides/abis#86-64) (x86 64-bit).

### Test the app bundle

[#](#test-the-app-bundle)

An app bundle can be tested in multiple ways. This section describes two.

#### Offline using the bundle tool

[#](#offline-using-the-bundle-tool)

1. If you haven't done so already, download `bundletool` from its [GitHub repository](https://github.com/google/bundletool/releases/latest).- [Generate a set of APKs](https://developer.android.com/studio/command-line/bundletool#generate_apks) from your app bundle.- [Deploy the APKs](https://developer.android.com/studio/command-line/bundletool#deploy_with_bundletool) to connected devices.

#### Online using Google Play

[#](#online-using-google-play)

1. Upload your bundle to Google Play to test it. You can use the internal test track, or the alpha or beta channels to test the bundle before releasing it in production.- Follow the steps to [upload your bundle](https://developer.android.com/studio/publish/upload-bundle) to the Play Store.

### Build an APK

[#](#build-an-apk)

Although app bundles are preferred over APKs, there are stores that don't yet support app bundles. In this case, build a release APK for each target ABI (Application Binary Interface).

If you completed the signing steps, the APK will be signed. At this point, you might consider [obfuscating your Dart code](/deployment/obfuscate) to make it more difficult to reverse engineer. Obfuscating your code involves adding flags to your build command.

From the command line:

1. Enter `cd [project]`.- Run `flutter build apk --split-per-abi`. (The `flutter build` command defaults to `--release`.)

This command results in three APK files:

* `[project]/build/app/outputs/apk/release/app-armeabi-v7a-release.apk`* `[project]/build/app/outputs/apk/release/app-arm64-v8a-release.apk`* `[project]/build/app/outputs/apk/release/app-x86_64-release.apk`

Removing the `--split-per-abi` flag results in a fat APK that contains your code compiled for *all* the target ABIs. Such APKs are larger in size than their split counterparts, causing the user to download native binaries that aren't applicable to their device's architecture.

### Install an APK on a device

[#](#install-an-apk-on-a-device)

Follow these steps to install the APK on a connected Android-powered device.

From the command line:

1. Connect your Android-powered device to your computer with a USB cable.- Enter `cd [project]`.- Run `flutter install`.

Publish to the Google Play Store
--------------------------------

[#](#publish-to-the-google-play-store)

For detailed instructions on publishing your app to the Google Play Store, check out the [Google Play launch](https://developer.android.com/distribute) documentation.

Update the app's version number
-------------------------------

[#](#update-the-apps-version-number)

The default version number of the app is `1.0.0`. To update it, navigate to the `pubspec.yaml` file and update the following line:

yaml

```
version: 1.0.0+1
```

The version number is three numbers separated by dots, such as `1.0.0` in the preceding example, followed by an optional build number, such as `1` in the preceding example, separated by a `+`.

Both the version and the build number can be overridden in Flutter's build by specifying `--build-name` and `--build-number`, respectively.

In Android, `build-name` is used as `versionName` while `build-number` used as `versionCode`. For more information, check out [Version your app](https://developer.android.com/studio/publish/versioning) in the Android documentation.

When you rebuild the app for Android, any updates in the version number from the pubspec file will update the `versionName` and `versionCode`in the `local.properties` file.

Android release FAQ
-------------------

[#](#android-release-faq)

Here are some commonly asked questions about deployment for Android apps.

### When should I build app bundles versus APKs?

[#](#when-should-i-build-app-bundles-versus-apks)

The Google Play Store recommends that you deploy app bundles over APKs because they allow a more efficient delivery of the application to your users. However, if you're distributing your application by means other than the Play Store, an APK might be your only option.

### What is a fat APK?

[#](#what-is-a-fat-apk)

A [fat APK](https://en.wikipedia.org/wiki/Fat_binary) is a single APK that contains binaries for multiple ABIs embedded within it. This has the benefit that the single APK runs on multiple architectures and thus has wider compatibility, but it has the drawback that its file size is much larger, causing users to download and store more bytes when installing your application. When building APKs instead of app bundles, it is strongly recommended to build split APKs, as described in [build an APK](#build-an-apk) using the `--split-per-abi` flag.

### What are the supported target architectures?

[#](#what-are-the-supported-target-architectures)

When building your application in release mode, Flutter apps can be compiled for [armeabi-v7a](https://developer.android.com/ndk/guides/abis#v7a) (ARM 32-bit), [arm64-v8a](https://developer.android.com/ndk/guides/abis#arm64-v8a) (ARM 64-bit), and [x86-64](https://developer.android.com/ndk/guides/abis#86-64) (x86 64-bit).

### How do I sign the app bundle created by `flutter build appbundle`?

[#](#how-do-i-sign-the-app-bundle-created-by-flutter-build-appbundle)

Check out [Sign the app](#sign-the-app).

### How do I build a release from within Android Studio?

[#](#how-do-i-build-a-release-from-within-android-studio)

In Android Studio, open the existing `android/` folder under your app's folder. Then, select **build.gradle (Module: app)** in the project panel:

![The Gradle build script menu in Android Studio.](/assets/images/docs/deployment/android/gradle-script-menu.png)

Next, select the build variant. Click **Build > Select Build Variant** in the main menu. Select any of the variants in the **Build Variants** panel (debug is the default):

![The build variant menu in Android Studio with Release selected.](/assets/images/docs/deployment/android/build-variant-menu.png)

The resulting app bundle or APK files are located in `build/app/outputs` within your app's folder.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/android/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/android.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/android/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/android.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/deployment/android.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/android/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/android.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   