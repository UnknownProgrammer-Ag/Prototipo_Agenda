import os
import pickle
import datetime
import time
from pyfiglet import Figlet
from colorama import Fore, init
init(autoreset=True)


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

        print("=======\nReunión "+Fore.LIGHTBLUE_EX+f"{self.nroR}"+Fore.RESET+"\n=======\n"
        "Modalidad: "+Fore.LIGHTBLUE_EX+f"{self.modalidad}\n"+Fore.RESET+
        "Detalle: "+Fore.LIGHTBLUE_EX+f"{self.detalle}\n"+Fore.RESET+
        "Tema: "+Fore.LIGHTBLUE_EX+f"{self.tema}\n"+Fore.RESET+
        "Participantes: "+Fore.LIGHTBLUE_EX+f"{self.participantes}\n"+Fore.RESET+
        "Fecha: "+Fore.LIGHTBLUE_EX+f"{self.fechaHora.strftime('%A %d %B %Y')}\n"+Fore.RESET+
        "Hora de Inicio: "+Fore.LIGHTBLUE_EX+f"{self.fechaHora.time()}\n"+Fore.RESET+
        "Duración: "+Fore.LIGHTBLUE_EX+f"{horas} hr : {minutos} min")
        if self.pendiente:
            print('Estado: '+Fore.LIGHTBLUE_EX+'PENDIENTE')
        else:
            print('Estado: '+Fore.LIGHTBLUE_EX+'ASISTIDO')
        Fore.RESET


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
        print("====================================")
        print('Reuniones Total: '+ Fore.CYAN+ f'{self.total}')
        print('Reuniones Asistidas: '+ Fore.CYAN+f'{self.asistidas}')
        print('Reuniones Pendientes: '+ Fore.CYAN+f'{self.pendientes}')
        print("===================================\n")


