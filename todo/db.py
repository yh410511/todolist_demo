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
        cursor = cursor.execute('select id,content,status from todo order by id desc')
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
        cursor.execute('create table IF not EXISTS todo (id INTEGER primary key AUTOINCREMENT, content varchar(50))')
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self, todo_id):
        # print('delete',todo_id)
        cursor = self.cursor()
        cursor = cursor.execute('delete from todo where id=?', (todo_id,))
        self.commit()
        cursor.close()
        return

    def read(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('select id ,content,status from todo where id=?', (todo_id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def create(self, text):
        cursor = self.cursor()
        cursor = cursor.execute('insert into todo(content) values (?)', (text,))
        cursor.close()
        self.commit()

    def migrate_latest(self):
        self.init_db()
        self.s2_add_status_colunm()

    def s2_add_status_colunm(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("alter table todo add column status varchar default 'done'")
        cursor.close()
        conn.commit()
        conn.close()

    def update_status(self, todo_id, status):
        cursor = self.cursor()
        cursor = cursor.execute('update todo set status = ? where id = ?', (status, todo_id))
        self.commit()
        data = cursor.fetchone()
        print(data)
        cursor.close()

        return data


if __name__ == "__main__":
    db = TodoDB()
    # db.read_all()
    # db.init_db()
    # db.read()
    # db.create()
    db.migrate_latest()
    # db.update_status(21,'done')
