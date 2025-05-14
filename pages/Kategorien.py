import streamlit as st
import pandas as pd
from db import Db
from db import Task
from controller import Controller

db = Db()

ctrl = Controller(db=db, st=st)
ctrl.meta(title='Kategorien', icon='📜')

ctrl.cat_list()
