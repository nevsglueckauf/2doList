import streamlit as st
import pandas as pd
from db import Db
from db import Task
from controller import Controller

st.set_page_config(page_title="Todo list", page_icon="📈")
st.sidebar.success("Sidebar")
st.sidebar.header("Aktuelle Liste")

# st.markdown(
#     """
#   # TODO Liste
  
#   ## Aktuelle Items:
# """
# )
db = Db()
ctrl = Controller(db=db, st=st)
ctrl.task_list()
st.html('<a href="/task" class="button">Neuer Eintrag</a>')
# task = Task(db=db)
# li = task.get_mandatory()
# df = pd.DataFrame(list(li), columns=li[0].keys())
# #print(li);
# st.dataframe(df, use_container_width=False)