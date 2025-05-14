import streamlit as st
import pandas as pd
from db import Db
from db import Task
from db import Category
from controller import Controller
title= "Tasks 📜"
st.set_page_config(page_title=title, page_icon="📜")
st.markdown('# ' + title)
db = Db()
task = Task(db)
cat = Category(db)
ctrl = Controller(db=db, st=st)
cat_nm = cat.get_dict()

li = task.get_mandatory()



# ['title', 'description', 'category_id', 'status', 'id']

 
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
    # mask = df.apply(lambda x: x)
    #df = df[df['status'] == 'DONE']
    if status_fil != 'Alle':
        df = df[df['Status'] == status_fil]


    
edited_df = st.data_editor(df, hide_index=True, use_container_width=True, column_order=('Titel', 'Beschreibung', 'Kategorie', 'Status', 'Start', 'Ende', 'Action'))

if st.button("Speichern"):
            merged_df = pd.merge(df, edited_df, how='outer', indicator=True)
            ctrl.task_parse_edited(merged_df[merged_df['_merge'] == 'right_only'])

#st.html('<button onclick="location.href=\'/Task_Neu\'"> Neuer Eintrag </button>')
# task = Task(db=db)
# li = task.get_mandatory()
# df = pd.DataFrame(list(li), columns=li[0].keys())
# #print(li);
# st.dataframe(df, use_container_width=False)