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
   - duración --> Total de minutos de duración transformados en hh:mm
   - horaI --> La hora de inicio de la duración en formato hh:mm
   - fecha --> Día en que se va a dar la reunión en formato YY.MM.DD
   - pendiente --> Estado de la reunión, en formato binario, representando la asistencia del usuario
# Clase: Usuario
### Atributos
   - usuario --> Representa el nombre de usuario
   - reuniones --> Colección de objetos 'Reunión'
   - cant --> Cuantifica el total de reuniones existentes para el usuario, asistidas o no.
