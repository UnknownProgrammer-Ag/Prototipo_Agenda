import os
import pickle
import datetime
import time


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
        f"Fecha: {self.fechaHora.strftime('%A %d %B %Y')}\n"
        f"Hora de Inicio: {self.fechaHora.time()}\n"
        f"Duración: {horas} hr : {minutos} min\n")
        if self.pendiente:
            print('Estado: PENDIENTE')
        else:
            print('Estado: ASISTIDO')

    def cambiarFecha(self, year, month, day, hour, min):
        self.fechaHora = datetime.datetime(year, month, day, hour, min)

    def cambiarDuracion(self, duration):
        self.duracion = duration

    def cambiarAsistencia(self):
        self.pendiente = False


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
            #Esto es para eliminar reunion
            return select-1
        else:
            return -1

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
        flag = False
        while not flag:
            try:
                year, month, day, hour, min = map(int, input("Ingrese fecha y hora de inicio, en formato YYYY MM DD hh mm, separado por espacio").split())
                date = datetime.datetime(year, month, day, hour, min)
                flag = True
            except ValueError:
                flag = False
                print("Ingrese una fecha válida")
        # Cargar de reunión e incremento de index
        id = self.indexReunion
        r = Reunion(id, mod, det, part, tem, date, dur)
        if not self.checkOverlap(r):
            self.reuniones.append(r)
            self.indexReunion += 1
            self.usuario.pendientes +=1
            self.usuario.total += 1

    def checkOverlap(self, r):
        overlap = []
        horaFin = r.fechaHora+datetime.timedelta(minutes=r.duracion)
        for re in self.reuniones:
            horaFin2 = re.fechaHora+datetime.timedelta(minutes = re.duracion)
            if r.fechaHora.date() == re.fechaHora.date() and ((r.fechaHora< re.fechaHora < horaFin) or (re.fechaHora < r.fechaHora < horaFin2)):
                overlap.append(re)
        if overlap != []:
            self.modify(r, overlap)
        else:
            return False

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
                self.indexReunion = self.usuario.total 
        except FileNotFoundError:
            self.usuario = ''
            self.create_user()

    def create_user(self):
        while (self.usuario == ''):
            name = input("¿Quién usará está agenda? ")
            if name != '':
                self.usuario = Usuario(name)
                print(f' Enlace realizado, bienvenido {self.usuario}')
            else:
                print("No se acepta vacío, indique un nombre de usuario")

    def modify(self, r, overlap):
        print("===Informe===\n")
        print(f"Reunión por cargar Nro {r.nroR}\n"
            f"De fecha {r.fechaHora.strftime('%d %B %Y %H %M')} y duración {r.dur} minutos\n"
            f"Presenta incompatibilidades con reuniones pendientes\n")
        print("A continuación se detallarán los choques...\n")
        for re in overlap:
            print(f"Reunión {re.nroR}\n"
                  f"En el horario {re.fechaHora.strftime('%H %M')}, hasta las {(re.fechaHora+datetime.timedelta(minutes=re.duracion)).strftime('%H %M')}\n")
        print("Indique si modificará fecha, horario o duración de la reunión\n")
        opt = input('Fecha | Hora | Duracion| Predeterminado: Fecha')
        components = r.fechaHora.timetuple()
        match opt:
            case 'Fecha':
                hor = components[3]
                min = components[4]
                year, month, day = map(int, input("Fecha nueva ").split())
                r.cambiarFecha(year, month, day, hor, min)
            case 'Hora':
                year = components[0]
                month = components[1]
                day = components[2]
                hor, min = map(int, input("Hora de inicio nueva ").split())
                r.cambiarFecha(year, month, day, hor, min)
            case 'Duracion':
                dur = int(input("Duración nueva "))
                r.cambiarDuracion(dur)
            case _:
                hor = components[3]
                min = components[4]
                year, month, day = map(int, input("Fecha nueva ").split())
                r.cambiarFecha(year, month, day, hor, min)
        print("Cambio guardado, realizando verificación...\n")
        clear()
        self.checkOverlap(r)
    
    def modifyAssistance(self):
        for re in self.reuniones:
            if re.pendiente:
                re.listar()
                opt = input("¿Asistió a la reunión? [Y|N] ")
                if opt == 'N':
                    pass
                    clear()
                else:
                    re.cambiarAsistencia()
                    re.listar()
                    time.sleep(3)
                    clear()
            else:
                pass

    def deleteReunion(self):
        index = self.showAndSelect()
        if index != -1:
            print("Eliminando reunión...")
            self.reuniones.pop(index)
            print("Eliminación exitosa")
        else:
            print("Cancelando eliminación...")

def clear():
    os.system('clear')

def menu():
    userFile = 'userLog.pk1'
    dataFile = 'reunionLog.pk1'
    meetlog = Agenda()
    meetlog.load_user(userFile)
    meetlog.load_reunion(dataFile)

    while True:
        clear()
        print(f"AGENDA PERSONAL de {meetlog.usuario}\n"
              "\t1.Agregar Reunión\n"
              "\t2.Mostrar Reuniones\n"
              "\t3.Actualizar Asistencia\n"
              "\t4.Eliminar Reuniones\n"
              "\t5.Salir\n")
        
        opt = input("Ingrese opcion... ")
        match opt:
            case '1':
                meetlog.cargar_reunion()
            case '2':
                meetlog.showAndSelect()
                input('Enter para continuar...')
            case '3':
                meetlog.modifyAssistance()
            case '4':
                meetlog.deleteReunion()
                time.sleep(10)
            case '5':
                print("Guardando información...")
                meetlog.save_reunion(dataFile)
                meetlog.save_user(userFile)
                time.sleep(2.5)
                return 'Finalizando agenda...'
            case _:
                input("Opción no reconocida...Presione ENTER para regresar ")

if __name__ == '__main__':
    menu()
