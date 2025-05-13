# 

## Repo clonen
<code>user@host % </code> <kbd>git clone https://github.com/nevsglueckauf/2doList</kbd>
    
<code>user@host % </code> <kbd>cd 2doList</kbd>

## VENV
Hier exemplarisch an einem <var>Mac</var>:

<code>user@host 2doList % </code><kbd>source ~/.venv/todo/bin/activate</kbd>
<br>
<code>user@host (todo) 2doList % </code><kbd>sqlite3 2do_list.db < curr_schema.sql</kbd>

--> eventuell VENV einrichten

## Dependencies auflösen
<code>2doList % </code> <kbd>pip install -r req.txt</kbd>
<pre>
<code>2doList % Collecting  (from -r req.txt) ...</code>
</pre>

## Start der App

<code> % </code> <kbd>python -m streamlit run Todo_List_App.py </kbd>


Hier exemplarisch in einer <var>.venv</var>

<code>(todo) 2doList % </code> <kbd>python -m streamlit run Todo_List_App.py& 2>&1 > /dev/null</kbd>

## SQLite spez.

### SQL Dump erstellen

<code>user@host %</code><kbd>sqlite3 2do_list.db .dump > curr_schema.sql</kbd>

### SQL Dump importieren

<code>user@host %</code><kbd>sqlite3 2do_list.db < curr_schema.sql</kbd>