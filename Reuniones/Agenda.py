import os
import pickle
import datetime


class Reunion:
    def __init__(self, id, mod, det, part, tem, dur, date):
        self.nroR = id
        # Dos opciones: Presencial o Virtual
        self.modalidad = mod
        # Presencial --> Dirección o descripción referencial
        # Virtual --> Código
        self.detalle = det
        self.participantes = part
        self.tema = tem
        # Contabilizada en minutoss --> Mostrada en horas:minutos
        self.duracion = dur
        # Fecha de reunión como un string
        self.fecha = date
        # Cuando el usuario revise las reuniones se le dará la posibilidad de "completar" las reuniones asistidas
        self.pendiente = True

    def __repr__(self):
        return "Representa la clase reunión con detalles de su modalidad, completitud, duración"

    def asistencia(self):
        self.pendiente = False
    
    def listar(self):
        horas = self.duracion//60
        minutos = self.duracion % 60
        print(f'=======\nReunión {self.nroR}\n=======\nModalidad: {self.modalidad}\nDetalle: {self.detalle}\nParticipantes: {self.participantes}\nTema: {self.tema}\nDuración: {horas} hrs : {minutos} min\nFecha: {self.fecha}')
        if self.pendiente:
            print('Estado: Pendiente')
        else:
            print('Estado: Asistido')


class Usuario:
    def __init__(self, name):
        self.usuario = name
        self.reuniones = []
        self.cant = 0

    def __repr__(self):
        return "Representa al usuario del que corresponde la agenda"
        
    def cargar_reunion(self):
        print('===========================')
        print('Creador de Reunión')
        print('===========================')
        mod = input('¿Que clase de reunión será? [ Presencial|Virtual ] ')
        if (mod == 'Presencial' or mod == 'presencial'):
            print('Ingrese una breve indicacion de lugar [Casa de X] ó una breve dirección [Calle X Piso X] ')
            det = input()
        else:
            print('Ingrese el código de la reunión [Presione Enter para dejar en blanco] ')
            det = input()
        part = []
        while True:
            item = input('Ingrese el nombre|apodo|apellido del participante ')
            part.append(item)
            add = input('¿Desea agregar más miembros? [Y|N] ')
            if add == 'N':
                break
        tem = input('Ingrese el tema de la reunión ')
        dur = int(input('Ingrese la duración en minutos de la reunión (estimada) '))
        entrada_fecha = input('Ingrese la fecha de la reunión YYYY.MM.DD ')
        year, month, day = map(int, entrada_fecha.split('.'))
        date = datetime.date(year, month, day)
        id = self.cant
        r = Reunion(id, mod, det, part, tem, dur, date)
        self.cant += 1
        self.reuniones.append(r)

    def mostrarReuniones(self):
        for re in self.reuniones:
            print(f'{re.listar()}\n')


def clear():
    #  os.system('cls') on Windows System
    os.system('clear')  # on Linux System


def save(reuniones, filename='save.pk1'):
    with open(filename, 'wb') as savefile:
        pickle.dump(reuniones, savefile)


def load(filename='save.pk1'):
    try:
        with open(filename, 'rb') as savefile:
            return pickle.load(savefile)
    except FileNotFoundError:
        return []


def main():
    backupUser = 'user.txt'
    if os.path.exists(backupUser):
        with open(backupUser, 'r') as userLoad:
            content = userLoad.readlines()
        name = content[0].strip()
        user = Usuario(name)
        user.cant = int(content[1].strip())
        user.reuniones = load()
    else:
        name = input("Antes de empezar a trabajar con la Agenda requerimos su nombre... ")
        user = Usuario(name)

    while True:
        clear()
        print(f'AGENDA PERSONAL de {user.usuario} \n')
        print('\t1.Agregar Reunión\n')
        print('\t2.Mostrar Reuniones\n')
        print('\t3.Modificar Asistencia\n')
        print('\t4.Salir\n')

        opt = input('Ingrese opcion... ')
        match opt:
            case '1':
                user.cargar_reunion()
            case '2':
                user.mostrarReuniones()
                input('Enter para continuar...')
            case '3':
                for re in user.reuniones:
                    if re.pendiente:
                        re.listar()
                        opt = input('¿Desea cambiar el estado de la reunión? [Y|N] ')
                        if opt == 'N':
                            pass
                        else:
                            re.asistencia()
                            re.listar()
                            input('Enter para continuar...')
                    else:
                        pass
            case '4':
                with open(backupUser, 'w') as userSave:
                    userSave.write(name+'\n')
                    userSave.write(str(user.cant))
                    save(user.reuniones)
                return 'Finalizando agenda'
            case _:
                input('Opción Inválida...Presione ENTER para regresar')


if __name__ == '__main__':
    main()
