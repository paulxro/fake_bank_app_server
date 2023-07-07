"""
This file contains the ResponseHandler class, which is used to handle the responses sent by the server.
"""

class ResponseTextHandler:
    USER_ALREADY_EXISTS_ERROR: str = 'User already exists.'
    USER_DOES_NOT_EXIST_ERROR: str = 'User does not exist.'
    INVALID_USERNAME_OR_PASSWORD_ERROR: str = 'Invalid username or password.'
    INVALID_JWT_ERROR: str = 'Invalid JWT.'
    EXPIRED_JWT_ERROR: str = 'Expired JWT.'
    SUCCESS: str = 'Success.'

class ResponseHandler:

    @staticmethod
    def register_user_fail() -> tuple:
        return {
            'message': ResponseTextHandler.USER_ALREADY_EXISTS_ERROR,
        }, 400
    
    @staticmethod
    def register_user_succ(user_data: dict, sessionJWT: str) -> tuple:
        return {
            'userData': {
                'name': user_data['username'],
                'user_id': user_data['user_id'],
            },
            'sessionData': {
                'JWT': sessionJWT,
            }
        }, 200

    @staticmethod
    def login_user_fail() -> tuple:
        return {
            'message': ResponseTextHandler.INVALID_USERNAME_OR_PASSWORD_ERROR,
        }, 401

    @staticmethod
    def login_user_succ(user_data: dict, sessionJWT: str) -> tuple:
        return {
            'userData': {
                'name': user_data['username'],
                'user_id': user_data['user_id'],
            },
            'sessionData': {
                'JWT': sessionJWT,
            }
        }, 200
    
    @staticmethod
    def verify_session_fail(type: str = 'expired') -> tuple:
        # The provided JWT is invalid
        if type == 'invalid':
            return {
                'isValid': False,
            }, 400

        # (Default) The provided JWT is expired
        return {
            'isValid': False,
        }, 401
    
    @staticmethod
    def verify_session_succ() -> tuple:
        return {
            'isValid': True,
        }, 200

    @staticmethod
    def send_expired_response():
        return {}
    
