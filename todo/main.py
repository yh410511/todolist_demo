from flask import Flask, render_template

from todo.db import TodoDB

app = Flask(__name__)


@app.route('/')
def index():
    db = TodoDB()
    todo = db.read_all()
    return render_template('index.html', data=todo)


@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    db = TodoDB()
    todo = db.delete(todo_id)
    return 'ok'


if __name__ == "__main__":
    app.run(debug=True)
