Archive of What's new
=====================

1. [Stay up to date](/release) chevron\_right- [Archive of What's new](/release/archive-whats-new)

This page contains archived announcements of what's new on the Flutter website and blog. For information on the latest releases, check out the [current what's new](/release/whats-new) page.

12 February 2025: 3.29 release
------------------------------

[#](#12-february-2025-3-29-release)

Flutter 3.29 is live! For more information, check out the [Flutter 3.29 technical blog post](https://medium.com/flutter/whats-new-in-flutter-3-29-f90c380c2317). You might also check out the [Dart 3.7 release](https://medium.com/dartlang/announcing-dart-3-7-bf864a1b195c) blog post.

**Docs updated or added since the 3.27 release**

* As Flutter evolves, so do its internals. The [Architectural overview page](/resources/architectural-overview) is updated.* For those of you coming from Android development who are familiar with Jetpack Compose, please visit [Flutter for Jetpack Compose devs](/get-started/flutter-for/compose-devs).* A new cookbook recipe is added for testing a widget's orientation, [Test orientation](/cookbook/testing/widget/orientation).* Also, don't forget to check out the [breaking changes](/release/breaking-changes#released-in-flutter-3-29) page for this release. That's also where you'll find useful migration info.

---

11 December 2024: 3.27 release
------------------------------

[#](#11-december-2024-3-27-release)

Flutter 3.27 is live! For more information, check out the [Flutter 3.27 umbrella blog post](https://medium.com/flutter/flutter-in-production-f9418261d8e1) and the [Flutter 3.27 technical blog post](https://medium.com/flutter/whats-new-in-flutter-3-27-28341129570c). You might also check out the [Dart 3.6 release](https://medium.com/dartlang/announcing-dart-3-6-778dd7a80983) blog post.

**Docs updated or added since the 3.24 release**

This website release includes several important updates!

* The Flutter AI Toolkit is launched! You'll find the docs on the website in the side navigation menu under **App solutions > AI** and at [Flutter AI Toolkit](/ai-toolkit).* For a long time now, we have been asked to create more guidance for developers who write large-scale, complex Flutter apps. Well, that work has begun: introducing [Architecting Flutter apps](/app-architecture)! This section includes eight new pages about architecting Flutter apps, including a [Design patterns](/app-architecture/design-patterns) page that has six recipes for common design patterns that you might find useful.* We've added more information about [Support for WebAssembly (Wasm)](/platform-integration/web/wasm).* We've also reworked the [Web renderers](/platform-integration/web/renderers) page to cover the two build modes for web and its two renderers.* Impeller is now the default rendering engine for iOS and Android. We've also added a link from the Impeller page to the detailed [Can I use Impeller?](https://flutter.dev/go/can-i-use-impeller) page.* For developers interested in monetization, we have introduced a new [Interactive Media Ads](https://pub.dev/packages/interactive_media_ads) package. You can find it through the website in the side navigation menu under **App solutions > Monetization > Advertising**. Also, check out the [Video & web app support in Flutter](https://medium.com/flutter/video-web-ad-support-in-flutter-f50e5a3480a8) blog post.* We have new docs for using Flutter with Android, specifically, [Launching a Jetpack Compose activity from your Flutter application](/platform-integration/android/compose-activity) and [Calling JetPack APIs](/platform-integration/android/call-jetpack-apis).* Work continues on the [Learn the fundamentals](/get-started/fundamentals) pages (formerly called the First Week Experience). Besides updates to several pages, check out the new [Intro to Dart](/get-started/fundamentals/dart) page.* Further support and updated docs for the Swift Package Manager. Specifically, you can now build on the stable channel for SPM, however, plugins will continue to be installed using CocoaPods as the SwiftPM feature remains unavailable on the stable channel: [Swift Package Manager for plugin authors](/packages-and-plugins/swift-package-manager/for-plugin-authors) and [Swift Package Manager for app authors](/packages-and-plugins/swift-package-manager/for-app-developers).* The [Deep linking validator tool](/tools/devtools/deep-links), part of DevTools, now works for both iOS and Android.* Also, don't forget to check out the [breaking changes](/release/breaking-changes#released-in-flutter-3-27) page for this release. That's also where you'll find useful migration info.

---

07 August 2024: I/O Connect Beijing 3.24 release
------------------------------------------------

[#](#07-august-2024-io-connect-beijing-3-24-release)

Flutter 3.24 is live! For more information, check out the [Flutter 3.24 umbrella blog post](https://blog.flutter.dev/flutter-3-24-dart-3-5-204b7d20c45d) and the [Flutter 3.24 technical blog post](https://blog.flutter.dev/whats-new-in-flutter-3-24-6c040f87d1e4). You might also check out the [Dart 3.5 release](https://medium.com/dartlang/dart-3-5-6ca36259fa2f) blog post.

**Docs updated or added since the 3.22 release**

This website release includes several important updates!

* An updated widget catalog:
  + Added 37 missing widgets to the [Cupertino catalog](/ui/widgets/cupertino), and a new screenshot for the updated `CupertinoActionSheet` widget.+ Added the new [`CarouselView`](https://api.flutter.dev/flutter/material/CarouselView-class.html) widget.+ `CupertinoButton` and `CupertinoTextField` also have updated behaviors.* New guides on adding support for Swift Package Manager to [iOS plugins](/packages-and-plugins/swift-package-manager/for-plugin-authors) and [iOS apps](/packages-and-plugins/swift-package-manager/for-app-developers). (Note that, until all of your app's dependencies are migrated, Flutter will continue to use CocoaPods.)* Updated web docs:
      + [Embedding Flutter on the web](/platform-integration/web/embedding-flutter-web), including how to enable multi-view mode+ [Embedding web content into a Flutter app](/platform-integration/web/web-content-in-flutter)* Update for Android 14: If you are using an Android device that runs on Android 14, you can now support Android's [predictive back gesture](/platform-integration/android/predictive-back).* Updates for iOS 18: The iOS 18 release is in beta at the time of this release. These iOS 18 features are already enabled in Flutter and are now mentioned in the docs:
          + Use an [iOS app extension](/platform-integration/ios/app-extensions) in your Flutter app to create a custom toggle. Your users can then add your app's toggle when customizing their Control Center.+ [Tinted app icons](/deployment/ios#add-an-app-icon) are supported* Two pages of the [Flutter fundamentals docs](/get-started/fundamentals) are updated:
            + [Widgets](/get-started/fundamentals/widgets)+ [Layout](/get-started/fundamentals/layout) We hope these pages are helpful for new Flutter developers.* DevTools also has updates. Check out the release notes for [DevTools 2.35.0](/tools/devtools/release-notes/release-notes-2.35.0), [DevTools 2.36.0](/tools/devtools/release-notes/release-notes-2.36.0), and [DevTools 2.37.2](/tools/devtools/release-notes/release-notes-2.37.2).

**Other**

* If you are interested in the new, experimental Flutter GPU API, check out the [Flutter GPU blog post](https://blog.flutter.dev/getting-started-with-flutter-gpu-f33d497b7c11).* The Flutter wiki has been divided up and moved into the relevant GitHub repos, making it easier to keep that info up to date.

---

14 May 2024: Google I/O 3.22 release
------------------------------------

[#](#14-may-2024-google-io-3-22-release)

Flutter 3.22 is live! For more information, check out the [Flutter 3.22 umbrella blog post](https://blog.flutter.dev/io24-5e211f708a37) and the [Flutter 3.22 technical blog post](https://blog.flutter.dev/whats-new-in-flutter-3-22-fbde6c164fe3).

You might also check out the [Dart 3.4 release](https://medium.com/dartlang/dart-3-4-bd8d23b4462a) blog post. In particular, Dart now provides a "baked in" language macro, `JsonCodable`, for serializing and deserializing JSON data. A future (and unspecified) Dart release will allow you to create your own macros. To learn more, check out [dart.dev/go/macros](http://dart.dev/go/macros).

**Docs updated or added since the 3.19 release**

* A new 7-page section on [Adaptive and Responsive design](/ui/adaptive-responsive). (This replaces our previous, somewhat scattered, documentation on this subject.)* For new-ish Flutter developer who has worked through the first Flutter codelab, we've added some "what's next" advice on how to move beyond that initial step. Check out the [Flutter fundamentals docs](/get-started/fundamentals).* Our [Flutter install](/get-started) docs have been revamped.* We have three new codelabs and a new guide for the Games Toolkit. To see the list of additions, check out the updated [Casual Games Toolkit](/resources/games-toolkit) page.* Flutter support for Web Assembly (Wasm) has now reached stable. To learn more, check out the updated [Support for WebAssembly (Wasm)](/platform-integration/web/wasm) page.* DevTools has a new screen for evaluating deep links on Android. To learn more, check out the new page, [Validate deep links](/tools/devtools/deep-links).* We have a new page that describes web bootstrapping for Flutter SDK release 3.22 and later. Check out [Flutter web app initialization](/platform-integration/web/initialization).* You can now provide code to transform your assets into another format at runtime. To learn more, check out [Transforming assets at build time](/ui/assets/asset-transformation).

**Website infrastructure**

* If you contribute to the website, you might have noticed some recent changes. Namely, the website infrastructure has been updated and the new workflow is simpler. For more details, check out the [website README](https://github.com/flutter/website/?tab=readme-ov-file#flutter-documentation-website).* You might also have noticed that the **App solutions** submenu in the sidenav now has an **AI** section, and an enhanced **Monetization** section, to name some of the changes.

15 February 2024: Valentine's-Day-adjacent 3.19 release
-------------------------------------------------------

[#](#15-february-2024-valentines-day-adjacent-3-19-release)

Flutter 3.19 is live! For more information, check out the [Flutter 3.19 umbrella blog post](https://blog.flutter.dev/starting-2024-strong-with-flutter-and-dart-cae9845264fe) and the [Flutter 3.19 technical blog post](https://blog.flutter.dev/whats-new-in-flutter-3-19-58b1aae242d2).

You might also check out the [Dart 3.3 release](https://medium.com/dartlang/new-in-dart-3-3-extension-types-javascript-interop-and-more-325bf2bf6c13) blog post.

**Docs updated or added since the 3.16 release**

* A new page on [migrating from Material 2 to Material 3](/release/breaking-changes/material-3-migration) is added. Thanks to [@TahaTesser](https://github.com/TahaTesser) for writing this guide.* Material 3 uses theming in new and different ways than Material 2. The [Use themes to share colors and font styles](/cookbook/design/themes) cookbook recipe is updated to reflect these changes.* The [Flutter install](/get-started) pages have been updated. Please [let us know](https://github.com/flutter/website/issues/new/choose) if you have any feedback.* The [Concurrency and isolates](/perf/isolates) page has been reworked.

**Other updates**

* Check out the just-published [Flutter and Dart 2024 Roadmap](https://github.com/flutter/flutter/blob/main/docs/roadmap/Roadmap.md).* Check out [Harness the Gemini API in your Dart and Flutter apps](https://blog.flutter.dev/harness-the-gemini-api-in-your-dart-and-flutter-apps-00573e560381).

15 November 2023: 3.16 release
------------------------------

[#](#15-november-2023-3-16-release)

Flutter 3.16 is live! For more information, check out the [Flutter 3.16 blog post](https://blog.flutter.dev/flutter-3-16-dart-3-2-high-level-umbrella-post-b9218b17f0f7) and the technical [What's new in Flutter 3.16](https://blog.flutter.dev/whats-new-in-flutter-3-16-dba6cb1015d1) blog post.

You might also check out [Dart 3.2 release](https://medium.com/dartlang/dart-3-2-c8de8fe1b91f).

**Docs updated or added since the 3.13 release**

* As of this release, the **default theme for Material Flutter apps is Material 3**. Unless you explicitly specify Material 2 (with `useMaterial3: false`) in your app's theme, your app *will* look different once you've updated.* While the Flutter Casual Games Toolkit isn't technically *part* of the 3.16 release, we've release a significant update of the toolkit *alongside* the 3.16 release. This update includes three completely new games code templates, three new games cookbook recipes, and a general reorganization of our games toolkit docs. For more information, check out [Casual Games Toolkit](/resources/games-toolkit) and make sure to look at the side nav!* The Impeller runtime is now **available for Android on Vulkan devices** behind the `--enable-impeller` flag. For more information, check out the [Impeller rendering engine](/perf/impeller) page.* You can now add Apple iOS app extensions to your Flutter app when running on iOS. To learn more, check out [Adding iOS app extensions](/platform-integration/ios/app-extensions).

**Articles**

The following articles were published on the [Flutter Medium](https://medium.com/flutter) publication since Flutter 3.13:

* [How IBM is creating a Flutter Center of Excellence](https://blog.flutter.dev/how-ibm-is-creating-a-flutter-center-of-excellence-3c6a3c025441)* [Introducing the Flutter Consulting Directory](https://blog.flutter.dev/introducing-the-flutter-consulting-directory-f6fc4c1d2ba3)* [Developing Flutter apps for large screens](https://blog.flutter.dev/developing-flutter-apps-for-large-screens-53b7b0e17f10)* [Dart & Flutter DevTools Extensions](https://blog.flutter.dev/dart-flutter-devtools-extensions-c8bc1aaf8e5f)* [Building your next casual game with Flutter](https://blog.flutter.dev/building-your-next-casual-game-with-flutter-716ef457e440)

16 August 2023: 3.13 release
----------------------------

[#](#16-august-2023-3-13-release)

Flutter 3.13 is live! For more information, check out the [Flutter 3.13 blog post](https://blog.flutter.dev/whats-new-in-flutter-3-13-479d9b11df4d).

You might also check out [Dart 3.1 & a retrospective on functional style programming in Dart 3](https://medium.com/dartlang/dart-3-1-a-retrospective-on-functional-style-programming-in-dart-3-a1f4b3a7cdda).

In addition to new docs since the last release, we have been incrementally releasing a revamped version of the docs.flutter.dev website. Specifically, we have reorganized (flattened) the information architecture (IA) and have incorporated some of our most popular cookbook recipes into the sidenav. [Let us know what you think!](https://github.com/flutter/website/issues)

**Docs updated or added since the 3.10 release**

* A rewrite and rename that completes the [Use a native language debugger](/testing/native-debugging?tab=from-vscode-to-xcode-ios) page. This page covers how to connect both a native debugger and a Dart debugger to your app for Android *and* iOS. (The previous version of this page was out of date and didn't cover iOS.)* A new [Layout/Scrolling](/ui/layout/scrolling) overview page. (In fact, scrolling is also a new section of the IA.)* We have sunsetted the Happy Paths recommendations in favor of the [Flutter Favorites program](/packages-and-plugins/favorites). Look for additions to Flutter Favorites very soon!* The Impeller runtime is now available for macOS behind a flag. For more information, check out the [Impeller rendering engine](/perf/impeller) page.* As always, this release includes a few [breaking changes](/release/breaking-changes). The following links have more information, including info on how to migrate to the new APIs:
          + [Removing the `ignoreSemantics` property from `IgnorePointer`, `AbsorbPointer`, and `SliverIgnorePointer`](/release/breaking-changes/ignoringsemantics-migration)+ [The `Editable.onCaretChanged` callback is removed](/release/breaking-changes/editable-text-scroll-into-view)+ Also check out the [deprecated APIs since 3.10](/release/breaking-changes/3-10-deprecations)

**Codelabs and workshops**

The following codelab has been published since Flutter 3.10:

* [Adding a Home Screen widget to your Flutter app](https://codelabs.developers.google.com/flutter-home-screen-widgets)

**Articles**

The following articles were published on the [Flutter Medium](https://medium.com/flutter) publication since Flutter 3.10:

* [The Future of iOS development with Flutter](https://blog.flutter.dev/the-future-of-ios-development-with-flutter-833aa9779fac)* [How it's made: I/O Flip](https://blog.flutter.dev/how-its-made-i-o-flip-da9d8184ef57)* [Flutter 2023 Q1 survey results](https://blog.flutter.dev/flutter-2023-q1-survey-api-breaking-changes-deep-linking-and-more-7ff692f974e0)

**What's coming**

Things that are coming soon-ish to a stable release:

**Material 3**

You've probably heard by now that [Material 3](https://m3.material.io) is coming. It's been available on Flutter for some time now, by setting `useMaterial3: true` in your code. By the next stable release in Q4, Material 3 will be enabled by default. Now would be a good time to start migrating your code. Most all of the example code on this website has been updated to use Material 3.

For more information, check out the following resources:

* [Flutter 3.13 blog post](https://blog.flutter.dev/whats-new-in-flutter-3-13-479d9b11df4d#4c90)* [Material Design for Flutter](/ui/design/material) page

**Impeller for Android**

Progress continues on Impeller for Android. For more information, check out the [Flutter 3.13 blog post](https://blog.flutter.dev/whats-new-in-flutter-3-13-479d9b11df4d#a7be).

**New scrolling APIs**

We have been working on updating our scrolling APIs. The rework will eventually result in 2D scrolling support for trees and tables, even diagonal scrolling! Flutter 3.13 also provides new Sliver classes for fancy scrolling. For more information, check out the [Flutter 3.13 blog post](https://blog.flutter.dev/whats-new-in-flutter-3-13-479d9b11df4d#02dc).

**Updates to the Games toolkit**

We are working on updates to the Flutter Games toolkit, including the sample code, additional docs, and a new video. The Games toolkit is developed independently of the Flutter SDK, so stay tuned for updates as they are ready. For more information, check out the [Flutter 3.13 blog post](https://blog.flutter.dev/whats-new-in-flutter-3-13-479d9b11df4d#30b2).

---

10 May 2023: Google I/O 2023: 3.10 release
------------------------------------------

[#](#10-may-2023-google-io-2023-3-10-release)

Flutter 3.10 is live! This release contains many updates and improvements. This page lists the documentation changes, but you can also check out the [3.10 blog post](https://blog.flutter.dev/whats-new-in-flutter-3-10-b21db2c38c73) and the [3.10 release notes](/release/release-notes/release-notes-3.10.0).

You might also check out [Introducing Dart 3](https://medium.com/dartlang/announcing-dart-3-53f065a10635).

**Docs updated or added since the 3.7 release**

* Added section on [wireless debugging](/add-to-app/debugging) for iOS or Android to the add-to-app module guide. You can debug your iOS or Android app on a physical device over Wi-Fi.* Updated the [Material Widget Catalog](/ui/widgets/material) to cover Material 3.* Added the new [canvasKitVariant runtime configuration](/platform-integration/web/initialization) setting. This web initialization option lets you configure which version of CanvasKit to download.* Updated the [Impeller](/perf/impeller) reference. iOS apps now default to the Impeller renderer.* Added the [Android Java Gradle migration](/release/breaking-changes/android-java-gradle-migration-guide) guide on resolving an incompatibility between Java 17 and Gradle releases prior to 7.3.* Updated the [DevTools](/tools/devtools) reference material.* Updated the [WebAssembly support](/platform-integration/web/wasm) reference with guidelines on trying out preview support.* Added guide on [adding iOS app extensions](/platform-integration/ios/app-extensions) to Flutter apps. This release enables using native iOS app extensions with your Flutter apps.* Added guide on [testing Flutter plugins](/testing/testing-plugins).* Added guide on [fonts and typography](/ui/design/text/typography).* Added guide on restoring state on [Android](/platform-integration/android/restore-state-android) and [iOS](/platform-integration/ios/restore-state-ios) Flutter apps.* Added a section about [sharing iOS and macOS plugin implementations](/packages-and-plugins/developing-packages#shared-ios-and-macos-implementations).* Added a guide on adapting the Material [top app bar and navigation bar](/platform-integration/platform-adaptations#top-app-bar-and-navigation-bar), and [bottom navigation bar](/platform-integration/platform-adaptations#bottom-navigation-bars) widgets to the current platform as a start of UI component platform adaptation guidelines.* Introduced the [Anatomy of an app](/resources/architectural-overview#anatomy-of-an-app) section in the Architectural overview.* Added provenance information per SLSA to all downloads in the [SDK archive page](/install/archive). Provenance guarantees that the built artifact comes from the expected source.

**Codelabs**

The following codelabs have been published since Flutter 3.7:

* [Records and Patterns in Dart 3](https://codelabs.developers.google.com/codelabs/dart-patterns-records)  
   Discover Dart 3's new records and patterns features. Learn how you can use them in a Flutter app to help you write more readable and maintainable Dart code.* [Building next generation UIs in Flutter](https://codelabs.developers.google.com/codelabs/flutter-next-gen-uis#0)  
     Learn how to build a Flutter app that uses the power of `flutter_animate`, fragment shaders, and particle fields. You will craft a user interface that evokes those science fiction movies and TV shows we all love watching when we aren't coding.* [Create haikus about Google products with the PaLM API and Flutter](https://codelabs.developers.google.com/haiku-generator)  
       **NEW** Learn how to build an app that uses the PaLM API to generate haikus based on Google product names. The PaLM API gives you access to Google's state-of-the-art large language models.

**Articles**

The Flutter team published the following articles on the [Flutter Medium](https://medium.com/flutter) publication since Flutter 3.7:

* [Flutter in 2023: strategy and roadmap](https://blog.flutter.dev/flutter-in-2023-strategy-and-roadmap-60efc8d8b0c7)* [Wonderous nominated for Webby Award](https://blog.flutter.dev/wonderous-nominated-for-webby-award-8e00e2a648c2)

25 Jan 2023: Flutter Forward: 3.7 release
-----------------------------------------

[#](#25-jan-2023-flutter-forward-3-7-release)

Flutter 3.7 is live! This release contains many updates and improvements. This page lists the documentation changes, but you can also check out the [3.7 blog post](https://blog.flutter.dev/whats-new-in-flutter-3-7-38cbea71133c) and the [3.7 release notes](/release/release-notes/release-notes-3.7.0).

You might also check out [What's next for Flutter](https://blog.flutter.dev/whats-next-for-flutter-b94ce089f49c) and [Introducing Dart 3 alpha](https://medium.com/dartlang/dart-3-alpha-f1458fb9d232).

**Docs updated or added since the 3.3 release**

* You can now pass configuration information to the engine in the `initializeEngine` method. For more information, check out [Customizing web app initialization](/platform-integration/web/initialization).* [Creating Flavors for Flutter](/deployment/flavors) Learn how to create a flavor in Flutter (also known as a *build configuration* in iOS).* Internationalization support has been revamped and the [Internationalizing Flutter apps](/ui/accessibility-and-internationalization/internationalization) page is updated.* The DevTools memory debugging tool has been completely overhauled and the corresponding page, [Using the memory view](/tools/devtools/memory), is rewritten.* This release includes numerous improvements to Flutter's support for custom fragment shaders. For more information, see the new [Writing and using fragment shaders](/ui/design/graphics/fragment-shaders) page.* Some security tools falsely report security vulnerabilities in Flutter apps. The new [Security false positives](/reference/security-false-positives) page lists the known false positives and why you can ignore them.* You can now invoke a platform channel from any isolate, including background isolates. For more information, check out [Writing custom platform-specific code](/platform-integration/platform-channels) and the [Introducing isolate background channels](https://medium.com/flutter/introducing-background-isolate-channels-7a299609cad8) article on Medium.* We've updated our Swift documentation. New and updated pages include:
                + [Flutter for SwiftUI developers](/get-started/flutter-for/swiftui-devs) - updated+ [Add a Flutter screen to an iOS app](/add-to-app/ios/add-flutter-screen) - updated for SwiftUI+ [Flutter concurrency for Swift developers](/get-started/flutter-for/dart-swift-concurrency) - new+ [Learning Dart as a Swift developer](https://dart.dev/guides/language/coming-from/swift-to-dart) on dart.dev - new* As of Xcode 14, Apple no longer supports bitcode. Two of our pages, [Adding an iOS clip target](/platform-integration/ios/ios-app-clip) and the [Flutter FAQ](/resources/faq), are updated to reflect this fact.* For developers who enjoy living on the bleeding edge, you might want to try Flutter's future rendering engine, Impeller. Because Impeller isn't yet ready for a stable release, you can find more information on our [Flutter GitHub wiki](/perf/impeller).

**Codelabs and workshops**

We have new codelabs since the last stable release:

* [Your first Flutter app](https://codelabs.developers.google.com/codelabs/flutter-codelab-first)  
   Learn about Flutter as you build an application that generates cool-sounding names, such as "newstay", "lightstream", "mainbrake", or "graypine". The user can ask for the next name, favorite the current one, and review the list of favorited names on a separate page. The final app is responsive to different screen sizes. (Note that this codelab replaces the previous "Write your first Flutter codelab for mobile, part 1 and part 2.")* [Using FFI in a Flutter plugin](https://codelabs.developers.google.com/codelabs/flutter-ffigen)  
     Dart's FFI (foreign function interface) allows Flutter apps to use of existing native libraries that expose a C API. Dart supports FFI on Android, iOS, Windows, macOS, and Linux.* [Building a game with Flutter and Flame](https://codelabs.developers.google.com/codelabs/flutter-flame-game)  
       Learn how to build a platformer game with Flutter and Flame! In the Doodle Dash game, inspired by Doodle Jump, you play as either Dash (the Flutter mascot), or her best friend Sparky (the Firebase mascot), and try to reach as high as possible by jumping on platforms.* [Add a user authentication flow to a Flutter app using FirebaseUI](https://firebase.google.com/codelabs/firebase-auth-in-flutter-apps)  
         Learn how to add Firebase Authentication to your Flutter app using the FlutterFire UI package. You'll add both email/password and Google Sign In authorization to a Flutter app. You'll also learn how to set up a Firebase project, and use the FlutterFire CLI to initialize Firebase in your Flutter app.* [Local development for your Flutter apps using the Firebase Emulator Suite](https://firebase.google.com/codelabs/get-started-firebase-emulators-and-flutter)  
           Learn how to use the Firebase Emulator Suite with Flutter during local development, including how to use email-password authentication with the Emulator Suite, and how to read and write data to the Firestore emulator. Also, you'll import and export data from the emulators, to work with the same faked data each time you return to development.

In addition, we've updated all of our existing codelabs to support multiplatform. The [codelabs & workshops](/reference/learning-resources) page is updated to reflect the latest available codelabs.

**Articles**

We've published the following articles on the [Flutter Medium](https://medium.com/flutter) publication since the last stable release:

* [What's next for Flutter](https://blog.flutter.dev/whats-next-for-flutter-b94ce089f49c)* [Adapting Wonderous to larger device formats](https://blog.flutter.dev/adapting-wonderous-to-larger-device-formats-ac51e1c00bc0)* [What's new in Flutter 3.7](https://blog.flutter.dev/whats-new-in-flutter-3-7-38cbea71133c)* [Announcing the Flutter News Toolkit](https://blog.flutter.dev/announcing-the-flutter-news-toolkit-180a0d32c012)* [How it's made: Holobooth](https://blog.flutter.dev/how-its-made-holobooth-6473f3d018dd)* [Playful typography with Flutter](https://medium.com/flutter/playful-typography-with-flutter-f030385058b4)* [Material 3 for Flutter](https://blog.flutter.dev/material-3-for-flutter-d417a8a65564)* [Introducing background isolate channels](https://blog.flutter.dev/introducing-background-isolate-channels-7a299609cad8)* [How can we improve the Flutter experience for desktop?](https://medium.com/flutter/how-can-we-improve-the-flutter-experience-for-desktop-70b34bff9392)* [What we learned from the Flutter Q3 2022 survey](https://medium.com/flutter/what-we-learned-from-the-flutter-q3-2022-survey-9b78803accd2)* [Supporting six platforms with two keyboards](https://medium.com/flutter/what-we-learned-from-the-flutter-q3-2022-survey-9b78803accd2)* [Studying developer's usage of IDEs for Flutter development](https://medium.com/flutter/studying-developers-usage-of-ides-for-flutter-development-4c0a648a48)

31 Aug 2022: Flutter Vikings: 3.3 release
-----------------------------------------

[#](#31-aug-2022-flutter-vikings-3-3-release)

Flutter 3.3 is live! For more information, see

[What's new in Flutter 3.3](https://medium.com/flutter/whats-new-in-flutter-3-3-893c7b9af1ff), and [Dart 2.18: Objective-C & Swift interop](https://medium.com/dartlang/dart-2-18-f4b3101f146c) (free articles on Medium), and the [Flutter 3.3 release notes](/release/release-notes/release-notes-3.3.0).

**Docs updated or added since the 3.0 release**

* The [navigation and routing overview](/ui/navigation) page has been rewritten with more guidance on using `Navigator` and `Router` together, named routes, and using a routing package.* The [URL strategies](/ui/navigation/url-strategies) page has also been updated to reflect a more streamlined API.* For apps not published to the Microsoft Store, you can now set the app's executable's file and product versions in the pubspec file. For more information, see [Build and release a Windows desktop app](/deployment/windows).* If you are developing software for iOS 16 and higher, you must enable [Developer mode](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device). The macOS [install page](/get-started) is updated with this information.* As described in the [3.3 release notes](/release/release-notes/release-notes-3.3.0), you should catch all errors and exceptions in your app by setting the `PlatformDispatcher.onError` callback, instead of using a custom `Zone`. The [Handling errors in Flutter](/testing/errors) page has been updated with this advice.

11 May 2022: Google I/O 2022: Flutter 3 release
-----------------------------------------------

[#](#11-may-2022-google-io-2022-flutter-3-release)

Flutter 3 is live!!! For more information, see [Introducing Flutter 3](https://medium.com/flutter/introducing-flutter-3-5eb69151622f), [What's new in Flutter 3](https://medium.com/flutter/whats-new-in-flutter-3-8c74a5bc32d0), and [Dart 2.17: Productivity and integration](https://medium.com/dartlang/dart-2-17-b216bfc80c5d) (free articles on Medium), and the [Flutter 3 release notes](/release/release-notes/release-notes-3.0.0).

**Docs updated or added since the 2.10 release**

* We have launched the Casual Games Toolkit to help you build games with Flutter. Learn more on the [Games page](https://flutter.dev/games) and the [Games doc page](/resources/games-toolkit).* Are you struggling to level up as a Flutter developer? We have created the Happy paths project to help. Learn more on the Happy paths page. (Note, this program has been discontinued in favor of the [Flutter Favorite Program](/packages-and-plugins/favorites).)* Are you a web developer who would like more control over your app's launch process? Check out the new page, [Customizing web app initialization](/platform-integration/web/initialization), which has been added to the newly updated and collected web docs under `/platform-integration/web`.* Flutter 3 supports Apple Silicon processors. We've updated the macOS [install page](/get-started) to offer an Apple Silicon download button.* In Flutter 3, the macOS and Linux platforms have reached stable, in addition to Windows. You can now develop your app to run on any or all of these platforms. As a result, the [Desktop](/platform-integration/desktop) (and related) pages are updated.* The [Performance best practices](/perf/best-practices) page has largely been rewritten and moved to be more visible. The changes include additional advice on avoiding jank, including how to minimize layout passes caused by intrinsics, and techniques to minimize calls to `saveLayer()`.* Firebase's Flutter docs have been overhauled. Check out the newly updated [Flutter Firebase get started guide](https://firebase.google.com/docs/flutter/setup).* The [dart.dev](https://dart.dev) site has its own [what's new](https://dart.dev/guides/whats-new) page, but one new page of note is the guide, [Learning Dart as a JavaScript developer](https://dart.dev/guides/language/coming-from/js-to-dart). Stay tuned for similar articles on Swift and C#.

**Codelabs and workshops**

We have a new codelab since the last stable release:

* [Take your Flutter app from boring to beautiful](https://codelabs.developers.google.com/codelabs/flutter-boring-to-beautiful) Learn how to use features in Material 3 to make your more beautiful *and* more responsive.

Also, check out the workshops written by our GDEs and available on the [Flutter community blog](https://medium.com/@flutter_community/622b52f70173).

**Videos**

Google I/O 2022 is over, but you can still check out the Flutter-specific updates and talks from Google I/O on the [videos](/resources/videos) page.

---

03 Feb 2022: Windows Support: 2.10 release
------------------------------------------

[#](#03-feb-2022-windows-support-2-10-release)

Desktop support for Microsoft Windows (a central feature of the 2.10 release) is live! For more information, see [Announcing Flutter for Windows](https://blog.flutter.dev/announcing-flutter-for-windows-6979d0d01fed) and [What's new in Flutter 2.10](https://blog.flutter.dev/whats-new-in-flutter-2-10-5aafb0314b12), free articles on Medium.

[Watch on YouTube in a new tab: "Flutter Update: Windows"](https://www.youtube.com/watch/g-0B_Vfc9qM)

---

08 Dec 2021: 2.8 release
------------------------

[#](#08-dec-2021-2-8-release)

Flutter 2.8 is live! For details, see [Announcing Flutter 2.8](https://blog.flutter.dev/announcing-flutter-2-8-31d2cb7e19f5) and [What's new in Flutter 2.8](https://blog.flutter.dev/whats-new-in-flutter-2-8-d085b763d181).

08 Sep 2021: 2.5 release
------------------------

[#](#08-sep-2021-2-5-release)

Flutter 2.5 is live! For details, see [What's new in Flutter 2.5](https://blog.flutter.dev/whats-new-in-flutter-2-5-6f080c3f3dc).

We've made significant changes to flutter/website repo to make it easier to use and maintain. If you contribute to this repo, see the [README](https://github.com/flutter/website/#flutter-website) file for more information.

**Docs updated or added since the 2.2 release**

* A new page on [Using Actions and Shortcuts](/ui/interactivity/actions-and-shortcuts).

**Articles**

We've published the following articles on the [Flutter Medium](https://medium.com/flutter) publication since the last stable release:

* [Raster thread performance optimization tips](https://blog.flutter.dev/raster-thread-performance-optimization-tips-e949b9dbcf06)* [Writing a good code sample](https://blog.flutter.dev/writing-a-good-code-sample-323358edd9f3)* [GSoC'21: Creating a desktop sample for Flutter](https://blog.flutter.dev/gsoc-21-creating-a-desktop-sample-for-flutter-7d77e74812d6)* [Flutter Hot Reload](https://blog.flutter.dev/flutter-hot-reload-f3c5994e2cee)* [What can we do to better improve Flutter?](https://blog.flutter.dev/what-can-we-do-better-to-improve-flutter-q2-2021-user-survey-results-1037fb8f057b)* [Adding Flutter to your existing iOS and Android codebases](https://blog.flutter.dev/adding-flutter-to-your-existing-ios-and-android-codebases-3e2c5a4797c1)* [Google I/O Spotlight: Flutter in action at ByteDance](https://blog.flutter.dev/google-i-o-spotlight-flutter-in-action-at-bytedance-c22f4b6dc9ef)* [Improving Platform Channel Performance in Flutter](https://blog.flutter.dev/improving-platform-channel-performance-in-flutter-e5b4e5df04af)

---

18 May 2021: Google I/O 2021: 2.2 release
-----------------------------------------

[#](#18-may-2021-google-io-2021-2-2-release)

Flutter 2.2 is live! For details, see [Announcing Flutter 2.2](https://blog.flutter.dev/announcing-flutter-2-2-at-google-i-o-2021-92f0fcbd7ef9) and [What's New in Flutter 2.2](https://blog.flutter.dev/whats-new-in-flutter-2-2-fd00c65e2039).

We continue migrating code on the website to use null safety, but that work is not yet completed.

**Docs updated or added since the 2.0 release**

* A new page on Building adaptive apps.* A new page describing how to use [Google APIs](/data-and-backend/google-apis) with Flutter.* A new landing page for [Embedded Support for Flutter](/embedded).* A new page on setting up and using [Deferred components](/perf/deferred-components) on Android.* Significant updates to the DevTools [Memory view page](/tools/devtools/memory).* The [desktop](/platform-integration/desktop) page is updated to reflect the progress on desktop support, particularly the new support for Windows UWP.

**Codelabs**

New codelabs since the last stable release:

* [Adding in-app purchases to your Flutter app](https://codelabs.developers.google.com/codelabs/flutter-in-app-purchases)* [Build Voice Bots for Android with Dialogflow Essentials & Flutter](https://codelabs.developers.google.com/codelabs/dialogflow-flutter)* [Get to know Firebase for Flutter](https://firebase.google.com/codelabs/firebase-get-to-know-flutter#0)

**Workshops**

For Google I/O 2021, we have added a new Flutter/Dart learning tool that is based on DartPad: **Workshops!** These workshops are designed to be instructor led. The instructor-led videos are available on the Flutter and Firebase YouTube channels:

* [Building your first Flutter app](https://www.youtube.com/watch?v=Z6KZ3cTGBWw)* [Firebase for Flutter](https://www.youtube.com/watch?v=4wunbF29Kkg)* [Flutter and Dialogflow voice bots](https://www.youtube.com/watch?v=O7JfSF3CJ84)* [Inherited widgets](https://www.youtube.com/watch?v=LFcGPS6cGrY)* [Null safety](https://www.youtube.com/watch?v=HdKwuHQvArY)* [Slivers](https://www.youtube.com/watch?v=YY-_yrZdjGc)

To see the event list of "all things Flutter" at I/O, see the [Google 2021 I/O Flutter](https://events.google.com/io/program/content?4=topic_flutter) page.

You can author your own DartPad workshops! If you are interested, check out the following resources:

* [DartPad Workshop Authoring Guide](https://github.com/dart-lang/dart-pad/wiki/Workshop-Authoring-Guide)* [DartPad Sharing Guide (using a Gist file)](https://github.com/dart-lang/dart-pad/wiki/Sharing-Guide)* [Embedding DartPad in your web page](https://github.com/dart-lang/dart-pad/wiki/Embedding-Guide)

**Articles**

We've published the following articles on the [Flutter Medium](https://medium.com/flutter) publication since the last stable release:

* [How It's Made: I/O Photo Booth](https://blog.flutter.dev/how-its-made-i-o-photo-booth-3b8355d35883)* [Which factors affected users' decisions to adopt Flutter? - Q1 2021 user survey results](https://blog.flutter.dev/which-factors-affected-users-decisions-to-adopt-flutter-q1-2021-user-survey-results-563e61fc68c9)

---

03 Mar 2021: Flutter Engage: 2.0 release
----------------------------------------

[#](#03-mar-2021-flutter-engage-2-0-release)

Flutter 2 is live!!! For more information, see [Announcing Flutter 2](https://developers.googleblog.com/2021/03/announcing-flutter-2.html), [What's new in Flutter 2](https://blog.flutter.dev/whats-new-in-flutter-2-0-fe8e95ecc65), [Flutter web support hits the stable milestone](https://blog.flutter.dev/flutter-web-support-hits-the-stable-milestone-d6b84e83b425), [Announcing Dart 2.12](https://medium.com/dartlang/announcing-dart-2-12-499a6e689c87), and the [Flutter 2 release notes](/release/release-notes/release-notes-2.0.0).

**Docs updated or added since the 1.22 release**

* A new [Who is Dash?](/dash) page!* Information about monetizing your apps has been collected in the new [Flutter Ads](https://flutter.dev/monetization) landing page.* Added a new page explaining the [Flutter Fix](/tools/flutter-fix) feature and how to use it.* New and updated web pages, including:
        + [Web support for Flutter](/platform-integration/web)+ [Configuring the URL strategy on the web](/ui/navigation/url-strategies)+ [Web FAQ](/platform-integration/web/faq)* The [Desktop support for Flutter](/platform-integration/desktop) page is updated, as well as other pages on the site that discuss desktop support.* The [DevTools](/tools/devtools) docs have been updated. The most significant updates are to the following page:
            + [Flutter inspector](/tools/devtools/inspector)* Added a page on how to [implement deep linking](/ui/navigation/deep-linking) for mobile and web.* Updated the [Creating responsive and adaptive apps](/ui/adaptive-responsive) page.* Many pages (including all codelabs on flutter.dev) and examples are updated to be null safe.* Added two new add to app pages:
                    + [Using multiple Flutter instances](/add-to-app/multiple-flutters)+ [Adding a Flutter view to an Android app](/add-to-app/android/add-flutter-view)* Added a page on how to [write integration tests using the integration\_test package](/testing/integration-tests).* Significant updates to the [internationalization](/ui/accessibility-and-internationalization/internationalization) page.* New and updated [performance](/perf) pages, including:
                          + [Performance metrics](/perf/metrics)+ [Performance faq](/perf/faq)+ [More thoughts about performance](/perf/appendix)

**Codelabs**

Many of our codelabs have been updated to null safety. We've also added a new codelab since the last stable release:

* [Adding AdMob banner and native inline ads to a Flutter app](https://codelabs.developers.google.com/codelabs/admob-inline-ads-in-flutter)

For a complete list, see [Flutter codelabs](/reference/learning-resources).

**Articles**

We've published the following articles on the [Flutter Medium](https://medium.com/flutter) publication since the last stable release:

* [Flutter performance updates in the first half of 2020](https://blog.flutter.dev/flutter-performance-updates-in-the-first-half-of-2020-5c597168b6bb)* [Are you happy with Flutter? - Q4 2020 user survey results](https://blog.flutter.dev/are-you-happy-with-flutter-q4-2020-user-survey-results-41cdd90aaa48)* [Join us for #30DaysOfFlutter](https://blog.flutter.dev/join-us-for-30daysofflutter-9993e3ec847b)* [Providing operating system compatibility on a large scale](https://blog.flutter.dev/providing-operating-system-compatibility-on-a-large-scale-374cc2fb0dad)* [Updates on Flutter Testing](https://blog.flutter.dev/updates-on-flutter-testing-f54aa9f74c7e)* [Announcing Dart null safety beta](https://blog.flutter.dev/announcing-dart-null-safety-beta-4491da22077a)* [Deprecation Lifetime in Flutter](https://blog.flutter.dev/deprecation-lifetime-in-flutter-e4d76ee738ad)* [New ad formats for Flutter](https://blog.flutter.dev/new-ads-beta-inline-banner-and-native-support-for-the-flutter-mobile-ads-plugin-e48a7e9a0e64)* [Accessible expression with Material Icons and Flutter](https://blog.flutter.dev/accessible-expression-with-material-icons-and-flutter-e3f3f622200b)* [Dart sound null safety: technical preview 2](https://blog.flutter.dev/null-safety-flutter-tech-preview-cb5c98aba187)* [Flutter on the web, slivers, and platform-specific issues: user survey results from Q3 2020](https://blog.flutter.dev/flutter-on-the-web-slivers-and-platform-specific-issues-user-survey-results-from-q3-2020-f8034236b2a8)* [Testable Flutter and Cloud Firestore](https://blog.flutter.dev/flutter/testable-flutter-and-cloud-firestore-1cf2fbbce97b)* [Performance testing on the web](https://blog.flutter.dev/performance-testing-on-the-web-25323252de69)

---

01 Oct 2020: 1.22 release
-------------------------

[#](#01-oct-2020-1-22-release)

Flutter 1.22 is live! For details, see [Announcing Flutter 1.22](https://blog.flutter.dev/announcing-flutter-1-22-44f146009e5f).

**Docs updated or added to flutter.dev since the 1.20 release**

* Updated the [Developing for iOS 14](/platform-integration/ios/ios-debugging) page with details about targeting iOS 14 with Flutter, including some Add-to-App, deep linking, and notification considerations.* Added a page on how to [add an iOS App Clip](/platform-integration/ios/ios-app-clip), a new iOS 14 feature that supports running lightweight, no-install apps under 10 MB.* Added a page that describes how to [migrate your app to use the new icon glyphs available in `CupertinoIcons`](/release/breaking-changes/cupertino-icons-1.0.0).* Added a page that describes the new implementation for Platform Views and how to use them to host native [Android views](/platform-integration/android/platform-views) and [iOS views](/platform-integration/ios/platform-views) in your Flutter app platform-views. This feature has enabled the [google\_maps\_flutter](https://pub.dev/packages/google_maps_flutter) and [webview\_flutter](https://pub.dev/packages/webview_flutter) plugins to be updated to production-ready release 1.0.* Added a page that describes how to use the new [App Size tool](/tools/devtools/app-size) in Dart DevTools.

**Codelabs**

We've added a new codelab since the last stable release:

* [Building Beautiful Transitions with Material Motion for Flutter](https://codelabs.developers.google.com/codelabs/material-motion-flutter)  
   Learn how to use the Material [animations](https://pub.dev/packages/animations) package to add prebuilt transitions to a Material app called Reply.

For a complete list, see [Flutter codelabs](/reference/learning-resources).

**Articles**

We've published the following articles on the [Flutter Medium](https://medium.com/flutter) publication since the last stable release:

* [Learning Flutter's new navigation and routing](https://blog.flutter.dev/learning-flutters-new-navigation-and-routing-system-7c9068155ade)* [Integration testing with flutter\_driver](https://blog.flutter.dev/integration-testing-with-flutter-driver-36f66ede5cf2)* [Announcing Flutter Windows Alpha](https://blog.flutter.dev/announcing-flutter-windows-alpha-33982cd0f433)* [Handling web gestures in Flutter](https://blog.flutter.dev/handling-web-gestures-in-flutter-e16946a04745)* [Supporting iOS 14 and Xcode 12 with Flutter](https://blog.flutter.dev/supporting-ios-14-and-xcode-12-with-flutter-15fe0062e98b)* [Learn testing with the new Flutter sample](https://blog.flutter.dev/learn-testing-with-the-new-flutter-sample-gsoc20-work-product-e872c7f6492a)* [Platform channel examples](https://blog.flutter.dev/platform-channel-examples-7edeaeba4a66)* [Updates on Flutter and Firebase](https://blog.flutter.dev/updates-on-flutter-and-firebase-8076f70bc90e)

05 Aug 2020: 1.20 release
-------------------------

[#](#05-aug-2020-1-20-release)

Flutter 1.20 is live! For details, see [Announcing Flutter 1.20](https://blog.flutter.dev/announcing-flutter-1-20-2aaf68c89c75).

**Docs updated or added to flutter.dev**

* [Flutter architectural overview](/resources/architectural-overview), a deep dive into Flutter's architecture, was added to the site just a few days after the 1.20 release.* [Reducing shader compilation jank on mobile](/perf/rendering-performance) is added to the performance docs.* [Developing for iOS 14 beta](/platform-integration/ios/ios-debugging) outlines some issues you might run into if developing for devices running iOS 14 beta.* New instructions for installing Flutter on Linux using snapd.* Updated the [Desktop support](/platform-integration/desktop) page to reflect that Linux desktop apps (as well as macOS) are available as alpha.* Several new Flutter books have been published. The [Flutter books](/resources/books) page is updated.* The [codelabs landing](/reference/learning-resources) page has been updated.

A deep dive into null safety has been added to dart.dev:

* [Understanding null safety](https://dart.dev/null-safety/understanding-null-safety)

**Codelabs**

[Flutter Day](https://events.withgoogle.com/flutter-day/) was held on 6/25/2020. In preparation for the event, we wrote new codelabs and updated existing codelabs. New codelabs include:

* [Adding Admob Ads to a Flutter app](https://codelabs.developers.google.com/codelabs/admob-ads-in-flutter/)* [How to write a Flutter plugin](https://codelabs.developers.google.com/codelabs/write-flutter-plugin)* [Multi-platform Firestore Flutter](https://codelabs.developers.google.com/codelabs/friendlyeats-flutter/)* [Using a plugin with a Flutter web app](https://codelabs.developers.google.com/codelabs/web-url-launcher/)* [Write a Flutter desktop application](https://codelabs.developers.google.com/codelabs/flutter-github-graphql-client/)

For a complete list, see [Flutter codelabs](/reference/learning-resources).

**Articles**

We've published the following articles on the [Flutter Medium](https://medium.com/flutter) publication since the last stable release:

* [Announcing Adobe XD support for Flutter](https://blog.flutter.dev/announcing-adobe-xd-support-for-flutter-4b3dd55ff40e)* [What are the important & difficult tasks for Flutter devs? - Q1 2020 survey results](https://blog.flutter.dev/what-are-the-important-difficult-tasks-for-flutter-devs-q1-2020-survey-results-a5ef2305429b)* [Optimizing performance in Flutter web apps with tree shaking and deferred loading](https://blog.flutter.dev/optimizing-performance-in-flutter-web-apps-with-tree-shaking-and-deferred-loading-535fbe3cd674)* [Flutter Package Ecosystem Update](https://blog.flutter.dev/flutter-package-ecosystem-update-d50645f2d7bc)* [Improving perceived performance with image placeholders, precaching, and disabled navigation transitions](https://blog.flutter.dev/improving-perceived-performance-with-image-placeholders-precaching-and-disabled-navigation-6b3601087a2b)* [Two Months of #FlutterGoodNewsWednesday](https://blog.flutter.dev/two-months-of-fluttergoodnewswednesday-a12e60bab782)* [Handling 404: Page not found error in Flutter](https://blog.flutter.dev/handling-404-page-not-found-error-in-flutter-731f5a9fba29)* [Flutter and Desktop apps](https://blog.flutter.dev/flutter-and-desktop-3a0dd0f8353e)* [What's new with the Slider widget?](https://blog.flutter.dev/whats-new-with-the-slider-widget-ce48a22611a3)* [New tools for Flutter developers, built in Flutter](https://blog.flutter.dev/new-tools-for-flutter-developers-built-in-flutter-a122cb4eec86)* [Canonical enables Linux desktop app support with Flutter](https://blog.flutter.dev/announcing-flutter-linux-alpha-with-canonical-19eb824590a9)* [Enums with Extensions in Dart](https://blog.flutter.dev/enums-with-extensions-dart-460c42ea51f7)* [Managing issues in a large-scale open source project](https://blog.flutter.dev/managing-issues-in-a-large-scale-open-source-project-b3be6eecae2b)* [What we learned from the Flutter Q2 2020 survey](https://blog.flutter.dev/what-we-learned-from-the-flutter-q2-2020-survey-a4f1fc8faac9)* [Building performant Flutter widgets](https://blog.flutter.dev/building-performant-flutter-widgets-3b2558aa08fa)* [How to debug layout issues with the Flutter Inspector](https://blog.flutter.dev/how-to-debug-layout-issues-with-the-flutter-inspector-87460a7b9db)* [Going deeper with Flutter's web support](https://blog.flutter.dev/going-deeper-with-flutters-web-support-66d7ad95eb52)* [Flutter Performance Updates in 2019](https://blog.flutter.dev/going-deeper-with-flutters-web-support-66d7ad95eb5224)

06 May 2020: Work-From-Home: 1.17 release
-----------------------------------------

[#](#06-may-2020-work-from-home-1-17-release)

Flutter 1.17 is live!

For more information, see [Announcing Flutter 1.17](https://blog.flutter.dev/announcing-flutter-1-17-4182d8af7f8e).

Docs added and updated since the last announcement include:

* Added a new page on [Understanding constraints](/ui/layout/constraints), contributed by Marcelo Glasberg, a Flutter community member.* The [animations landing page](/ui/animations) has been re-written. This page now includes the animation decision tree that helps you figure out which animation approach is right for your needs. It also includes information on the new [package for pre-canned Material widget animations](https://pub.dev/packages/animations).* The [hot reload](/tools/hot-reload) page has been re-written. We hope you find it to be clearer!* The [Desktop](/platform-integration/desktop) page has been updated and now includes information on setting up entitlements and using the App Sandbox on macOS.* The plugin docs are updated to cover the new Android Plugin APIs and also to describe Federated Plugins. Affected pages include:
          + [Developing packages and plugins](/packages-and-plugins/developing-packages)+ [Developing plugin packages](/packages-and-plugins/developing-packages#federated-plugins)+ [Supporting the new Android plugin APIs](/release/breaking-changes/plugin-api-migration)+ [Writing custom platform-specific code](/platform-integration/platform-channels)* Added an [Obfuscating Dart code](/deployment/obfuscate) page. (Moved from the wiki and updated as of 1.16.2.)* Added a page on using Xcode 11.4 and how to manually update your project. The tooling, which automatically updates your configuration when possible, might direct you to this page if it detects that it's needed.* Added a page on [Managing plugins and dependencies in add-to-app](/add-to-app/android/plugin-setup) when developing for Android.

Other newness:

* We've published a number of articles on the [Flutter Medium](https://medium.com/flutter) publication since the last stable release:
  + [Custom implicit animations in Flutter…with TweenAnimationBuilder](https://blog.flutter.dev/custom-implicit-animations-in-flutter-with-tweenanimationbuilder-c76540b47185)+ [Directional animations with build-in explicit animations](https://blog.flutter.dev/directional-animations-with-built-in-explicit-animations-3e7c5e6fbbd7)+ [When should I use AnimatedBuilder or AnimatedWidget?](https://blog.flutter.dev/when-should-i-useanimatedbuilder-or-animatedwidget-57ecae0959e8)+ [Improving Flutter with your opinion - Q4 2019 survey results](https://blog.flutter.dev/improving-flutter-with-your-opinion-q4-2019-survey-results-ba0e6721bf23)+ [How to write a Flutter web plugin, Part 2](https://blog.flutter.dev/how-to-write-a-flutter-web-plugin-part-2-afdddb69ece6)+ [It's Time: The Flutter Clock contest results](https://blog.flutter.dev/its-time-the-flutter-clock-contest-results-dcebe2eb3957)+ [How to float an overlay widget over a (possibly transformed) UI widget](https://blog.flutter.dev/how-to-float-an-overlay-widget-over-a-possibly-transformed-ui-widget-1d15ca7667b6)+ [How to embed a Flutter application in a website using DartPad](https://blog.flutter.dev/how-to-embed-a-flutter-application-in-a-website-using-dartpad-b8fd0ee8c4b9)+ [Flutter web: Navigating URLs using named routes](https://blog.flutter.dev/web-navigating-urls-using-named-routes-307e1b1e2050)+ [How to choose which Flutter animation widget is right for you?](https://blog.flutter.dev/how-to-choose-which-flutter-animation-widget-is-right-for-you-79ecfb7e72b5)+ [Announcing a free Flutter introductory course](https://blog.flutter.dev/learn-flutter-for-free-c9bc3b898c4d)+ [Announcing CodePen support for Flutter](https://blog.flutter.dev/announcing-codepen-support-for-flutter-bb346406fe50)+ [Animation deep dive](https://blog.flutter.dev/animation-deep-dive-39d3ffea111f)+ [Flutter Spring 2020 update](https://blog.flutter.dev/spring-2020-update-f723d898d7af)+ [Introducing Google Fonts for Flutter v 1.0.0!](https://blog.flutter.dev/introducing-google-fonts-for-flutter-v-1-0-0-c0e993617118)+ [Flutter web support updates](https://blog.flutter.dev/web-support-updates-8b14bfe6a908)+ [Modern Flutter plugin development](https://blog.flutter.dev/modern-flutter-plugin-development-4c3ee015cf5a)

11 Dec 2019: Flutter Interact: 1.12 release
-------------------------------------------

[#](#11-dec-2019-flutter-interact-1-12-release)

Flutter 1.12 is live!

For more information, see [Flutter: the first UI platform designed for ambient computing](https://developers.googleblog.com/2019/12/flutter-ui-ambient-computing.html?m=1), [Announcing Flutter 1.12: What a year!](https://blog.flutter.dev/announcing-flutter-1-12-what-a-year-22c256ba525d) and the [Flutter 1.12.13](/release/release-notes/release-notes-1.12.13) release notes.

Docs added and updated since the last announcement include:

* To accompany an updated implementation of add-to-app, we have added documentation on how to [add Flutter to an existing app](/add-to-app) for both iOS and Android.* If you own plugin code, we encourage you to update to the new plugin APIs for Android. For more information, see [Migrating your plugin to the new Android APIs](/release/breaking-changes/plugin-api-migration).* Web support has moved to the beta channel. For more information, see [Web support for Flutter](/platform-integration/web) and [Web support for Flutter goes beta](https://blog.flutter.dev/web-support-for-flutter-goes-beta-35b64a1217c0) on the Medium publication. Also, the [building a web app with Flutter](/platform-integration/web/building) page is updated.* A new write your first Flutter app on the web codelab is added to the [Get started](/get-started) docs, and includes instructions on setting breakpoints in DevTools!* We've introduced a program for recommending particular Dart and Flutter plugins and packages. Learn more about the [Flutter Favorite program](/packages-and-plugins/favorites).* A new [implicit animations](/codelabs/implicit-animations) codelab is available featuring DartPad. (To run it, you don't need to download any software!)* Alpha support for macOS (desktop) is now available in release 1.13 on the master and dev channels. For more information, see [Desktop support for Flutter](/platform-integration/desktop).* The iOS section of the [app size](/perf/app-size#ios) page is updated to reflect the inclusion of bitcode.* An alpha release of Flutter Layout Explorer, a new feature (and part of the Flutter inspector) that allows you to explore a visual representation of your layout is available. For more information, see the [Flutter Layout Explorer](/tools/devtools/legacy-inspector#flutter-layout-explorer) docs.

Other newness:

* A brand-new version of [Flutter Gallery](https://flutter-gallery-archive.web.app).

Happy Fluttering!

10 Sep 2019: 1.9 release
------------------------

[#](#10-sep-2019-1-9-release)

Flutter 1.9 is live!

For more information, see [Flutter news from GDD China: uniting Flutter on web and mobile, and introducing Flutter 1.9](https://developers.googleblog.com/2019/09/flutter-news-from-gdd-china-flutter1.9.html?m=1) and the [1.9.1 release notes](/release/release-notes/release-notes-1.9.1).

For the 1.9 release, Flutter's web support has been merged ("unforked") into the main repo. **Web support hasn't reached beta, and is not ready to be used in production.** Web and desktop support (which is also coming), will impact the website, which was originally written exclusively for developing Flutter mobile apps. Some website updates are available now (and listed below), but more will be coming.

New and updated docs on the site include:

* We've revamped the [Showcase](https://flutter.dev/showcase) page.* The Flutter layout codelab has been rewritten and uses the updated DartPad, the browser-based tool for running Dart code. DartPad now supports Flutter! [Try it out](https://dartpad.dev) and let us know what you think.* A new page on [using the dart:ffi library](/platform-integration/android/c-interop) to bind your app to native code (a feature currently under development).* The Performance view tool, which allows you to record and profile a session from your Dart/Flutter application, has been enabled in DevTools. For more information, see the [Performance view](/tools/devtools/performance) page.* A new page on [building a web application](/platform-integration/web/building).* A new page on [creating responsive apps](/ui/adaptive-responsive) in Flutter.* A new page on [preparing a web app for release](/deployment/web).* A new [web FAQ](/platform-integration/web/faq).* The [Flutter for web](/platform-integration/web) page is updated.

Other relevant docs:

* Error messages have been improved in SDK 1.9. For more information, read [Improving Flutter's Error Messages](https://blog.flutter.dev/improving-flutters-error-messages-e098513cecf9) on the [Flutter Medium publication](https://medium.com/flutter).* If you already have a web app that depends on the flutter\_web package, the following instructions tell you how to migrate to the flutter package: Upgrading from package:flutter\_web to the Flutter SDK.* A new [`ToggleButtons`](https://api.flutter.dev/flutter/material/ToggleButtons-class.html) widget, described in the API docs. [ToggleButtons demo](https://github.com/csells/flutter_toggle_buttons)* A new [`ColorFiltered`](https://api.flutter.dev/flutter/widgets/ColorFiltered-class.html) widget, also described in the API docs. [ColorFiltered demo](https://github.com/csells/flutter_color_filter)* New behavior for the [`SelectableText`](https://api.flutter.dev/flutter/material/SelectableText-class.html) widget.

Happy Fluttering!

09 Jul 2019: 1.7 release
------------------------

[#](#09-jul-2019-1-7-release)

Flutter 1.7 is live!

For more information, see [Announcing Flutter 1.7](https://blog.flutter.dev/announcing-flutter-1-7-9cab4f34eacf) on the [Flutter Medium Publication](https://medium.com/flutter), and the [1.7.8 release notes](/release/release-notes/release-notes-1.7.8).

New and updated docs on the site include:

* The [Preparing an Android app for release](/deployment/android) page is updated to discuss how to build an Android release using an app bundle, as well as how to create separate APK files for both 32-bit and 64-bit devices.* The [DevTools](/tools/devtools) docs are migrated to flutter.dev. If you haven't tried this browser-based suite of debugging, performance, memory, and inspection tools that work with both Flutter and Dart apps and can be launched from Android Studio/IntelliJ *and* VS Code, please check it out!* The [Simple app state management](/data-and-backend/state-mgmt/simple) page is updated. The example code in the page now uses the 3.0 release of the Provider package.* A new animation recipe, [Animate a page route transition](/cookbook/animation/page-route-animation) has been added to the Flutter Cookbook.* The [Debugging](/testing/debugging), [Flutter's build modes](/testing/build-modes), [Performance best practices](/perf/best-practices), and [Performance profiling](/perf/ui-performance) pages are updated to reflect DevTools. A [Debugging apps programmatically](/testing/code-debugging) page has also been added.

The Flutter 1.7 release includes the new [`RangeSlider`](https://api.flutter.dev/flutter/material/RangeSlider-class.html) component, which allows the user to select both the upper and lower endpoints in a range of values. For information about this component and how to customize it, see [Material RangeSlider in Flutter](https://blog.flutter.dev/material-range-slider-in-flutter-a285c6e3447d).

07 May 2019: Google I/O 2019: 1.5 release
-----------------------------------------

[#](#07-may-2019-google-io-2019-1-5-release)

[Flutter 1.5](https://developers.googleblog.com/2019/05/Flutter-io19.html) is live!

For more information on updates, see the [1.5.4 release notes](/release/release-notes/release-notes-1.5.4) or [download the release](/install/archive).

We are updating DartPad to work with Flutter. Try the new Basic Flutter layout codelab and tell us what you think!

26 Feb 2019: 1.2 release
------------------------

[#](#26-feb-2019-1-2-release)

Flutter released [version 1.2](https://developers.googleblog.com/2019/02/launching-flutter-12-at-mobile-world.html) at Mobile World Congress (MWC) in Barcelona. For more information, see the [1.2.1 release notes](/release/release-notes/release-notes-1.2.1) or [download the release](/install/archive).

In addition, here are some recent new and updated docs:

* We've updated our [state management advice](/data-and-backend/state-mgmt/intro). New pages include an [introduction](/data-and-backend/state-mgmt/intro), [thinking declaratively](/data-and-backend/state-mgmt/declarative), [ephemeral vs app state](/data-and-backend/state-mgmt/ephemeral-vs-app), [simple app state management](/data-and-backend/state-mgmt/simple), and [different state management options](/data-and-backend/state-mgmt/options). Documenting state management is a tricky thing, as there is no one-size-fits-all approach. We'd love your feedback on these new docs!* A new page on [Performance best practices](/perf/best-practices).* Also at MWC, we announced a preview version of the new Dart DevTools for profiling and debugging Dart and Flutter apps. You can find the docs on the DevTools wiki (Note: since moved to [this site](/tools/devtools).) In particular, check out the DevTool's [widget inspector](/tools/devtools/inspector) for debugging your UI, or the [timeline view](/tools/devtools/performance) for profiling your Flutter application. Try them out and let us know what you think!* An update to the [Performance profiling](/perf/ui-performance) page that incorporates the new Dart DevTools UI.* Updates to the [Android Studio/IntelliJ](/tools/android-studio) and [VS Code](/tools/vs-code) pages incorporating info from the new Dart DevTools UI.

If you have questions or comments about any of these docs, [file an issue](https://github.com/flutter/website/issues).

05 Nov 2018: new website
------------------------

[#](#05-nov-2018-new-website)

Welcome to the revamped Flutter website!

We've spent the last few months redesigning the website and how its information is organized. We hope you can more easily find the docs you are looking for. Some of the changes to the website include:

* Revised [front](/) page* Revised [showcase](https://flutter.dev/showcase) page* Revised [community](https://flutter.dev/community) page* Revised navigation in the left side bar* Table of contents on the right side of most pages

Some of the new content includes:

* Deep dive on Flutter internals, [Inside Flutter](/resources/inside-flutter)* [Technical videos](/resources/videos)* [State management](/data-and-backend/state-mgmt)* [Background Dart processes](/packages-and-plugins/background-processes)* [Flutter's build modes](/testing/build-modes)

If you have questions or comments about the revamped site, [file an issue](https://github.com/flutter/website/issues).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/archive-whats-new/&page-source=https://github.com/flutter/website/tree/main/src/content/release/archive-whats-new.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/archive-whats-new/&page-source=https://github.com/flutter/website/tree/main/src/content/release/archive-whats-new.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-25. [View source](https://github.com/flutter/website/tree/main/src/content/release/archive-whats-new.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/archive-whats-new/&page-source=https://github.com/flutter/website/tree/main/src/content/release/archive-whats-new.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   