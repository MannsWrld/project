from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import user
import pprint
from flask_app import app
from flask import flash

DB = "Instruments_schema"

class Instrument:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.brand = data['brand']
        self.type = data['type']
        self.price = data['price']
        self.year = data['year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.seller = None
        
    @classmethod
    def create_new_instru(cls,data):
        query = """ INSERT INTO instruments (name,brand,type,price,year,user_id)
                VALUES (%(name)s,%(brand)s,%(type)s,%(price)s,%(year)s,%(user_id)s)
        """
        results = connectToMySQL(DB).query_db(query,data)
        pprint.pprint(results)
    
    @classmethod
    def all_instruments(cls):
        query = """ SELECT * FROM instruments"""
        results = connectToMySQL(DB).query_db(query)
        
        instruments = []
        
        for instrument in results:
            instruments.append(cls(instrument))
        
        return instruments
    
    @classmethod
    def join_all(cls,instrument_data):
        query = """ SELECT * FROM users
                JOIN instruments ON users.id = instruments.user_id
                WHERE instruments.id = %(id)s;
            """
        results = connectToMySQL(DB).query_db(query,instrument_data)
        pprint.pprint(results)

        instruments_user = cls(results[0])
        # instruments.seller = results[0]['first_name']
    
        return instruments_user
    
    @classmethod
    def update_instrument(cls,data):
        query = """ UPDATE instruments 
                    SET name = %(name)s, brand = %(brand)s,type = %(type)s, price = %(price)s, year = %(year)s
                    WHERE id = %(id)s
                """
        results = connectToMySQL(DB).query_db(query,data)
        pprint.pprint(results)
        return results
    
    @classmethod
    def get_one(cls,data):
        query = """ SELECT * FROM instruments
                    WHERE id = %(id)s;
                """
        results = connectToMySQL(DB).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_one_user(cls,data):
        query = """SELECT * FROM users
                    WHERE id =  %(id)s;
                """
        results = connectToMySQL(DB).query_db(query,data)
        return results
    
    @classmethod
    def delete_Instru(cls,instrument_data):
        query = """ DELETE FROM instruments
                WHERE id = %(id)s;
            """
        results = connectToMySQL(DB).query_db(query,instrument_data)
        pprint.pprint(results)
        return results
    
    @staticmethod
    def validate_instrument(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            flash("Name must be greater")
            is_valid = False
        if len(form_data['brand']) < 3:
            flash("Brand must be greater")
            is_valid = False
        if len(form_data['type']) < 3:
            flash("Type must be greater")
            is_valid = False
        if len(form_data['price']) < 3:
            flash("Price must be greater")
            is_valid = False
        if len(form_data['year']) < 3:
            flash("Year must be greater")
            is_valid = False
        return is_valid
        
        