def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    radek, sloupec = cilova_pozice
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False  # mimo šachovnici

    aktualni_radek, aktualni_sloupec = figurka["pozice"]
    typ = figurka["typ"]

    # Pěšec
    if typ == "pěšec":
        if sloupec == aktualni_sloupec:
            if radek == aktualni_radek + 1 and (radek, sloupec) not in obsazene_pozice:
                return True
            if aktualni_radek == 1 and radek == aktualni_radek + 2 and (radek, sloupec) not in obsazene_pozice:
                return True
        return False

    # Jezdec
    elif typ == "jezdec":
        dr = abs(radek - aktualni_radek)
        ds = abs(sloupec - aktualni_sloupec)
        return (dr, ds) in [(2, 1), (1, 2)] and (radek, sloupec) not in obsazene_pozice

    # Věž
    elif typ == "věž":
        if radek != aktualni_radek and sloupec != aktualni_sloupec:
            return False
        # pohyb po řádku
        if radek == aktualni_radek:
            for s in range(min(aktualni_sloupec, sloupec) + 1, max(aktualni_sloupec, sloupec)):
                if (radek, s) in obsazene_pozice:
                    return False
        # pohyb po sloupci
        else:
            for r in range(min(aktualni_radek, radek) + 1, max(aktualni_radek, radek)):
                if (r, sloupec) in obsazene_pozice:
                    return False
        return (radek, sloupec) not in obsazene_pozice

    # Střelec
    elif typ == "střelec":
        if abs(radek - aktualni_radek) != abs(sloupec - aktualni_sloupec):
            return False
        krok_r = 1 if radek > aktualni_radek else -1
        krok_s = 1 if sloupec > aktualni_sloupec else -1
        for i in range(1, abs(radek - aktualni_radek)):
            if (aktualni_radek + i * krok_r, aktualni_sloupec + i * krok_s) in obsazene_pozice:
                return False
        return (radek, sloupec) not in obsazene_pozice

    # Dáma
    elif typ == "dáma":
        if radek == aktualni_radek or sloupec == aktualni_sloupec:
            return je_tah_mozny({"typ":"věž","pozice":figurka["pozice"]}, cilova_pozice, obsazene_pozice)
        if abs(radek - aktualni_radek) == abs(sloupec - aktualni_sloupec):
            return je_tah_mozny({"typ":"střelec","pozice":figurka["pozice"]}, cilova_pozice, obsazene_pozice)
        return False

    # Král
    elif typ == "král":
        return max(abs(radek - aktualni_radek), abs(sloupec - aktualni_sloupec)) == 1 \
               and (radek, sloupec) not in obsazene_pozice

    return False



if __name__ == "__main__":
    
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici