The forgetChild() method must call super
========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [The forgetChild() method must call super](/release/breaking-changes/forgetchild-call-super)

Summary
-------

[#](#summary)

A recent global key duplication detection refactor now requires `Element` subclasses that override the `forgetChild()` to call `super()`.

Context
-------

[#](#context)

When encountering a global key duplication that will be cleaned up by an element rebuild later, we must not report global key duplication. Our previous implementation threw an error as soon as duplication was detected, and didn't wait for the rebuild if the element with the duplicated global key would have rebuilt.

The new implementation keeps track of all global key duplications during a build cycle, and only verifies global key duplication at the end of the that cycle instead of throwing an error immediately. As part of the refactoring, we implemented a mechanism to remove previous global key duplication in `forgetChild` if the rebuild had happened. This, however, requires all `Element` subclasses that override `forgetChild` to call the `super` method.

Description of change
---------------------

[#](#description-of-change)

The `forgetChild` of abstract class `Element` has a base implementation to remove global key reservation, and it is enforced by the `@mustCallSuper` meta tag. All subclasses that override the method have to call `super`; otherwise, the analyzer shows a linting error and global key duplication detection might throw an unexpected error.

Migration guide
---------------

[#](#migration-guide)

In the following example, an app's `Element` subclass overrides the `forgetChild` method.

Code before migration:

dart

```
class CustomElement extends Element {

    @override
    void forgetChild(Element child) {
        ...
    }
}
```

Code after migration:

dart

```
class CustomElement extends Element {

    @override
    void forgetChild(Element child) {
        ...
        super.forgetChild(child);
    }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`Element`](https://api.flutter.dev/flutter/widgets/Element-class.html)* [`forgetChild()`](https://api.flutter.dev/flutter/widgets/Element/forgetChild.html)

Relevant issues:

* [Issue 43780](https://github.com/flutter/flutter/issues/43780)

Relevant PRs:

* [PR 43790: Fix global key error](https://github.com/flutter/flutter/pull/46183)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/forgetchild-call-super/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/forgetchild-call-super.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/forgetchild-call-super/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/forgetchild-call-super.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/forgetchild-call-super.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/forgetchild-call-super/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/forgetchild-call-super.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   