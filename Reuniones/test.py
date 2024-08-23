import datetime


class Reunion:
    def __init__(self, id, date, dur):
        self.nroR = id
        self.fecha = date
        self.duracion = dur


def modificar(r, overlap):
    print("Informacion de la reuniones\n")
    print(r.nroR, r.fecha.datetime(), r.duracion)
    print([(re.nroR, re.fecha.datetime(), re.duracion) for re in overlap])
    print("\nModificar la reunion inicial")
    year, month, day, hour, min = map(int, input("Modificacion ").split())
    r.fecha= datetime.datetime(year, month, day, hour, min)

reuniones = []
indexReunion = 0
overlap = []
while True:
    year, month, day, hour, min = map(int, input("Fecha y Hora ").split())
    dura = int(input("Duracion "))
    date = datetime.datetime(year, month, day, hour, min)
    x = Reunion(indexReunion, date, dura)
    reuniones.append(x)
    indexReunion += 1
    y = int(input("0 --> Salir "))
    if y == 0:
        break

r = reuniones[0]
horaFin = r.fecha+datetime.timedelta(minutes=r.duracion)
for re in reuniones:
    if r.fecha.date() == re.fecha.date() and ((r.fecha< re.fecha< horaFin) or (re.fecha < r.fecha < (re.fecha+datetime.timedelta(minutes = re.duracion)))):
        overlap.append(re)
print([(re.nroR, re.fecha.datetime()) for re in overlap])
modificar(r, overlap)


