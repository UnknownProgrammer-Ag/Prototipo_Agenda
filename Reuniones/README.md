Una agenda personal permita registrar reuniones en las que el usuario va a participar.
En tal agenda debe registrarse donde ocurrirá la reunión, quienes van a participar de ella, el tema que van a tratar y la duración de la misma.

# Clases
Reunion
## Atributos
    Id de Reunion (Entero)
    Modo de Reunion (Presencial, Virtual) --> ¿Dónde ocurrirá la reunión? En el Zoom/Meet o en X Calle X Piso.
    Si presencial 
        Dirección (String Alfanumerico) 
    Si virtual
        Código (String Alfanumerico)

    Participantes (Colección) --> ¿Quiénes participan de la reunión?

    Tema (String) --> ¿Qué tema será el eje de la reunión?
    Hora de Inicio --> Formato Hr:mts --> Permitir calcular con duración
    Duración (Entero o formateado a estilo horas:minutos) ¿Cuánto dura la reunión?
    Fecha (Date) --> Usar para filtrar las reuniones
    

    Se deberá poder buscar reuniones por fecha, el sistema detecte solapamientos y permita anularlos
    Se deberá poder eliminar reuniones

Usuario
## Atributos
    Username (Alfanumerico) --> Identificador de usuario
    Reuniones (Colección Clase Reunion)
    

