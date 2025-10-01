Migrate a Windows project to set version information
====================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migrate a Windows project to set version information](/release/breaking-changes/windows-version-information)

Flutter 3.3 added support for setting the Windows app's version from the `pubspec.yaml` file or through the `--build-name` and `--build-number` build arguments. For more information, refer to the [Build and release a Windows app](/deployment/windows#updating-the-apps-version-number) documentation.

Projects created before Flutter version 3.3 need to be migrated to support versioning.

Migration steps
---------------

[#](#migration-steps)

Your project can be updated using these steps:

1. Verify you are on Flutter version 3.3 or newer using `flutter --version`- If needed, use `flutter upgrade` to update to the latest version of the Flutter SDK- Backup your project, possibly using git or some other version control system- Delete the `windows/runner/CMakeLists.txt` and `windows/runner/Runner.rc` files- Run `flutter create --platforms=windows .`- Review the changes to your `windows/runner/CMakeLists.txt` and `windows/runner/Runner.rc` files- Verify your app builds using `flutter build windows`

*info* Note

Follow the [run loop migration guide](/release/breaking-changes/windows-run-loop) if the build fails with the following error message:

```
flutter_window.obj : error LNK2019: unresolved external symbol "public: void __cdecl RunLoop::RegisterFlutterInstance(class flutter::FlutterEngine *)" (?RegisterFlutterInstance@RunLoop@@QEAAXPEAVFlutterEngine@flutter@@@Z) referenced in function "protected: virtual bool __cdecl FlutterWindow::OnCreate(void)" (?OnCreate@FlutterWindow@@MEAA_NXZ)
```

Example
-------

[#](#example)

[PR 721](https://github.com/flutter/gallery/pull/721/files) shows the migration work for the [Flutter Gallery](https://flutter-gallery-archive.web.app) app.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-version-information/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-version-information.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-version-information/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-version-information.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-version-information.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-version-information/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-version-information.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   