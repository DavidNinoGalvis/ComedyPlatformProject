[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6rk6xNey)
# Proyecto Final Programación Orientada a Objetos
# Proyecto Website Comediantes

![Logo Proyecto Principal](docs/logo_main.webp)

##### Integrantes:
- Juan David Niño Galvis
- Juan David Tabares

##### Creación del Logo:

Para la creación del logo para nuestra plataforma de comedia utilizamos una inteligencia artificial llamada "Leonardo AI" la cual nos da distintas posiblidades a elegir, y tomar la que más nos gusté.

##### Librerias Utilizadas

- streamlit-Lottie:
- Font Awesome and Boostrap icons

Esta la utilizamos para mejorar la estetica del proyecto, esta funciona como un banco de diseños y animaciones para llamar facilemente mientras desarrollamos

## Objetivos Planteados

- New: Agregar Distintas excepciones
- Vista de Usuario
- Dashboard para Administrador
- Vista de Login para identificar el usuario o Administrador
- Vista de Artistas
- Vista de Publicidad
- Buscar mejores maneras de almacenar datos, leer y escribir en formatos seguros.
- Vista de Reportes, uso de pandas para crear graficas y estadisticas para imprimir en esta sección.

Nota: Aún no sabemos como podemos representar los reportes, probablemente sea con una clase
# Vistas del proyecto

- Login User
- Dashboard
- Creacion Evento (Admin)
- Compra de Evento (Usuario)

```mermaid
classDiagram
    class Event {
        * artists : list<string>
        * eventName : string
        * eventDate : string
        * openingTime: string
        * duration : string
        * venue : string
        * address : string
        * city : string
        * state : string
        * ticketOffice : TicketOffice
        + Event()
        + changeState() : void
        + updateDetails() : void
    }

    class BarEvent  {
        - eventType : string
        + BarEvent()
    }

    class LoginDB{
        - usersDB : dict[name, User]
        + findUser()
        + deleteUser()
    }

    class TheaterEvent {
        - eventType : string
        - venueCost : int
        + TheaterEvent()
    }

    class CharityEvent {
        - eventType : string
        - sponsors : dict[string, int]
        + CharityEvent()
    }

    class TicketOffice {
        - soldTickets : int
        - courtesyTickets : int
        - tickets : dict[int, Ticket]
        * TicketOffice()
        + createCategory()
        + updateCategory()
        + setCourtesies()
        * findTicket()
    }

    class Ticket {
        - price : int
        - buyerID : int
        - category : string
        - phase : string
        - saleCode : int
        - paymentMethod : string
        - refundMethod : string
        - isActive : bool
        + Ticket()
    }

    class DashboardManager {
        +create()
        +read()
        +update()
    }
    
    class Performer {
        - name
        - eventList : list[string]
        + Performer()
        + registerEvent()
        + listEvents()
    }
    class Account {
        - username : string
        - password : string
        - email : string
        - address : string
        + Account()
        + getUsername()
    }

    class Administrator {
        - managedEvents : list[string]
        dashboardAdmin : DashboardManager
        + Administrator()
        + scheduleEvent()
        + generateReport()
    }

    class Artist{
        - Nombre : string
        - Dni: int
        - City : string
        - Genero : string
    }
    class Customer {
        - tickets : list[int]
        + Customer()
        + purchaseTicket()
        + downloadTicketPDF()
    }

    class UserInterface {
        + displayRegistrationPage()
        + displayAdminPage()
        + displayEventCreationPage()
        + displayEventManagementPage()
        + displayUserProfilePage()
        + displayPurchasePage()
        + displayLoginPage()
    }

    class Application {
        +start()
    }

    class GUIController {
        - activePage : string
        - managementController : ManagementController
        + UIController()
    }

    class ManagementController {
        - events : dict[string, Event]
        - accounts : dict[string, Account]
        - performers : dict[string , Performer]
        - reports : Report
        + ManagementController()
        + createEvent()
        + deleteEvent()
        + ticketSale()
        + generateReport()
        + editEvent()
        + checkInEvent()
    }


    GUIController <.. Application : launches
    Event <-- BarEvent : is-a
    Event <-- TheaterEvent : is-a
    Event <-- CharityEvent : is-a
    ManagementController <-- UIController : has
    UserInterface <..> UIController : uses
    ManagementController o-- Event : has
    ManagementController o-- Account : has
    ManagementController o-- LoginDB : has
    ManagementController o-- Performer : has
    ManagementController --> Report : has
    Event --> TicketOffice : has
    TicketOffice o-- Ticket : has
    Account <-- Administrator : is-a
    Account <-- Customer : is-a
    Administrator ..> DashboardManager : uses
```