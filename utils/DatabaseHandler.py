# import mongodb
from pymongo import MongoClient, collection
from dotenv import load_dotenv
import os
import uuid
import bcrypt

from utils.ResponseHandler import ResponseTextHandler

class DatabaseStatusCode:
        SUCCESS: int = 0
        FAIL: int = 1

class DatabaseHandler:
    load_dotenv()

    _client: MongoClient = MongoClient(
        f'mongodb+srv://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}@{os.getenv("DATABASE_NAME")}.6gnckw0.mongodb.net'
    )

    @staticmethod
    def register_user(user_data: dict) -> dict:
        bank_user_ids: collection = DatabaseHandler._client['bank_users']['user_ids']

        raw_username: str = user_data['username']
        raw_password: str = user_data['password']

        hashed_password: str = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

        # Check if the user already exists
        if bank_user_ids.find_one({'username': raw_username}) != None:
            return {
                'status': DatabaseStatusCode.FAIL,
                'message': ResponseTextHandler.USER_ALREADY_EXISTS_ERROR,
            }
        
        # Generate a unique uuid
        raw_user_id: str = str(uuid.uuid4())

        # Insert the user into the database
        database_insert_res: dict = bank_user_ids.insert_one({
            'username': raw_username,
            'password': hashed_password,
            'user_id': raw_user_id,
        })

        print(database_insert_res)

        # Return a success message
        return {
            'status': DatabaseStatusCode.SUCCESS,
            'message':  ResponseTextHandler.SUCCESS,
        } 

    @staticmethod
    def login_user(auth_info: dict) -> dict:
        raw_username: str = auth_info['username']
        raw_password: str = auth_info['password']

        # Check if the user exists
        bank_user_ids = DatabaseHandler._client['bank_users']['user_ids']

        database_find_res: dict = bank_user_ids.find_one({
            'username': raw_username,
        })

        if database_find_res == None:
            return {
                'status': DatabaseStatusCode.FAIL,
                'message': ResponseTextHandler.USER_DOES_NOT_EXIST_ERROR,
            }
        
        # Check if the password is correct
        if not bcrypt.checkpw(raw_password.encode('utf-8'), database_find_res['password']):
            return {
                'status': DatabaseStatusCode.FAIL,
                'message': ResponseTextHandler.INVALID_USERNAME_OR_PASSWORD_ERROR,
            }
        
        # Return a success message
        return {
            'status': DatabaseStatusCode.SUCCESS,
            'message': ResponseTextHandler.SUCCESS,
            'userData': {
                'username': database_find_res['username'],
                'password': database_find_res['password'],
                'user_id': database_find_res['user_id'],
            }
        }
        

    

    
    @staticmethod
    def update_client_info(user_id: uuid, new_user_data: dict) -> dict:
        bank_user_info = DatabaseHandler._client['bank_users']['user_info']

        


# def register_user(user_data: dict) -> dict:
#     # Check if the user already exists
#     if client['users']['users'].find_one({'username': user_data['username']}) != None:
#         return {
#             'message': 'User already exists.'
#         }

#     # Insert the user into the database
#     client['users']['users'].insert_one(user_data)

#     # Return a success message
#     return {
#         'message': 'User successfully registered.'
#     }