from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
from bankapp.models import LoanDetail, User, LoanUserAddress, Document, Review, AddressType
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    authentication_token = serializers.CharField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False, write_only=True)
    password = serializers.CharField(required=True, allow_blank=False, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'authentication_token')


    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is not None:
            # the password verified for the user
            if user.is_active:
                (token, created) = Token.objects.get_or_create(user=user)  # token.key has the key
                user.authentication_token = token.key
                update_last_login(None, user=user)
                return user
            else:
                raise serializers.ValidationError("Account is not active. Contact support!")
        else:
            raise serializers.ValidationError("The username/password is incorrect.")


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanDetail
        fields = ('job_no', 'loan_account_no', 'loan_type', 'job_status', 'applicant_type',
         'customer_name', 'father_name', 'mother_name', 'spouse_name', 'martial_status',
         'nationality', 'resident', 'dob', 'sex', 'kyc_status', 'job_type', 'gross_annual_income',
         'political_influence', 'created_date', 'modified_date')
        depth = 1


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanUserAddress
        fields = ('id', 'address_type', 'house_name', 'street', 'area', 'landmark', 'city', 'state', 'village',
            'thaluk', 'survey_no', 'telephone', 'mobile_primary', 'mobile_secondary', 'email',
            'created_date', 'latitude', 'longitude', 'verified', 'address_verifier', 'mark_borders')
        depth = 1


class LatLongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    latitude = serializers.CharField(required=True)
    longitude = serializers.CharField(required=True)
    mark_borders = serializers.CharField(required=True)

    class Meta:
        model = LoanUserAddress
        fields = ('latitude', 'longitude', 'id', 'mark_borders')


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('name', 'document')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('__all__')


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanDetail
        fields = ('loan_account_no', 'customer_name', 'job_no')


class AddressTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressType
        fields = ('address_type', 'id')
