import streamlit as st
from db import Db
from db import Category
from db import Task
title = "Task anlegen 📝"
db = Db()




category = Category(db)
cats = category.get_all()
cat_list=[]
for i in cats:
  cat_list.append(i['title'])

st.set_page_config(page_title = title)
 

with st.form("my_form"):
   st.write(title)
   n_title = st.text_input('Titel:', '')
   n_description = st.text_input('Beschreibung:', '')
   n_start = st.date_input('Startdatum', format="DD.MM.YYYY",)
   n_end = st.date_input('Enddatum', format="DD.MM.YYYY")
   n_prio = st.slider("Priorität", 1,5)
   cat = st.selectbox("Kategorie", cat_list)
   submitted = st.form_submit_button('Anlegen')

  

# This is outside the form
if submitted:
  cat_id= category.get_id(cat)
  task = Task(db)
  task.new(title=n_title, desc=n_description, cat_id=cat_id, start=n_start, end=n_end)
  st.write(n_title + ' wurde angelegt')
  st.write(cat + ' wurde ausgewählt' + str(cat_id))
