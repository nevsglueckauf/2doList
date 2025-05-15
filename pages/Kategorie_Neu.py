import streamlit as st
import pandas as pd
from db import Db
from db import Category
from controller import Controller

db = Db()
category = Category(db)
ctrl = Controller(db=db, st=st)
ctrl.meta(title = 'Kategorie anlegen', icon='📝')


cats = category.get_all()
cat_list=[]
for i in cats:
  cat_list.append(i['title'])

with st.form("my_cat_form"):
   n_title = st.text_input('Titel:', '')
   submitted = st.form_submit_button('Anlegen')

if submitted:
  category.new(title=n_title)
  ctrl.save_success()
  st.write(n_title + ' wurde angelegt')
  

