from rest_framework import serializers
from auths.models import User

from auths.utils.serializers_utils import (
    get_user_token_data,
    validate_user,
)

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    '''Registration serializer'''

    class Meta:
        model = User
        fields = [
            'nickname',
            'email',
            'password'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):

    '''Login jwt Serializer'''

    verify_field = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        '''returns user from nickname/email'''

        return validate_user(data)
    
    def get_user_token_data(self, user):

        '''return user data & token'''

        return get_user_token_data(user)