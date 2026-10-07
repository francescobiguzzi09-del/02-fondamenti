from apparati import (
    APPARATI,
    aggiungi_apparato,
    aggiorna_stato,
    filtra_per_bus,
    filtra_per_stato,
)
from riepilogo import crea_riepilogo


def mostra_dizionario(titolo: str, dati_dizionario: dict):
    """Funzione di supporto per formattare la stampa a schermo."""
    print(f"\n=== {titolo} ===")
    if not dati_dizionario:
        print("Nessun apparato trovato.")
        return

    for codice, info in dati_dizionario.items():
        print(
            f"  • {codice}: {info['nome']} | Bus: {info['bus']} | Stato: {info['stato']}"
        )


def main():
    # 1. Mostra il registro completo degli apparati
    mostra_dizionario("REGISTRO COMPLETO APPARATI", APPARATI)

    # 2. Dimostrazione modifica registro
    print("\n--- Aggiornamento registro in corso... ---")
    aggiungi_apparato("RAD-04", "Radar Altimetrico", "BUS-A", "OK")
    aggiorna_stato("COM-02", "OK")

    mostra_dizionario("REGISTRO DOPO LE MODIFICHE", APPARATI)

    # 3. Report per Stato
    apparati_ok = filtra_per_stato("OK")
    mostra_dizionario("REPORT: APPARATI IN STATO 'OK'", apparati_ok)

    # 4. Report per Bus
    apparati_bus_a = filtra_per_bus("BUS-A")
    mostra_dizionario("REPORT: APPARATI COLLEGATI A 'BUS-A'", apparati_bus_a)

    # 5. Generazione e stampa del Riepilogo
    stats = crea_riepilogo()
    print("\n=== RIEPILOGO STATISTICO ===")
    print(f"  • Totale apparati : {stats['totale']}")
    print(f"  • Stato OK        : {stats['OK']}")
    print(f"  • Stato ATTENZIONE: {stats['ATTENZIONE']}")
    print(f"  • Stato OFFLINE   : {stats['OFFLINE']}")


if __name__ == "__main__":
    main()