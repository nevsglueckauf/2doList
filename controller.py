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
         df = pd.DataFrame(list(cats), columns=['id', 'Titel'])
         #print(li);
         edited = self.st.data_editor(df,  hide_index=True, use_container_width=False)
        
         
         if self.st.button("Speichern"):
            msg = "Datensatz gespeichert"
            self.st.write(msg)
            self.st.sidebar.success(msg)
            merged_df = pd.merge(df, edited, how='outer', indicator=True)
            self.cat_parse_edited(merged_df[merged_df['_merge'] == 'right_only'])
            
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
        
    def get_status(self):
        li = ['Alle', 'PENDING', 'DONE', 'IN_PROGRESS', 'CANCELLED', 'PAUSED']
        return self.st.selectbox("Statusfilter", li)
        
        
    def cat_parse_edited(self, df:pd.DataFrame):
        
        #print(df)
        
        #exit(66)
        print('Writing to DB')
        for row in df.itertuples():
            #tpl = 'UPDATE category SET title=? WHERE id=?'
            tpl23 = f"UPDATE category SET title='{row.Titel}' WHERE id={row.id}"
            self.db.exec(tpl23)
            #self.db.exec(tpl, [row.id, row.Titel])
            print(tpl23)
            