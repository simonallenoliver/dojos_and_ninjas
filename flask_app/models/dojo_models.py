from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM dojos
        """

        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        dojo_row = []
        for row in results:
            new_dojo = cls(row)

            dojo_row.append(new_dojo)
        
        return dojo_row
    
    @classmethod
    def add_dojo(cls, form_data):

        query = """
            INSERT INTO dojos (name)
            VALUES(%(name)s);
        """

        return connectToMySQL("dojos_and_ninjas").query_db(query, form_data)
    

    @classmethod
    def get_one(cls, id):
        data = {
            "id":id
        }

        query = """
            SELECT * FROM dojos WHERE id = %(id)s
        """
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)

        if results:
            row = results[0]
            new_dojo = cls(row)
            return new_dojo
        
