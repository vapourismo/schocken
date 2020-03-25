class Spieler:
    def __init__(self, name):
        self.name = name
        self.deckel = 0
        self.aktiv = False
        self.augen = [None, None, None]
        self.anzahl_wuerfe = 0

    def __str__(self):
        return f"Spieler {self.name}\nDeckel: {self.deckel}\n Augen: {self.augen}\n"

    def __repr__(self):
        return self.__str__()
