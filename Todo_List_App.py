import streamlit as st
import pandas as pd
from db import Db
from db import Task
from db import Category
from controller import Controller

db = Db()
task = Task(db=db)
db = Db()
ctrl = Controller(db=db, st=st)
ctrl.meta(title='Todoliste Startseite', icon='👋')
ctrl.task_list()
li = db.exec("SELECT count(*) as amount FROM task where status <> 'DONE' ").get()
st.markdown('`' + str(li['amount']) + ' angefangene Tasks`')

    