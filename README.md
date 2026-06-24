# Stephan Epp — Senior Software Entwickler | M.Sc. Informatik

> *Erfahrener Senior Software Entwickler aus Bielefeld mit über einem Jahrzehnt Erfahrung in der Entwicklung komplexer Softwarelösungen für die Bereiche Automotive, Verkehrstechnik und Finanzverwaltung.*

## Über mich

Ich bin Stephan Epp, geboren am 29. August 1986 in Bielefeld, wo ich auch heute noch mit meiner Familie lebe. Verheiratet und Vater von fünf Kindern, bringe ich die Fähigkeit zur Organisation, Belastbarkeit und Ausdauer nicht nur aus dem Beruf mit — sondern auch aus dem Alltag.

Mein Weg in die Informatik begann früh: Nach der Fachoberschulreife an der Kuhlo-Realschule Bielefeld (2002) und dem Abschluss als **Staatlich geprüfter Informationstechnischer Assistent** am Carl-Severing-Berufskolleg Bielefeld (2005) habe ich an der **Universität Paderborn** zunächst meinen **Bachelor of Science in Informatik** (Note 2,6, Nebenfach Elektrotechnik) und anschließend meinen **Master of Science in Informatik** (Note 1,6 — *sehr gut*, Schwerpunkt Softwaretechnik, Nebenfach Elektrotechnik) erworben.

Meine Masterarbeit trug den Titel **"Learning M-DNF in Boolean Circuits"** — eine wissenschaftliche Arbeit, in der ich einen Algorithmus entwickelte, einen Korrektheitsbeweis und eine Laufzeitanalyse durchführte sowie eine experimentelle Implementierung in Java erstellte.

## Profil & Stärken

Ich verfüge über ein breites Technologie-Spektrum mit ausgewiesenen Schwerpunkten in:

