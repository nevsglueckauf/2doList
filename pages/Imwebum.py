import streamlit as st
import pandas as pd
from db import Db
from db import Category
from controller import Controller
db = Db()
category = Category(db)
ctrl = Controller(db=db, st=st)
ctrl.meta(title = 'Imwebum', icon='👁️')

st.markdown('### Projektarbeit bei Datacraft')
st.markdown("""- Sandra, Sascha, Sven""")