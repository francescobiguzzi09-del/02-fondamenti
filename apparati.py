APPARATI = {
    "NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
    "COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
    "SEN-03": {"nome": "Sensore assettio", "bus": "BUS-A", "stato": "OFFLINE"},
}


def aggiungi_apparato(codice: str, nome: str, bus: str, stato: str = "OK") -> bool:
    codice = codice.upper()

    if codice in APPARATI:
        print(f"Errore: Apparato con codice '{codice}' già presente.")
        return False

    APPARATI[codice] = {
        "nome": nome,
        "bus": bus.upper(),
        "stato": stato.upper(),
    }
    return True


def aggiorna_stato(codice: str, nuovo_stato: str) -> bool:
    codice = codice.upper()

    if codice not in APPARATI:
        print(f"Errore: Apparato con codice '{codice}' non trovato.")
        return False

    if nuovo_stato.upper() not in ["OK", "ATTENZIONE", "OFFLINE"]:
        print(f"Errore: Stato '{nuovo_stato}' non valido. Deve essere 'OK', 'ATTENZIONE' o 'OFFLINE'.")
        return False

    vecchio_stato = APPARATI[codice]["stato"]
    APPARATI[codice]["stato"] = nuovo_stato.upper()
    return True