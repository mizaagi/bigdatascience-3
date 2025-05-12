import sqlite3
con = sqlite3.connect('chinook.db')
cursor = con.cursor()
obt1 = cursor.execute('SELECT Name, Composer FROM tracks WHERE tracks.GenreId==17')
print(obt1.fetchall())






cursor.close()
con.close()