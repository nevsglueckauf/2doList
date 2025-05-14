import streamlit as st
import pandas as pd
from db import Db
from db import Category

title = "Kategorie anlegen 📝"
db = Db()
category = Category(db)
cats = category.get_all()
cat_list=[]
for i in cats:
  cat_list.append(i['title'])

st.set_page_config(page_title = title)

 

with st.form("my_cat_form"):
   st.write(title)
   n_title = st.text_input('Titel:', '')
   submitted = st.form_submit_button('Anlegen')

# This is outside the form
if submitted:
  
  category.new(title=n_title)
  st.write(n_title + ' wurde angelegt')
  

