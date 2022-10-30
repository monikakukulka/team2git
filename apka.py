def NrStrefy():
  strefa = input("podaj region: (EUR , USA, Other: ")
  if strefa != "EUR" and strefa != "USA":
    strefa = ""
  return strefa

wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
  exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
  print("Witamy!")

strefa = NrStrefy()
print("wskazano", strefa)


