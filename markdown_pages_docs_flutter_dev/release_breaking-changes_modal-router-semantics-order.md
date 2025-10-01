Semantics Order of the Overlay Entries in Modal Routes
======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Semantics Order of the Overlay Entries in Modal Routes](/release/breaking-changes/modal-router-semantics-order)

Summary
-------

[#](#summary)

We changed the semantics traverse order of the overlay entries in modal routes. Accessibility talk back or voice over now focuses the scope of a modal route first instead of its modal barrier.

Context
-------

[#](#context)

The modal route has two overlay entries, the scope and the modal barrier. The scope is the actual content of the modal route, and the modal barrier is the background of the route if its scope does not cover the entire screen. If the modal route returns true for `barrierDismissible`, the modal barrier becomes accessibility focusable because users can tap the modal barrier to pop the modal route. This change specifically made the accessibility to focus the scope first before the modal barrier.

Description of change
---------------------

[#](#description-of-change)

We added additional semantics node above both the overlay entries of modal routes. Those semantics nodes denote the semantics traverse order of these two overlay entries. This also changed the structure of semantics tree.

Migration guide
---------------

[#](#migration-guide)

If your tests start failing due to semantics tree changes after the update, you can migrate your code by expecting a new node on above of the modal route overlay entries.

Code before migration:

dart

```
import 'dart:ui';

import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/material.dart';

void main() {
  testWidgets('example test', (WidgetTester tester) async {
    final SemanticsHandle handle =
        tester.binding.pipelineOwner.ensureSemantics();

    // Build our app and trigger a frame.
    await tester.pumpWidget(MaterialApp(home: Scaffold(body: Text('test'))));

    final SemanticsNode root =
        tester.binding.pipelineOwner.semanticsOwner.rootSemanticsNode;

    final SemanticsNode firstNode = getChild(root);
    expect(firstNode.rect, Rect.fromLTRB(0.0, 0.0, 800.0, 600.0));

    // Fixes the test by expecting an additional node above the scope route.
    final SemanticsNode secondNode = getChild(firstNode);
    expect(secondNode.rect, Rect.fromLTRB(0.0, 0.0, 800.0, 600.0));

    final SemanticsNode thirdNode = getChild(secondNode);
    expect(thirdNode.rect, Rect.fromLTRB(0.0, 0.0, 800.0, 600.0));
    expect(thirdNode.hasFlag(SemanticsFlag.scopesRoute), true);

    final SemanticsNode forthNode = getChild(thirdNode);
    expect(forthNode.rect, Rect.fromLTRB(0.0, 0.0, 56.0, 14.0));
    expect(forthNode.label, 'test');
    handle.dispose();
  });
}

SemanticsNode getChild(SemanticsNode node) {
  SemanticsNode child;
  bool visiter(SemanticsNode target) {
    child = target;
    return false;
  }

  node.visitChildren(visiter);
  return child;
}
```

Code after migration:

dart

```
import 'dart:ui';

import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/material.dart';

void main() {
  testWidgets('example test', (WidgetTester tester) async {
    final SemanticsHandle handle =
        tester.binding.pipelineOwner.ensureSemantics();

    // Build our app and trigger a frame.
    await tester.pumpWidget(MaterialApp(home: Scaffold(body: Text('test'))));

    final SemanticsNode root =
        tester.binding.pipelineOwner.semanticsOwner.rootSemanticsNode;

    final SemanticsNode firstNode = getChild(root);
    expect(firstNode.rect, Rect.fromLTRB(0.0, 0.0, 800.0, 600.0));

    // Fixes the test by expecting an additional node above the scope route.
    final SemanticsNode secondNode = getChild(firstNode);
    expect(secondNode.rect, Rect.fromLTRB(0.0, 0.0, 800.0, 600.0));

    final SemanticsNode thirdNode = getChild(secondNode);
    expect(thirdNode.rect, Rect.fromLTRB(0.0, 0.0, 800.0, 600.0));
    expect(thirdNode.hasFlag(SemanticsFlag.scopesRoute), true);

    final SemanticsNode forthNode = getChild(thirdNode);
    expect(forthNode.rect, Rect.fromLTRB(0.0, 0.0, 56.0, 14.0));
    expect(forthNode.label, 'test');
    handle.dispose();
  });
}

SemanticsNode getChild(SemanticsNode node) {
  SemanticsNode child;
  bool visiter(SemanticsNode target) {
    child = target;
    return false;
  }

  node.visitChildren(visiter);
  return child;
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.19.0  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`ModalRoute`](https://api.flutter.dev/flutter/widgets/ModalRoute-class.html)* [`OverlayEntry`](https://api.flutter.dev/flutter/widgets/OverlayEntry-class.html)

Relevant issue:

* [Issue 46625](https://github.com/flutter/flutter/issues/46625)

Relevant PR:

* [PR 59290](https://github.com/flutter/flutter/pull/59290)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/modal-router-semantics-order/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/modal-router-semantics-order.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/modal-router-semantics-order/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/modal-router-semantics-order.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/modal-router-semantics-order.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/modal-router-semantics-order/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/modal-router-semantics-order.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   