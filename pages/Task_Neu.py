
import streamlit as st
from db import Db
from db import Category
from db import Task
from controller import Controller


db = Db()
ctrl = Controller(db=db, st=st)
ctrl.meta(title = 'Task anlegen', icon='📝')

category = Category(db)
cats = category.get_all()
cat_list=[]
for i in cats:
  cat_list.append(i['title'])


with st.form("my_form"):
   n_title = st.text_input('Titel:', '')
   n_description = st.text_input('Beschreibung:', '')
   n_start = st.date_input('Startdatum', format="DD.MM.YYYY",)
   n_end = st.date_input('Enddatum', format="DD.MM.YYYY")
   n_prio = st.slider("Priorität", 1,5)
   cat = st.selectbox("Kategorie", cat_list)
   submitted = st.form_submit_button('Anlegen')

  

if submitted:
  cat_id= category.get_id(cat)
  task = Task(db)
  task.new(title=n_title, desc=n_description, cat_id=cat_id, start=n_start, end=n_end)
  ctrl.save_success()
