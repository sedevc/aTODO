from bottle import route, run, debug, template, request, redirect
import model

DB_NAME = "todo.db"
DB_TABLE = "todo"

@route('/')
@route('/<id>')
def todo_list(id=False):
    return template('view', id=id, rows=todoDB.get())

@route('/new', method='GET')
def new_item():
    if request.GET.get('save','').strip():
        new = request.GET.get('task', '').strip()
        status = request.GET.get('status', '').strip()
        todoDB.new(new, status)
        redirect("/")


@route('/edit/:no', method='GET')
def edit_item(no):
    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()
        todoDB.edit(edit, status, no)
        redirect("/")

@route('/remove/:no', method='GET')
def remove_item(no):
    todoDB.delete(no)
    redirect("/")

todoDB = model.DbHandle(DB_NAME, DB_TABLE)

debug(True)
run(host='0.0.0.0', port=8080, reloader=True)