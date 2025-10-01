SystemContextMenuController.show Deprecated
===========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [SystemContextMenuController.show Deprecated](/release/breaking-changes/system_context_menu_controller_show)

Summary
-------

[#](#summary)

`SystemContextMenuController.show` is deprecated. The same functionality can be achieved by passing the result of calling `SystemContextMenu.getDefaultItems` to `SystemContextMenuController.showWithItems`.

Background
----------

[#](#background)

The iOS-drawn `SystemContextMenu` feature was originally added without the ability to control which items are shown in the menu. The platform would decide which items to show based on the active `TextInputConnection`.

The problem with this approach is that an "Autofill" button is often shown, but Flutter does not have the ability to respond to this button. So in many cases, users see an "Autofill" button that does nothing when tapped, and Flutter app developers have no way to hide the button.

This problem is solved by introducing a new method, `SystemContextMenuController.showWithItems`, which requires a list of `items` to be passed.

Developers that have no preference which items are shown can call the new method `SystemContextMenu.getDefaultItems` to get the default items based on the given `EditableTextState`. For example, if the `EditableTextState` indicates that there is nothing selected, then the **Copy** button won't be included, since it requires a selection to copy.

Migration guide
---------------

[#](#migration-guide)

Most users use the system context menu through the `SystemContextMenu` widget, and in this case there will be no change required. The `SystemContextMenu` widget automatically gets the default items under the hood.

No migration is needed:

dart

```
class _MyWidgetState extends State<MyWidget> {
  @override
  Widget build(BuildContext context) {
    TextField(
      contextMenuBuilder: (BuildContext context, EditableTextState editableTextState) {
        return SystemContextMenu.editableText(
          editableTextState: editableTextState,
        );
      }
    );
  }
}
```

For advanced users that directly work with `SystemContextMenuController`, migrate to the new method `SystemContextMenuController.showWithItems`. The default can be obtained from `SystemContextMenu.getDefaultItems` as a list of `IOSSystemContextMenuItem`s, which can be converted to the format required by `showWithItems` through `IOSSystemContextMenuItem.getData`.

Code before migration:

dart

```
_controller.show(selectionRect);
```

Code after migration:

dart

```
final List<IOSSystemContextMenuItem> defaultItems =
    SystemContextMenu.getDefaultItems(editableTextState);
final WidgetsLocalizations localizations =
    WidgetsLocalizations.of(context);
final List<IOSSystemContextMenuItemData> defaultItemDatas =
    defaultItems
        .map((IOSSystemContextMenuItem item) =>
            item.getData(localizations))
        .toList();
_controller.showWithItems(selectionRect, defaultItemDatas);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.29.0-0.3.pre  
 In stable release: 3.32

References
----------

[#](#references)

API documentation:

* [`TextInputConnection`](https://api.flutter.dev/flutter/services/TextInputConnection-class.html)* [`SystemContextMenuController.show`](https://api.flutter.dev/flutter/services/SystemContextMenuController/show.html)* [`SystemContextMenuController.showWithItems`](https://api.flutter.dev/flutter/services/SystemContextMenuController/showWithItems.html)* [`SystemContextMenu`](https://api.flutter.dev/flutter/services/SystemContextMenu.html)

Relevant issues:

* [Flutter should support iOS 15's Secure Paste feature](https://github.com/flutter/flutter/issues/103163)

Relevant PRs:

* [Secure paste milestone 2](https://github.com/flutter/flutter/pull/159013)* [ios secure\_paste show menu item based on info sent from framework](https://github.com/flutter/engine/pull/161103)* [Native ios context menu](https://github.com/flutter/flutter/pull/143002)* [ios\_edit\_menu add native edit menu](https://github.com/flutter/flutter/pull/50095)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/system_context_menu_controller_show/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/system_context_menu_controller_show.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/system_context_menu_controller_show/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/system_context_menu_controller_show.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/system_context_menu_controller_show.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/system_context_menu_controller_show/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/system_context_menu_controller_show.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   