from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
import pprint

DB = "Instruments_schema"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.instrument = []
        
    
    @classmethod
    def insert_new_user(cls,data):
        query = """ INSERT INTO users (first_name, last_name,email, password)
                Values (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_all_users(cls):
        query = """ SELECT * FROM users """
        results = connectToMySQL(DB),query_db(query)
        
        users = []
        
        for user in results:
            users.append(cls(user))
        
        return users
    
    @classmethod
    def one_email(cls,data):
        query = """ SELECT * FROM users
                WHERE email = %(email)s;
        """
        results = connectToMySQL(DB).query_db(query,data)
        pprint.pprint(results)
        
        if len(results) ==0:
            return None
        
        return cls(results[0])
    
    @classmethod
    def get_one_user(cls,data):
        query = """ SELECT * FROM users
                WHERE id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update_user(cls,data):
        query = """UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s,
                email = %(email)s, password = %(password)s
                WHERE id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query,data)
        pprint.pprint(results)
        
        return results
    
    @classmethod
    def delete_user(cls,data):
        query = """ DELETE FROM users
                WHERE id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query,data)
        pprint.pprint(results)
        
        return results
    
    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        if len(form_data['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(form_data['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(form_data['password']) < 8:
            flash("Name must be at least 8 characters.")
            is_valid = False
        if form_data['password'] != form_data["confirm_password"]:
            is_valid = False
            flash("passwords must agree")
        return is_valid


    @staticmethod
    def validate_login(form_data):
        is_valid = True
        found_user = User.one_email({"email": form_data["email"]})
        if found_user == None:
            is_valid = False
            flash("invalid login")
            return False
        if not bcrypt.check_password_hash(found_user.password,form_data["password"]):
            is_valid = False
            flash("Invalid login")
        return is_valid
        
        