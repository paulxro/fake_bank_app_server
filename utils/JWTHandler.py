import jwt
import datetime
import dotenv

from utils.ResponseHandler import ResponseHandler

class JWTHandler:
    JWT_TOKEN_TIMEOUT: int = 1000 * 60 * 30 # 30 minutes
    dotenv.load_dotenv('../.env')

    def decode_jwt(raw_jwt: str) -> dict:
        # Read the JWT from the request
        encoded_jwt: bytes = raw_jwt.encode('utf-8')

        # Decode the JWT
        try:
            decoded_jwt: dict = jwt.decode(
                encoded_jwt, 
                dotenv.dotenv_values()["JWT_SECRET"], 
                algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            return ResponseHandler.verify_session_fail('expired')
        except jwt.InvalidTokenError:
            return ResponseHandler.verify_session_fail('invalid')

        return decoded_jwt

    def construct_jwt(user_data: dict) -> str:
        # Construct a JWT with the following payload:
        presentDate: datetime.datetime.date = datetime.datetime.now()
        unix_timestamp: datetime.datetime.timestamp = datetime.datetime.timestamp(presentDate) * 1000

        # Return the encoded JWT
        encoded_jwt: dict = jwt.encode({
            'iat': unix_timestamp,
            'user_id': user_data['user_id'],
            'exp': unix_timestamp + JWTHandler.JWT_TOKEN_TIMEOUT,
        }, dotenv.dotenv_values()["JWT_SECRET"], algorithm='HS256')

        return encoded_jwt.decode('utf-8')
    
    def verify_jwt(decoded_jwt: dict) -> bool:
        current_unix_timestamp: datetime.datetime.timestamp = datetime.datetime.timestamp(datetime.datetime.now()) * 1000

        return decoded_jwt['exp'] > current_unix_timestamp




