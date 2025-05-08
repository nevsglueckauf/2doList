from db import Db
from db import Category
from db import Task
from db import Generic





db = Db()
cat = Category(db)
g = Generic(db, 'task')

foo = {'title': 'Foyer des Arts: 1989: Was ist super? (live)','description': 'Sehr schwierig zu bekommen - auf Vinyl, oder CD. Digital - z.B. YT: kein Problem', 'end_dt': '2075-12-09', 'category_id': 4, 'start_dt': '2025-12-09'}

g.change(foo, 7)

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
    
    
        
