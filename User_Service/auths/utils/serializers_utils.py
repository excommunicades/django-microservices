from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from auths.models import User

def validate_user(data):

    '''UserLoginSerializer utility for user validaion'''

    try:
        user = User.objects.get(nickname=data['verify_field'])
    except Exception as e:
        try:
            user = User.objects.get(email=data['verify_field'])
        except Exception as e:
            raise ValidationError({"errors": {"error": "User does not exist"}})

    if not user.check_password(data['password']):
        raise ValidationError({"errors": {"password": "Wrong Password."}})
    
    data['verify_field'] = user

    return data

def get_user_token_data(user):

    '''UserLoginSerializer utility for user token creation'''

    refresh = RefreshToken.for_user(user)
    return {
        'user': {
            'id': user.id,
            'nickname': user.nickname,
            'email': user.email,
        },
        'tokens':{
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
    }
