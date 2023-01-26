import logging
import sys

#-----------------------------------------------------------------------------------------------------------------------
# Ziel des Moduls ist die Eingabe von einen oder mehreren Datumsangaben. Gibt den  zurück.

# Nötiger Aufruf:
## Bei einem Datum:
### import datumseingabe
### datumseingabe.eindatum()
## Bei zwei Data_collection:
### import datumseingabe
### datumseingabe.zweidaten()

# Gibt zurück:
## Bei einem benötigten Datum:
### Variable "datum"
## Bei zwei benötigten Data_collection:
### Variable "datestart"
### Variable "dateend"

# ----------------------------------------------------------------------------------------------------------------------
# Zu Testzwecken:
#anz_date = 1

# ----------------------------------------------------------------------------------------------------------------------
# Ein Datum benötigt:
def eindatum():
    datum = input("Bitte das gewünschte Datum im Format YYYY-MM-DD eingeben ")
    print(datum)
    return datum

# Zwei Data_collection benötigt:
def zweidaten():
    datestart = input("Bitte das Startdatum im Format YYYY-MM-DD eingeben ")
    dateend = input("Bitte das Enddatum im Format YYYY-MM-DD eingeben ")
    while True:
        if dateend > datestart:
            print("Das gewünschte Startdatum liegt vor dem Enddatum")
            break
        else:
            dateend = eval(input("Das gewünschte Enddatum liegt vor dem Startdatum. Bitte ein neues Enddatum im Format "
                            "YYYY-MM-DD eingeben. Für Abbruch bitte 1 eingeben. "))
            if dateend == 1:
                sys.exit()
            else:
                continue
    return datestart, dateend

def main(anz_dat):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in '
               'function %(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if anz_dat == 1:
        datum = eindatum()
        return datum
    if anz_dat == 2:
        daten = zweidaten()
        datestart = daten[0]
        dateend = daten[1]
        return datestart, dateend