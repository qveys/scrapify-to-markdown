A new way to customize context menus
====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [A new way to customize context menus](/release/breaking-changes/context-menus)

Summary
-------

[#](#summary)

Context menus, or text selection toolbars, are the menus that show up when long pressing or right clicking on text in Flutter, and they show options like **Cut**, **Copy**, **Paste**, and **Select all**. Previously, it was only possible to narrowly customize them using `ToolbarOptions` and `TextSelectionControls`. Now, they have been made composable using widgets, just like everything else in Flutter, and the specific configuration parameters have been deprecated.

Context
-------

[#](#context)

Previously, it was possible to disable buttons from the context menus using `TextSelectionControls`, but any customization beyond that required copying and editing hundreds of lines of custom classes in the framework. Now, all of this has been replaced by a simple builder function, `contextMenuBuilder`, which allows any Flutter widget to be used as a context menu.

Description of change
---------------------

[#](#description-of-change)

Context menus are now built from the `contextMenuBuilder` parameter, which has been added to all text-editing and text-selection widgets. If one is not provided, then Flutter just sets it to a default that builds the correct context menu for the given platform. All of these default widgets are exposed to users for re-use. Customizing context menus now consists of using `contextMenuBuilder` to return whatever widget you want, possibly including reusing the built-in context menu widgets.

Here's an example that shows how to add a **Send email** button to the default context menus whenever an email address is selected. The full code can be found in the samples repository in [email\_button\_page.dart](https://github.com/flutter/samples/blob/main/context_menus/lib/email_button_page.dart) on GitHub.

dart

```
TextField(
  contextMenuBuilder: (context, editableTextState) {
    final TextEditingValue value = editableTextState.textEditingValue;
    final List<ContextMenuButtonItem> buttonItems =
        editableTextState.contextMenuButtonItems;
    if (isValidEmail(value.selection.textInside(value.text))) {
      buttonItems.insert(
          0,
          ContextMenuButtonItem(
            label: 'Send email',
            onPressed: () {
              ContextMenuController.removeAny();
              Navigator.of(context).push(_showDialog(context));
            },
          ));
    }
    return AdaptiveTextSelectionToolbar.buttonItems(
      anchors: editableTextState.contextMenuAnchors,
      buttonItems: buttonItems,
    );
  },
)
```

A large number of examples of different custom context menus are available [in the samples repo](https://github.com/flutter/samples/tree/main/context_menus) on GitHub.

All related deprecated features were flagged with the deprecation warning "Use `contextMenuBuilder` instead."

Migration guide
---------------

[#](#migration-guide)

In general, any previous changes to context menus that have been deprecated now require the use of the `contextMenuBuilder` parameter on the relevant text-editing or text-selection widget ( [on `TextField`](https://api.flutter.dev/flutter/material/TextField/contextMenuBuilder.html), for example). Return a built-in context menu widget like [`AdaptiveTextSelectionToolbar`](https://api.flutter.dev/flutter/material/AdaptiveTextSelectionToolbar-class.html) to use Flutter's built-in context menus, or return your own widget for something totally custom.

To transition to `contextMenuBuilder`, the following parameters and classes have been deprecated.

### [`ToolbarOptions`](https://api.flutter.dev/flutter/widgets/ToolbarOptions-class.html)

[#](#toolbaroptions)

This class was previously used to explicitly enable or disable certain buttons in a context menu. Before this change, you might have passed it into `TextField` or other widgets like this:

dart

```
// Deprecated.
TextField(
  toolbarOptions: ToolbarOptions(
    copy: true,
  ),
)
```

Now, you can achieve the same effect by adjusting the `buttonItems` passed into `AdaptiveTextSelectionToolbar`. For example, you could ensure that the **Cut** button never appears, but the other buttons do appear as usual:

dart

```
TextField(
  contextMenuBuilder: (context, editableTextState) {
    final List<ContextMenuButtonItem> buttonItems =
        editableTextState.contextMenuButtonItems;
    buttonItems.removeWhere((ContextMenuButtonItem buttonItem) {
      return buttonItem.type == ContextMenuButtonType.cut;
    });
    return AdaptiveTextSelectionToolbar.buttonItems(
      anchors: editableTextState.contextMenuAnchors,
      buttonItems: buttonItems,
    );
  },
)
```

Or, you could ensure that the **Cut** button appears exclusively and always:

dart

```
TextField(
  contextMenuBuilder: (context, editableTextState) {
    return AdaptiveTextSelectionToolbar.buttonItems(
      anchors: editableTextState.contextMenuAnchors,
      buttonItems: <ContextMenuButtonItem>[
        ContextMenuButtonItem(
          onPressed: () {
            editableTextState.cutSelection(SelectionChangedCause.toolbar);
          },
          type: ContextMenuButtonType.cut,
        ),
      ],
    );
  },
)
```

### [`TextSelectionControls.canCut`](https://api.flutter.dev/flutter/widgets/TextSelectionControls/canCut.html) and other button booleans

[#](#textselectioncontrols-cancut-and-other-button-booleans)

These booleans previously had the same effect of enabling and disabling certain buttons as `ToolbarOptions.cut`, and so on had. Before this change, you might have been hiding and showing buttons by overriding `TextSelectionControls` and setting these booleans like this:

dart

```
// Deprecated.
class _MyMaterialTextSelectionControls extends MaterialTextSelectionControls {
  @override
  bool canCut() => false,
}
```

See the previous section on `ToolbarOptions` for how to achieve a similar effect with `contextMenuBuilder`.

### [`TextSelectionControls.handleCut`](https://api.flutter.dev/flutter/widgets/TextSelectionControls/handleCut.html) and other button callbacks

[#](#textselectioncontrols-handlecut-and-other-button-callbacks)

These functions allowed the modification of the callback called when the buttons were pressed. Before this change, you might have been modifying context menu button callbacks by overriding these handler methods like this:

dart

```
// Deprecated.
class _MyMaterialTextSelectionControls extends MaterialTextSelectionControls {
  @override
  bool handleCut() {
    // My custom cut implementation here.
  },
}
```

This is still possible using `contextMenuBuilder`, including calling out to the original buttons' actions in the custom handler, using toolbar widgets like `AdaptiveTextSelectionToolbar.buttonItems`.

This example shows modifying the **Copy** button to show a dialog in addition to doing its usual copy logic.

dart

```
TextField(
  contextMenuBuilder: (BuildContext context, EditableTextState editableTextState) {
    final List<ContextMenuButtonItem> buttonItems =
        editableTextState.contextMenuButtonItems;
    final int copyButtonIndex = buttonItems.indexWhere(
      (ContextMenuButtonItem buttonItem) {
        return buttonItem.type == ContextMenuButtonType.copy;
      },
    );
    if (copyButtonIndex >= 0) {
      final ContextMenuButtonItem copyButtonItem =
          buttonItems[copyButtonIndex];
      buttonItems[copyButtonIndex] = copyButtonItem.copyWith(
        onPressed: () {
          copyButtonItem.onPressed();
          Navigator.of(context).push(
            DialogRoute<void>(
              context: context,
              builder: (BuildContext context) =>
                const AlertDialog(
                  title: Text('Copied, but also showed this dialog.'),
                ),
            );
          )
        },
      );
    }
    return AdaptiveTextSelectionToolbar.buttonItems(
      anchors: editableTextState.contextMenuAnchors,
      buttonItems: buttonItems,
    );
  },
)
```

A full example of modifying a built-in context menu action can be found in the samples repository in [modified\_action\_page.dart](https://github.com/flutter/samples/blob/main/context_menus/lib/modified_action_page.dart) on GitHub.

### [`buildToolbar`](https://api.flutter.dev/flutter/widgets/TextSelectionControls/buildToolbar.html)

[#](#buildtoolbar)

This function generated the context menu widget similarly to `contextMenuBuilder`, but required more setup to use. Before this change, you might have been overriding `buildToolbar` as a part of `TextSelectionControls`, like this:

dart

```
// Deprecated.
class _MyMaterialTextSelectionControls extends MaterialTextSelectionControls {
  @override
  Widget buildToolbar(
    BuildContext context,
    Rect globalEditableRegion,
    double textLineHeight,
    Offset selectionMidpoint,
    List<TextSelectionPoint> endpoints,
    TextSelectionDelegate delegate,
    ClipboardStatusNotifier clipboardStatus,
    Offset lastSecondaryTapDownPosition,
  ) {
    return _MyCustomToolbar();
  },
}
```

Now you can simply use `contextMenuBuilder` directly as a parameter to `TextField` (and others). The information provided in the parameters to `buildToolbar` can be obtained from the `EditableTextState` that is passed to `contextMenuBuilder`.

The following example shows how to build a fully-custom toolbar from scratch while still using the default buttons.

dart

```
class _MyContextMenu extends StatelessWidget {
  const _MyContextMenu({
    required this.anchor,
    required this.children,
  });

  final Offset anchor;
  final List<Widget> children;

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Positioned(
          top: anchor.dy,
          left: anchor.dx,
          child: Container(
            width: 200,
            height: 200,
            color: Colors.amberAccent,
            child: Column(
              children: children,
            ),
          ),
        ),
      ],
    );
  }
}

class _MyTextField extends StatelessWidget {
  const _MyTextField();

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _controller,
      maxLines: 4,
      minLines: 2,
      contextMenuBuilder: (context, editableTextState) {
        return _MyContextMenu(
          anchor: editableTextState.contextMenuAnchors.primaryAnchor,
          children: AdaptiveTextSelectionToolbar.getAdaptiveButtons(
            context,
            editableTextState.contextMenuButtonItems,
          ).toList(),
        );
      },
    );
  }
}
```

A full example of building a custom context menu can be found in the samples repository in [`custom_menu_page.dart`](https://github.com/flutter/samples/blob/main/context_menus/lib/custom_menu_page.dart) on GitHub.

Timeline
--------

[#](#timeline)

Landed in version: 3.6.0-0.0.pre  
 In stable release: 3.7.0

References
----------

[#](#references)

API documentation:

* [`TextField.contextMenuBuilder`](https://api.flutter.dev/flutter/material/TextField/contextMenuBuilder.html)* [`AdaptiveTextSelectionToolbar`](https://api.flutter.dev/flutter/material/AdaptiveTextSelectionToolbar-class.html)

Relevant issues:

* [Simple custom text selection toolbars](https://github.com/flutter/flutter/issues/73574)* [Right click menu outside of text fields](https://github.com/flutter/flutter/issues/98272)* [Text editing for desktop - stable](https://github.com/flutter/flutter/issues/90563)* [Ability to disable context menu on TextFields](https://github.com/flutter/flutter/issues/79796)* [Missing APIs for text selection toolbar styling](https://github.com/flutter/flutter/issues/22210)* [Enable copy toolbar in all widgets](https://github.com/flutter/flutter/issues/49996)* [Disable context menu from browser](https://github.com/flutter/flutter/issues/78671)* [Custom context menus don't show up for Flutter web](https://github.com/flutter/flutter/issues/84219)

Relevant PRs:

* [ContextMenus](https://github.com/flutter/flutter/pull/107193)* [Ability to disable the browser's context menu on web](https://github.com/flutter/flutter/pull/118194)* [Ability to disable the browser's context menu on web (engine)](https://github.com/flutter/engine/pull/38682)* [Custom context menus in SelectableRegion on web](https://github.com/flutter/flutter/pull/121653)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/context-menus/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/context-menus.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/context-menus/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/context-menus.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-21. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/context-menus.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/context-menus/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/context-menus.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   