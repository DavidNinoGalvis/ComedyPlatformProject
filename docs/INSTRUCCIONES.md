#### Proyecto POO [PARTE 2]:

# 🎭 Sistema de Gestión de Eventos de Comedia

## Descripción General

Los eventos de comedia se han popularizado por todo el país.
El éxito de los comediantes ha llevado a la necesidad de tener un sistema de información que permita gestionar
los shows y los elementos que allí convergen. En este contexto, el proyecto busca desarrollar un sistema de gestión de
eventos enfocado en la comedia. Este sistema permitirá a los administradores crear, editar y eliminar eventos, gestionar
la boletería y generar reportes. Para este proyecto deberán aplicar sus conocimientos en Programación Orientada a
Objetos, Python y Streamlit.

La siguiente información contiene la misma información que tenía la primera parte del proyecto, más adiciones señaladas
con señaladas en **negrilla**

### Tipos de Eventos

El sistema debe manejar tres tipos específicos de eventos, cada uno con características propias:

- **Evento en Bar**:
    - Los comediantes son pagados por presentarse.
    - La boletería tiene una distribución de utilidades de 20% para el bar y 80% para el artista.

- **Evento en Teatro**:
    - Se debe pagar un valor por el alquiler del teatro.
    - Dada la amplia cantidad de asistentes, la tiquetera retiene el 7% de cada boleta vendida.

- **Evento Filantrópico**:
    - No maneja costo de alquiler y las boletas se ofrecen a cero pesos.
    - Los ingresos se obtienen de patrocinadores, por lo que se debe registrar quiénes son estos patrocinadores (nombre)
      y el valor aportado.

#### Criterios de aceptación:

- Se deben manejar 3 tipos de eventos en el sistema: evento en Bar, evento en Teatro y evento Filantrópico (boletería
  sin costo).
- El sistema permite ingresar detalles del evento como artista o artistas del show, nombre, fecha, hora de apertura de
  puertas, hora del show, lugar, dirección y ciudad.
- El sistema permite definir el estado del evento (realizado, por realizar, cancelado, aplazado, cerrado). Cambios en el
  estado "realizado" están restringidos.
- El administrador puede definir precios de boletas para diferentes categorías y fases de venta (preventa y venta
  regular).
- Se impide la eliminación de eventos con boletería vendida.
- El sistema permite definir el aforo total del evento.

## 🎟️ Gestión de Boletería

- Se requieren datos del comprador y cómo se enteró del evento al vender una boleta.
- El sistema verifica la disponibilidad de aforo antes de completar la venta.
- El precio de la boleta varía según la fase de venta y aplicaciones de descuentos.
- Las boletas de cortesía se pueden emitir con un precio de cero.
- **Generación de PDF con la boleta:** Use alguna librería de Python para generar la boleta. Agregue en el PDF
  información importante para el acceso al evento. Piense que su aplicación le aporte valor a los usuarios potenciales
  entonces analice cuidadosamente la información que incluiría en su pdf. El administrador usará esa boleta para
  enviarla posteriormente al cliente.

### Criterios de aceptación:

- Se requieren datos del comprador y cómo se enteró del evento al vender una boleta.
- El sistema verifica la disponibilidad de aforo antes de completar la venta.
- El precio de la boleta varía según la fase de venta y aplicaciones de descuentos.
- Las boletas de cortesía se pueden emitir con un precio de cero.
- **Generación de PDF con la boleta (use alguna librería de Python para generar la boleta). Agregue en el PDF
  información importante para el acceso al evento. Piense que su aplicación le aporte valor a los usuarios potenciales
  entonces analice cuidadosamente la información que incluiría en su pdf. El administrador usará esa boleta para
  enviarla posteriormente al cliente.**

## 🚪 Gestión de Ingreso al Evento

- Su aplicación debe permitir registrar el día del evento el ingreso.
- Para ello debe contar con algún mecanismo que permita buscar rápidamente una boleta vendida o un comprador a fin de
  registrar su asistencia.
- Nuevamente, piense que su aplicación le aporte valor a los usuarios potenciales entonces analice cuidadosamente que
  mecanismo usaría para facilitar la búsqueda.

