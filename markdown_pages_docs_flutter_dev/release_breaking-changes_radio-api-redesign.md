Redesigned the Radio widget
===========================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Redesigned the Radio widget](/release/breaking-changes/radio-api-redesign)

Summary
-------

[#](#summary)

Introduced the `RadioGroup` widget to centralize `groupValue` management and the `onChanged` callback for a set of `Radio` widgets. As a result, the individual `Radio.groupValue` and `Radio.onChanged` properties have been deprecated.

Context
-------

[#](#context)

To meet APG (ARIA Practices Guide) requirements for keyboard navigation and semantic properties in radio button groups, Flutter needed a dedicated radio group concept. Introducing a wrapper widget, `RadioGroup`, provides this out-of-the-box support. This change also presented an opportunity to simplify the API for individual `Radio` widgets.

Description of change
---------------------

[#](#description-of-change)

The following API is deprecated:

* `Radio.onChanged`* `Radio.groupValue`* `CupertinoRadio.onChanged`* `CupertinoRadio.groupValue`* `RadioListTile.groupValue`* `RadioListTile.onChanged`.

Migration guide
---------------

[#](#migration-guide)

If you are using these properties, you can refactor them with `RadioGroup`.

### Case 1: trivial case

[#](#case-1-trivial-case)

Code before migration:

dart

```
Widget build(BuildContext context) {
  return Column(
    children: <Widget>[
      Radio<int>(
        value: 0,
        groupValue: _groupValue,
        onChanged: (int? value) {
          setState(() {
            _groupValue = value;
          });
        },
      ),
      Radio<int>(
        value: 2,
        groupValue: _groupValue,
        onChanged: (int? value) {
          setState(() {
            _groupValue = value;
          });
        },
      ),
    ],
  );
}
```

Code after migration:

dart

```
Widget build(BuildContext context) {
  return RadioGroup<int>(
    groupValue: _groupValue,
    onChanged: (int? value) {
      setState(() {
        _groupValue = value;
      });
    },
    child: Column(
      children: <Widget>[
        Radio<int>(value: 0),
        Radio<int>(value: 2),
      ],
    ),
  );
}
```

### Case 2: disabled radio

[#](#case-2-disabled-radio)

Code before migration:

dart

```
Widget build(BuildContext context) {
  return Column(
    children: <Widget>[
      Radio<int>(
        value: 0,
        groupValue: _groupValue,
        onChanged: (int? value) {
          setState(() {
            _groupValue = value;
          });
        },
      ),
      Radio<int>(
        value: 2,
        groupValue: _groupValue,
        onChanged: null, // disabled
      ),
    ],
  );
}
```

Code after migration:

dart

```
Widget build(BuildContext context) {
  return RadioGroup<int>(
    groupValue: _groupValue,
    onChanged: (int? value) {
      setState(() {
        _groupValue = value;
      });
    },
    child: Column(
      children: <Widget>[
        Radio<int>(value: 0),
        Radio<int>(value: 2, enabled: false),
      ],
    ),
  );
}
```

### Case 3: mixed group or multi-selection

[#](#case-3-mixed-group-or-multi-selection)

Code before migration:

dart

```
Widget build(BuildContext context) {
  return Column(
    children: <Widget>[
      Radio<int>(
        value: 1,
        groupValue: _groupValue,
        onChanged: (int? value) {
          setState(() {
            _groupValue = value;
          });
        }, // disabled
      ),
      Radio<String>(
        value: 'a',
        groupValue: _stringValue,
        onChanged: (String? value) {
          setState(() {
            _stringValue = value;
          });
        },
      ),
      Radio<String>(
        value: 'b',
        groupValue: _stringValue,
        onChanged: (String? value) {
          setState(() {
            _stringValue = value;
          });
        },
      ),
      Radio<int>(
        value: 2,
        groupValue: _groupValue,
        onChanged: (int? value) {
          setState(() {
            _groupValue = value;
          });
        }, // disabled
      ),
    ],
  );
}
```

Code after migration:

dart

```
Widget build(BuildContext context) {
  return RadioGroup<int>(
    groupValue: _groupValue,
    onChanged: (int? value) {
      setState(() {
        _groupValue = value;
      });
    },
    child: Column(
      children: <Widget>[
        Radio<int>(value: 1),
        RadioGroup<String>(
          child: Column(
            children: <Widget>[
              Radio<String>(value: 'a'),
              Radio<String>(value: 'b'),
            ]
          ),
        ),
        Radio<int>(value: 2),
      ],
    ),
  );
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.34.0-0.0.pre  
 In stable release: 3.35

References
----------

[#](#references)

* [`APG`](https://www.w3.org/WAI/ARIA/apg/patterns/radio)

API documentation:

* [`Radio`](https://api.flutter.dev/flutter/material/Radio-class.html)* [`CupertinoRadio`](https://api.flutter.dev/flutter/cupertino/CupertinoRadio-class.html)* [`RadioListTile`](https://api.flutter.dev/flutter/material/RadioListTile-class.html)* [`RadioGroup`](https://api.flutter.dev/flutter/widgets/RadioGroup-class.html)

Relevant issue:

* [Issue 113562](https://github.com/flutter/flutter/issues/113562)

Relevant PR:

* [PR 168161](https://github.com/flutter/flutter/pull/168161)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/radio-api-redesign/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/radio-api-redesign.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/radio-api-redesign/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/radio-api-redesign.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/radio-api-redesign.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/radio-api-redesign/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/radio-api-redesign.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   