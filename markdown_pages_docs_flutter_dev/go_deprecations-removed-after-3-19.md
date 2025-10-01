
Deze browserversie wordt niet meer ondersteund. Upgrade naar een ondersteunde browser.

Flutter Deprecations Removed after 3.19

Tab

Extern

Delen

[Inloggen](https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&osid=1&continue=https://docs.google.com/spreadsheets/d/1x_UJ7GiB61ByBo6cPLm_JfLrgFqAfkQo7pPK_lHvsUo/edit?usp%3Dsharing&followup=https://docs.google.com/spreadsheets/d/1x_UJ7GiB61ByBo6cPLm_JfLrgFqAfkQo7pPK_lHvsUo/edit?usp%3Dsharing&ltmpl=sheets&ec=GAZAmwI)

Bestand

Bewerken

Bekijken

Invoegen

Opmaak

Gegevens

Extra

Uitbreidingen

Hulp

Toegankelijkheid

Foutopsporing

Niet-opgeslagen wijzigingen in Drive

Toegankelijkheid

Alleen reageren

Bezig met laden...

|  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Publicly Shared |  | flutter.dev/go/deprecations-removed-after-3-19 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Deprecations to be removed from Flutter after 3.19 Release - see significant migration below. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Tracking Issue: | https://github.com/flutter/flutter/issues/143956 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | Deprecation Policy: | https://github.com/flutter/flutter/wiki/Tree-hygiene#deprecation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | Announcement: | https://groups.google.com/g/flutter-announce/c/8XjXpUKlnf8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | Cutoff: | Changes preceding 1/24/2023 (3.7 stable release) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | Full Migration Guide: | TBA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Package / Library | Old API |  | New API | Deprecated In | dart fix support | Notes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 | flutter/cupertino | CupertinoContextMenu | previewBuilder | CupertinoContextMenu.builder | v3.4 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | flutter/material | TextTheme | headline1 | displayLarge | v3.1 | Yes | Carried over from last deprecation cycle. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 |  | TextTheme | headline2 | displayMedium | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 |  | TextTheme | headline3 | displaySmall | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 |  | TextTheme | headline4 | headlineMedium | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 |  | TextTheme | headline5 | headlineSmall | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 |  | TextTheme | headline6 | titleLarge | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 |  | TextTheme | subtitle1 | titleMedium | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 |  | TextTheme | subtitle2 | titleSmall | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 |  | TextTheme | bodyText1 | bodyLarge | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 |  | TextTheme | bodyText2 | bodyMedium | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 |  | TextTheme | caption | bodySmall | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 |  | TextTheme | button | labelLarge | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 |  | TextTheme | overline | labelSmall | v3.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 |  | ThemeData | errorColor | colorScheme.error | v3.3 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 |  | ThemeData | backgroundColor | colorScheme.background | v3.3 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 |  | ThemeData | bottomAppBarColor | BottomAppBarTheme.color | v3.3 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 |  | ThemeData | toggleableActiveColor | N/A, no longer used by the framework | v3.4 | Yes | https://docs.flutter.dev/release/breaking-changes/toggleable-active-color |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 |  | Scrollbar | showTrackOnHover | ScrollbarThemeData.trackVisibility | v3.4 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 |  | ScrollbarThemeData | showTrackOnHover | ScrollbarThemeData.trackVisibility | v3.4 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 | flutter/widgets | KeepAliveHandle | release | dispose | v3.3 | No | Dispose should already be called. If not, replace relase with a call to dispose. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 |  | InteractiveViewer | alignPanAxis | panAxis | v3.3 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 |  | MediaQuery | boldTextOverride | boldTextOf | v3.5 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 |  | AnimatedListItemBuilder |  | AnimatedItemBuilder | v3.5 | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 |  | AnimatedListRemovedItemBuilder |  | AnimatedRemovedItemBuilder | v3.5 | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 | flutter\_driver | FlutterDriver | enableAccessibility | setSemantics(true) | v2.3 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 38 |  | TimelineSummary | writeSummaryToFile | writeTimelineToFile | v2.1 | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 39 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | Significant Migration |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 41 | CupertinoTextField | toolbarOptions | See the full context menu migration guide:  https://docs.flutter.dev/release/breaking-changes/context-menus | v3.3 | Currently evaluating extension, developers are encouraged to migrate. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 | CupertinoTextFormFieldRow | toolbarOptions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 | CupertinoTextSelectionHandleControls | whole class |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 | SelectableText | toolbarOptions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 45 | TextField | toolbarOptions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 46 | TextFormField | toolbarOptions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 47 | MaterialTextSelectionHandleControls | whole class |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 48 | ToolbarOptions | whole class |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 49 | EditableText | toolbarOptions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 | SelectableRegionState | cutEnabled |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 51 | SelectableRegionState | pasteEnabled |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 52 | SelectableRegionState | copySelection |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 53 | SelectableRegionState | textEditingValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 54 | SelectableRegionState | bringIntoView |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 | SelectableRegionState | cutSelection |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 56 | SelectableRegionState | userUpdateTextEditingValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 57 | SelectableRegionState | pasteText |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 58 | EditableTextState | buttonItemsForToolbarOptions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 59 | TextSelectionControls | buildToolbar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 | TextSelectionControls | canCut |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 61 | TextSelectionControls | canCopy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 62 | TextSelectionControls | canPaste |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 63 | TextSelectionControls | canSelectAll |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 64 | TextSelectionControls | handleCut |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 65 | TextSelectionControls | handleCopy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 66 | TextSelectionControls | handlePaste |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 67 | TextSelectionControls | handleSelectAll |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 68 | plus subclasses: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 69 | CupertinoDesktopTextSelectionControls | buildToolbar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 70 | CupertinoDesktopTextSelectionControls | handleSelectAll |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 71 | MaterialTextSelectionControls | buildToolbar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 72 | MaterialTextSelectionControls | canSelectAll |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 73 | CupertinoTextSelectionControls | buildToolbar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 74 | DesktopTextSelectionControls | buildToolbar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 75 | DesktopTextSelectionControls | canSelectAll |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 76 | DesktopTextSelectionControls | handleSelectAll |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 77 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 78 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 79 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 81 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 82 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 83 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 84 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 87 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 88 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 89 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 91 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 92 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 93 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 94 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 95 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 96 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 97 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 98 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 99 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| De koersen zijn niet voor alle markten beschikbaar en kunnen met 20 minuten vertraging worden weergegeven. De informatie wordt in de huidige staat aangeboden en is alleen bedoeld ter informatie, niet voor handelsdoeleinden of advies. [Disclaimer](http://www.google.com/googlefinance/disclaimer/) | | | | |
|  |  | Sheet1 |  |  |

Er is een browserfout opgetreden.  
 Houd de Shift-toets ingedrukt en druk op de knop 'Vernieuwen' om het nogmaals te proberen.