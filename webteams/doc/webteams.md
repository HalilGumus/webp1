**Gruppe D**
**Team Serda Acimis, Halil Ibrahim Gümüs**
**Gültigkeitsdatum 21.10.2019**

# Aufbau der Anwendung

Die Webanwendung besteht aus den folgenden Seiten:<br>
<br>
Startseite: Auflistung der Daten der erfassten Teams<br>
Buttons zum erfassen, löschen, bearbeiten der Daten und ein Button  zum ändern der Ansicht<br>
<br>
Formular: Erfassung neuer Daten oder Bearbeitung vorhandener Daten<br>
Buttons zum speichern und übermitteln des Formulars und zum abbrechen der Eingabe


# Durchgeführte Ergänzungen

2 Funktionen in application.py:<br>
changeForm() und back()<br>
(Siehe Abbildung 3)<br>
ein neues Template für Aufzählungsansicht

# Beschreibung des HTTP-Datenverkehrs


## beim Start der Anwendung

Es werden 4 Elemente mit GET geladen:<br>
"/"<br>
"/webteams.js"<br>
"/webteams.css"<br>
"favicon.ico"<br>

Siehe Abbildung 1

## beim speichern von Formulardaten

Es werden durch POST Parameter übergeben:<br>
id_spa<br>
name1_spa<br>
vorname1_spa<br>
matrnr1_spa<br>
semesteranzahl1_spa<br>
name2_spa<br>
vorname2_spa<br>
matrnr2_spa<br>
semesteranzahl2_spa<br>

Siehe Abbildung 2

## Screenshots
Abbildung 1
![](Abbildung1.png)

Abbildung 2
![](Abbildung2.png)

Abbildung 3
![](Abbildung3.png)