# import mongodb
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import uuid

class DatabaseHandler:
    # Private static variable
    load_dotenv()

    _client = client = MongoClient(
        f'mongodb+srv://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}@{os.getenv("DATABASE_NAME")}.6gnckw0.mongodb.net')

    @staticmethod
    def get_client_id(username: str, password: str) -> str:
        bank_users = DatabaseHandler._client['bank_users']['users']

        return uuid(bank_users.find_one({
            'username': username,
            'password': password
        })['client_id'])

    @staticmethod
    def get_client_info(user_id: uuid) -> dict:
        bank_user_info = DatabaseHandler._client['bank_users']['user_info']

        return bank_user_info.find_one({
            'user_id': str(user_id)
        })
    
    @staticmethod
    def register_user(user_id: uuid, user_data: dict) -> dict:
        bank_user_info = DatabaseHandler._client['bank_users']['user_info']
        bank_user_ids = DatabaseHandler._client['bank_users']['user_ids']

        # Check if the user already exists
        if bank_user_info.find_one({'user_id': str(user_id)}) != None:
            return {
                'message': 'User already exists.'
            }

        # Insert the user into the database
        bank_user_info.insert_one(user_data)

        # Return a success message
        return {
            'message': 'User successfully registered.'
        }
    
    @staticmethod
    def update_client_info(user_id: uuid, user_data: dict) -> dict:
        bank_user_info = DatabaseHandler._client['bank_users']['user_info']

        # Check if the user already exists
        if bank_user_info.find_one({'user_id': str(user_id)}) == None:
            return {
                'message': 'User does not exist.'
            }
        
        # Update the user's data
        bank_user_info.update_one({
            'user_id': user_id
        }, {
            '$set': user_data
        })

        # Return a success message
        return {
            'message': 'User successfully updated.'
        }

        


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