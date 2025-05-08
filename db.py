import sqlite3
from typing import Any, Self

class Db:
    def __init__(self):
        
        self.conn = sqlite3.connect('data/2do.db')
        self.conn.row_factory = sqlite3.Row 

        self.crs  = self.conn.cursor()

    def exec (self, query:str) -> Self:
        self.res = self.crs.execute(query)
        return self
    
    def get(self) -> sqlite3.Row:
        return self.res.fetchone()
    
         
    def get_all(self) -> list:
        return self.res.fetchall()
        
    def get_by_id(self, rel:str, id:int) -> sqlite3.Row:
        return self.exec(f'SELECT * FROM {rel} WHERE id={id}').get()
    
    def __del__(self):
        self.conn.close()
    
    
    
    
    
    
    
    
