import sqlite3

class Db:
    def __init__(self):
        
        self.conn = sqlite3.connect('data/2do.db')
        self.conn.row_factory = sqlite3.Row 

        self.crs  = self.conn.cursor()

    def exec (self, query:str):
        self.res = self.crs.execute(query)
        return self
    
    def get(self):
        return self.res.fetchone()
    
         
    def get_all(self):
        return self.res.fetchall()
        
    def get_by_id(self, rel:str, id:int):
        return self.exec(f'SELECT * FROM {rel} WHERE id={id}').get()
    
    def __del__(self):
        self.conn.close()
    
    
    
    
    
    
    
    
