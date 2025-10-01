Using HTML slots to render platform views in the web
====================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Using HTML slots to render platform views in the web](/release/breaking-changes/platform-views-using-html-slots-web)

Summary
-------

[#](#summary)

Flutter now renders all web platform views in a consistent location of the DOM, as direct children of `flt-glass-pane` (regardless of the rendering backend: `html` or `canvaskit`). Platform views are then *"slotted"* into the correct position of the App's DOM with standard HTML features.

Up until this change, Flutter web would change the styling of the rendered contents of a platform views to position/size it to the available space. **This is no longer the case.** Users can now decide how they want to utilize the space allocated to their platform view by the framework.

Context
-------

[#](#context)

The Flutter framework frequently tweaks its render tree to optimize the paint operations that are ultimately made per frame. In the web, these render tree changes often result in DOM operations.

Flutter web used to render its platform views ([`HtmlElementView` widgets](https://api.flutter.dev/flutter/widgets/HtmlElementView-class.html)) directly into its corresponding position of the DOM.

Using certain DOM elements as the "target" of some DOM operations causes those elements to lose their internal state. In practice, this means that `iframe` tags are going to reload, `video` players might restart, or an editable form might lose its edits.

Flutter now renders platform views using [slot elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot) inside of a single, app-wide [shadow root](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot). Slot elements can be added/removed/moved around the Shadow DOM without affecting the underlying slotted content (which is rendered in a constant location)

This change was made to:

* Stabilize the behavior of platform views in Flutter web.* Unify how platform views are rendered in the web for both rendering backends (`html` and `canvaskit`).* Provide a predictable location in the DOM that allows developers to reliably use CSS to style their platform views, and to use other standard DOM API, such as `querySelector`, and `getElementById`.

Description of change
---------------------

[#](#description-of-change)

A Flutter web app is now rendered inside a common [shadow root](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot) in which [slot elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot) represent platform views. The actual content of each platform view is rendered as a **sibling of said shadow root**.

### Before

[#](#before)

html

```
...

<flt-glass-pane>
  ...
  <div id="platform-view">Contents</div> <!-- canvaskit -->
  <!-- OR -->
  <flt-platform-view>
    #shadow-root
    | <div id="platform-view">Contents</div> <!-- html -->
  </flt-platform-view>
  ...
</flt-glass-pane>

...
```

### After

[#](#after)

html

```
...

<flt-glass-pane>
  #shadow-root
  | ...
  | <flt-platform-view-slot>
  |   <slot name="platform-view-1" />
  | </flt-platform-view-slot>
  | ...
  <flt-platform-view slot="platform-view-1">
    <div id="platform-view">Contents</div>
  </flt-platform-view>
  ...
</flt-glass-pane>

...
```

After this change, when the framework needs to move DOM nodes around, it operates over `flt-platform-view-slot`s, which only contain a `slot` element. The slot *projects* the contents defined in `flt-platform-view` elements outside the shadow root. `flt-platform-view` elements are never the target of DOM operations from the framework, thus preventing the reload issues.

From an app's perspective, this change is transparent. **However**, this is considered a *breaking change* because some tests make assumptions about the internal DOM of a Flutter web app, and break.

Migration guide
---------------

[#](#migration-guide)

### Code

[#](#code)

The engine may print a warning message to the console similar to:

bash

```
Height of Platform View type: [$viewType] may not be set. Defaulting to `height: 100%`.
Set `style.height` to any appropriate value to stop this message.
```

or:

bash

```
Width of Platform View type: [$viewType] may not be set. Defaulting to `width: 100%`.
Set `style.width` to any appropriate value to stop this message.
```

Previously, the content returned by [`PlatformViewFactory` functions](https://github.com/flutter/engine/blob/58459a5e342f84c755919f2ad5029b22bcddd548/lib/web_ui/lib/src/engine/platform_views/content_manager.dart#L15-L18) was resized and positioned by the framework. Instead, Flutter now sizes and positions `<flt-platform-view-slot>`, which is the parent of the slot where the content is projected.

To stop the warning above, platform views need to set the `style.width` and `style.height` of their root element to any appropriate (non-null) value.

For example, to make the root `html.Element` fill all the available space allocated by the framework, set its `style.width` and `style.height` properties to `'100%'`:

dart

```
ui.platformViewRegistry.registerViewFactory(viewType, (int viewId) {
  final html.Element htmlElement = html.DivElement()
    // ..other props
    ..style.width = '100%'
    ..style.height = '100%';
  // ...
  return htmlElement;
});
```

If other techniques are used to lay out the platform view (like `inset: 0`) a value of `auto` for `width` and `height` is enough to stop the warning.

Read more about [`CSS width`](https://developer.mozilla.org/en-US/docs/Web/CSS/width) and [`CSS height`](https://developer.mozilla.org/en-US/docs/Web/CSS/height).

### Tests

[#](#tests)

After this change, user's test code does **not** need to deeply inspect the contents of the shadow root of the App. All of the platform view contents will be placed as direct children of `flt-glass-pane`, wrapped in a `flt-platform-view` element.

Avoid looking inside the `flt-glass-pane` shadow root, it is considered a **"private implementation detail"**, and its markup can change at any time, without notice.

(See Relevant PRs below for examples of the "migrations" described above).

Timeline
--------

[#](#timeline)

Landed in version: 2.3.0-16.0.pre  
 In stable release: 2.5

References
----------

[#](#references)

Design document:

* [Using slot to embed web Platform Views](/go/web-slot-content)

Relevant issues:

* [Issue #80524](https://github.com/flutter/flutter/issues/80524)

Relevant PRs:

* [flutter/engine#25747](https://github.com/flutter/engine/pull/25747): Introduces the feature.* [flutter/flutter#82926](https://github.com/flutter/flutter/pull/82926): Tweaks `flutter` tests.* [flutter/plugins#3964](https://github.com/flutter/plugins/pull/3964): Tweaks to `plugins` code.* [flutter/packages#364](https://github.com/flutter/packages/pull/364): Tweaks to `packages` code.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/platform-views-using-html-slots-web/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/platform-views-using-html-slots-web.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/platform-views-using-html-slots-web/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/platform-views-using-html-slots-web.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/platform-views-using-html-slots-web.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/platform-views-using-html-slots-web/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/platform-views-using-html-slots-web.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   