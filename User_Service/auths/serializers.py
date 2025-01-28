from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from auths.models import User

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

        try:
            user = User.objects.get(nickname=data['verify_field'])
        except Exception as e:
            try:
                user = User.objects.get(email=data['verify_field'])
            except Exception as e:
                raise serializers.ValidationError({"errors": "User does not exist"})

        if not user.check_password(data['password']):
            raise serializers.ValidationError({"errors": "Wrong Password."})

        return data
    
    def get_user_token_data(self, user):

        '''return user data & token'''

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
