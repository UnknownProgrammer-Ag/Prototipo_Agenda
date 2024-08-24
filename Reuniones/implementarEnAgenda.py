import datetime


class Reunion:
    def __init__(self, id, date, dur):
        self.nroR = id
        self.fecha = date
        self.duracion = dur


def modificar(r, overlap):
    print("Informacion de la reuniones\n")
    print(r.nroR, r.fecha.ctime(), r.duracion)
    print([(re.nroR, re.fecha.ctime(), re.duracion) for re in overlap])
    print("\nModificar la reunion inicial")
    year, month, day, hour, min = map(int, input("Modificacion ").split())
    r.fecha = datetime.datetime(year, month, day, hour, min)
    checkOverlap(r)


def checkOverlap(r):
    overlap = []
    horaFin = r.fecha+datetime.timedelta(minutes=r.duracion)
    for re in reuniones:
        horaFin2 = re.fecha+datetime.timedelta(minutes = re.duracion)
        if r.fecha.date() == re.fecha.date() and ((r.fecha< re.fecha< horaFin) or (re.fecha < r.fecha < horaFin2)):
            overlap.append(re)
    print([(re.nroR, re.fecha.ctime()) for re in overlap])
    if overlap != []: 
        modificar(r, overlap)
    else:
        return False


reuniones = []
indexReunion = 0
for _ in range(5):
    year, month, day, hour, min = map(int, input("Fecha y Hora ").split())
    dura = int(input("Duracion "))
    date = datetime.datetime(year, month, day, hour, min)
    x = Reunion(indexReunion, date, dura)
    reuniones.append(x)
    indexReunion += 1

r = reuniones[0]
check = checkOverlap(r)
if not check:
    print("Fin de Test --> No hay solapamiento")
