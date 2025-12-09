def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
     bin_str = str(binarni_cislo)
     vysledek = 0
     mocnina = 0

     for cifra in reversed(bin_str):
        if cifra not in "01":
            raise ValueError("Neplatné binární číslo")

        vysledek += int(cifra) * (2 ** mocnina)
        mocnina += 1

     return vysledek

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128


print(bin_to_dec(10011101))