from unidecode import unidecode
import string 

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ""ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abeceda = string.ascii_uppercase #abeceda pomoci knihony
delka = len(abeceda)

text = input("Zadej text ")
text = unidecode(text)
text = text.upper()

posun = int(input("zadej posun (celé číslo) "))

for znak in text:
    if znak in abeceda:
        index = abeceda.index(znak) + posun
    #if index >= delka:
     #   index = index - delka
     # operace procento mě stále drží v rozmšezí 0 až delka seznamu
        print(abeceda[index % delka], end=" ")
print()





