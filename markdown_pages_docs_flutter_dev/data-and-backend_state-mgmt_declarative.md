Start thinking declaratively
============================

1. [Data & backend](/data-and-backend) chevron\_right- [State management](/data-and-backend/state-mgmt) chevron\_right- [Start thinking declaratively](/data-and-backend/state-mgmt/declarative)

If you're coming to Flutter from an imperative framework (such as Android SDK or iOS UIKit), you need to start thinking about app development from a new perspective.

Many assumptions that you might have don't apply to Flutter. For example, in Flutter it's okay to rebuild parts of your UI from scratch instead of modifying it. Flutter is fast enough to do that, even on every frame if needed.

Flutter is *declarative*. This means that Flutter builds its user interface to reflect the current state of your app:

![A mathematical formula of UI = f(state). 'UI' is the layout on the screen. 'f' is your build methods. 'state' is the application state.](/assets/images/docs/development/data-and-backend/state-mgmt/ui-equals-function-of-state.png)

When the state of your app changes (for example, the user flips a switch in the settings screen), you change the state, and that triggers a redraw of the user interface. There is no imperative changing of the UI itself (like `widget.setText`)—you change the state, and the UI rebuilds from scratch.

Read more about the declarative approach to UI programming in the [get started guide](/get-started/flutter-for/declarative).

The declarative style of UI programming has many benefits. Remarkably, there is only one code path for any state of the UI. You describe what the UI should look like for any given state, once—and that is it.

At first, this style of programming might not seem as intuitive as the imperative style. This is why this section is here. Read on. [chevron\_left

Previous Intro](/data-and-backend/state-mgmt)[Next Ephemeral versus app state

chevron\_right](/data-and-backend/state-mgmt/ephemeral-vs-app) 

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/data-and-backend/state-mgmt/declarative/&page-source=https://github.com/flutter/website/tree/main/src/content/data-and-backend/state-mgmt/declarative.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/data-and-backend/state-mgmt/declarative/&page-source=https://github.com/flutter/website/tree/main/src/content/data-and-backend/state-mgmt/declarative.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-10. [View source](https://github.com/flutter/website/tree/main/src/content/data-and-backend/state-mgmt/declarative.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/data-and-backend/state-mgmt/declarative/&page-source=https://github.com/flutter/website/tree/main/src/content/data-and-backend/state-mgmt/declarative.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   