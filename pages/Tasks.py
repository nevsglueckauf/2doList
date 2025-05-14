import streamlit as st
import pandas as pd
from db import Db
from db import Task
from db import Category
from controller import Controller
db = Db()
task = Task(db)
ctrl = Controller(db=db, st=st)
ctrl.meta(title='Tasks' ,icon='📜')
cat = Category(db)
cat_nm = cat.get_dict()
li = task.get_mandatory()



de_keys = ['Titel', 'Beschreibung', 'KatId', 'Status', 'id', 'Start', 'Ende']
df = pd.DataFrame(list(li), columns=de_keys)
df['Kategorie'] = df['KatId'].apply(lambda x: cat_nm[x]) 
df['Action'] = df['Status'].apply(lambda x: True if x =='DONE' else (False)) 
query = st.text_input("Datenfilter")
status_fil = ctrl.get_status()


if query:
    mask = df.applymap(lambda x: query in str(x).lower()).any(axis=1)
    df = df[mask]

if status_fil:
    
    if status_fil != 'Alle':
        df = df[df['Status'] == status_fil]


    
edited_df = st.data_editor(df, hide_index=True, use_container_width=True, column_order=('Action', 'Titel', 'Beschreibung', 'Kategorie', 'Status', 'Start', 'Ende'))
li = db.exec("SELECT count(*) as amount FROM task where status <> 'DONE' ").get()

st.markdown('`' + str(li['amount']) + ' angefangene Tasks`')
if st.button("Speichern"):
            merged_df = pd.merge(df, edited_df, how='outer', indicator=True)
            ctrl.task_parse_edited(merged_df[merged_df['_merge'] == 'right_only'])

st.html('<a href="Task_Neu">Neuer Eintrag</a>')