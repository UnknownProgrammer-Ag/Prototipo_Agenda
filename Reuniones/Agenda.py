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
        self.agenda = None

    # Método para resguardar usuario


