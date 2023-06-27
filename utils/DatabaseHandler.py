# import mongodb
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

client = MongoClient(
    f'mongodb+srv://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_NAME}.6gnckw0.mongodb.net'
)

user_info = client['bank_users']

usernames = user_info['usernames']

print(usernames.find_one({'username': 'test'}))