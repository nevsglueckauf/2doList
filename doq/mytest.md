## Anwendung Sequenzdiagramm Anmeldung bis rollenbasierter GUI

<dl>
<dt>UserAgent</dt> 
<dd>HTTP-Client, z.B: Browser</dd>
</dl>
```mermaid
sequenceDiagram
    UserAgent->>Webserver: https://host.exaample.com/Kategorien
    Webserver-->>UserAgent:  Anzeige der Daten () 
    UserAgent->>Webserver: Eingabe der Änderungen -> POST
    Webserver-->>UserAgent:  diff(DF, DF_edit) --> generiere SQL Stmts (UPDATE ...) -> execute  
```