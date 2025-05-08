from db import Db
from db import Category
from db import Task

db = Db()
tsk = Task(db)

cat = Category(db)
cat.new('Namentanzen')
tsk.new(title='Skinny Puppy - Remission & Bites', cat_id=4, desc='Höchstens 1000€!!', start='2025-09-01', end='2025-09-11')



    
dta = tsk.get_all();

for item in dta:
    print(dict(item))
    
    
        
dta = cat.get_all();

for item in dta:
    print(dict(item))