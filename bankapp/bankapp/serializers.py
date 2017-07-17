from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
from bankapp.models import LoanDetail, User, LoanUserAddress, Document, Review
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
        fields = ('job_no', 'loan_account_no', 'loan_type', 'job_status', 'applicant_type',
         'customer_name', 'father_name', 'mother_name', 'spouse_name', 'martial_status',
         'nationality', 'resident', 'dob', 'sex', 'kyc_status', 'job_type', 'gross_annual_income',
         'political_influence', 'created_date', 'modified_date')


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanUserAddress
        fields = ('id', 'address_type', 'house_name', 'street', 'area', 'landmark', 'city', 'state', 'village',
            'thaluk', 'survey_no', 'telephone', 'mobile_primary', 'mobile_secondary', 'email',
            'created_date', 'latitude', 'longitude', 'verified')


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
