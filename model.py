import sqlite3

class DbHandle():
	def __init__(self, dbname, tablename):
		self.dbname = dbname
		self.tablename = tablename
		self.conn = sqlite3.connect(self.dbname)
		self.createTable()
		self.c = self.conn.cursor()
	def get(self):
		self.c.execute("SELECT id, status, task FROM todo")
		result = self.c.fetchall()
		return result
	def new(self, new, status):
		self.c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,status))
		self.conn.commit()
	def edit(self, edit, status, no):
		self.c.execute("UPDATE todo SET task = ?, status = ? WHERE id=?", (edit, status, no))
		self.conn.commit()
	def delete(self, id_task):
		self.c.execute("DELETE FROM todo WHERE id LIKE ?", (id_task,))
		self.conn.commit()
	def createTable(self):
		self.conn.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
		self.conn.commit()
	def __del__(self):
		self.c.close()