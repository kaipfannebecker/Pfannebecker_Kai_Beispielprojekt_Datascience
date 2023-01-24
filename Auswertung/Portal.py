import sys
import logging

import plot_date_on_landkarte
import ein_lk_vs_zeit
import aktualitaet

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
## Weiteren Module zur Darstellung

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

    # Zum debuggen auskommentieren:
    # logger = logging.getLogger(__name__)
    # handler = logging.FileHandler(f"{__name__}.log")
    # formatter = logging.Formatter(
    #    '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
    #    datefmt='%Y-%m-%d:%H:%M:%S'
    # )
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    begruessung()
    # abfrage_vorgehen()
    var = abfrage_variablen()
    ebene = var[0]
    datensatz = var[1]
    abfrage_visualisierung(ebene, datensatz)
# ----------------------------------------------------------------------------------------------------------------------


# Begrüßung:
def begruessung():
    print("Herzlich Willkommen bei der Darstellung von Coronadaten in verschiedenen Visualisierungen.")


# ----------------------------------------------------------------------------------------------------------------------


# Abfrage Ebene:
def abfrage_vorgehen():
    vorgehen = eval(input(
        "Möchten Sie die Daten zuerst aktualisieren oder die vorhandenen Daten direkt auswerten? \n"
        "1) aktualisieren\n"
        "2) auswerten\n"
        "3) Abbruch\n"
        " "
    ))

    if vorgehen == 1:
        while True:
            aktualitaet.main()
            break

    if vorgehen == 4:
        sys.exit()

    # return (vorgehen)

# ----------------------------------------------------------------------------------------------------------------------


# Abfrage der Variablen:
def abfrage_variablen():
    # Abfrage Ebene:
    ebene = eval(input(
        "Auf welcher Ebene möchten Sie die Daten betrachten:\n"
        "1) Landkreise\n"
        "2) Bundesländer\n"
        "3) Bundesgebiet\n"
        "4) Abbruch\n"
        " "
    ))

    if ebene == 4:
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
    # Abgefragter Datensatz:
    datensatz = eval(input(
        "Welche Daten möchten Sie angezeigt haben:\n"
        "1) Neue Fälle\n"
        "2) Neue Genesene\n"
        "3) Neue Todesfälle\n"
        "4) Abbruch\n"
        " "
    ))

    if datensatz == 4:
        sys.exit()

    return ebene, datensatz

# ----------------------------------------------------------------------------------------------------------------------


# Abgefragte Visualisierung:
def abfrage_visualisierung(ebene, datensatz):
    visualisierung = eval(input(
        "Bitte wählen Sie die gewünschte Visualisierung:\n"
        "1) XY-Diagramm einer Ebene entlang der Zeitachse\n"
        "2) Heatmap Deutschland mit Auflösung der gewählten Ebene\n"
        "3) Abbruch\n"
        " "
    ))

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
