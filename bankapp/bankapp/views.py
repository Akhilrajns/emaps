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
from bankapp.serializers import UserSerializer, LoanSerializer, AddressSerializer, LatLongSerializer, LoanSerializer
from bankapp.models import LoanDetail, LoanUserAddress, User
from rest_framework.authtoken.models import Token

class Login(APIView, ResponseViewMixin):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})
        else:
            return self.jp_error_response('HTTP_400_BAD_REQUEST', 'INVALID_LOGIN',
                                          self.error_msg_list(serializer.errors))


class Loan(APIView, ResponseViewMixin):

    def get(self, request, *args, **kwargs):
        Loans = LoanDetail.objects.all()
        serializer = LoanSerializer(Loans, many=True)
        return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})


class AddressList(APIView, ResponseViewMixin):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        try:
            token = kwargs['token'];
            token = Token.objects.get(pk=token)
        except Exception as e:
            return self.jp_error_response('HTTP_400_BAD_REQUEST', 'INVALID_UPDATE', str(e))
        
        address = LoanUserAddress.objects.filter(verified=False, address_verifier_id=token.user_id)
        serializer = AddressSerializer(address, many=True)
        return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})


class UpdateLatLong(APIView, ResponseViewMixin):

    def post(self, request, *args, **kwargs):
        serializer = LatLongSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            try:
                UserAddress = LoanUserAddress.objects.get(pk=data['id'])
                UserAddress.latitude = data['latitude']
                UserAddress.longitude = data['longitude']
                UserAddress.verified = True
                UserAddress.save()
                return self.jp_response(s_code='HTTP_200_OK', data={'user': serializer.data})
            except Exception:
                return self.jp_response(s_code='HTTP_400_BAD_REQUEST', data={'user': 'No record exists.'})
        else:
            return self.jp_response(s_code='HTTP_400_BAD_REQUEST', data={'user': serializer.errors})


class SearchLoan(APIView, ResponseViewMixin):

    def get(self, request, *args, **kwargs):
        loan = kwargs['loan'].split(',');
        result = []
        loans = LoanDetail.objects.filter(loan_account_no__in=loan)
        for loan in loans:
            serializer = LoanSerializer(loan)
            job_no = serializer.data['job_no']
            addresses = LoanUserAddress.objects.filter(loan=job_no, verified=True)
            if addresses.exists():
                address = AddressSerializer(addresses, many=True)
                new_data = serializer.data
                new_data['addresses'] = address.data
                result.append(new_data)
        return self.jp_response(s_code='HTTP_200_OK', data=result)
        
