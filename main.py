from db import Db
from db import Category
from db import Task

db = Db()
cat = Category(db)
cat.new('Foo')
tsk = Task(db)
dta = tsk.get_all();

for item in dta:
    print(dict(item))

    
tsk.new(title='PF _ tdsotm', cat_id=4, desc='Höchstens 55€!!', start='2025-09-01', end='2025-09-11')



    
dta = cat.get_all();

for item in dta:
    print(dict(item))