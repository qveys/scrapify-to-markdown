Use the Debug console
=====================

1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [Use the Debug console](/tools/devtools/console)

The DevTools Debug console allows you to watch an application's standard output (`stdout`), evaluate expressions for a paused or running app in debug mode, and analyze inbound and outbound references for objects.

*info* Note

This page is up to date for DevTools 2.23.0.

The Debug console is available from the [Inspector](/tools/devtools/inspector), [Debugger](/tools/devtools/debugger), and [Memory](/tools/devtools/memory) views.

Watch application output
------------------------

[#](#watch-application-output)

The console shows the application's standard output (`stdout`):

![Screenshot of stdout in Console view](/assets/images/docs/tools/devtools/console-stdout.png)

Explore inspected widgets
-------------------------

[#](#explore-inspected-widgets)

If you click a widget on the **Inspector** screen, the variable for this widget displays in the **Console**:

![Screenshot of inspected widget in Console view](/assets/images/docs/tools/devtools/console-inspect-widget.png)

Evaluate expressions
--------------------

[#](#evaluate-expressions)

In the console, you can evaluate expressions for a paused or running application, assuming that you are running your app in debug mode:

![Screenshot showing evaluating an expression in the console](/assets/images/docs/tools/devtools/console-evaluate-expressions.png)

To assign an evaluated object to a variable, use `$0`, `$1` (through `$5`) in the form of `var x = $0`:

![Screenshot showing how to evaluate variables](/assets/images/docs/tools/devtools/console-evaluate-variables.png)

Browse heap snapshot
--------------------

[#](#browse-heap-snapshot)

To drop a variable to the console from a heap snapshot, do the following:

1. Navigate to **Devtools > Memory > Diff Snapshots**.- Record a memory heap snapshot.- Click on the context menu `[⋮]` to view the number of **Instances** for the desired **Class**.- Select whether you want to store a single instance as a console variable, or whether you want to store *all* currently alive instances in the app.

![Screenshot showing how to browse the heap snapshots](/assets/images/docs/tools/devtools/browse-heap-snapshot.png)

The Console screen displays both live and static inbound and outbound references, as well as field values:

![Screenshot showing inbound and outbound references in Console](/assets/images/docs/tools/devtools/console-references.png)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/console/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/console.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/console/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/console.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-09. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/console.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/console/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/console.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   