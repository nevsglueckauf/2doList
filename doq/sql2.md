# SQL 


-    Data Query Language (DQL) Abfrage von Daten
-    Data Manipulation Language (DML) Bearbeitung von Daten
-    Data Definition Language (DDL) Definition / Strukturierung von Daten
-    Data Control Language (DCL)  Verwaltung / Steuerung der Datenbank
-    außerdem: (weiter unten)
    * Transaction Control Language (TCL) Transaktionssteuerung




``` mermaid
%%{init: "quadrantChart": {"chartWidth": 1650, "chartHeight": 700}, 
         "themeVariables": {"quadrant1TextFill": "#ff0000",
                            "quadrant3TextFill": "#00ff00",
                            "quadrant3TextFill": "#ff0000",
                            "quadrant4TextFill": "#ff00ff",
                            "fillType0": "#ff00f0",
                            "fillType1": "#0000f0",
         } 
         
         
         }%%
quadrantChart
    title Teilmengen von SQL
    quadrant-1 DDL 
    quadrant-2 DML
    quadrant-3 DCL
    quadrant-4 DQL
    
    INSERT: [0.25, 0.9] color: #00ff33, radius: 0
    UPDATE: [0.25, 0.85] color:  #00ff33, radius: 0
    DELETE: [0.25, 0.80] color:  #00ff33, radius: 0

    CREATE: [0.75, 0.9] color:  #ff0000, radius: 0
    ALTER : [0.75, 0.85] color:  #ff0000, radius: 0
    DROP: [0.75, 0.8] color:  #ff0000, radius: 0
    RENAME : [0.75, 0.75] color:  #ff0000, radius: 0
    TRUNCATE : [0.75, 0.7] color:  #ff0000, radius: 0
    COMMENT : [0.75, 0.65] color:  #ff0000, radius: 0


    GRANT : [0.25, 0.4] color: #ffffff,  radius: 0
    REVOKE: [0.25, 0.35] color: #ffffff,  radius: 0

    SELECT: [0.75, 0.4] color: #ffff00, radius: 0
    
    

```
## Transaktionen (manchmal <em><abbr title="Transaction Control Language">TCL</em> - </abbr> genannt)
    - COMMIT
    - ROLLBACK
    - SAVEPOINT
    - SET TRANSACTION

 