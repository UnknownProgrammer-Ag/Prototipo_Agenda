from random import randrange


class Escudo:
    def __init__(self, defensa):
        self.proteccion = defensa


# Unidad
class Unidad:
    def __init__(self):
        self.tipo = "soldado"
        self.vida = 1
        self.reduccion = 0

    def generarEscudo(self, escudo):
        self.reducción = escudo.proteccion / 100

    def disparo(self, objetivo):
        objetivo.vida -= (1-objetivo.reduccion)

    def vivo(self):
        if self.vida == 0:
            return False
        else:
            return True


class Tanques(Unidad):
    def __init__(self):
        self.vida = 2
        self.tipo = "tanque"


class Buques(Unidad):
    def __init__(self):
        self.vida = 3}
        self.tipo = "buque"


def main():
    battleRoyale = []
    while True:
        opt = input("Quiere colocar un escudo? (N) Y|N ")
        if opt == 'Y':
            prot = randrange(1, 100)
        else:
            prot = 0

        shield = Escudo(prot)
        choice = input("Soldado (s), Tanque (t), Buque(b)?")
        match choice:
            case 's':
                sold = Unidad()
                sold.generarEscudo(shield)
                battleRoyale.append(sold)
            case 't':
                tank = Tanques()
                tank.generarEscudo(shield)
                battleRoyale.append(tank)
            case 'b':
                ship = Buques()
                ship.generarEscudo(shield)
                battleRoyale.append(ship)
        exit = input(" Seguir (Y) N")
        if exit == "N":
            break

    # Guerra

    while battleRoyale.len > 1:
        id1 = randrange(0, battleRoyale.len)
        id2 = randrange(0, battleRoyale.len)
        if id1 != id2:
            battleRoyale[id1].disparo(battleRoyale[id2])
            battleRoyale[id2].disparo(battleRoyale[id1])
            if battleRoyale[id1].vivo ==False:
                battleRoyale.pop(id1)
            elif battleRoyale[id2].vivo ==False:
                battleRoyale.pop(id2)
            elif (battleRoyale[id1].vivo ==False) && (battleRoyale[id2].vivo == False) :
                battleRoyale.pop(id1)
                battleRoyale.pop(id2)
    
    print(f"Ganador: {battleRoyale[0].tipo}")


