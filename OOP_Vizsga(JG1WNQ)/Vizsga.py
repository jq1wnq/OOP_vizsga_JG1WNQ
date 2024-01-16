class Utanfuto:
    def __init__(self, tipus, ar, teherbiras):
        self.tipus = tipus
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
    def __init__(self, kolcsonzonev, honap, nap, ktipus, ar):
        self.kolcsonzonev = kolcsonzonev
        self.honap = honap
        self.nap = nap
        self.ktipus = ktipus
        self.ar = ar

    def __str__(self):
        return f"{self.kolcsonzonev}, {self.honap}, {self.nap}, {self.ktipus}, {self.ar} "

    def getkolcsonzonev(self):
        for kolcsonzonev in self.kolcsonzonev:
            print(f"{self.kolcsonzonev}, {self.honap}, {self.nap}, {self.ktipus}, {self.ar}")




kolcs1 = Kolcsonzes("Ági", "Január", 8, "Ponyvás", "10 000 Ft")
kolcs2 = Kolcsonzes("János", "Február", 27, "Ponyvás", "10 000 Ft")
foglalasok = [kolcs1, kolcs2]

afoglalas = Kolcsonzes
print(afoglalas)





for i in range(2):
    ugyfel = input("Add meg az ügyfél nevét: ")
    fhonap = input("Add meg a foglalás hónapját: ")
    fnap = input("Add meg a foglalás napját: ")
    ftipus = input("Add meg a típust(Fekezett, Ponyvas): ")
    far = input("Add meg az árat: ")
    print(ugyfel, fhonap, fnap, ftipus, far)







print(kolcs1)












