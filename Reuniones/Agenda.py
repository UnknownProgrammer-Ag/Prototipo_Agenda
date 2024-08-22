import os
import pickle
import datetime


class Reunion:
    def __init__(self, id, mod, det, part, tem, hour, dur, date):
        self.nroR = id
        self.modalidad = mod
        self.detalle = det
        self.participantes = part
        self.tema = tem
        self.horaInicio = hour
        self.duracion = dur
        self.fecha = date
        self.pendiente = True

    def listar(self):
        horas = self.duracion // 60
        minutos = self.duracion % 60

        print(f"=======\nReunión {self.nroR}\n=======\n"
        f"Modalidad: {self.modalidad}\n"
        f"Detalle: {self.detalle}\n"
        f"Tema: {self.tema}\n"
        f"Participantes: {self.participantes}\n"
        f"Hora de Inicio: {self.horaInicio}\n"
        f"Duración: {horas} hr : {minutos} min\n"
        f"Fecha: {self.fecha}\n")

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
        hour = input("Indique la hora de inicio en formato hh:mm ")
        dur = int(input("Indique la duración en minutos de la reunión (estimada en minutos) "))
        entrada_fecha = input("Indique la fecha de la reunión YYYY.MM.DD ")
        year, month, day = map(int, entrada_fecha.split('.'))
        date = datetime.date(year, month, day)
        id = self.indexReunion
        self.indexReunion += 1
        r = Reunion(id, mod, det, part, tem, hour, dur, date)
        self.reuniones.append(r)

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

    def deleteOrModify(self):


    # Método para un menú o generar una función principal?
    # Figlet
