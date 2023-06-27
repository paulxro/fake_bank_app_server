import random

class ResponseHandler:
    @staticmethod
    def login_user_fail(user_data: dict) -> tuple:
        return {
            'message': 'Invalid username or password.',
        }, 401

    @staticmethod
    def login_user_succ(user_data: dict, sessionJWT: str) -> tuple:
        return {
            'userData': {
                'name': user_data['username'],
                'discriminant': f'{random.randint(10000, 99999)}',

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