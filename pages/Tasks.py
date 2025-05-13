import streamlit as st
import pandas as pd
from db import Db
from db import Task
from controller import Controller

st.set_page_config(page_title="Todo list", page_icon="📈")
#st.sidebar.success("Sidebar")
#st.sidebar.header("Aktuelle Liste")

# st.markdown(
#     """
#   # TODO Liste
  
#   ## Aktuelle Items:
# """
# )
db = Db()
task = Task(db)
ctrl = Controller(db=db, st=st)

li = task.get_mandatory()
# ['title', 'description', 'category_id', 'status', 'id']

st.markdown('# Taskliste')
de_keys = ['Titel', 'Beschreibung', 'Kategorie', 'Status', 'id']
df = pd.DataFrame(list(li), columns=de_keys)

query = st.text_input("Datenfilter")
status_fil = ctrl.get_status()


if query:
    mask = df.applymap(lambda x: query in str(x).lower()).any(axis=1)
    df = df[mask]

if status_fil:
    # mask = df.apply(lambda x: x)
    #df = df[df['status'] == 'DONE']
    if status_fil != '--':
        df = df[df['Status'] == status_fil]
    
    
edited_df = st.data_editor(df, hide_index=True, use_container_width=True)



st.html('<a href="/task" class="button">Neuer Eintrag</a>')
# task = Task(db=db)
# li = task.get_mandatory()
# df = pd.DataFrame(list(li), columns=li[0].keys())
# #print(li);
# st.dataframe(df, use_container_width=False)