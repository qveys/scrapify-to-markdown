
Deze browserversie wordt niet meer ondersteund. Upgrade naar een ondersteunde browser.

Flutter Deprecations Removed after 3.13

Tab

Extern

Delen

[Inloggen](https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&osid=1&continue=https://docs.google.com/spreadsheets/d/1zzyBRdIkqiEcpv_njEQA7pyG7X8PcNhvXFYrEAB8P78/edit?usp%3Dsharing&followup=https://docs.google.com/spreadsheets/d/1zzyBRdIkqiEcpv_njEQA7pyG7X8PcNhvXFYrEAB8P78/edit?usp%3Dsharing&ltmpl=sheets&ec=GAZAmwI)

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

Alleen bekijken

Bezig met laden...

|  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Publicly Shared |  | flutter.dev/go/deprecations-removed-after-3-13 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Deprecations to be removed from Flutter after 3.13 Release |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Tracking Issue: | https://github.com/flutter/flutter/issues/133171 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | Deprecation Policy: | https://github.com/flutter/flutter/wiki/Tree-hygiene#deprecation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | Announcement: | https://groups.google.com/g/flutter-announce/c/KQR0cV65IB8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | Cutoff: | Changes preceding 5/11/2021 (3.0 stable release) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | Full Migration Guide: | https://docs.flutter.dev/release/breaking-changes/3-13-deprecations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Package / Library | Deprecated in | Old API |  | New API | Removal PR | Notes | dart fix support |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 | flutter / material | v2.10 | DeletableChipAttributes | useDeleteButtonTooltip | deleteButtonTooltipMessage |  |  | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | v2.10 | Chip | useDeleteButtonTooltip | deleteButtonTooltipMessage |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 | v2.10 | RawChip | useDeleteButtonTooltip | deleteButtonTooltipMessage |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 | v2.10 | InputChip | useDeleteButtonTooltip | deleteButtonTooltipMessage |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 | v2.11 | MaterialButtonWithIconMixin |  | None | https://github.com/flutter/flutter/pull/133173 | This mixin no longer has an effect in the framework. | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 | v2.13 | MaterialScrollBehavior | androidOverscrollIndicator | ThemeData.useMaterial3 | https://github.com/flutter/flutter/pull/133181 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 | v2.13 | ThemeData | androidOverscrollIndicator | ThemeData.useMaterial3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 | flutter / painting | v2.13 | PaintingBinding | instantiateImageCodec | instantiateImageCodecFromBuffer | https://github.com/flutter/flutter/pull/132679 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | v2.13 | DecoderCallback |  | DecoderBufferCallback with ImageProvider.loadBuffer |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 | v2.13 | ImageProvider.load |  | Implement loadBuffer |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 | flutter / services | v2.11 | PlatformViewsService | synchronizeToNativeViewHierarchy | None | https://github.com/flutter/flutter/pull/133175 | No longer necessary for performance improvements. | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 | flutter / widgets | v2.12 | TextSelectionOverlay | fadeDuration | SelectionOverlay.fadeDuration |  |  | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 | v2.13 | ScrollBehavior | androidOverscrollIndicator | override ScrollBehavior.buildOverscrollIndicator | https://github.com/flutter/flutter/pull/133181 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 | flutter\_test | v2.11 | TestWindow | localeTestValue | WidgetTester.platformDispatcher.localeTestValue | https://github.com/flutter/flutter/pull/131098 |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 | v2.11 | TestWindow | clearLocaleTestValue | WidgetTester.platformDispatcher.clearLocaleTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 | v2.11 | TestWindow | localesTestValue | WidgetTester.platformDispatcher.localesTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 | v2.11 | TestWindow | clearLocalesTestValue | WidgetTester.platformDispatcher.clearLocalesTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 | v2.11 | TestWindow | initialLifecycleStateTestValue | WidgetTester.platformDispatcher.initialLifecycleStateTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | v2.11 | TestWindow | textScaleFactorTestValue | WidgetTester.platformDispatcher.textScaleFactorTestValue | https://github.com/flutter/flutter/pull/133176 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 | v2.11 | TestWindow | clearTextScaleFactorTestValue | WidgetTester.platformDispatcher.clearTextScaleFactorTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 | v2.11 | TestWindow | platformBrightnessTestValue | WidgetTester.platformDispatcher.platformBrightnessTestValue | https://github.com/flutter/flutter/pull/133178 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 | v2.11 | TestWindow | clearPlatformBrightnessTestValue | WidgetTester.platformDispatcher.clearPlatformBrightnessTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 | v2.11 | TestWindow | alwaysUse24HourFormatTestValue | WidgetTester.platformDispatcher.alwaysUse24HourFormatTestValue | https://github.com/flutter/flutter/pull/131098 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 | v2.11 | TestWindow | clearAlwaysUse24HourTestValue | WidgetTester.platformDispatcher.clearAlwaysUse24HourTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 | v2.11 | TestWindow | brieflyShowPasswordTestValue | WidgetTester.platformDispatcher.brieflyShowPasswordTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 | v2.11 | TestWindow | defaultRouteNameTestValue | WidgetTester.platformDispatcher.defaultRouteNameTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 38 | v2.11 | TestWindow | clearDefaultRouteNameTestValue | WidgetTester.platformDispatcher.clearDefaultRouteNameTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 39 | v2.11 | TestWindow | semanticsEnabledTestValue | WidgetTester.platformDispatcher.semanticsEnabledTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | v2.11 | TestWindow | clearSemanticsEnabledTestValue | WidgetTester.platformDispatcher.clearSemanticsEnabledTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 41 | v2.11 | TestWindow | accessibilityFeaturesTestValue | WidgetTester.platformDispatcher.accessibilityFeaturesTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 | v2.11 | TestWindow | clearAccessibilityFeaturesTestValue | WidgetTester.platformDispatcher.clearAccessibilityFeaturesTestValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 | v2.11 | TestWindow & TestPlatformDispatcher | onPlatformMessage (getter) | ServicesBinding.instance.channelBuffers.push | https://github.com/flutter/flutter/pull/133183 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 | v2.11 | TestWindow & TestPlatformDispatcher | onPlatformMessage (setter) | ServicesBinding.instance.defaultBinaryMessenger.setMessageHandler |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
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