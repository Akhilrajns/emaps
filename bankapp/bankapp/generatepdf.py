from django.views.generic.base import View
from wkhtmltopdf.views import PDFTemplateResponse
from bankapp.models import LoanDetail, LoanUserAddress, Document, Review
from bankapp.serializers import LoanSerializer, AddressSerializer, DocumentSerializer, ReviewSerializer

class MyPDFView(View):
    template = 'pdf/pdftemplate.html'  # the template

    def get(self, request, pk):
        #data = {"mydata": "your data"}  # data that has to be renderd to pdf templete

        loan = LoanDetail.objects.get(pk=pk)
        address = LoanUserAddress.objects.filter(loan=loan)
        documents = Document.objects.filter(loan=loan)
        reviews = Review.objects.filter(loan=loan)


        loanDetail = loan
        serializer = LoanSerializer(loan)
        serializedAddress = AddressSerializer(address, many=True)
        serializedDocs = DocumentSerializer(documents, many=True)
        serializedReviews = ReviewSerializer(reviews, many=True)
        #print(serializedReviews)
        serializerData = serializer.data
        serializerData['sex'] = loanDetail.get_sex_display()
        serializerData['job_type'] = loanDetail.get_job_type_display()
        serializerData['loan_type'] = loanDetail.get_loan_type_display()
        serializerData['job_status'] = loanDetail.get_job_status_display()
        serializerData['applicant_type'] = loanDetail.get_applicant_type_display()
        serializerData['martial_status'] = loanDetail.get_martial_status_display()
        serializerData['nationality'] = loanDetail.get_nationality_display()
        serializerData['kyc_status'] = loanDetail.get_kyc_status_display()
        serializerData['gross_annual_income'] = loanDetail.get_gross_annual_income_display()

        serializerData['address'] = serializedAddress.data
        serializerData['documents'] = serializedDocs.data
        serializerData['reviews'] = serializedReviews.data

        try:
            response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="loan-details.pdf",
                                       context=serializerData,
                                       show_content_in_browser=True,
                                       cmd_options={'margin-top': 15,
                                                    "zoom": 1,
                                                    "viewport-size": "1366 x 513",
                                                    'javascript-delay': 1000,
                                                    'footer-center': '[page]',
                                                    "no-stop-slow-scripts": True},
                                       )
            return response

        except Exception as e:
            print(str(e))