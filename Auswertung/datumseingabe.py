#-----------------------------------------------------------------------------------------------------------------------
# Ziel des Moduls ist die Eingabe von einenn oder mehreren Datumsangaben. Gibt den  zurück.

# Nötiger Aufruf:
## Bei einem Datum:
### import datumseingabe
### datumseingabe.eindatum()
## Bei zwei Daten:
### import datumseingabe
### datumseingabe.zweidaten()

# Gibt zurück:
## Bei einem benötigten Datum:
### Variable "datum"
## Bei zwei benötigten Daten:
### Variable "datestart"
### Variable "dateend"

# ----------------------------------------------------------------------------------------------------------------------
# Zu Testzwecken:
#anz_date = 1

# ----------------------------------------------------------------------------------------------------------------------
def eindatum():
    global datum
    datum = input("Bitte das gewünschte Datum im Format YYYY-MM-DD eingeben ")
    print(datum)


def zweidaten():
    global datestart
    global dateend
    datestart = input("Bitte das Startdatum im Format YYYY-MM-DD eingeben ")
    dateend = input("Bitte das Enddatum im Format YYYY-MM-DD eingeben ")
    while True:
        if dateend > datestart:
            print("Das gewünschte Startdatum liegt vor dem Enddatum")
            break
        else:
            dateend = input("Das gewünschte Enddatum liegt vor dem Startdatum. Bitte ein neues Enddatum im Format "
                            "YYYY-MM-DD eingeben. Für Abbruch bitte 1 eingeben. ")
            if dateend == 1:
                quit()
            else:
                continue
    print(datestart)
    print(dateend)