## 📊 Generación de Reportes Detallados

### Criterios de aceptación:

- **Reporte de Ventas de Boletas:** Detalla cantidad de boletas vendidas por tipo (incluyendo cortesías) y los ingresos
  totales por preventa y venta regular.
- **Reporte Financiero:** Desglosa los ingresos por tipo de pago y tipo de boletería.
- **Reporte de Datos de los Compradores:** Ofrece información detallada de los compradores permitiendo análisis
  demográficos y de comportamiento para estrategias de marketing. Debe incluir al menos dos gráficas visualizando esta
  información (en Plotly) y estar disponible para descargar en formato Excel.
- **Reporte de Datos por Artista:** Dado un artista (que se puede filtrar desde la interfaz gráfica) será posible
  reportar datos generales de sus eventos gestionados en el sistema. En los datos generales de cada evento deben estar
  cosas como (nombre del evento, fecha, lugar, cantidad de boletas vendidas, porcentaje de aforo cubierto).

### 📈 Tablero de Control

Para el usuario es importante tener un tablero de control (dashboard) en el que pueda visualizar el estado de la gestión
de eventos para un rango de fechas. Agregue al menos en este dashboard gráficos que permitan ver información relacionada
con la cantidad de eventos por tipo que se han organizado en cierto periodo de tiempo, ingresos totales por eventos para
el rango de fechas definidas.## 🚪 Gestión de Ingreso al Evento

- Su aplicación debe permitir registrar el día del evento el ingreso.
- Para ello debe contar con algún mecanismo que permita buscar rápidamente una boleta vendida o un comprador a fin de
  registrar su asistencia.
- Nuevamente, piense que su aplicación le aporte valor a los usuarios potenciales entonces analice cuidadosamente que
  mecanismo usaría para facilitar la búsqueda.

## 📊 Generación de Reportes Detallados

### Criterios de aceptación:

- **Reporte de Ventas de Boletas:** Detalla cantidad de boletas vendidas por tipo (incluyendo cortesías) y los ingresos
  totales por preventa y venta regular.
- **Reporte Financiero:** Desglosa los ingresos por tipo de pago y tipo de boletería.
- **Reporte de Datos de los Compradores:** Ofrece información detallada de los compradores permitiendo análisis
  demográficos y de comportamiento para estrategias de marketing. Debe incluir al menos dos gráficas visualizando esta
  información (en Plotly) y los datos (sin las gráficas) deben estar disponibles para descargar en formato Excel ( puede usar pandas u openpyxl).
- **Reporte de Datos por Artista:** Dado un artista (que se puede filtrar desde la interfaz gráfica) será posible
  reportar datos generales de sus eventos gestionados en el sistema. En los datos generales de cada evento deben estar
  cosas como (nombre del evento, fecha, lugar, cantidad de boletas vendidas, porcentaje de aforo cubierto).

### 📈 Tablero de Control

**Para el usuario es importante tener un tablero de control (dashboard) en el que pueda visualizar el estado de la
gestión
de eventos para un rango de fechas. Agregue al menos en este dashboard gráficos que permitan ver información relacionada
con la cantidad de eventos por tipo que se han organizado en cierto periodo de tiempo, ingresos totales por eventos para
el rango de fechas definidas. [Puede usar cualquier librería gráfica de Python]
Puede agregar otras gráficas que puedan ser útiles para el usuario.**

## 🔧 Requerimientos Técnicos

- Se deben aplicar conocimientos de análisis y diseño UML, aplicación de Herencia, sobreescritura, sobrecarga, clases
  abstractas y concretas, y codificación en Python.
- Debe incluir pruebas unitarias.
- Se espera el uso de buenas prácticas de programación para separar las responsabilidades a fin de NO mezclar lógica de
  negocio con lógica de presentación. Muy importante tomar decisiones que favorezcan la mantenibilidad del código.
