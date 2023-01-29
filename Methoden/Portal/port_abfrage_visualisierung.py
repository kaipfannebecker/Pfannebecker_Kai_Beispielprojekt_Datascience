import sys
import logging

from Methoden.Auswertung import ein_lk_vs_zeit_main, plot_date_on_landkarte_main

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
##

# Benötigt:
##

# Gibt zurück:
##

# ----------------------------------------------------------------------------------------------------------------------


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


def main(ebene, datensatz):
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    abfrage_visualisierung(ebene, datensatz)

# ----------------------------------------------------------------------------------------------------------------------
