Migrate a Windows project to the idiomatic run loop
===================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migrate a Windows project to the idiomatic run loop](/release/breaking-changes/windows-run-loop)

Flutter 2.5 replaced Windows apps' run loop with an idiomatic Windows message pump to reduce CPU usage.

Projects created before Flutter version 2.5 need to be migrated to get this improvement. You should follow the migration steps below if the `windows/runner/run_loop.h` file exists in your project.

Migration steps
---------------

[#](#migration-steps)

*info* Note

As part of this migration, you must recreate your Windows project, which clobbers any custom changes to the files in the `windows/runner` folder. The following steps include instructions for this scenario.

Your project can be updated using these steps:

1. Verify you are on Flutter version 2.5 or newer using `flutter --version`- If needed, use `flutter upgrade` to update to the latest version of the Flutter SDK- Backup your project with git (or your preferred version control system), since you need to reapply any local changes you've made (if any) to your project in a later step- Delete all files under the `windows/runner` folder- Run `flutter create --platforms=windows .` to recreate the Windows project- Review the changes to files in the `windows/runner` folder- Reapply any custom changes made to the files in the `windows/runner` folder prior to this migration- Verify that your app builds using `flutter build windows`

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-run-loop/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-run-loop.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-run-loop/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-run-loop.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-run-loop.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-run-loop/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-run-loop.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   