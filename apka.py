

wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
region="U"

def pelnoletni(wiek,region):
    if wiek>0 and wiek<=120:
        if region=="USA" and wiek >= 21 or region=="EUR" and wiek>=18:
             print("Witamy!")

        else:
            print("Jesteś niepełnoletni")

    else:
        print("Podałeś nieprawidłową wartość, wiek musi być z przedziału 1-120")

print(pelnoletni(wiek,region))

