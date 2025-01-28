from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from auths.models import User
from auths.serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
)

class UserRegistrationView(generics.CreateAPIView):

    '''Registration endpoint for user'''

    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer


class UserLoginView(generics.GenericAPIView):

    '''User login enpoint'''

    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(verify_field=request.data['verify_field'])
        response = serializer.get_user_token_data(user)

        return Response(response, status=status.HTTP_200_OK)
