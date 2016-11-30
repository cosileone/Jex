import sqlite3

with sqlite3.connect("jex.db") as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE users(username TEXT, email TEXT, password TEXT)")
	c.execute('INSERT INTO users VALUES("cosi", "a@b.c", "cosi123")')
	c.execute('INSERT INTO users VALUES("admin", "admin@b.c", "admin")')
