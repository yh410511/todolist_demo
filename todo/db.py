import sqlite3


class TodoDB(object):
    def __init__(self):
        self.conn = sqlite3.connect('test.db')

    def cursor(self):
        return self.conn.cursor()

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def read_all(self):
        cursor = self.cursor()
        cursor = cursor.execute('select id,content from todo')
        data = cursor.fetchall()
        # data = [d[0] for d in data]
        cursor.close()
        return data

        # return ["测试1",
        #         "测试2",
        #         "测试3",
        #         "测试4",
        #         "测试5",
        #         "测试6"]

    def init_db(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('create table todo (id INTEGER primary key AUTOINCREMENT, content varchar(50))')
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self, todo_id):
        # print('delete',todo_id)
        cursor = self.cursor()
        cursor = cursor.execute('delete from todo where id=?', (todo_id,))
        cursor.close()
        self.commit()
        return

    def read(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('select id ,content from todo where id=?', (todo_id,))
        data = cursor.fetchone()
        cursor.close()
        return data


if __name__ == "__main__":
    db = TodoDB()
    # db.read_all()
    # db.init_db()
    db.read()
