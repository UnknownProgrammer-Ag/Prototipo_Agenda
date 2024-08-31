'Una agenda personal permita registrar reuniones en las que el usuario va a participar. En tal agenda debe registrarse donde ocurrirá la reunión, quienes van a participar de ella, el tema que van a tratar y la duración de la misma.'
# Resumen de Funciones
- Alta/Baja/Modificación de reuniones
- Modificación de Asistencia, Fecha y Horario
- Listar las reuniones existentes para el usuario
- Filtrar por fecha (MM.DD) y por asistencia
- Detectar solapamiento de horarios, en un misma fecha.
# Clase: Reunion
### Atributos
   - nroR --> Id de la reunión 
   - modalidad --> Formato de la reunión (Presencial | Virtual)
   - detalle --> Información opcional dependiente del formato
   - participantes --> Listado de participantes de la reunión 
   - tema --> Temática de la reunión
   - fechaHora --> Atributo que contiene ambos, fecha y hora de inicio de la reunión
   - duración --> Total de minutos de duración transformados en hh:mm
   - pendiente --> Estado de la reunión, en formato binario, representando la asistencia del usuario
# Clase: Usuario
### Atributos
   - identidad --> Almacena el nombre de usuario
   - pendientes --> Almacena la cantidad de reuniones pendientes existentes
   - asistidas --> Almacena la cantidad de reuniones ya asistidas existentes
   - total --> Almacena la cantidad total de reuniones (asistidas + pendientes)
# Clase: Agenda
   - La agenda es la clase principal que esta compuesta de N instancias de Reunion y 1 instancia de Usuario.
   - La agenda puede mostrar todas las reuniones existentes para el usuario, filtradas por fecha u asistencia.
   - La agenda puede guardar y cargar el usuario y las reuniones de una sesión anterior.
   - La agenda puede cargar una reunión nueva, modificar su asistencia, modificar su fecha, duración u hora si existe solapamientos, y eliminar una instancia de Reunión.
### Atributos
   - usuario --> Almacena la instancia de Usuario
   - reuniones --> Almacena de 0..n instancias de Reunion
   - indexReunion --> Contador que identifica univocamente a cada instancia nueva
