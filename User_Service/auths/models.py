from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


'''
#TODO:
# Profile fields
# Avatar saving
'''


class UserManager(BaseUserManager):
    
    def create_user(self, email,nickname, password=None, **extra_fields):

        if not nickname and not email:
            raise ValueError('Nickname or Email must be implemented')

        email = self.normalize_email(email)
        user = self.model(nickname=nickname, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        
        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    
    nickname = models.CharField(max_length=30, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    registration_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'