
Deze browserversie wordt niet meer ondersteund. Upgrade naar een ondersteunde browser.

Flutter Deprecations removed after 2.2

Tab

Extern

Delen

[Inloggen](https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&osid=1&continue=https://docs.google.com/spreadsheets/d/18VuxojMGFKrFJCeilg3tErAtp23-_tp43XUioC_34To/edit?usp%3Dsharing&followup=https://docs.google.com/spreadsheets/d/18VuxojMGFKrFJCeilg3tErAtp23-_tp43XUioC_34To/edit?usp%3Dsharing&ltmpl=sheets&ec=GAZAmwI)

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
| 1 | Publicly Shared |  | flutter.dev/go/deprecations-removed-after-2-2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Deprecations to be removed from Flutter after 2.2 Release |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Deprecation Policy: | https://github.com/flutter/flutter/wiki/Tree-hygiene#deprecation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | Announcement: | https://groups.google.com/g/flutter-announce/c/wSyaQWLuVN8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | Cutoff: | 5/6/2020 1.17 stable release |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | Full Migration Guide: | https://github.com/flutter/website/pull/6024 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | Library/Package | Deprecated in | Old API |  | New API | Removal PR | Notes | dart fix support |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Material | v1.13.2 | InputDecoration | hasFloatingPlaceholder | floatingLabelBehavior | https://github.com/flutter/flutter/pull/83923 | dart fixes already available on stable | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 |  | v1.13.2 | InputDecoration.collapsed | hasFloatingPlaceholder | floatingLabelBehavior |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 |  | v1.13.2 | InputDecorationTheme | hasFloatingPlaceholder | floatingLabelBehavior |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 |  | v1.13.2 | InputDecorationTheme.copyWith | hasFloatingPlaceholder | floatingLabelBehavior | This one is missing a dart fix, will add |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 |  | v1.13.8 | TextTheme | display4 | headline1 | https://github.com/flutter/flutter/pull/83924 | dart fixes already available on stable | Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 |  | v1.13.8 | TextTheme | display3 | headline2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 |  | v1.13.8 | TextTheme | display2 | headline3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 |  | v1.13.8 | TextTheme | display1 | headline4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 |  | v1.13.8 | TextTheme | headline | headline5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 |  | v1.13.8 | TextTheme | title | headline6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 |  | v1.13.8 | TextTheme | subhead | subtitle1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 |  | v1.13.8 | TextTheme | subtitle | subtitle2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 |  | v1.13.8 | TextTheme | body2 | bodyText1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 |  | v1.13.8 | TextTheme | body1 | bodyText2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 |  | v1.13.8 | TextTheme.copyWith | display4 | headline1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 |  | v1.13.8 | TextTheme.copyWith | display3 | headline2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 |  | v1.13.8 | TextTheme.copyWith | display2 | headline3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 |  | v1.13.8 | TextTheme.copyWith | display1 | headline4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 |  | v1.13.8 | TextTheme.copyWith | headline | headline5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 |  | v1.13.8 | TextTheme.copyWith | title | headline6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 |  | v1.13.8 | TextTheme.copyWith | subhead | subtitle1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 |  | v1.13.8 | TextTheme.copyWith | subtitle | subtitle2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 |  | v1.13.8 | TextTheme.copyWith | body2 | bodyText1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 |  | v1.13.8 | TextTheme.copyWith | body1 | bodyText2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 |  | v1.13.8 | Typography | (constructor) | material2014 or material2018 | https://github.com/flutter/flutter/pull/83926 | Default of Typography() changes from material2014 to material2018 | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
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