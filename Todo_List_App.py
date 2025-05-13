import streamlit as st
import pandas as pd
from db import Db
from db import Task
welcome = "Todoliste Startseite"
st.set_page_config(page_title=welcome,   page_icon="👋")
st.markdown('# ' + welcome)
db = Db()
task = Task(db=db)
li = task.get_mandatory(where=" status <> 'DONE' ORDER BY end_dt ")
df = pd.DataFrame(list(li), columns=li[0].keys())
#print(li);
#st.dataframe(df, use_container_width=False)
st.markdown('178 angefangene Tasks')

