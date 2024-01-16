class Utanfuto:
    def __init__(self, tipus, ar, teherbiras):
        self.tipus = Utanfutotipus.tipus
        self.ar = ar
        self.teherbiras = teherbiras

class Utanfutotipus:
    def __init__(self, tipus):
        self.tipus = tipus

class Kolcsonzo:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

class Kolcsonzes:
    def __init__(self, kolcsonzonev, honap, nap, ido, tipus):
        self.kolcsonzonev = kolcsonzonev
        self.honap = honap
        self.nap = nap
        self.ido = ido
        self.tipus = Utanfutotipus.tipus

