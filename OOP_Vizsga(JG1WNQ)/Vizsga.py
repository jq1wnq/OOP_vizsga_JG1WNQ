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
    def __init__(self, kolcsonzonev, honap, nap, tipus, ar):
        self.kolcsonzonev = kolcsonzonev
        self.honap = honap
        self.nap = nap
        self.tipus = tipus
        self.ar = ar




kolcs1 = Kolcsonzes("Ági", "Január", 8, "Ponyvás", "10 000 Ft")
kolcs2 = Kolcsonzes("János", "Február", 27, "Ponyvás", "10 000 Ft")

foglalasok= [kolcs1, kolcs2]

Utanfutotipus.utipus = ["Fekezett", "Ponyvas"]


kolcsi = Kolcsonzes(input("Add meg az ügyfél nevét: "),
input("Add meg a foglalás hónapját: "),
input("Add meg a foglalás napját: "),
input("Add meg a típust(Fekezett, Ponyvas): "),
input("Add meg az árat: "))





print(foglalasok)









