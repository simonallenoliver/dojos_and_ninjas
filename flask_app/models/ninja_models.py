from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM ninjas
        """

        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        ninja_row = []
        for row in results:
            new_ninja = cls(row)

            ninja_row.append(new_ninja)
        
        return ninja_row
    
    @classmethod
    def add_ninja(cls, form_data):

        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """

        return connectToMySQL("dojos_and_ninjas").query_db(query, form_data)
    

    @classmethod
    def get_ninjas_in_dojo(cls, id):

        data = {
            "id":id
        }

        query = """
            SELECT * FROM ninjas WHERE dojo_id = %(id)s
        """

        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        ninja_row = []
        for row in results:
            new_ninja = cls(row)

            ninja_row.append(new_ninja)
        
        return ninja_row