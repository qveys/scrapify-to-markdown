
Deze browserversie wordt niet meer ondersteund. Upgrade naar een ondersteunde browser.

Flutter Deprecations Removed after 2.10

Tab

Extern

Delen

[Inloggen](https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&osid=1&continue=https://docs.google.com/spreadsheets/d/12krawYCu6X_g_5wLGpmiAIi-VcTRV6xG7RGbRovuatQ/edit?usp%3Dsharing&followup=https://docs.google.com/spreadsheets/d/12krawYCu6X_g_5wLGpmiAIi-VcTRV6xG7RGbRovuatQ/edit?usp%3Dsharing&ltmpl=sheets&ec=GAZAmwI)

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

|  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Publicly Shared |  | flutter.dev/go/deprecations-removed-after-2-10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Deprecations to be removed from Flutter after 2.10 Release |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Tracking Issue: | https://github.com/flutter/flutter/issues/98537 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | Deprecation Policy: | https://github.com/flutter/flutter/wiki/Tree-hygiene#deprecation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | Announcement: | https://groups.google.com/g/flutter-announce/c/gq1dAIBXW9A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | Cutoff: | Changes preceding 3/3/2021 (2.0 stable release) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | Full Migration Guide: | https://docs.flutter.dev/release/breaking-changes/2-10-deprecations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Library/Package | Deprecated in | Old API |  | New API | Removal PR | Notes | dart fix support |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 | Cupertino | v1.25 | CupertinoTextField | maxLengthEnforced | maxLengthEnforcement | https://github.com/flutter/flutter/pull/98539 | https://docs.flutter.dev/release/breaking-changes/use-maxLengthEnforcement-instead-of-maxLengthEnforced | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | Gestures | v1.22 | VelocityTracker() |  | VelocityTracker.withKind | https://github.com/flutter/flutter/pull/98541 |  | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 | Material | v1.26 | DayPicker | whole class | CalendarDatePicker | https://github.com/flutter/flutter/pull/98543 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 |  | v1.26 | MonthPicker | whole class | CalendarDatePicker |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 |  | v1.26 | FlatButton | whole class | TextButton | https://github.com/flutter/flutter/pull/98545 | https://docs.flutter.dev/release/breaking-changes/buttons | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 |  | v1.26 | OutlineButton | whole class | OutlinedButton | https://github.com/flutter/flutter/pull/98546 | https://docs.flutter.dev/release/breaking-changes/buttons | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 |  | v1.26 | RaisedButton | whole class | ElevatedButton | https://github.com/flutter/flutter/pull/98547 | https://docs.flutter.dev/release/breaking-changes/buttons | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 |  | v1.23 | Scaffold | showSnackBar | ScaffoldMessenger.showSnackBar | https://github.com/flutter/flutter/pull/98549 | https://docs.flutter.dev/release/breaking-changes/scaffold-messenger | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 |  | v1.23 | Scaffold | removeCurrentSnackBar | ScaffoldMessenger.removeCurrentSnackBar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 |  | v1.23 | Scaffold | hideCurrentSnackBar | ScaffoldMessenger.hideCurrentSnackBar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 |  | v1.26 | RectangularSliderTrackShape | disabledThumbGapWidth | None | https://github.com/flutter/flutter/pull/98613 |  | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 |  | v1.25 | TextField | maxLengthEnforced | maxLengthEnforcement | https://github.com/flutter/flutter/pull/98539 | https://docs.flutter.dev/release/breaking-changes/use-maxLengthEnforcement-instead-of-maxLengthEnforced | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 |  | v1.25 | TextFormField | maxLengthEnforced | maxLengthEnforcement |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 |  | v1.23 | ThemeData | useTextSelectionTheme | None | https://github.com/flutter/flutter/pull/98578 | https://docs.flutter.dev/release/breaking-changes/text-selection-theme | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 |  | v1.26 | ThemeData | textSelectionColor | TextSelectionThemeData.selectionColor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 |  | v1.26 | ThemeData | cursorColor | TextSelectionThemeData.cursorColor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 |  | v1.26 | ThemeData | textSelectionHandleColor | TextSelectionThemeData.selectionHandleColor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 | Rendering | v1.26 | RenderEditable | onSelectionChanged | textSelectionDelegate.userUpdateTextEditingValue | https://github.com/flutter/flutter/pull/98582 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 |  | v1.22 | Overflow | enum | Removed from framework, use Clip enum for clipBehavior | https://github.com/flutter/flutter/pull/98583 | https://docs.flutter.dev/release/breaking-changes/clip-behavior | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 | Semantics | v1.26 | UpdateLiveRegionEvent |  | None | https://github.com/flutter/flutter/pull/98615 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 | Services | v1.26 | TextSelectionDelegate | textEditingValue | userUpdateTextEditingValue | https://github.com/flutter/flutter/pull/98582 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 | Widgets | v1.22 | Stack | overflow | clipBehavior | https://github.com/flutter/flutter/pull/98583 | https://docs.flutter.dev/release/breaking-changes/clip-behavior | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 |  | v1.21 | RenderObjectElement | insertChildRenderObject | insertRenderObjectChild | https://github.com/flutter/flutter/pull/98616 |  | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 |  | v1.21 | RenderObjectElement | moveChildRenderObject | moveRenderObjectChild |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 |  | v1.21 | RenderObjectElement | removeChildRenderObject | removeRenderObjectChild |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 38 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 39 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 45 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 46 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 47 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 48 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 49 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 52 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 53 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 54 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 56 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 57 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 58 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 59 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 61 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 62 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 63 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 65 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 66 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 67 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 68 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 69 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 70 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 71 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 72 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 73 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 74 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 76 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 77 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 78 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 79 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 81 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 82 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 83 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 84 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 87 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 88 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 89 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 91 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 92 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 93 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 94 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 95 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 96 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 97 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 98 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 99 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| De koersen zijn niet voor alle markten beschikbaar en kunnen met 20 minuten vertraging worden weergegeven. De informatie wordt in de huidige staat aangeboden en is alleen bedoeld ter informatie, niet voor handelsdoeleinden of advies. [Disclaimer](http://www.google.com/googlefinance/disclaimer/) | | | | |
|  |  | Sheet1 |  |  |

Er is een browserfout opgetreden.  
 Houd de Shift-toets ingedrukt en druk op de knop 'Vernieuwen' om het nogmaals te proberen.