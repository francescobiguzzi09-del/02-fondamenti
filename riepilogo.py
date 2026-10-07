from apparati import APPARATI


def crea_riepilogo() -> dict:
    """
    Calcola il totale degli apparati e il conteggio suddiviso per ciascuno stato:
    OK, ATTENZIONE e OFFLINE.
    """
    riepilogo = {
        "totale": len(APPARATI),
        "OK": 0,
        "ATTENZIONE": 0,
        "OFFLINE": 0,
    }

    for dati in APPARATI.values():
        stato = dati.get("stato", "").upper()
        if stato in riepilogo:
            riepilogo[stato] += 1

    return riepilogo