- Las clases deben estar documentadas en cuanto a funcionalidad y la codificación debe cumplir con el estándar de Python
  PEP8 (https://peps.python.org/pep-0008/).
- Uso de repositorio utilizando Github y buenas prácticas de programación y documentación.
- Puede usar **GitHub Copilot** o algún otro asistente de IA generativa para apoyarse en el desarrollo de su trabajo,
  pero debe tener en cuenta que debe poder **explicar, cambiar, mejorar y dar cuenta de TODO** lo que tenga su proyecto
  durante la sustentación.
- Aproveche la IA para que sea su compañero y lo potencialice. 🚀

## 📦 Entregables

- Entregas parciales:
    - Entrega 1: Semana 1 de asignación - Diagrama de clases, esqueleto de las clases en Python, pantalla de inicio,
      funcionalidad para crear un evento con todos sus campos. Pruebas unitarias relacionadas
    - Entrega 2: Semana 2 de asignación - Funcionalidad completa gestión de boletería, gestión de ingreso y generación
      de boletería, inicio de módulo de reportes. Pruebas unitarias relacionadas
    - Entrega final: Semana 3 de asignación - Funcionalidad completa. Pruebas unitarias relacionadas
- Código fuente del programa y pruebas unitarias. Use este GitHub Classroom para iniciar el proyecto.
- Despliegue en la Nube de la aplicación con Streamlit.
- [Manual técnico]: Con presentación general del proyecto, imágenes y textos que muestren el cumplimiento de los
  requerimientos, diagrama de clases UML en formato .MERMAID incluido en el README (uno por equipo). Todos los
  entregables deben ser subidos al repositorio de Git del equipo. Los documentos deben tener una calidad de redacción,
  ortografía y presentación esperadas a nivel universitario.

## 📦 Autoevaluación y Coevaluación

Debe elaborar un informe de autoevaluación en un documento individual en PDF [SUBIDO EN EL BRIGHSPACE] en el que
explique:

- Qué problemas tuvo al hacer su proyecto, qué aprendió, qué le gustó, que no le gustó.
- Cómo usó la IA, qué beneficios y dificultades le trajo el uso de la IA.
- Qué hizo cada uno de los miembros del equipo.
- Evaluación y coevaluación: califique de manera individual y para cada compañero cada uno de los siguientes elementos:
    - Colaboración y trabajo en equipo
    - Responsabilidad y compromiso
    - Contribución al Desarrollo del Trabajo
    - Uso de asistentes de IA en el desarrollo del proyecto
    - Nota consolidada (promedio de las anteriores)
    - Tenga en cuenta la siguiente rúbrica

        * Colaboración y Trabajo en Equipo
            - **Excelente (5):** El estudiante participa activamente y mejora la dinámica del equipo mediante una
              colaboración efectiva, mostrando respeto y apertura hacia las ideas de los demás.
            - **Bueno (4):** Participa regularmente y colabora bien, aunque en ocasiones puede ser pasivo. Respetuoso
              con los compañeros la mayoría del tiempo.
            - **Adecuado (3):** Participa sin tomar un rol activo, realiza lo mínimo necesario para no obstaculizar el
              equipo. Puede mejorar en respeto y colaboración.
            - **Insuficiente (2):** Participación mínima o negativa, a menudo no colabora o desestima a los demás,
              afectando negativamente la dinámica del equipo.

        * Responsabilidad y Compromiso
            - **Excelente (5):** Cumple con todas las tareas asignadas a tiempo, mostrando un alto nivel de compromiso y
              capacidad para tomar iniciativas adicionales.
            - **Bueno (4):** Generalmente cumple con las tareas en los plazos establecidos y muestra un buen nivel de
              compromiso.
            - **Adecuado (3):** Cumple con las tareas básicas, pero raramente toma iniciativas adicionales y a veces no
              cumple con los plazos.
            - **Insuficiente (2):** Falta frecuentemente a sus responsabilidades, mostrando poco compromiso y afectando
              el rendimiento del equipo.

        * Contribución al Desarrollo del Trabajo
            - **Excelente (5):** Aporta ideas y soluciones que son esenciales para el proyecto. Participa de manera
              activa en la planificación y ejecución de tareas clave.
            - **Bueno (4):** Realiza contribuciones que benefician al proyecto. Participa en la planificación y
              ejecución de tareas.
            - **Adecuado (3):** Realiza contribuciones que cumplen con los requisitos básicos del proyecto.
              Participación regular en la planificación y ejecución de tareas.
            - **Insuficiente (2):** Realiza pocas o ninguna contribución al desarrollo del trabajo. Participa poco o
              nada en la planificación y ejecución de tareas.

        * Uso de Asistentes de IA en el Desarrollo del Proyecto (Usarlo solo en la autoevaluación)
            - **Excelente (5):** Utiliza el asistente de codificación de manera estratégica, integrándolo efectivamente
              en el flujo de trabajo para mejorar significativamente la productividad y la calidad del código. Demuestra
              una comprensión profunda del código generado, realizando adaptaciones precisas que mejoran el proyecto.
              Muestra un juicio crítico excelente, seleccionando cuándo y cómo utilizar el asistente para optimizar
              resultados.
            - **Bueno (4):** Emplea el asistente de codificación regularmente, con una integración generalmente
              efectiva, contribuyendo positivamente al desarrollo del proyecto. Comprende bien el código generado y
              realiza ajustes necesarios para alinear el código con los objetivos del proyecto. Demuestra un buen juicio
              al evaluar la utilidad y precisión del código sugerido, aunque hay espacio para una evaluación más crítica
              en algunas situaciones.
            - **Adecuado (3):** Utiliza el asistente de codificación de forma inconsistente, integrándolo solo
              parcialmente en el proyecto. Entiende en términos generales el código generado pero no siempre realiza las
              modificaciones necesarias para que se ajuste completamente a las necesidades del proyecto. A veces depende
              demasiado de las sugerencias del asistente sin una evaluación crítica suficiente, afectando la
              optimización del desarrollo.
            - **Insuficiente (2):** Hace un uso esporádico e inefectivo del asistente de codificación, con poca
              evidencia de que su uso contribuya al proyecto. Incorpora código sin entenderlo adecuadamente, resultando
              en problemas de integración y funcionalidad. Falta un criterio crítico adecuado, aceptando sugerencias del
              asistente sin una evaluación pertinente de su aplicabilidad o corrección.

## 🚚 Información de entrega

1. Todos los entregables deben ser subidos al repositorio de Git del equipo. Los documentos deben tener una calidad de
   redacción, ortografía y presentación esperadas a nivel universitario.
2. **Fecha de Entrega Final**: jueves 23 de mayo del 2024, 11:59 PM vía GitHub.
3. **Sustentaciones:** Las sustentaciones serán entre el 27 y el 29 de mayo de 2024 de forma presencial. Para las
   sustentaciones es importante tener un computador disponible en el que pueda hacer modificaciones, eliminaciones,
   adiciones al proyecto entregado.
4. **Participación del Equipo:** Todos los miembros del equipo deben participar en todas las etapas del desarrollo (
   diseño, codificación, documentación y pruebas).
5. **Rol del Cliente y el Profesor**
    - **Gonzalo será su cliente**, así que puede solicitar información, reuniones o apoyo ya sea como cliente.
    - **La profesora Luisa actuará como profesora**, puede solicitarme espacios para aclarar dudas o asesorías en este
      link: [Agenda Luisa Rincón](https://outlook.office365.com/owa/calendar/AgendaLuisaRincn@javerianacaliedu.onmicrosoft.com/bookings/).
6. **Evaluación**
    - **Autoevaluación:** 5%
    - **Calificación del compañero:** 5%. En trabajos individuales, la autoevaluación tendrá un 10% de peso. Equipos de
      máximo dos personas.
    - **Calificación de los profesores:** compuesta por entregables, diseño, funcionalidad, estilo de codificación y
      mejores prácticas: 90%. La rúbrica de evaluación explica los elementos que se consideran para la calificación del
      proyecto.
7. **Propiedad Intelectual:**- **Valor entre 0 y 1** que multiplica la calificación total. Se demuestra durante la
   sustentación.
8. **Nota Final:** (criterios de evaluación%) * propiedad intelectual.

## Rúbrica

### Rúbrica de Evaluación

| Criterio                   | 5 puntos                                                                                                                                                                                                      | 4 puntos                                                                                                                                                                          | 3 puntos                                                                                                                                                                                                                                                     | 2 puntos                                                                                       | 1 punto                                                                                                                   | 0 puntos                                                                                                    |  
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|  
| Entregables 10%            | Los informes contienen toda la información solicitada, tienen alta calidad en cuanto a estilo y formato                                                                                                       | Se entregaron todos los informes. En términos de contenido están completos, pero podría mejorar en cuanto a estilo o formato                                                      | Se entregaron todos los informes. En términos de contenido están completos, pero podría mejorar en cuanto a estilo Y formato                                                                                                                                 | Faltan algunos de los informes, pero los entregados tienen buen estilo y formato               | Faltan algunos de los informes y los entregados necesitan mejoras de estilo y formato                                     | No se entregaron los informes                                                                               |  
| Diseño y codificación   60% | Las clases y métodos necesarios están identificados con claridad. Se utiliza herencia y polimorfismo de manera efectiva para optimizar la reutilización del código. La códificación cumple con los requisitos | Las clases y métodos principales están identificados. La herencia y el polimorfismo se utilizan adecuadamente, aunque con pequeñas áreas para mejorar en reutilización de código. Las relaciones entre clases son mayormente correctas, pero con uno o dos errores menores o omisiones que no afectan la funcionalidad principal. El diseño es coherente con la mayoría de los requisitos, pero puede mejorarse para alinear mejor con algunos.  La codificación corresponde a el 75% de los requisitos | El diseño responde a los requisitos.  Faltó detectar  algunas clases importantes. Faltó detectar algunos de los atributos y métodos importantes. Tiene algunas relaciones incorrectas.  La codificación cubre menos del  75  y más del 50% de los requisitos | Faltó detectar muchos de los  atributos y métodos  importantes. Tiene muchas relaciones incorrectas. La codificación corresponde al esqueleto del proyecto pero solo cubre el 25% de los requisitos | El diseño no satisface los requisitos. La codificación corresponde al esqueleto del proyecto o no se entregó codificación | No se entregó el diseño. La codificación corresponde al esqueleto del proyecto o no se entregó codificación |   
| Mejores prácticas       10% | El código sigue consistentemente principios de código limpio.                                                                                                                                                 | El código sigue en gran medida los principios de código limpio, incluyendo nombres adecuados, funciones de tamaño apropiado.                                                      | El código aplica principios de código limpio de forma inconsistente.                                                                                                                                                                                         | Principios de código limpio aplicados de manera limitada.                                      | Escasa aplicación de los principios de código limpio.                                                                     | No se entregó proyecto o el proyecto no cubre al menos el 25% de las funcionalidades.                       |  
| Entregas parciales      10% | Cumplió con las dos entregas parciales                                                                                                                                                                        |                                                                                                                                 | Cumplió con una entrega parcial                                                                                                                                                                                                                              |                                                 |                                                                          | No hizo ninguna entrega parcial                                                                             |
## Rúbrica de propiedad intelectual

| Criterio     | 1.0                                                                                                                                | 0.8                                                                                                                                                              | 0.6                                                                                                                                    | 0.4                                                                                                                                                                                                                                  | 0.2                                                                                                                            | 0.0                                                                                                                                        |
|--------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Sustentación | Es evidente que el estudiante entiende el código que desarrolló, lo explica con claridad y responde correctamente a las preguntas. | La sustentación es buena, pero se evidenció inseguridad del estudiante para explicar algunas partes del trabajo desarrollado o para responder algunas preguntas. | La sustentación es aceptable, se evidencia que el estudiante desarrolló el código pero le cuesta trabajo explicar aspectos del código. | La sustentación es regular, se evidenció inseguridad del estudiante para explicar gran parte del trabajo desarrollado o para responder muchas de las preguntas. Parece que el código no hubiera sido desarrollado por el estudiante. | El estudiante demuestra que entiende partes del código pero no tiene claro cómo se relacionan con la funcionalidad solicitada. | Se evidencia que el estudiante no entiende el código desarrollado, no es capaz de responder a las preguntas formuladas de manera correcta. |
