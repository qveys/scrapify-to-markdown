Performance
===========

1. [Performance](/perf)

[Watch on YouTube in a new tab: "Flutter performance tips | Flutter in Focus"](https://www.youtube.com/watch/PKGguGUwSYE)

*info* Note

If your app has a performance issue and you are trying to debug it, check out the DevTool's page on [Using the Performance view](/tools/devtools/performance).

What is performance? Why is performance important? How do I improve performance?

Our goal is to answer those three questions (mainly the third one), and anything related to them. This document should serve as the single entry point or the root node of a tree of resources that addresses any questions that you have about performance.

The answers to the first two questions are mostly philosophical, and not as helpful to many developers who visit this page with specific performance issues that need to be solved. Therefore, the answers to those questions are in the [appendix](/perf/appendix).

To improve performance, you first need metrics: some measurable numbers to verify the problems and improvements. In the [metrics](/perf/metrics) page, you'll see which metrics are currently used, and which tools and APIs are available to get the metrics.

There is a list of [Frequently asked questions](/perf/faq), so you can find out if the questions you have or the problems you're having were already answered or encountered, and whether there are existing solutions. (Alternatively, you can check the Flutter GitHub issue database using the [performance](https://github.com/flutter/flutter/issues?q=+label%3A%22severe%3A+performance%22) label.)

Finally, the performance issues are divided into four categories. They correspond to the four labels that are used in the Flutter GitHub issue database: "[perf: speed](https://github.com/flutter/flutter/issues?q=is%3Aopen+label%3A%22perf%3A+speed%22+sort%3Aupdated-asc+)", "[perf: memory](https://github.com/flutter/flutter/issues?q=is%3Aopen+label%3A%22perf%3A+memory%22+sort%3Aupdated-asc+)", "[perf: app size](https://github.com/flutter/flutter/issues?q=is%3Aopen+label%3A%22perf%3A+app+size%22+sort%3Aupdated-asc+)", "[perf: energy](https://github.com/flutter/flutter/issues?q=is%3Aopen+label%3A%22perf%3A+energy%22+sort%3Aupdated-asc+)".

The rest of the content is organized using those four categories.

Speed
-----

[#](#speed)

Are your animations janky (not smooth)? Learn how to evaluate and fix rendering issues.

[Improving rendering performance](/perf/rendering-performance)

App size
--------

[#](#app-size)

How to measure your app's size. The smaller the size, the quicker it is to download.

[Measuring your app's size](/perf/app-size)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/index.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/index.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-07-06. [View source](https://github.com/flutter/website/tree/main/src/content/perf/index.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/index.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   