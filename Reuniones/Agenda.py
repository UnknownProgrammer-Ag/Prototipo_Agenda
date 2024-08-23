import os
import pickle
import datetime


class Reunion:
    def __init__(self, id, mod, det, part, tem, datetime, dur):
        self.nroR = id
        self.modalidad = mod
        self.detalle = det
        self.participantes = part
        self.tema = tem
        self.fechaHora = datetime
        self.duracion = dur
        self.pendiente = True

    def listar(self):
        horas = self.duracion // 60
        minutos = self.duracion % 60

        print(f"=======\nReunión {self.nroR}\n=======\n"
        f"Modalidad: {self.modalidad}\n"
        f"Detalle: {self.detalle}\n"
        f"Tema: {self.tema}\n"
        f"Participantes: {self.participantes}\n"
        f"Fecha: {self.fechaHora.date()}\n"
        f"Hora de Inicio: {self.fechaHora.time()}\n"
        f"Duración: {horas} hr : {minutos} min\n")
        if self.pendiente:
            print('Estado: PENDIENTE')
        else:
            print('Estado: ASISTIDO')


class Usuario:
    def __init__(self, name):
        self.identidad = name
        self.pendientes = 0
        self.asistidas = 0
        self.total = 0

    def estadistica(self):
        print(f'Reuniones Total: {self.total}\n')
        print(f'Reuniones Asistidas: {self.asistidas}\n')
        print(f'Reuniones Pendientes: {self.pendientes}\n')


class Agenda:
    def __init__(self):
        self.usuario = None
        self.reuniones = []
        self.indexReunion = 0

    def showAndSelect(self):
        for (i, re) in enumerate(self.reuniones):
            print(f"{i+1}. Reunión {re.nroR}| {re.modalidad}| Sobre {re.tema}")

        select = int(input('Indique el item [1..n] de la reunión que desea expandir.\n Ingrese 0 para salir '))
        if select != 0:
            self.reuniones[select-1].listar()

    def cargar_reunion(self):
        print("=====================")
        print(" CREADOR DE REUNION ")
        print("=====================")
        mod = input("Indique modalidad de la reunión [ Presencial | Virtual ] ")
        if (mod == 'Presencial' or mod == 'presencial'):
            print("Indique una breve indicación de lugar [Casa de X] ó una breve dirección [Calle X Piso X] ")
        else:
            print("Indique el código de la reunión [Presione Enter para dejar en blanco] ")
        det = input()
        part = []
        while True:
            item = input("Indique el nombre|apodo|apellido del participante ")
            part.append(item)
            add = input("¿Desea agregar más miembros? [ Y|N ] ")
            if add == 'N':
                break
        tem = input("Indique el tema de la reunión ")
        dur = int(input("Indique la duración en minutos de la reunión (estimada en minutos) "))
        # --------
        # Carga de fecha usando datetime y un catch de error
        datetime = None
        while datetime == None:
            try:
                year, month, day, hour, min = map(int, input("Ingrese fecha y hora de inicio, en formato YYYY MM DD hh mm, separado por espacio").split())
                datetime = datetime.datetime(year, month, day, hour, min)
            except ValueError:
                print("Ingrese una fecha válida")
        # Cargar de reunión e incremento de index
        id = self.indexReunion
        r = Reunion(id, mod, det, part, tem, datetime, dur)
        if self.checkOverlap(r):
            self.reuniones.append(r)
            self.indexReunion += 1

    def checkOverlap(self, r):
        overlap = []
        for re in self.reuniones:
            if re.fechaHora.date() == r.fechaHora.date() and re.fechaHora.time() < (r.fechaHora+datetime.timedelta(minutes = r. duracion)):
                overlap.append(re)
            horaFin = r.fechaHora + datetime.timedelta(minutes = r.duracion)
        for re in overlap:
            horaFin2 = re.fechaHora + datetime.timedelta(minutes = re.duracion)

            if horaFin > re.fechaHora.time():
                print(f"La reunión creada {r.nroR} choca con la reunión existente {re.nroR}")
                print(f"Hay una diferencia de {horaFin - re.fechaHora.time()}")
                self.Modify(r)
            else horaFin2 > r.fechaHora.time():
                print(f"La reunión existente {re.nroR} choca con la reunión creada {r.nroR}")
                print(f"Hay una diferencia de {horaFin2 - r.fechaHora.time()}")
                self.Modify(re)

    def save_reunion(self, filename):
        with open(filename, 'wb') as savefile:
            pickle.dump(self.reuniones, savefile)

    def load_reunion(self, filename):
        try:
            with open(filename, 'rb') as loadfile:
                self.reuniones = pickle.load(loadfile)
        except FileNotFoundError:
            self.reuniones = []

    def save_user(self, filename):
        with open(filename, 'wb') as savefile:
            pickle.dump(self.usuario, savefile)

    def load_user(self, filename):
        try:
            with open(filename, 'rb') as loadfile:
                self.usuario = pickle.load(loadfile)
        except FileNotFoundError:
            self.usuario = None

    def create_user(self):
        while (self.usuario == None):
            name = input("¿Quién usará está agenda? ")
            if name != '':
                self.usuario = Usuario(name)
                print(f' Enlace realizado, bienvenido {self.usuario}')
            else:
                print("No se acepta vacío, indique un nombre de usuario")

    def Modify(self, Reunion):


    # Método para un menú o generar una función principal?
    # Figlet
