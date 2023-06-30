from flask import Flask, request
from flask_cors import CORS

from utils.ResponseHandler import ResponseHandler
from utils.DatabaseHandler import DatabaseHandler
from utils.JWTHandler import JWTHandler


app = Flask(__name__)
cors = CORS(app)

@app.route('/api/login', methods=['POST'])
def index() -> tuple:
    user_data: dict = request.json['userData']
    # meta_data: dict = request.json['metaData']

    """ Always return a 200 response, even if the login fails. """
    return ResponseHandler.login_user_succ(user_data, JWTHandler.construct_jwt())


@app.route('/api/verifySession', methods=['POST'])
def verifySession() -> tuple:

    # Read the JWT from the request
    raw_jwt: str = request.json['sessionJWT']

    # Verify the JWT
    is_valid_jwt: bool = JWTHandler.verify_jwt(JWTHandler.decode_jwt(raw_jwt))

    # Return the response
    if is_valid_jwt:
        return ResponseHandler.verify_session_succ()
    
    return ResponseHandler.verify_session_fail()
