import sqlite3


class TodoDB(object):

    def read_all(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor = cursor.execute('select id,content from todo')
        data = cursor.fetchall()
        # data = [d[0] for d in data]
        cursor.close()
        conn.close()
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


if __name__ == "__main__":
    db = TodoDB()
    db.read_all()
    # db.init_db()
