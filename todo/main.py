from flask import Flask, render_template, jsonify, request

from todo.db import TodoDB

app = Flask(__name__)


@app.route('/')
def index():
    db = TodoDB()
    todo = db.read_all()
    db.close()
    return render_template('index.html', data=todo)


@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    db = TodoDB()
    todo = db.delete(todo_id)
    result = db.read(todo_id)
    db.close()

    return jsonify({'existed': True}) if result else \
        jsonify({'existed': False})


@app.route('/todo', methods=['POST'])
def add():
    data = request.get_json()
    db = TodoDB()
    todo = db.create(data['text'])
    db.close()
    return "ok"


@app.route('/todo/<int:todo_id>',  methods=['PUT'])
def flip_status(todo_id):
    db = TodoDB()
    todo = db.read(todo_id)
    print("ddsdsdsd")
    if todo:
        status = todo[2]
        print(status)
        status = 'done' if status == 'doing' else 'doing'
        print(status)
        db.update_status(todo_id, status)
        db.commit()
    db.close()
    return 'ok'


if __name__ == "__main__":
    app.run(debug=True)
