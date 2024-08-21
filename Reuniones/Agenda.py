import os, pickle, datetime

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

        print(f'=======\nReunión {self.nroR}\n=======\n')
        print(f'
        Modalidad: {self.modalidad}\n
        Detalle: {self.detalle}\n
        Tema: {self.tema}\n
        Participantes: {self.participantes}\n
        Hora de Inicio: {self.horaInicio}\n
        Duración: {horas} hr : {minutos} min\n
        Fecha: {self.fecha}\n')
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

def clear():
    os.system('cls')

class Agenda:
    def __init__(self):
        self.usuario = None
        self.reuniones = []
        self.indexReunion = 0

    # Listar una version resumida de todas las reuniones con una numeración. Ex: ID y Modalidad y Tema
    # Usuario ingrese número de item (no ID) que quiera expandir, y llamar a listar()
    # Método para guardar y cargar usuario
    # Método para guardar y cargar reuniones
    # Método de creacion de Reuniones
    # Método de creacion de usuario
    # Método de eliminación y modificación de reuniones

    # Método para un menú o generar una función principal?
    # Figlet

