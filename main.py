from db import Db
my_db = Db()

dta = my_db.exec('SELECT * FROM category').get_all()
#dta = my_db

for item in dta:
    print(item['id'], item['title'])
    
print(my_db.get_by_id('category', 2))