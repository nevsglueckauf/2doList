# Design & Architecture Dossier

## Klassen

```mermaid classDiagram

class Db{
        def exec(self, query:str, param:list=[]) -> Self:
        def get(self) -> sqlite3.Row:
        def get_all(self) -> list:
        def get_by_id(self, rel:str, id:int) -> sqlite3.Row:
        def __del__(self):
        def set_res(self, res)
    }


```



## Dat
![Entity-Relationship Model](er.png "Entity-Relationship Model")