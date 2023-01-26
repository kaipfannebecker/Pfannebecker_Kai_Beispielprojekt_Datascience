import sys
import logging

from Methoden.Auswertung.Helper import aktualitaet
from Methoden.Auswertung import ein_lk_vs_zeit_main, plot_date_on_landkarte_main



# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## Bestimmt über das Modul "aufruf_lk.py" genau einen Landkreis, prüft die Data_collection über das Module "aktualitaet.py" auf
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
    filename='./log/%slog' % __file__[:-2],
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
    abfrage_vorgehen()
    ebene = abfrage_variablen_ebene()
    datensatz = abfrage_variablen_datensatz()
    abfrage_visualisierung(ebene, datensatz)
# ----------------------------------------------------------------------------------------------------------------------


# Begrüßung:
def begruessung():
    print("Herzlich Willkommen bei der Darstellung von Coronadaten in verschiedenen Visualisierungen.")


# ----------------------------------------------------------------------------------------------------------------------


# Abfrage Ebene:
def abfrage_vorgehen():
    vorgehen_1 = eval(input(
        "Möchten Sie die Data_collection zuerst aktualisieren oder die vorhandenen Data_collection direkt auswerten? \n"
        "1) aktualisieren\n"
        "2) auswerten\n"
        "3) Abbruch\n"
        " "
    ))

    if vorgehen_1 == 1:
        while True:
            aktualitaet.main()
            weitere_akt = eval(input(
                "Möchten Sie eine weitere Aktualisierung vornehmen?\n"
                "1) Ja\n"
                "2) Nein\n"
                "3) Abbruch\n"
                "")
            )
            #if weitere_akt == 1:
             #   continue

            if weitere_akt == 2:
                break

            if weitere_akt == 3:
                sys.exit()

    if vorgehen_1 == 3:
        sys.exit()

    # return (vorgehen)

# ----------------------------------------------------------------------------------------------------------------------


# Abfrage der Variablen:
def abfrage_variablen_ebene():
    # Abfrage Ebene:
    ebene = eval(input(
        "Auf welcher Ebene möchten Sie die Data_collection betrachten:\n"
        "1) Landkreise\n"
        "2) Bundesländer\n"
        "3) Bundesgebiet\n"
        "4) zurück zur vorherigen Auswahl\n"
        "5) Abbruch\n"
        " "
    ))

    if ebene == 4:
        sys.exit()  # to change

    if ebene == 5:
        sys.exit()
    return ebene

# ----------------------------------------------------------------------------------------------------------------------


def abfrage_variablen_datensatz():
    # Abgefragter Datensatz:
    datensatz = eval(input(
        "Welche Data_collection möchten Sie angezeigt haben:\n"
        "1) Neue Fälle\n"
        "2) Neue Genesene\n"
        "3) Neue Todesfälle\n"
        "4) zurück zur vorherigen Auswahl\n"
        "5) Abbruch\n"
        " "
    ))

    if datensatz == 4:
        sys.exit()  # to change

    if datensatz == 5:
        sys.exit()

    return datensatz

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
    # SyntaxError
    if visualisierung == 1:
        ein_lk_vs_zeit_main.main(ebene, datensatz)
    if visualisierung == 2:
        plot_date_on_landkarte_main.main(ebene, datensatz)
    if visualisierung == 3:
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------


main()
# ----------------------------------------------------------------------------------------------------------------------
