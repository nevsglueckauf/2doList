# Hinweise zur Installation

## Repo clonen
<code>user@host % </code> <kbd>git clone https://github.com/nevsglueckauf/2doList</kbd>
    
<code>user@host % </code> <kbd>cd 2doList</kbd>

--> eventuell VENV einrichten

## VENV einrichten/aktivieren
Hier exemplarisch an einem <kbd>Mac</kbd>:

<code>user@host 2doList % </code><kbd>python3 -m venv ~/.venv/todo</kbd><br>
<code>user@host 2doList % </code><kbd>source ~/.venv/todo/bin/activate</kbd>


Hier an einer <kbd>Wintendo</kbd>-Box:

<code>PS C:\Users\Foo\2doList</code><kbd>python -m venv C:\path_to\venv</kbd><br>
<code>PS C:\Users\Foo\2doList</code><kbd>C:\path_to\venv\Scripts\Activate.ps1</kbd>



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

 