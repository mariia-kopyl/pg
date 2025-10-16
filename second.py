def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    # Převeď vstup na int
    n = int(cislo)

    zaklad = [
        "nula", "jedna", "dva", "tři", "čtyři", "pět",
        "šest", "sedm", "osm", "devět", "deset",
        "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct",
        "šestnáct", "sedmnáct", "osmnáct", "devatenáct" ]

    desitky = {
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát",
        100: "sto"}
    
    if n < 20:
        return zaklad[n]
    
    elif n in desitky:
        return desitky[n]
    
    elif 20 < n < 100:
        des = (n // 10) * 10  
        jed = n % 10        
        return desitky[des] + " " + zaklad[jed]
    
    else:
        return "mimo rozsah"

    


if __name__ == "__main__":
    while True:
     cislo = input("Zadej číslo: ")
     text = cislo_text(cislo)
     print(text)