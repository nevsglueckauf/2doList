from db import Db
my_db = Db()

my_db.exec('SELECT * FROM category')
dta = my_db.get_all()

for item in dta:
    print(item['id'], item['title'])