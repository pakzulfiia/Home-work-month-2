from lessons.playlist import PlayList
import sqlite3
from lessons.database import (create_tables, add_student,get_all_students)


play1 = PlayList('pop-2')
print(play1)
connection = sqlite3.connect('database.db')
create_tables(connection)
add_student(connection, 
            'Igor', 
            36, 
            'Bishkek'
            )
add_student(connection, 'Masha', 23, 'Tokmok')
add_student(connection, 'Vanya', 42, "Naryn")

# for st in get_all_students(connection):
#     print(st)
print("== select ==")
print(get_all_students(connection))
connection.close()