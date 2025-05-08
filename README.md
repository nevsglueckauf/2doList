## Anwendung Sequenzdiagramm Anmeldung bis rollenbasierter GUI
```mermaid
sequenceDiagram
    autonumber
    create actor User
    Python->>User: src/main.py
    Note over User, Role_Window: Der Benutzer muss sich zunächst authentifizieren
    User->>App: Start # Start der Applikation
    App->>User: Bitte Login
    
    loop Login
        User->>Auth: check(username, password)
        Auth->>App: ok
        
        destroy Auth
        App-xAuth: end()
    
    end
   
    Role_Window->>User: Rollenbasierte GUI-Ansicht
    create actor G as Gast
    Role_Window->>G: Zugriff als Gast
    create actor A as Admin
    Role_Window->>A: Zugriff als Admin
    create actor S as Mitarbeiter
    Role_Window->>S: Zugriff als Mitarbeiter
    create actor M as Mitglied
    Role_Window->>M: Zugriff als Mitglied
    participant db as Persistenzschicht
    App->>db: (anlegen, auflisten, speichern, ändern)
    
    
```
## Persistenzschicht


```mermaid
architecture-beta
    service left_disk(disk)[file format JSON]
    service top_disk(disk)[file format CSV]
    service bottom_disk(disk)[file format XLSX]
    service top_gateway(server)[GUI]
    service bottom_gateway(server)[APP]
    junction junctionCenter
    junction junctionRight

    left_disk:R -- L:junctionCenter
    top_disk:B -- T:junctionCenter
    bottom_disk:T -- B:junctionCenter
    junctionCenter:R -- L:junctionRight
    top_gateway:B -- T:junctionRight
    bottom_gateway:T -- B:junctionRight


```
```mermaid
architecture-beta
    group api(cloud)[API]

    service db(database)[Database] in api
```
## "Mini-ER" - Beispiel Buchung

```mermaid
erDiagram
MEMBER ||--o{ Buchung: "beantragt"
    MEMBER {
        int member_id
    }
    Buchung ||--|{ Buchungs-Items:  "besteht aus"
    Buchung {
        int book_id
    }
    Buchungs-Items  {
        datettime start
        datettime end
        int member_id
        int course_id
        flag status
    }

```

## Klassendiagramm 

```mermaid
classDiagram

 
    
    class Main{
        # dispatch
    }

    class Login{
        + __init__(self, root, app)
        + login(self)
        + show_mask(self)
    }

    class App{
        + __init__(self, root)
        + set_role(self, role_name='guest')
        + run(self)
        + dispatch_role(self, role_name='guest')
        + admin(self)
        + guest(self)
        + staff(self)
        + member(self)
        + menu(self)
        + debug(self)
        + workbench(self)
   }

    class DataProvider{
        + __init__(self)
        + course_list(self)
        + trainer_list(self)
        + weekday_list(self)
        + time_slot_per_day(self, day)
        + time_slots_per_course(self, course)
        + save(self, topic='course')
        + stop(self, msg)
    }

    class Customers{
        + __init__(self)
        + edit(self, id, mode)
        + new(self, data)
        + delete(self, data)
        + save()
    }

   class CustomerCalendar{
        + __init__(self)
        + save(self)
        + book(self, ...)
        + edit(self, line)
        ...
   }

   class TableHelper{
    + __init__(self)
    + get_table(self, context, topic = 'customers')
    + read_data(sel, topic)
   }

   class MenuHelper{
    + __init__(self)
    + get_menu_by_role(self, role_name)
}

    class Gui{
    
    }

    Main --|> App
    Main  --|> Login

    App  --|> CustomerCalendar
    App  --|> Customers
    App  --|> DataProvider
    App --|> Gui

    App  --|> pandas
    App  --|> Tk
    Gui --|> MenuHelper
    Gui --|> TableHelper
    TableHelper --|> pandastable.Table


```

## Screenshots
![alt text](admin_customer_small.png "Admin Fenster - Kundentabelle")


## Dateistruktur

<pre><code>
.
├── customer_calendar
│   ├── README.md
│   ├── README_TOO.md
│   ├── data
│   │   ├── CalendarLog.json
│   │   ├── Kursplan.xlsx
│   │   ├── calendar_log.json
│   │   ├── course_plan.xlsx
│   │   ├── customers_database.json
│   │   ├── customers_new.json
│   │   ├── kurs.csv
│   │   ├── passwd.csv
│   │   ├── time_slot.csv
│   │   ├── trainer.csv
│   │   └── wochentag.csv
│   ├── doq
│   │   ├── admin_customer_small.png
│   │   ├── cc_doq.ipynb
│   │   └── tech_doc.md
│   ├── main.py
│   ├── requirements.txt
│   ├── src
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── calendar_log.py
│   │   │   ├── customer_calendar.py
│   │   │   ├── customers.py
│   │   │   ├── data_provider.py
│   │   │   └── table_helper.py
│   │   ├── gui
│   │   │   ├── __init__.py
│   │   │   ├── app.py
│   │   │   ├── app_new.py
│   │   │   ├── config.py
│   │   │   ├── foo.php
│   │   │   ├── gf_gui.ipynb
│   │   │   ├── login.py
│   │   │   ├── main.py
│   │   │   ├── menu_helper.py
│   │   │   └── mitarbeit.py
│   │   ├── main.py
│   │   ├── test_dp.py
│   │   └── test_import.py
│   ├── tests
│   └── file.txt
</code></pre>

## Metriken

<pre><code>
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
JSON                             5              0              0           2020
Python                          23            312            100            819
Jupyter Notebook                 8              0            914            606
Markdown                         3             43              0            154
CSV                              5              0              0             44
PHP                              1              2              0              6
-------------------------------------------------------------------------------
SUM:                            45            357           1014           3649
-------------------------------------------------------------------------------
</code></pre>