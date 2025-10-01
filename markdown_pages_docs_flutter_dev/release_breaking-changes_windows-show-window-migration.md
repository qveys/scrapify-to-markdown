Migrate a Windows project to ensure the window is shown
=======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migrate a Windows project to ensure the window is shown](/release/breaking-changes/windows-show-window-migration)

Flutter 3.13 fixed a [bug](https://github.com/flutter/flutter/issues/119415) that could result in the window not being shown. Windows projects created using Flutter 3.7 or Flutter 3.10 need to be migrated to fix this issue.

Migration steps
---------------

[#](#migration-steps)

Verify you are on Flutter version 3.13 or newer using `flutter --version`. If needed, use `flutter upgrade` to update to the latest version of the Flutter SDK.

Projects that have not modified their `windows/runner/flutter_window.cpp` file will be migrated automatically by `flutter run` or `flutter build windows`.

Projects that have modified their `windows/runner/flutter_window.cpp` file might need to migrate manually.

Code before migration:

cpp

```
flutter_controller_->engine()->SetNextFrameCallback([&]() {
  this->Show();
});
```

Code after migration:

cpp

```
flutter_controller_->engine()->SetNextFrameCallback([&]() {
  this->Show();
});

// Flutter can complete the first frame before the "show window" callback is
// registered. The following call ensures a frame is pending to ensure the
// window is shown. It is a no-op if the first frame hasn't completed yet.
flutter_controller_->ForceRedraw();
```

Example
-------

[#](#example)

[PR 995](https://github.com/flutter/gallery/pull/995/files) shows the migration work for the [Flutter Gallery](https://flutter-gallery-archive.web.app) app.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-show-window-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-show-window-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-show-window-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-show-window-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-show-window-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-show-window-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-show-window-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   