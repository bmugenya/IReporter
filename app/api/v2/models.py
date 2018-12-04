"""Product Model and data storage functions"""
from datetime import datetime

from ...db_con import connection


class Flag_model():
    """This class defines the Product model and
        the various methods of manipulating the product data"""

    def __init__(self):
        """Initialise constructor"""
        self.db = init_db()

    def save(self, title, flag_type, location, incident):
        """Product Class method to add product to list"""

        flag = {
            "Id": flag_id,
            "Title": title,
            "Type": flag_type,
            "location": location,
            "Incident": incident,
            "Date": created_on

        }
        # Validation

        query = """INSERT INTO flag
                              (id, title, type, location, incident,post_date)
                              VALUES(%(flag_id)s, %(title)s, %(flag_type)s,
                              %(location)s, %(incident)s, %(time)s;"""
        self.cursor.execute(query)
        self.connection.commit()

    def get(self):
        """Product Class method to fetch all products"""
        self.custom_cursor.execute("SELECT * FROM flag;")
        flags = self.custom_cursor.fetchall()
        self.connection.close()

        for post in flags:
            return post, 200

    def get_flag(self, post_id):
        """Product Class method to fetch a single product by ID"""

        self.custom_cursor.execute("SELECT * FROM flag WHERE id = (%s);", (post_id,))
        flags = self.custom_cursor.fetchall()
        self.connection.close()

        for post in flags:
            return post

    def update_flag(self, flag_id, title, flag_type, location, incident):
        """Class method to Edit Product details"""
        self.cursor.execute("SELECT * FROM flag WHERE id = %s", (flag_id,))
        flags = self.cursor.fetchone()

        time = datetime.now()
        query = """UPDATE flag SET title = %s,
                     type = %s, location=%s, incident = %s,
                     post_date = %s WHERE id = %s"""
        self.cursor.execute(query, (title, flag_type, location, incident,
                                    time))
        self.connection.commit()
        self.connection.close()
        return 'success'

    def delete_product(self, flag_id):
        """Class method to delete products from inventory"""
        self.cursor.execute("SELECT * FROM flag WHERE id = (%s);", (flag_id,))
        query = self.cursor.fetchone()
        self.cursor.execute("DELETE FROM flag WHERE id = (%s);", (flag_id,))
        self.connection.commit()
        self.connection.close()
        return 'success'
