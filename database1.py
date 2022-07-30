import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='maktabkhoone')
cursor = con.cursor
#cursor.execute('create table test1(name varchar(50), weight integer, height integer);')
#cursor.execute('insert into table test1 values(\'Amin\', 75, 180);')
#cursor.execute('insert into table test1 values(\'Mahdi\', 90, 190);')
#cursor.execute('insert into table test1 values(\'Mohammad\', 75, 175);')
#cursor.execute('insert into table test1 values(\'Ahmad\', 60, 175);')

cursor.execute('select * from test1 order by height desc, weight asc;')
for (name, height, weight) in cursor:
    print("%s %d %d" %(name, height, weight))
