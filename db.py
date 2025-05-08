import sqlite3
from typing import Any, Self

class Db:
    def __init__(self):
        
        self.conn = sqlite3.connect('data/2do.db', autocommit=True)
        self.conn.row_factory = sqlite3.Row 

        self.crs  = self.conn.cursor()

    def exec(self, query:str, param:list=[]) -> Self:
        self.res = self.crs.execute(query, param)
        return self
    
    def get(self) -> sqlite3.Row:
        return self.res.fetchone()
    
         
    def get_all(self) -> list:
        return self.res.fetchall()
        
    def get_by_id(self, rel:str, id:int) -> sqlite3.Row:
        self.res = self.crs.execute("SELECT * FROM " + rel + " WHERE id = ?", [id])
        return self.res.fetchone()
    
    def __del__(self):
        self.conn.close()
        
    def set_res(self, res):
        self.res
    
    
class Category():
    relation = 'category'
    
    def __init__(self, db):
        self.db = db
    
    def new(self, title:str):
        tpl = "INSERT INTO " + self.relation +" (title) VALUES (?)"
        self.db.res = self.db.crs.execute(tpl, [title])
        
    def get_all(self):
        self.db.res = self.db.crs.execute("SELECT * FROM " + self.relation)
        return self.db.get_all()
    
class Task():
    relation = 'task'
    
    def __init__(self, db):
        self.db = db
    
    
    def new(self, title:str, desc:str, cat_id:int, start='', end=''):
        tpl = "INSERT INTO " + self.relation + "  (title, description, category_id, start_dt, end_dt) VALUES (?, ?, ?, ?, ?)"
        self.db.res = self.db.crs.execute(tpl, [title, desc, cat_id, start, end])
    
    def get_all(self):
        self.db.res = self.db.crs.execute("SELECT * FROM " + self.relation)
        return self.db.get_all()
    
    
    
    
