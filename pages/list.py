import streamlit as st
import pandas as pd
from db import Db
from db import Task
st.set_page_config(page_title="Todo list", page_icon="📈")

st.sidebar.success("Sidebar")
st.sidebar.header("Aktuelle Liste")
st.markdown(
    """
  # TODO Liste
  
  ## Aktuelle Items:
"""
)
db = Db()
task = Task(db=db)
li = task.get_mandatory()
df = pd.DataFrame(list(li), columns=li[0].keys())
#print(li);
st.dataframe(df, use_container_width=False)