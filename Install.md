# 

## Repo clonen
<code>UserName % </code> <kbd>git clone https://github.com/nevsglueckauf/2doList</kbd>
<code>UserName % </code> <kbd>cd 2doList</kbd>

## VENV
Hier exemplarisch an einem <var>Mac</var>:

<code>sven@Thanos 2doList % </code><kbd>source ~/.venv/todo/bin/activate</kbd>
<br>
<code>sven@Thanos (todo) 2doList % </code><kbd>sqlite3 2do_list.db < curr_schema.sql</kbd>

--> eventuell VENV einrichten

## Dependencies auflösen
<code>2doList % </code> <kbd>pip install -r req.txt</kbd>
<pre>
<code>2doList % Collecting  (from -r req.txt) ...</code>
</pre>

## Start der App

Hier exemplarisch in einer <var>.venv</var>

<code>(todo) 2doList % </code> <kbd>python -m streamlit run streamlit_app.py& 2>&1 > /dev/null</kbd>

### SQLite spez.

<code>sven@Thanos %</code><kbd>sqlite3 2do_list.db .dump > curr_schema.sql</kbd>
<br>
<code>sven@Thanos %</code><kbd>sqlite3 2do_list.db < curr_schema.sql</kbd>