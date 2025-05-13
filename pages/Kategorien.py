import streamlit as st
import pandas as pd
from db import Db
from db import Task
from controller import Controller

st.set_page_config(page_title="Todo list", page_icon="📈")
st.markdown('### Kategorien')
db = Db()
ctrl = Controller(db=db, st=st)
ctrl.cat_list()