- **Jakarta EE** und **Spring Boot** für serverseitige Geschäftslogik
- **Python (FastAPI)** für moderne REST-APIs
- **.NET / Entity Framework (C#)** für Windows-nahe Entwicklung
- **PostgreSQL / Oracle SQL** für relationale Datenbanken
- **Embedded-Entwicklung in C** (MISRA-konform) und hardwarenahe Programmierung mit **VHDL/Verilog**

Meine Arbeitsweise ist selbstständig, sorgfältig, zielorientiert, strukturiert und qualitätsbewusst. Nach dem Gallup-Stärkenprofil liegen meine Kernstärken in: **Wiederherstellung, Wissbegier, Einzelwahrnehmung, Analytik, Behutsamkeit, Eigeninitiative, Zuverlässigkeit, Belastbarkeit** und **Teamfähigkeit**.

## Beruflicher Werdegang

### Peter Berghaus GmbH, Bielefeld — *Senior Software Entwickler, Verkehrstechnik* `11/2023 – 03/2024`

Entwicklung von Reportings und Auswertungen (z. B. Batterieverbrauch, Kfz-Geschwindigkeiten), Erstellung von Testumgebungen und REST-API-Erweiterungen sowie Implementierung von Unit-Tests, Integrationstests und Audit-Logs. Bewertung: *„zu unserer vollen Zufriedenheit"*

### SALZ Automation GmbH, Bad Salzuflen — *Qualitätssicherung & Automatisierung* `07/2023 – 09/2023`

Automatisierung von Softwaretests mit dem **LDRA Testtool**, Dokumentation mit **Visure Requirements Management** und Versionsverwaltung mit **Git**. Bewertung: *„zu unserer vollen Zufriedenheit"*

### Rechenzentrum der Finanzverwaltung NRW, Paderborn — *Technische Produktbetreuung, Finanzverwaltung* `12/2022 – 05/2023`

Koordination und Begleitung des Einsatzes von KONSENS-Produkten, Software-Fehleranalyse sowie Abstimmung mit dem Entwicklungsbereich. Produkt- und Prozessdokumentation, Einarbeitung in **COBOL**. Bewertung: *„zu unserer Zufriedenheit"*

### Hella GmbH & Co. KGaA, Lippstadt — *Software Entwickler & Software Architekt, Automotive* `04/2017 – 04/2019`

Software-Architektur in Kundenprojekten, Bearbeitung von Änderungsanfragen und Fehleranalyse. Tool- und Prozessentwicklung für **NonVolatile Daten** (Modellierung & Code-Generierung), Software-Architektur für **CyberSecurity-Anforderungen** sowie internationale Zusammenarbeit mit HELLA-Standorten weltweit. Schwerpunkt: **AUTOSAR**. Bewertung: *„in bester Weise entsprochen"*

### Deutsche Post Adress GmbH & Co. KG, Gütersloh — *Software Entwickler, Adress-Recherche* `05/2016 – 03/2017`

Vollständiger Software-Entwicklungszyklus: Analyse, Implementierung und Testing. Erstellung von Unit-Tests, Integrationstests sowie Inbetriebnahme und 2nd-Level-Support. Technologien: **Java EE 7**, **JPA**, **CDI**.

### dSPACE GmbH, Paderborn — *Software Entwickler, Automotive / Luft- und Raumfahrt* `04/2013 – 11/2015`

Neuentwicklung und Erweiterung des Testautomatisierungsprodukts **AutomationDesk**. Steuergeräte-Diagnose, Messen und Kalibrieren, Verantwortung von Common Components sowie Unit-Tests. Implementierung in **C#**, **C/C++** und **Python**. Bewertung: *„jederzeit voll zufrieden"*

## Besondere Erfolge & Innovationen

### Research

Die Übersicht meiner wissenschaftlichen Arbeiten von 2026 wird in github.com/hjstephan86/science gegeben.

### Beweis P = NP (2024)

Finde ein Problem P, die eindeutige Schneeflocke.

Gegeben: Eine Schneeflocke mit 5 gleichlangen Armen. \newline
Frage: Wie wird diese Schneeflocke eindeutig unter allen bereits vorhandenen Schneeflocken? \newline
Idee: Finde einen Algorithmus, der in polynomieller Zeit immer eine neue Schneeflocke erzeugt.

IB: Sei $S$ die Menge aller eindeutigen Schneeflocken, oBdA.\newline
IA: $|S| = 0$ trivial, $|S| = 1$ trivial\newline
IS: $|S| \rightarrow |S| + 1$, $|S| = n, n \in \mathbb{N}$\newline
Ziel: Mache aus 8 Knoten wieder 6 Knoten mit gleicher Kantenlänge in polynomieller Zeit.\newline
Idee: Berechne dazu die Restklasse 6.\newline
Jeder Knoten berechnet eine Funktion $f(b_1, \ldots, b_n) = \{0, \ldots, 9\}$, $b_i \in \{0, 1\}$.\newline
Bei Hinzufügen zwei neuer Knoten erhöht sich die Wertemenge des vorhandenen Graphen um maximal $18\equiv 0 \mod 6$.

Man dachte, das Problem P sei NP-vollständig. Da dieses Problem aber in polynomieller Zeit lösbar ist, ist es echt in $P$.

### Integrationstests nach Zyklomatischer Komplexität — Peter Berghaus GmbH (2024)
Konzeption und Umsetzung eines komplexitätsgetriebenen Testansatzes zur Maximierung der Testüberdeckung. Automatisierte, absteigende Sortierung kritischer Methoden als `*.txt`-Datei im Git-Repository — ermöglicht Entwicklern gezielte Refaktorierung und kontinuierliche Qualitätsverbesserung durch nachverfolgbare Reduktion der Komplexitätswerte.

### Dezentrale NV-Datengenerierung aus Rational Rhapsody — Hella GmbH (2019)
Entwicklung eines Entwicklungsprozesses und Java-Plugins für **IBM Rational Rhapsody** nach dem V-Modell. Beinhaltet modellgetriebene Code-Generierung aus einem UML-Profil — auf Architektur- sowie Modulebene während aktiver Release-Phasen.

### Signal Editor für AutomationDesk & ControlDesk NG — dSPACE GmbH (2015)
Eigenständige Entwicklung einer Common Component für **signalbasiertes Testen** in der Testautomatisierung. Die Produkt-Idee, Architektur und Umsetzung stammen maßgeblich von mir. Das Produkt wurde öffentlich präsentiert: [▶ YouTube-Präsentation](https://www.youtube.com/watch?v=GIzrmQBHw2A)

### Masterarbeit — Universität Paderborn (2013)
Entwicklung, Korrektheitsbeweis und Laufzeitanalyse eines Algorithmus zum Thema **"Learning M-DNF in Boolean Circuits"** inklusive Java-Implementierung und experimenteller Analyse. Note: **1,6 (sehr gut)**

## Technologie-Stack

### Programmiersprachen
Java · C# · Python · JavaScript · C (MISRA) · PHP · COBOL (Grundkenntnisse)

### Backend Frameworks
FastAPI (Python) · Spring Boot (Java) · Wildfly · Entity Framework (C#) · Jakarta EE · REST-API

### Frontend & Mobile
HTML · CSS · JavaScript · NodeJS · npm · Capacitor (Android)

### Datenbanken
PostgreSQL · Microsoft SQL · Oracle SQL · MySQL · MariaDB

### Development Tools
Visual Studio Code · Visual Studio Community · Eclipse · LDRA tool suite · Git · SVN · Maven · Jenkins

### Qualitätssicherung
Clean Code · TDD · Unit Tests (JUnit, NUnit) · Integrationstests · Code Coverage (Jacoco) · Black-/White-Box-Testing · SonarQube · LDRA

### Requirements & Modellierung
Atlassian Jira · IBM Rational DOORS · Visure Requirements · UML · IBM Rational Rhapsody · Visual Paradigm · Enterprise Architect

### Automotive Standards
AUTOSAR (Workshop & Praxis) · ISO 26262 (Functional Safety) · CyberSecurity · MISRA C

## Ausbildung

| Zeitraum | Institution | Abschluss |
|---|---|---|
| 04/2011 – 04/2013 | Universität Paderborn | **M.Sc. Informatik**, Note 1,6 — Schwerpunkt Softwaretechnik, Nebenfach Elektrotechnik |
| 10/2005 – 03/2011 | Universität Paderborn | **B.Sc. Informatik**, Note 2,6 — Nebenfach Elektrotechnik |
| 06/2005 | Carl-Severing-Berufskolleg, Bielefeld | **Fachhochschulreife**, Note 2,0 |
| 06/2005 | Carl-Severing-Berufskolleg, Bielefeld | **Staatl. gepr. Informationstechnischer Assistent**, Note 2,0 |
| 05/2002 | Kuhlo-Realschule, Bielefeld | **Fachoberschulreife** |

## Zertifizierungen & Weiterbildungen

**AUTOSAR Workshop & Praxis** — Vector Academy & Hella *(Feb & Mai 2017)*  
Umfassende Schulung zu AUTOSAR-Fundamentals, RTE, BSW und Methodologie

**Functional Safety — ISO 26262** — Quint Academy & Kugler Maag Cie *(Okt & Dez 2017)*  
Automotive Functional Safety mit Fokus auf Software-Entwicklung

**Java EE 7 Intensivkurs** — GEDOPLAN IT Training *(Oktober 2016)*  
JPA 2.1, CDI 1.1, Maven 3 — Entwicklung serverseitiger Geschäftslogik

**UNIX/Linux Einführung** — RZF NRW *(2023)*  
Erfolgreiche Teilnahme an Fortbildungsmaßnahme

## Frühe Praxis & Praktika

| Zeitraum | Unternehmen | Tätigkeit |
|---|---|---|
| 08/2008 – 10/2008 | Fecher e.K., Paderborn | Entwicklung von Unit Tests, C# Database Unit Tests, VMware-Testumgebungen |
| 10/2004 & 04/2004 | OEDIV KG & KTI Distribution GmbH, Bielefeld | Auto-Installationsprogrammierung, Netzwerkadapter-Installation |

## Weitere Qualifikationen

**Sprachen:** Englisch (verhandlungssicher) · Französisch (Grundkenntnisse)

**Stärken (nach Gallup, Inc.):** Wiederherstellung · Wissbegier · Einzelwahrnehmung · Analytisch · Behutsamkeit · Eigeninitiative · Zuverlässigkeit · Belastbarkeit · Teamfähigkeit

**Arbeitsweise:** Selbstständig · Sorgfältig · Zielorientiert · Strukturiert · Qualitätsbewusst

**Interessen:** Wissenschaftliche Artikel verfassen · Software entwickeln · Bloggen · Fußball · Fitness · Schwimmen · Fotografie · Lesen · Spaziergänge

## Rechtliche Verfahren
Hier ist ein Überblick über die rechtlichen Verfahren, die ich führe: https://drive.google.com/drive/folders/1b978yvTBytCg8amzRYgvdTs1B3Z03Ij0?usp=sharing.

## Ansprachen

Ansprachen vom 31.12.2023, 14.01.2024 und 28.01.2024:
- https://drive.google.com/file/d/1ce7o-_HODSS-c_HWdTDns9eL0Vtxaie5/view?usp=drivesdk (ab 1:09:29)
- https://drive.google.com/file/d/1ne2rAoHA3CtqnSGrCx1lopkW-1NA3_-1/view?usp=drivesdk (ab 1:32:40)
- https://drive.google.com/file/d/1SV_nwSJmtzGpn5tS0MNS4K0UEk-eBC5n/view?usp=drivesdk (ab 1:13:11)

## Hyperlinks

Nachfolgend eine Übersicht wichtiger Dokumente und Unterlagen, die über Google Drive zugänglich sind:

- **Bewerbungen:** [→ Google Drive](https://drive.google.com/drive/folders/16LqTdquTBQdjwp0MrYhvyFHCghq0dNRF)  
  Sammlung meiner Bewerbungsunterlagen

- **Studium Informatik — Universität Paderborn:** [→ Google Drive](https://drive.google.com/drive/folders/17OvQYkgzgbq4bxrWElkYIo2tcBkMOK5L)  
  Unterlagen, Skripte und Dokumente aus meinem Informatikstudium an der Universität Paderborn

- **Prophetie:** [→ Google Drive](https://drive.google.com/drive/folders/1_1VCJ5YVKH0XQRyFoKY2-TBcE3tIPt8f)  
  Unterlagen zur Prophetie

## Kontakt

- **GitLab:** [github.com/hjstephan86](https://github.com/hjstephan86)
- **E-Mail:** Stephan_Epp@web.de
- **Standort:** Bielefeld, Deutschland
