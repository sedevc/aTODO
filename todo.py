import sqlite3
from bottle import route, run, debug, template, request, redirect

@route('/')
@route('/todo')
def todo_list():
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("SELECT id, status, task FROM todo")
	#c.execute("SELECT id, status, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	c.close()
	print result
	return template('make_table', rows=result)

@route('/new', method='GET')
def new_item():
	if request.GET.get('save','').strip():
		new = request.GET.get('task', '').strip()
		status = request.GET.get('status', '').strip()
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		if status == 'open':
			status = 1
		else:
			status = 0
		c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,status))
		new_id = c.lastrowid

		conn.commit()
		c.close()
		redirect("/")
		
	else:
		return template('new_task.tpl')

@route('/edit/:no', method='GET')
def edit_item(no):

	if request.GET.get('save','').strip():
		edit = request.GET.get('task','').strip()
		status = request.GET.get('status','').strip()

		if status == 'open':
			status = 1
		else:
			status = 0

		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute("UPDATE todo SET task = ?, status = ? WHERE id=?", (edit, status, no))
		conn.commit()
		redirect("/")
	else:
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute("SELECT task FROM todo WHERE id LIKE ?", (no,))
		cur_data = c.fetchone()

		return template('edit_task', old=cur_data, no=no)

@route('/remove/:no', method='GET')
def remove_item(no):
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("DELETE FROM todo WHERE id LIKE ?", (no,))
	conn.commit()
	redirect("/")

debug(True)
run(host='0.0.0.0', port=8080, reloader=True)
