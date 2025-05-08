import sqlite3

class Db:
    def __init__(self):
        
        self.conn = sqlite3.connect('data/2do.db')
        self.conn.row_factory = sqlite3.Row 

        self.crs  = self.conn.cursor()

    def exec (self, query:str):
        self.res = self.crs.execute(query)
        return self
         
    def get_all(self):
        return self.res.fetchall()
        
    
    
    
    
    
    
    
    
    
    
