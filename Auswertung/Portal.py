import sys
import logging
import plot_date_on_landkarte
import ein_lk_vs_zeit

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## Bestimmt über das Modul "aufruf_lk.py" genau einen Landkreis, prüft die Daten über das Module "aktualitaet.py" auf
## Aktualität und sortiert über "sort_meld.py" nach Meldedatum. Danach wird das Startdatum sowie Enddatum bestimmt und
## die Zahl der resultierenden Fälle pro Tag als Graph ausgegeben.

# Benötigt:
## "aufruf_lk.py"
## "aktualitaet.py"
## "sort_meld.py"
## "datumseingabe.py"

# Gibt zurück:
## 2d-Graph mit der x = Datum und Y = Anzahl Fälle

# ----------------------------------------------------------------------------------------------------------------------
# Logging:
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='a'
)

# ----------------------------------------------------------------------------------------------------------------------
def main():
    begruessung()
    abfrage_variablen()
    abfrage_visualisierung()
# ----------------------------------------------------------------------------------------------------------------------
def begruessung():
    # Begrüßung:
    print("Herzlich Willkommen bei der Darstellung von Coronadaten in verschiedenen Visualisierungen.")

# ----------------------------------------------------------------------------------------------------------------------
def abfrage_variablen():
    # Abfrage Ebene:
    global ebene
    ebene = eval(input("Auf welcher Ebene möchten Sie die Daten betrachten:\n"
                        "1) Landkreise\n"
                        "2) Bundesländer\n"
                        "3) Bundesgebiet\n"
                        "4) Abbruch\n"
                        " "))

    if ebene == 4:
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
    # Abgefragter Datensatz:
    global datensatz
    datensatz = eval(input("Welche Daten möchten Sie angezeigt haben:\n"
                            "1) Neue Fälle\n"
                            "2) Neue Genesene\n"
                            "3) Neue Todesfälle\n"
                            "4) Abbruch\n"
                            " "))
    if datensatz == 4:
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
def abfrage_visualisierung():
    # Abgefragter Datensatz:
    global visualisierung
    visualisierung = eval(input("Bitte wählen Sie die gewünschte Visualisierung:\n"
                                "1) XY-Diagramm einer Ebene entlang der Zeitachse\n"
                                "2) Heatmap Deutschland mit Auflösung der gewählten Ebene\n"
                                "3) Abbruch\n"
                                " "))

    if visualisierung == 1:
        ein_lk_vs_zeit.main(ebene, datensatz)
    if visualisierung == 2:
        plot_date_on_landkarte.main(ebene, datensatz)
    if visualisierung == 3:
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------
main()
# ----------------------------------------------------------------------------------------------------------------------