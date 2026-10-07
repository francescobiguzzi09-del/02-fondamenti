from apparati import APPARATI


def filtra_per_stato(stato_cercato):
    risultato = {}
    stato_normalizzato = stato_cercato.upper()

    for codice, dati in APPARATI.items():
        if dati["stato"] == stato_normalizzato:
            risultato[codice] = dati

    return risultato


def filtra_per_bus(bus_cercato):
    risultato = {}
    bus_normalizzato = bus_cercato.upper()

    for codice, dati in APPARATI.items():
        if dati["bus"] == bus_normalizzato:
            risultato[codice] = dati

    return risultato


