# Primera Lectura
Aplicación orientada a organizar:
### Participantes de la Bienal:
   - Escultores --> Nombre, biografia, contacto, obras previas
   - Ciudadanos - Visitantes -
   - ¿ Organizadores ?
### Eventos
   - Atributos Indispensables: fecha, lugar, descripción y temática
   - ¿ Votos Especificos ?
   - ¿ Comentarios Especificos ?
### Esculturas
   - Temática --> Descripción Extensa
   - Fecha de Creación 
   - A definir...

*Los visitantes deben poder votar y realizar comentarios durante la realización de la bienal y los eventos.*
Eventos --> Integrado por votos y comentarios específicos.
Bienal --> Integrada por votos y comentarios generales.

>[NOTE] ¿ Responsabilidad de los organizadores ?
> Los eventos deben ser registrados al igual que los escultores.

# Requerimientos Funcionales
## Registro
   - Generar Eventos Nuevos
   - Tener historial de eventos pasados (¿ DB ?)
   - ABM de información de los eventos 
   - ABM de escultores
   - ABM Esculturas
   - Galería de fotos ¿Filtrado por etapas?
## Interactividad con visitantes (Aplicación Web)
   - Dentro de la aplicación un calendario de eventos, un programa de eventos interactivo.
   - Sección de escultores (similar a la galería de imágenes pero con esculturas)
   - Cada escultor y escultura tendrá asociada una métrica --> ¿ Contabilizar los votos, ranking, los más votados en la página principal ? 
## Medidas de Seguridad
   - Sistema de Registro de usuario --> Organizadores tendrán funciones distintas al visitante
   - Visitante debe tener un mail vinculado ( Imposible evitar el review-bombing )
   - Manejo de QR

# Requerimientos No Funcionales
## Mayor alcance
   - Interfaz multiplataforma (Multiples Resoluciones)
   - Navegabilidad --> La página debe ser intuitiva, no llevar de la mano al usuario, marcarle el camino
   - Accesibilidad e Integración con Redes Sociales. Implementar temas para daltónicos, aumentar la fuente de la páǵina, narrador para personas sin o poca visión.
## Seguridad
   - Autenticación --> Ya abarcado en los requerimientos funcionales
   - Protección de la DB
   - Validación de Votos (Captcha es la opción más sencilla. ¿ Métodos Externos ?)
## Performance
   - Optimización de Imágenes y tiempo de respuesta: Seguir buenas prácticas en FrontEnd para reducir los ms