class Agenda:
    def __init__(self):
        self.usuario = None
        self.reuniones = []
        self.indexReunion = 0

    def showAndSelect(self, reunion):
        for (i, re) in enumerate(reunion):
            print(f"{i+1}. Reunión "+Fore.BLUE+f"{re.nroR}"+Fore.RESET+f"| {re.modalidad} acerca de "+Fore.BLUE+f"{re.tema}")
        select = int(input('Indique el item [1..n] de la reunión que desea expandir.\n Ingrese 0 para salir '))
        if select != 0:
            reunion[select-1].listar()
            # Esto es para eliminar_reunion
            choosed = reunion[select-1]
            return choosed
        else:
            return -1

    def manageReunion(self, arg):
        if arg == '':
            sel = self.showAndSelect(self.reuniones)
        elif isinstance(arg, (datetime.date)):
            print(f"Filtrado por: {arg.date()} ")
            filter = [re for re in self.reuniones if re.fechaHora.date() == arg.date()]
            sel = self.showAndSelect(filter)
        else:
            print(f"Filtrado por: {arg} ")
            filter = [re for re in self.reuniones if (re.pendiente == arg)]
            sel = self.showAndSelect(filter)
        return sel

    def cargar_reunion(self):
        clear()
        print(Fore.GREEN+"===========================================================================")
        f = Figlet(font="doom")
        print(Fore.GREEN+f.renderText("CREADOR DE REUNION "))
        print(Fore.GREEN+"===========================================================================")
        mod = input("Indique modalidad de la reunión [ Presencial | Virtual ] "+Fore.LIGHTGREEN_EX)
        if mod.lower() == 'presencial':
            print(Fore.RESET+"Indique una breve indicación de lugar [Casa de X] ó una breve dirección [Calle X Piso X] ")
        else:
            print(Fore.RESET+"Indique el código de la reunión [Presione Enter para dejar en blanco] ")
        det = input(Fore.LIGHTGREEN_EX)
        part = []
        while True:
            item = input(Fore.RESET+"Indique el nombre|apodo|apellido del participante "+Fore.LIGHTGREEN_EX)
            part.append(item)
            add = input(Fore.RESET+"¿Desea agregar más miembros? [ Y|N ]\nPor defecto (Y) "+Fore.LIGHTGREEN_EX)
            if add.lower() == 'n':
                break
        tem = input(Fore.RESET+"Indique el tema de la reunión "+Fore.LIGHTGREEN_EX)
        dur = int(input(Fore.RESET+"Indique la duración en minutos de la reunión (estimada en minutos) "+Fore.LIGHTGREEN_EX))
        # --------
        # Carga de fecha usando datetime y un catch de error
        flag = False
        while not flag:
            try:
                year, month, day, hour, min = map(int, input(Fore.RESET+"Ingrese fecha y hora de inicio, en formato YYYY MM DD hh mm, separado por espacio "+Fore.LIGHTGREEN_EX).split())
                date = datetime.datetime(year, month, day, hour, min)
                flag = True
            except ValueError:
                flag = False
                print(Fore.RED+"Ingrese una fecha válida")
        # Cargar de reunión e incremento de index
        id = self.indexReunion
        r = Reunion(id, mod, det, part, tem, date, dur)
        if not self.checkOverlap(r):
            self.reuniones.append(r)
            self.indexReunion += 1
            self.usuario.pendientes += 1
            self.usuario.total += 1

    def checkOverlap(self, r):
        overlap = []
        horaFin = r.fechaHora+datetime.timedelta(minutes=r.duracion)
        for re in self.reuniones:
            horaFin2 = re.fechaHora+datetime.timedelta(minutes=re.duracion)
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
            self.create_user()

    def create_user(self):
        while True:
            name = input("¿Quién usará está agenda? "+Fore.BLUE)
            if name != '':
                self.usuario = Usuario(name)
                print(Fore.LIGHTGREEN_EX+f' Enlace realizado, bienvenido {self.usuario}')
                break
            else:
                print(Fore.RED+"No se acepta vacío, indique un nombre de usuario")

    def modify(self, r, overlap):
        f = Figlet(font='slant')
        print(Fore.YELLOW+f.renderText("<<<Informe>>>"))
        print("Reunión por cargar: "+Fore.LIGHTMAGENTA_EX+f"Nro {r.nroR}\n"+Fore.RESET+
            "Con fecha para el "+Fore.LIGHTMAGENTA_EX+f"{r.fechaHora.strftime('%d %B %Y %H:%M')}"+Fore.RESET+" y duración de "+Fore.LIGHTMAGENTA_EX+f"{r.duracion} minutos\n"
            +Fore.LIGHTRED_EX+"Presenta incompatibilidades con reuniones existentes\n")
        print("A continuación se detallarán los choques...\n")
        for re in overlap:
            print("Reunión "+Fore.GREEN+f"{re.nroR}\n"
                +Fore.RESET+"Que va de las "+Fore.GREEN+f"{re.fechaHora.strftime('%H:%M')}"+Fore.RESET+" hasta las "+Fore.GREEN+f"{(re.fechaHora+datetime.timedelta(minutes=re.duracion)).strftime('%H:%M')}\n")
        print("Indique si modificará fecha, horario o duración de la reunión\n")
        opt = input('Fecha | Hora | Duracion| Predeterminado: Fecha '+Fore.BLUE)
        components = r.fechaHora.timetuple()
        match opt:
            case 'Fecha':
                hor = components[3]
                min = components[4]
                year, month, day = map(int, input("Fecha nueva "+Fore.BLUE).split())
                r.cambiarFecha(year, month, day, hor, min)
            case 'Hora':
                year = components[0]
                month = components[1]
                day = components[2]
                hor, min = map(int, input("Hora de inicio nueva "+Fore.BLUE).split())
                r.cambiarFecha(year, month, day, hor, min)
            case 'Duracion':
                dur = int(input("Duración nueva "+Fore.BLUE))
                r.cambiarDuracion(dur)
            case _:
                hor = components[3]
                min = components[4]
                year, month, day = map(int, input("Fecha nueva "+Fore.BLUE).split())
                r.cambiarFecha(year, month, day, hor, min)
        print(Fore.RESET+"Cambio guardado, realizando verificación...\n")
        clear()
        self.checkOverlap(r)

    def modifyAssistance(self):
        for re in self.reuniones:
            if re.pendiente:
                re.listar()
                opt = input("¿Asistió a la reunión? [Y|N]\nPor defecto (Y)")
                if opt.lower() == 'n':
                    pass
                    clear()
                else:
                    re.cambiarAsistencia()
                    re.listar()
                    self.usuario.pendientes -= 1
                    self.usuario.asistidas += 1
                    time.sleep(3)
                    clear()
            else:
                pass

    def deleteReunion(self, arg):
        deleted = self.manageReunion(arg)
        if deleted != -1:
            confirm = input("Como ultima oportunidad, ¿Desea eliminar esta reunion? [Y|N]\nPor Defecto (N) "+Fore.BLUE)
            if confirm.lower() == 'y':
                print(Fore.RED+"Eliminando reunión...")
                if deleted.pendiente:
                    self.usuario.pendientes -= 1
                else:
                    self.usuario.asistidas -= 1
                self.usuario.total -= 1
                self.reuniones.remove(deleted)
                print(Fore.LIGHTGREEN_EX+"Eliminación exitosa")
            else:
                print(Fore.MAGENTA+"Cancelando eliminación...")
        else:
            print(Fore.MAGENTA+"Cancelando eliminación...")


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
        f = Figlet(font='slant')
        print(Fore.BLUE+f.renderText("AGENDA PERSONAL de"))
        print(Fore.BLUE+f.renderText(f"{meetlog.usuario.identidad}"))
        meetlog.usuario.estadistica()
        Fore.RESET
        print("\t\t1.Agregar Reunión\n"
              "\t\t2.Mostrar Reuniones\n"
              "\t\t3.Actualizar Asistencia\n"
              "\t\t4.Eliminar Reuniones\n"
              "\t\t5.Salir\n")

        opt = input("Ingrese opcion... ")
        match opt:
            case '1':
                meetlog.cargar_reunion()
            case '2':
                print("Puedes ver todas, filtrar por fecha "+Fore.LIGHTCYAN_EX+"(YYYY MM DD) "+Fore.RESET+"o por asistencia"+Fore.LIGHTCYAN_EX+" (Asistida | Pendiente)")
                inp = input("Ingrese la fecha o la asistencia en el formato mostrado o Enter para no filtrar... ")
                if inp.lower() == 'asistida':
                    filt = False
                elif inp.lower() == 'pendiente':
                    filt = True
                elif inp != '':
                    try:
                        year, month, day = map(int, inp.split())
                        filt = datetime.datetime(year, month, day, 0, 0)
                    except ValueError as e:
                        print(Fore.RED+"Fecha Inválida")
                        filt = ""
                        raise e
                else:
                    filt = inp
                meetlog.manageReunion(filt)
                input('Enter para continuar...')
            case '3':
                meetlog.modifyAssistance()
            case '4':
                print("Puedes ver todas, filtrar por fecha "+Fore.LIGHTCYAN_EX+"(YYYY MM DD)"+Fore.RESET+"o por asistencia "+Fore.LIGHTCYAN_EX+"(Asistida | Pendiente) ")
                inp = input("Ingrese la fecha o la asistencia en el formato mostrado o Enter para no filtrar... ")
                if inp.lower() == 'asistida':
                    filt = False
                elif inp.lower() == 'pendiente':
                    filt = True
                elif inp != '':
                    try:
                        year, month, day = map(int, inp.split())
                        filt = datetime.datetime(year, month, day, 0, 0)
                    except ValueError as e:
                        print(Fore.RED+"Fecha Inválida")
                        filt = ""
                        raise e
                else:
                    filt = inp
                meetlog.deleteReunion(filt)
                time.sleep(3.5)
            case '5':
                print(Fore.LIGHTGREEN_EX+"Guardando información...")
                meetlog.save_reunion(dataFile)
                meetlog.save_user(userFile)
                time.sleep(0.5)
                return 'Finalizando agenda...'
            case _:
                input(Fore.LIGHTRED_EX+"Opción no reconocida...Presione ENTER para regresar ")


if __name__ == '__main__':
    menu()
