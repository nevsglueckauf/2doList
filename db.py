import sqlite3
from typing import Any, Self,  Dict, List, Optional, Sequence, Tuple, Union
""" TODO (haha), FIXME:
                    - Sanitizing all arguments
"""

class Db:
    conn: sqlite3.Connection
    csr: sqlite3.Cursor
    
    def __init__(self):
        
        self.conn = sqlite3.connect('data/2do_list.db', autocommit=True)
        self.conn.row_factory = sqlite3.Row 

        self.crs  = self.conn.cursor()
        self.exec('PRAGMA foreign_keys = 1')

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
    
    
        
   
    
class Generic():
    """ 
        Collection of generic queries - to be used with several other entity classes
    """
    relation:str
    
    def __init__(self, db:Db, relation:str):
        self.db = db
        self.relation = relation
    
    def del_by_id(self, id:int) -> None:
        tpl = "DELETE FROM " + self.relation + " WHERE id = ?"
        self.db.res = self.db.crs.execute(tpl, [id])
        
    def get_where(self, where:str) -> list:
        tpl = "SELECT * FROM " + self.relation + f" WHERE {where}"
        #print(tpl)
        #exit()
        self.db.res = self.db.crs.execute(tpl)
        return self.db.res.fetchall()
        
    def change(self, dta:dict, id:id) -> None:
        tpl = "UPDATE " + self.relation + " SET "
        tmp = []
        for k, v in dta.items():
            print(k,v)
            tmp.append(k + " = '" + str(v) + "'") 
        tpl += ', '.join(tmp)
        tpl += f" WHERE id=?"
        #print(tpl)
        self.db.crs.execute(tpl, [id])
    
    
class Category():
    relation:str = 'category'
    gen:Generic
    
    def __init__(self, db):
        self.db = db
        self.gen = Generic(self.db, self.relation)
        
    def new(self, title:str) -> None:
        """ Inserting new item

        Args:
            title (str): category title
            
        FIXME: returning created id
        """
        tpl = "INSERT INTO " + self.relation +" (title) VALUES (?)"
        self.db.res = self.db.crs.execute(tpl, [title])
        
    def get_all(self) -> list:
        self.db.res = self.db.crs.execute("SELECT * FROM " + self.relation)
        return self.db.get_all()
    
    def get_id(self, title:str):
        for item in self.get_all():
            if item['title'] == title:
                return item['id']
    
    def get_dict(self):
        ret_dict = {}
        for item in self.get_all():
           ret_dict[item['id']] = item['title']
        return ret_dict
    
    
class Task():
    relation:str = 'task'
    gen:Generic
    def __init__(self, db):
        self.db = db
        self.gen = Generic(self.db, self.relation)
        
    
    def new(self, title:str, desc:str, cat_id:int, start='', end='') -> None:
        """ Inserting new item

        FIXME: returning created id

        Args:
            title (str): _description_
            desc (str): _description_
            cat_id (int): _description_
            start (str, optional): _description_. Defaults to ''.
            end (str, optional): _description_. Defaults to ''.
        """
        tpl = "INSERT INTO " + self.relation + "  (title, description, category_id, start_dt, end_dt) VALUES (?, ?, ?, ?, ?)"
        self.db.res = self.db.crs.execute(tpl, [title, desc, cat_id, start, end])
    
    def get_all(self) -> list:
        self.db.res = self.db.crs.execute("SELECT * FROM " + self.relation)
        return self.db.get_all()
    
    def get_mandatory(self, where:str = '') -> list:
        query = "SELECT title, description, category_id, status, id, start_dt, end_dt FROM " + self.relation
        
        if where != '':
            query += f' WHERE {where}'
        
        self.db.res = self.db.crs.execute(query)
        return self.db.get_all()
    
    
    
    
