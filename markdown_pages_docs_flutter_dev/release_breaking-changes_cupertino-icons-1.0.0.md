New CupertinoIcons has icon glyph changes
=========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [New CupertinoIcons has icon glyph changes](/release/breaking-changes/cupertino-icons-1.0.0)

Summary
-------

[#](#summary)

The existing cupertino\_icons [0.1.3 icons](https://raw.githubusercontent.com/flutter/cupertino_icons/master/map.png) are based on iOS 11 aesthetics with sharp angles and thin lines.

As Apple's iconography updates with new OS versions, the `cupertino_icons` package is also refreshed.

Generally, all previous glyphs referenced from the [`CupertinoIcons`](https://api.flutter.dev/flutter/cupertino/CupertinoIcons-class.html) API are automatically mapped to very similar looking icons in the new SF Symbols style (featuring rounder, thicker lines).

Some icons that have no equivalents in the new SF Symbols style are left as is.

Some icons that have less variation (such as thickness, alternative looks, and so on) are automapped and collapsed to the best matching variation in the new SF Symbols style but should be double checked to determine whether they preserve the intended visual effect.

Description of change
---------------------

[#](#description-of-change)

The new `cupertino_icons 1.0.0` font is handcrafted to best preserve the intent and aesthetic of the symbology through the transition. All existing `CupertinoIcons`' static `IconData` fields (and thus all of the font `.ttf`'s codepoints) continue to work and point to a reasonable new icon.

The new cupertino\_icons 1.0.0 package also has ~1,000 more icons to choose from.

### Unchanged icons

[#](#unchanged-icons)

No SF Symbols styled alternatives exist for the icons in the following list. The previous cupertino\_icons 0.1.3 icons have been kept as is in 1.0.0.

* bluetooth* bus* car* car\_detailed* chevron\_back* chevron\_forward* lab\_flask* lab\_flask\_solid* news* news\_solid* train\_style\_one* train\_style\_two

### Merged icons

[#](#merged-icons)

Icons within the same group are now the exact same icon in 1.0.0. In other words, the distinctions between those icon variations that existed in 0.1.3 is lost and now renders the same SF Symbols styled icon that represents the theme of the group.

This affects the following icon groups:

* share, share\_up* battery\_charging, battery\_full, battery\_75\_percent* shuffle, shuffle\_medium, shuffle\_thick* delete, delete\_simple* refresh, refresh\_thin, refresh\_thick* clear, clear\_thick* clear\_circled\_solid, clear\_thick\_circled* gear, gear\_alt, gear\_big* loop, loop\_thick* time\_solid, clock\_solid* time, clock* tag, tags* tag\_solid, tags\_solid

This is mainly due to some artistic liberties taken when creating the original `cupertino_icons` set that no longer match the variations diversity of the more formal SF Symbols icon set for some of the icons.

Migration guide
---------------

[#](#migration-guide)

After upgrading to 1.22, if you also upgrade the `cupertino_icons` pubspec dependency from 0.1.3 to 1.0.0, for example, by changing:

yaml

```
dependencies:
  ... // Other dependencies
  cupertino_icons: ^0.1.0
```

to:

yaml

```
dependencies:
  ... // Other dependencies
  cupertino_icons: ^1.0.0
```

All your `CupertinoIcons` should automatically update to the new aesthetic (except for the [unchanged icons](#unchanged-icons) listed above).

At this point, you can also explore [`CupertinoIcons`](https://api.flutter.dev/flutter/cupertino/CupertinoIcons-class.html) for new icons to use in your application.

You're encouraged to verify your application after migrating to ensure that the automatically mapped new icons are suitable for your desired aesthetics.

Timeline
--------

[#](#timeline)

Landed in: 1.22.0-10.0.pre.65  
 In stable release: 1.22

References
----------

[#](#references)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/cupertino-icons-1.0.0/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-icons-1.0.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/cupertino-icons-1.0.0/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-icons-1.0.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-icons-1.0.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/cupertino-icons-1.0.0/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-icons-1.0.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   