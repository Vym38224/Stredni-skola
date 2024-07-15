from random import randint, choice

def menu():
    print("""
Co chceš dělat?
1) Převést na malá písmena.
2) Nahrazení znaků jiným znakem.
3) Statistika výskytu jednotlivých znaků v souboru.
4) Generování náhodného textu.
""")
    volba = input("Zadej svoji volbu: ")
    

    if volba == "1":
        prevod()

    elif volba == "2":
        nahrada()

    elif volba == "3":
        statistika()

    elif volba == "4":
        veta()

    else:
        print("Zadal si špatnou volbu")

    


def prevod():
    try:
        f1 = open(input("Zadej název vstupního souboru: "),"r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    try:
        f2 = open(input("Zadejte název výstupního souboru: "),"w")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    text = f1.read().lower()
    f2.write(text)
    
    f1.close()
    f2.close()




def nahrada():

    try:
        f1 = open(input("Zadej název vstupního souboru: "),"r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    
    f2 = open(input("Zadej název výstupního souboru: "), "w")

    znak1 = input("Zadej znak, kterým chceš nahradit: ")
    znak2 = input("Zadej znak, který chceš nahradit: ")

    while True:
        znak = f1.read(1)
        if znak == "":
            break
        if znak == znak2:
            znak = znak1
        f2.write(znak)
    
    f1.close()
    f2.close()


def statistika():
    pocet = {}
    try:
        f1 = open(input("Zadej název vstupního souboru: "),"r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    while True:
        pismeno = f1.read(1)
        if pismeno =="":
            break
        
        if pismeno.isalpha():
            if pismeno not in pocet.keys():
                pocet[pismeno] = 1
            else:
                pocet[pismeno] += 1

    nej = max(pocet.values())
    for key in sorted(pocet.keys()):
        print(key, pocet[key])
    
    f1.close()
    
    
def slovo(minznak =1 , maxznak =7):
    
    samohlasky = "aeiyou"
    souhlasky = "qwrtpsdfghjklzxcvbnm"

    vysledek = ""
    pocet = randint(minznak, maxznak)

    for i in range(pocet):
        if i % 2 == 0:
            vysledek = vysledek + choice(samohlasky)
        else:
            vysledek = vysledek + choice(souhlasky)
    return vysledek

def veta():

    f2 = open(input("Zadej název výstupního souboru: "),"w")
    
    max_slov = int(input("Kolik je max slov?: "))
    vysledek2 = ""
    for i in range(max_slov):
        vysledek2 = vysledek2 + slovo() + " "
    f2.write(vysledek2)
    return vysledek2.capitalize()[0:-1] + "."

    

menu()




    




        
        




















    











    
    



        
    

    

       


    

    
    

