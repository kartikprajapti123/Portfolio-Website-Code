import random
from datetime import datetime,timedelta
from decouple import config
import jwt
def generate_otp():
    # Generate a random 6-digit OTP
    otp = random.randint(100000, 999999)  # 6 digits
    return otp

def generate_token(email=None, token_time=None):
    exp_time = datetime.now() + timedelta(days=token_time)
    JWT_PAYLOAD = {
        "email": email,
        "exp": exp_time,
    }
    jwt_token = jwt.encode(JWT_PAYLOAD, config("SECRET_KEY"), algorithm="HS256")
    return jwt_token


def decode_token(token):
    payload = jwt.decode(token, config("SECRET_KEY"), algorithms="HS256")
    return payload