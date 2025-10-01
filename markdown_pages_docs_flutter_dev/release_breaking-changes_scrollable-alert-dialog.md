Scrollable AlertDialog (No longer deprecated)
=============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Scrollable AlertDialog (No longer deprecated)](/release/breaking-changes/scrollable-alert-dialog)

Summary
-------

[#](#summary)

*info* Note

`AlertDialog.scrollable` is no longer deprecated because there is no backwards-compatible way to make `AlertDialog` scrollable by default. Instead, the parameter will remain and you can set `scrollable` to true if you want a scrollable `AlertDialog`.

An `AlertDialog` now scrolls automatically when it overflows.

Context
-------

[#](#context)

Before this change, when an `AlertDialog` widget's contents were too tall, the display overflowed, causing the contents to be clipped. This resulted in the following issues:

* There was no way to view the portion of the content that was clipped.* Most alert dialogs have buttons beneath the content to prompt users for actions. If the content overflowed, obscuring the buttons, users might be unaware of their existence.

Description of change
---------------------

[#](#description-of-change)

The previous approach listed the title and content widgets consecutively in a `Column` widget.

dart

```
Column(
  mainAxisSize: MainAxisSize.min,
  crossAxisAlignment: CrossAxisAlignment.stretch,
  children: <Widget>[
    if (title != null)
      Padding(
        padding: titlePadding ?? EdgeInsets.fromLTRB(24, 24, 24, content == null ? 20 : 0),
        child: DefaultTextStyle(
          style: titleTextStyle ?? dialogTheme.titleTextStyle ?? theme.textTheme.title,
          child: Semantics(
          child: title,
          namesRoute: true,
          container: true,
          ),
        ),
      ),
    if (content != null)
      Flexible(
        child: Padding(
        padding: contentPadding,
        child: DefaultTextStyle(
          style: contentTextStyle ?? dialogTheme.contentTextStyle ?? theme.textTheme.subhead,
          child: content,
        ),
      ),
    ),
    // ...
  ],
);
```

The new approach wraps both widgets in a `SingleChildScrollView` above the button bar, making both widgets part of the same scrollable and exposing the button bar at the bottom of the dialog.

dart

```
Column(
  mainAxisSize: MainAxisSize.min,
  crossAxisAlignment: CrossAxisAlignment.stretch,
  children: <Widget>[
    if (title != null || content != null)
      SingleChildScrollView(
        child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.stretch,
         children: <Widget>[
           if (title != null)
             titleWidget,
             if (content != null)
             contentWidget,
         ],
       ),
     ),
   // ...
  ],
),
```

Migration guide
---------------

[#](#migration-guide)

You might see the following issues as a result of this change:

**Semantics tests might fail because of the addition of a `SingleChildScrollView`.**: Manual testing of the `Talkback` and `VoiceOver` features show that they still exhibit the same (correct) behavior as before. **Golden tests might fail.**: This change might have caused diffs in (previously passing) golden tests since the `SingleChildScrollView` now nests both the title and content widgets. Some Flutter projects have taken to creating semantics tests by taking goldens of semantics nodes used in Flutter's debug build. Any semantics golden updates that reflect the scrolling container addition are expected and these diffs should be safe to accept. Sample resulting Semantics tree:

```
flutter:        ├─SemanticsNode#30 <-- SingleChildScrollView
flutter:          │ flags: hasImplicitScrolling
flutter:          │ scrollExtentMin: 0.0
flutter:          │ scrollPosition: 0.0
flutter:          │ scrollExtentMax: 0.0
flutter:          │
flutter:          ├─SemanticsNode#31 <-- title
flutter:          │   flags: namesRoute
flutter:          │   label: "Hello"
flutter:          │
flutter:          └─SemanticsNode#32 <-- contents
flutter:              label: "Huge content"
```

**Layout changes might result because of the scroll view.**: If the dialog was already overflowing, this change corrects the problem. This layout change is expected. A nested `SingleChildScrollView` in `AlertDialog.content` should work properly if left in the code, but should be removed if unintended, since it might cause confusion.

Code before migration:

dart

```
AlertDialog(
  title: Text(
    'Very, very large title that is also scrollable',
    textScaleFactor: 5,
  ),
  content: SingleChildScrollView( // won't be scrollable
    child: Text('Scrollable content', textScaleFactor: 5),
  ),
  actions: <Widget>[
    TextButton(child: Text('Button 1'), onPressed: () {}),
    TextButton(child: Text('Button 2'), onPressed: () {}),
  ],
)
```

Code after migration:

dart

```
AlertDialog(
  title: Text('Very, very large title', textScaleFactor: 5),
  content: Text('Very, very large content', textScaleFactor: 5),
  actions: <Widget>[
    TextButton(child: Text('Button 1'), onPressed: () {}),
    TextButton(child: Text('Button 2'), onPressed: () {}),
  ],
)
```

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

Design doc:

* [Scrollable `AlertDialog`](/go/scrollable-alert-dialog)

API documentation:

* [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html)

Relevant issue:

* [Overflow exceptions with maximum accessibility font size](https://github.com/flutter/flutter/issues/42696)

Relevant PRs:

* [Update to `AlertDialog.scrollable`](https://github.com/flutter/flutter/pull/45079)* [Original attempt to implement scrollable `AlertDialog`](https://github.com/flutter/flutter/pull/43226)* [Revert of original attempt to implement scrollable `AlertDialog`](https://github.com/flutter/flutter/pull/44003)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scrollable-alert-dialog/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scrollable-alert-dialog.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scrollable-alert-dialog/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scrollable-alert-dialog.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scrollable-alert-dialog.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/scrollable-alert-dialog/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/scrollable-alert-dialog.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   