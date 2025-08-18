from app.db import connectdb

class todo:
    def __init__(self, id, title, content, status):
        self.id =  id
        self.title = title
        self.content = content
        self.status = status

    # create
    @staticmethod
    def create(title, content, status = False):
        conn = connectdb()
        cursor = conn.cursor()
        query = "INSERT INTO todos (title, content, status) VALUES (%s, %s, %s)"
        cursor.execute(query, (title,content, status))
        conn.commit()
        cursor.close()
        conn.close()
    

    # get all datas
    @staticmethod
    def get_all():
        conn = connectdb()
        cursor = conn.cursor(dictionary = True)
        cursor.execute("SELECT * FROM todos")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [todo(row["id"], row["title"], row["content"], row["status"]) for row in rows]

    # get one item using id
    @staticmethod
    def get_by_id(id):
        conn = connectdb()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM todos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row :
            return todo(row['id'], row['title'], row['content'], row['status'])
        return None
    
    # update a data     
    @staticmethod
    def update(title, content, status, id):
        conn = connectdb()
        cursor = conn.cursor()
        query = 'UPDATE todos SET title=%s, content=%s, status=%s WHERE id=%s'
        cursor.execute(query, (title, content, status, id))
        conn.commit()
        cursor.close()
        conn.close()

    # delete a row 
    @staticmethod
    def delete(id):
        conn = connectdb()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    # transform on dict for jinja
    def to_dict(self):
        return{
            'id' : self.id,
            'title' : self.title,
            'content' : self.content,
            'status' : self.status
        }