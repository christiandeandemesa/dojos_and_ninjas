from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = [] # Why is this here?
        for d in result: # What does this do?
            dojos.append(cls(d))
        return dojos

    @classmethod
    def read_one_with_ninjas(cls, data):
        query  = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data) # result will be a list of ??? with the ninja attached to each row. 
        dojo = cls(result[0])
        for row in result:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo