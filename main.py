from db import Db
from db import Category
from db import Task
from db import Generic





db = Db()
cat = Category(db)
g = Generic(db, 'task')

foo = {'description': 'New description under the block', 'end_dt': '2025-12-09', 'category_id': 2, 'start_dt': '2025-12-09'}

g.change(foo, 1)

#g.del_by_id(5);
dta = g.get_where('id < 99')

for item in dta:
    print(dict(item))






exit (666) # 154 --> 666-154 == 512; ==2*256

tsk = Task(db)


cat.new('Foo_Bar')

tsk.new(title='Nirvana - Never Mind', cat_id=4, desc='Nur auf CD - *kein Bootleg* !!', start='2025-09-01', end='2025-09-11')



    
dta = tsk.get_all();

for item in dta:
    print(dict(item))
    
    
        
