def je_prvocislo(cislo):
    
    result = False
    if cislo > 1:
        for delitel in range(2, 8):
            if cislo % delitel == 0 :
                if cislo / delitel == 1:
                    result = True
                    break
                else:
                    result = False 
                    break
            else: result = True
    else:  result = False       
        
    return result

def vrat_prvocisla(maximum):
    cisla = []
    for current in range(1, maximum+1):
        if je_prvocislo(current) == True:
            cisla.append(current)
        else: continue 
    
    return cisla

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    
    
    # check pokud je nebo neni prvocislo
    # if je_prvocislo(cislo) == True:
    #     print("je prvocislo")
    # else: print("neni prvocislo")
    
    
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)