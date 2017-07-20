from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from utilities.mixins import ResponseViewMixin
from utilities.pagination import CustomOffsetPagination
from datetime import date
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from bankapp.serializers import UserSerializer, LoanSerializer, AddressSerializer, LatLongSerializer
from bankapp.models import LoanDetail, LoanUserAddress

class Login(APIView, ResponseViewMixin):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})
        else:
            return self.jp_response(s_code='HTTP_400_OK', data={'user': serializer.data})


class Loan(APIView, ResponseViewMixin):

    def get(self, request, *args, **kwargs):
        Loans = LoanDetail.objects.all()
        serializer = LoanSerializer(Loans, many=True)
        return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})


class AddressList(APIView, ResponseViewMixin):

    def get(self, request, *args, **kwargs):
        address = LoanUserAddress.objects.filter(verified=False)
        serializer = AddressSerializer(address, many=True)
        return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})


class UpdateLatLong(APIView, ResponseViewMixin):

    def post(self, request, *args, **kwargs):
        serializer = LatLongSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            user = LoanUserAddress.objects.get(pk=data['id'])
            user.latitude = data['latitude']
            user.longitude = data['longitude']
            user.verified = True
            user.save()

            return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})
        else:
            return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.validated})



