Introduction of FlutterEngine::ProcessExternalWindowMessage
===========================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Introduction of FlutterEngine::ProcessExternalWindowMessage](/release/breaking-changes/win-lifecycle-process-function)

Summary
-------

[#](#summary)

When you add any external windows to your Flutter app, you need to include them in the Window's app lifecycle logic. To include the window, its `WndProc` function should invoke `FlutterEngine::ProcessExternalWindowMessage`.

Who is affected
---------------

[#](#who-is-affected)

Windows applications built against Flutter 3.13 or newer that open non-Flutter windows.

Description of change
---------------------

[#](#description-of-change)

Implementing application lifecycle on Windows involves listening for Window messages in order to update the lifecycle state. In order for additional non-Flutter windows to affect the lifecycle state, they must forward their window messages to `FlutterEngine::ProcessExternalWindowMessage` from their `WndProc` functions. This function returns an `std::optional<LRESULT>`, which is `std::nullopt` when the message is received, but not consumed. When the returned result has a value, the message has been consumed, and further processing in `WndProc` should cease.

Migration guide
---------------

[#](#migration-guide)

The following example `WndProc` procedure invokes `FlutterEngine::ProcessExternalWindowMessage`:

cpp

```
LRESULT Window::Messagehandler(HWND hwnd, UINT msg, WPARAM wparam, LPARAM lparam) {
    std::optional<LRESULT> result = flutter_controller_->engine()->ProcessExternalWindowMessage(hwnd, msg, wparam, lparam);
    if (result.has_value()) {
        return *result;
    }
    // Original contents of WndProc...
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.14.0-3.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

Relevant PRs:

* [Reintroduce Windows lifecycle with guard for posthumous OnWindowStateEvent](https://github.com/flutter/engine/pull/44344)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/win-lifecycle-process-function/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/win-lifecycle-process-function.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/win-lifecycle-process-function/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/win-lifecycle-process-function.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/win-lifecycle-process-function.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/win-lifecycle-process-function/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/win-lifecycle-process-function.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   