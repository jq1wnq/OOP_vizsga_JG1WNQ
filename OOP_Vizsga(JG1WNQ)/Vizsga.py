class Utanfuto:
    def __init__(self, tipus, ar, teherbiras):
        self.tipus = Utanfutotipus.tipus
        self.ar = ar
        self.teherbiras = teherbiras

class Utanfutotipus:
    def __init__(self, utipus):
        self.utipus = utipus

class Kolcsonzo:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

class Kolcsonzes:
    def __init__(self, kolcsonzonev, honap, nap, tipus):
        self.kolcsonzonev = kolcsonzonev
        self.honap = honap
        self.nap = nap
        self.tipus = tipus



Utanfutotipus.utipus = ["Fekezett", "Ponyvas"]

for i in range(2):
    kolcsonzonev = input("Add meg az ügyfél nevét: ")
    honap = input("Add meg a foglalás hónapját: ")
    nap = input("Add meg a foglalás napját: ")
    tipus = input("Add meg a típust(Fekezett, Ponyvas): ")
    Kolcsonzes(kolcsonzonev, honap, nap, tipus)

print(Kolcsonzes)






