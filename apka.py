wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
    print("Witamy!")


def plec(x):
    if x == 1:
        print("Aperol gratis")
    else:
        print("Pij i płać")


x = int(input("Podaj płeć: kobieta(1), mężczyzna(2), inne(3) "))

plec(x)



