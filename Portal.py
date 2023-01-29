import logging

from Methoden.Portal import port_abfrage_vorgehen, port_abfrage_ebene, port_abfrage_datensatz, \
    port_abfrage_visualisierung


# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
##

# Benötigt:
##

# Gibt zurück:
##

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


# Abfrage Vorgehen:
def abfrage_vorgehen():

    port_abfrage_vorgehen.main()

# ----------------------------------------------------------------------------------------------------------------------


# Abfrage der Variablen:
def abfrage_variablen_ebene():
    ebene = port_abfrage_ebene.main()

    return ebene

# ----------------------------------------------------------------------------------------------------------------------


def abfrage_variablen_datensatz():
    # Abgefragter Datensatz:
    datensatz = port_abfrage_datensatz.main()

    return datensatz

# ----------------------------------------------------------------------------------------------------------------------


# Abgefragte Visualisierung:
def abfrage_visualisierung(ebene, datensatz):
    port_abfrage_visualisierung.main(ebene, datensatz)
# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------


main()
# ----------------------------------------------------------------------------------------------------------------------
