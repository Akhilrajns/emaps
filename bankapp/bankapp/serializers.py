from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
from bankapp.models import LoanDetail, User
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'email',)

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDetail
        fields = ('__all__')
                        