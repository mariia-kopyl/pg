def je_prvocislo(cislo):
    
   if cislo <= 1:
       return False
   for i in range(2, cislo):
       if cislo % i == 0:
           return False
   return True

def vrat_prvocisla(maximum):
    cisla = []
    for current in range(1, maximum+1):
        if je_prvocislo(current) == True:
            cisla.append(current)
        else: continue 
    
    return cisla

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    

    if je_prvocislo(cislo) == True:
      print("je prvocislo")
    else: print("neni prvocislo")
    
    
    #prvocisla = vrat_prvocisla(cislo)
    #print(prvocisla)
