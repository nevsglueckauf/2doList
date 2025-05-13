#!/bin/sh
source ~/.venv/todo/bin/activate
python -m streamlit run Todo_List_App.py& 2>&1 > /dev/null