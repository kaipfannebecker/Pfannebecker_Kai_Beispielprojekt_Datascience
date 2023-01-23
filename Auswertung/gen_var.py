import logging

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
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------


def main(ebene, datensatz):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"{__name__}.log")
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in '
               'function %(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    variablen = variablengeneration(ebene, datensatz)
    var_eb = variablen[0]
    var_da = variablen[1]
    var_da_anz = variablen[2]
    var_da_sort = variablen[3]
    var_da_verb = variablen[4]

    return var_eb, var_da, var_da_anz, var_da_sort, var_da_verb

# ----------------------------------------------------------------------------------------------------------------------


def variablengeneration(ebene, datensatz):

    if ebene == 1:
        var_eb = "IdLandkreis"
    if ebene == 2:
        var_eb = "IdBundesländer"
    if ebene == 3:
        var_eb = "IdBund"

    if datensatz == 1:
        var_da = "Gesamtzahl neue Infektionen"
        var_da_sort = 'NeuerFall'
        var_da_anz = "AnzahlFall"
        var_da_verb = "infected"
    if datensatz == 2:
        var_da = "Gesamtzahl neue Genesene"
        var_da_sort = 'NeuGenesen'
        var_da_anz = "AnzahlGenesen"
        var_da_verb = "recovered"
    if datensatz == 3:
        var_da = "Gesamtzahl neue Todesfälle"
        var_da_sort = 'NeuerTodesfall'
        var_da_anz = "AnzahlTodesfall"
        var_da_verb = "killed"

    return var_eb,var_da,var_da_anz, var_da_sort, var_da_verb
