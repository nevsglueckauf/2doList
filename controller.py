import streamlit # type: ignore
import pandas as pd
from db import Db
from db import Category
from db import Task
from db import Generic


class Controller:
    def __init__(self, db:Db, st:streamlit):
        self.db = Db()
        self.st = st
        self.task = Task(db=self.db)
        self.cat = Category(db=self.db)
 
        
    def meta(self, title:str='', icon:str=''):
        self.st.set_page_config(page_title = title, page_icon=icon)
        self.st.markdown('# ' + title)
        
        
    def cat_list(self):
         self.gen = Generic(db=self.db, relation='Category')
         cats = self.cat.get_all()
         df = pd.DataFrame(list(cats), columns=['id', 'Titel'])
         edited = self.st.data_editor(df,  hide_index=True, use_container_width=False)
        
         
         if self.st.button("Speichern"):
            self.save_success()
            # Hint zum Merge:   how='outer' -> UNION der Keys; indicator=True -> ['_merge'] ('left_only', 'right_only', 'both')
            merged_df = pd.merge(df, edited, how='outer', indicator=True)
            self.cat_parse_edited(merged_df[merged_df['_merge'] == 'right_only'])

    def save_success(self):
            msg = "Daten gespeichert 💾"
            self.st.write(msg)
            self.st.sidebar.success(msg)          
              
    def task_list(self):
        
        li = self.task.get_mandatory()
        df = pd.DataFrame(list(li), columns=['Titel', 'Beschreibung', 'KatId', 'Status', 'id', 'Start', 'Ende'])
        edited_df = self.st.data_editor(df)
        
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
        for row in df.itertuples():
            tpl23 = f"UPDATE category SET title='{row.Titel}' WHERE id={row.id}"
            self.db.exec(tpl23)
            #self.db.exec(tpl, [row.id, row.Titel])
            print(tpl23)
            
            
    def cat_parse_edited_pp(self, df:pd.DataFrame):
        for row in df.itertuples():
            q = "UPDATE category SET title=? WHERE id=?"
            self.db.exec(q, [row.id, row.Titel])
            return self
            
            
    def task_parse_edited(self, df:pd.DataFrame):
        self.save_success()
        
        # Titel Beschreibung  KatId   Status  id       Start        Ende    Kategorie  Action      _merge
        # 4   Foo   Bar techn.      4  PENDING  10  2025-05-12  2025-05-29  Plattenkauf   False  right_only

        
        
        # print('Writing to DB')
        for row in df.itertuples():
            #tpl = 'UPDATE task SET title=? WHERE id=?'
            tpl23 = f"UPDATE task SET title='{row.Titel}'," 
            tpl23 += f" description='{row.Beschreibung}',"
            tpl23 += f" status='{row.Status}',"
            tpl23 += f" start_dt='{row.Start}',"
            tpl23 += f" end_dt='{row.Ende}',"
            tpl23 += f" category_id='{row.KatId}'"
            tpl23 += f" WHERE id={row.id}"
            
            print(tpl23)
            #exit(23)
            
            self.db.exec(tpl23)
            #self.db.exec(tpl, [row.id, row.Titel])
    