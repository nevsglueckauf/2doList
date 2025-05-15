# SQL 

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
    title SWOT Analyse
    quadrant-1 DDL 
    quadrant-2 DML
    quadrant-3 DCL
    quadrant-4 TCL
    
    "INSERT": [0.25, 0.9] color: #00ff33, radius: 0
    UPDATE: [0.25, 0.85] color:  #00ff33, radius: 1
    DELETE: [0.25, 0.65] color:  #00ff33, radius: 1

    Limitierte Liquiditat: [0.75, 0.9] color:  #ff0000, radius: 1
    Marginale Bekanntkeit Prod. : [0.75, 0.85] color:  #ff0000, radius: 1
    Kaum Vertriebsinfrastruktur: [0.75, 0.8] color:  #ff0000, radius: 1
    Marginale Bekanntkeit Unt. : [0.75, 0.75] color:  #ff0000, radius: 1
    Geringe Kundenbasis : [0.75, 0.7] color:  #ff0000, radius: 1

    Wachstumspotential IoT: [0.25, 0.4] color: #ffffff,  radius: 1
    Partnerschaften : [0.25, 0.35] color: #ffffff,  radius: 1
    Zeitpunkt Markteintritt: [0.25, 0.3] color: #ffffff,  radius: 1
    Patente  LPWA, BT: [0.25, 0.25] color: #ffffff,  radius: 1
    
    
    Entwicklung ext. Effekte: [0.75, 0.4] color: #ffff00, radius: 1
    Bedingungen Finanzierung : [0.75, 0.35] color: #ffff00,  radius: 1
    Globaler Wettbewerb: [0.75, 0.3] color: #ffff00,  radius: 1
    "Preisentwicklung: - Energie": [0.75, 0.25] color: #ffff00,  radius: 1
    "- Seltene Erden": [0.75, 0.2] color: #ffff00, radius: 1
    "- HLT": [0.75, 0.15] color: #ffff00, radius: 1

```


<br><br><br><br><br><br><br><br><hr>
<p><small>[^radio] - LPWA: low power wide area; BT: Bluetooth
[^hlt] - HLT_ Halbleitertechnik</small></p>