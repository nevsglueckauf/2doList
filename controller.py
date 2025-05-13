import pandas as pd
from db import Db
from db import Category
from db import Task
from db import Generic


class Controller:
    def __init__(self, db:Db, st):
        self.db = Db()
        self.st = st
        self.task = Task(db=self.db)
        self.cat = Category(db=self.db)
        #
        
        
    def cat_list(self):
         self.gen = Generic(db=self.db, relation='Category')
         cats = self.gen.get_where('id <> 666')
         df = pd.DataFrame(list(cats))
         #print(li);
         self.st.dataframe(df, use_container_width=False)
            
    def task_list(self):
        
        li = self.task.get_mandatory()
        df = pd.DataFrame(list(li), columns=li[0].keys())
        edited_df = self.st.data_editor(df)

        #df['work'] = '<a href="/work.py?id=' + str(df['id']) + '">bearb.</a>'
        #print(li);
        #self.st.dataframe(df, use_container_width=False)
        
    def task_new(self):
        cats = self.cat.get_all()
        cat_list=[]
        for i in cats:
            cat_list.append(i['title'])   
        self.cat_lst = cat_list
        
        
    