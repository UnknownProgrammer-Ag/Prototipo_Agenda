from random import randrange, choice


def disparo(objetivo):
    objetivo.vida -= (1-objetivo.reduccion)
    print(objetivo.tipo)
    print(objetivo.reduccion)
    print(objetivo.vida)

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
        self.reduccion = escudo.proteccion / 100

    def disparar(self, objetivo):
        disparo(objetivo)

    def vivo(self):
        if self.vida <= 0:
            return False
        else:
            return True


class Tanques(Unidad):
    def __init__(self):
        self.vida = 2
        self.tipo = "tanque"


class Buques(Unidad):
    def __init__(self):
        self.vida = 3
        self.tipo = "buque"


def main():
    battleRoyale = []
    types = ['s', 'b', 't']
    armor = ['Y', 'N']
    turns = 0
    size = -1
    while size < 0 or size >= 1000:
        size = int(input("¿Cuántas unidades desea liberar? Max 1000 "))
    print(f"A continuación se generarán {size} unidades aleatorias compuestas por soldados, tanques y buques")
    print("Las unidades aleatoriamente tendrán puntos de escudo o no, permitiendoles reducir el daño recibido")
    for _ in range(size):
        opt = choice(armor)
        if opt == 'Y':
            prot = randrange(1, 100)
        else:
            prot = 0

        shield = Escudo(prot)
        unidades = choice(types)
        match unidades:
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
    # Guerra
    print("GUERRA")
    while (len(battleRoyale)) > 1:
        id1 = randrange(0, len(battleRoyale)-1)
        id2 = randrange(0, len(battleRoyale)-1)
        unit1 = battleRoyale[id1]
        unit2 = battleRoyale[id2]
        if id1 != id2:
            unit1.disparar(unit1)
            unit1.disparar(unit2)
            if not unit1.vivo():
                print("ENTRO a unit1 muerto")
                battleRoyale.pop(id1)
            elif not unit2.vivo():
                print("ENTRO a unit2 muerto")
                battleRoyale.pop(id2)
            elif not (unit1.vivo()) and not (unit2.vivo()):
                print("ENTRO a ambos muertos")
                battleRoyale.pop(id1)
                battleRoyale.pop(id2)
        turns += 1
        print(f"Turno {turns}")
        print(f"Arreglo de unidades: {battleRoyale[0].vida} y {battleRoyale[1].vida}")
        input()

    print(f"Después de {turns} turnos, el ganador es: {battleRoyale[0].tipo}")


if __name__ == "__main__":
    main()
