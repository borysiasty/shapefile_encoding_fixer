<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.0" language="pl_PL">
<context>
    <name>EncodingFixerDialog</name>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="135"/>
        <source>NOTE: With this tool you can set or clear attribute table encoding &lt;u&gt;declaration&lt;/u&gt; for Shapefiles. It doesn&apos;t change the real data encoding though.</source>
        <translation>UWAGA: Tym narzędziem możesz poprawić lub wyczyścić &lt;u&gt;deklarację&lt;/u&gt; kodowania atrybutów w plikach Shapefile. Jednak samego kodowania atrybutów ono nie zmieni. </translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="392"/>
        <source>Shapefile Encoding Fixer</source>
        <translation>Napraw deklarację kodowania plików Shapefile</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="228"/>
        <source>ERROR: Cannot find the DBF file</source>
        <translation>BŁĄD: Nie mogę znaleźć pliku DBF</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="238"/>
        <source>ERROR: Cannot open the DBF file</source>
        <translation>BŁĄD: Nie mogę otworzyć pliku DBF</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="241"/>
        <source>NOT SET</source>
        <translation>NIEUSTAWIONY</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="247"/>
        <source>UNKNOWN</source>
        <translation>NIEZNANE</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="264"/>
        <source>NONE</source>
        <translation>BRAK</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="281"/>
        <source>Clearing LDID byte and removing CPG file will disable encoding autodetection. Exactly like in older QGIS versions, you will be able to use the drop-down list in the Add Vector Layer window to choose the layer encoding.</source>
        <translation>Wyczyszczenie bajtu LDID i usunięcie pliku CPG wyłączy autodetekcję kodowania. Kodowanie będziesz wybierać z rozwijalnej listy w oknie Dodaj Warstwę Wektorową, dokładnie jak w starszych wersjach QGISa.</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="288"/>
        <source>The LDID byte of dbf file declares the codepage of attribute table. Please note the LDID byte doesn&apos;t support other encodings, especially UTF-8. Setting LDID byte will automatically remove the concurrent CPG file, if exists.</source>
        <translation>Dwudziesty dziewiąty bajt pliku DBF zawiera LDID, czyli deklarację strony kodowej tablicy atrybutów. Zauważ, że bajt LDID nie wspiera wszystkich kodowań, w tym UTF-8. Ustawienie bajtu LDID spowoduje usunięcie pliku CPG, jeśli taki istnieje.</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="295"/>
        <source>CPG is a small additional file for Shapefile. It&apos;s an alternative for LDID byte, and it supports much more encodings. Creating CPG file will automatically clear the concurrent LDID byte, if set. If you can&apos;t find your encoding, please &lt;a href=&apos;http://hub.qgis.org/projects/shpencodingfixer/issues&apos;&gt;request it&lt;/a&gt;.</source>
        <translation>Alternatywą dla bajtu LDID jest mały plik CPG, dołączany do warstwy Shapefile. Plik ten wspiera znacznie więcej kodowań, niż bajt LDID. Utworzenie pliku spowoduje wyczyszczenie bajtu LDID. Jeśli nie możesz znaleźć potrzebnego kodowania, wystarczy to &lt;a href=&apos;http://hub.qgis.org/projects/shpencodingfixer/issues&apos;&gt;zgłosić&lt;/a&gt;. </translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="301"/>
        <source>Select file</source>
        <translation>Wybierz plik</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="324"/>
        <source>The layer is in editing mode. You have to save changes and close the editing mode first.</source>
        <translation>Warstwa jest w trynie edycji. Musisz go najpierw opuścić.</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="358"/>
        <source>Oooops, I can&apos;t reload the modified layer :(</source>
        <translation>Cholercia, nie mogę załadować zmodyfikowanej warstwy :(</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="378"/>
        <source>Can&apos;t write to the DBF file. Check permissions.</source>
        <translation>Nie mogę zapisać pliku DBF. Sprawdź uprawnienia.</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="392"/>
        <source>Can&apos;t write to the CPG file. Check permissions.</source>
        <translation>Nie mogę zapisać pliku CPG. Sprawdź uprawnienia.</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="243"/>
        <source>Unclear: either current ANSI or ISO-8859-1. &lt;u&gt;Usually this is the culprit.&lt;/u&gt;</source>
        <translation type="obsolete">Niejasne: albo bieżąca strona kodowa, albo ISO-9959-1.&lt;u&gt;Zwykle to jest winowajca.&lt;/u&gt;</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="243"/>
        <source>Either current ANSI or ISO-8859-1. &lt;u&gt;Usually this is the culprit.&lt;/u&gt;</source>
        <translation>Bieżąca strona ANSI albo ISO-8859-1: &lt;u&gt;zwykle to jest winowajca.&lt;/u&gt;</translation>
    </message>
</context>
<context>
    <name>EncodingFixerDialogBase</name>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="30"/>
        <source>Fix Shapefile Encoding</source>
        <translation>Napraw kodowanie warstwy Shapefile</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="51"/>
        <source>Shapefile</source>
        <translation>Warstwa Shapefile</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="61"/>
        <source>Layer info</source>
        <translation>Informacje o warstwie</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="67"/>
        <source>Dbf File:</source>
        <translation>Plik DBF:</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="74"/>
        <source>LDID byte:</source>
        <translation>Bajt LDID:</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="120"/>
        <source>--</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="94"/>
        <source>CPG file:</source>
        <translation>Plik CPG:</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="136"/>
        <source>...</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="190"/>
        <source>Description placeholder...</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="212"/>
        <source>Set LDID</source>
        <translation>Ustaw bajt LDID</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="244"/>
        <source>SET CPG file</source>
        <translation>Stwórz plik CPG</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="305"/>
        <source>Clear LDID and delete CPG file</source>
        <translation>Wyczyść bajt LDID i usuń plik CPG</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="162"/>
        <source>Fix encoding declaration</source>
        <translation>Napraw deklarację kodowania</translation>
    </message>
</context>
<context>
    <name>EncodingFixerPlugin</name>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="432"/>
        <source>&amp;Shapefile Encoding Fixer</source>
        <translation>Naprawa &amp;kodowania Shapefile</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="424"/>
        <source>Fix Shapefile Encoding</source>
        <translation>Napraw kodowanie warstwy Shapefile</translation>
    </message>
</context>
</TS>
