from django.views.generic.base import View
from wkhtmltopdf.views import PDFTemplateResponse

class MyPDFView(View):
    template = 'pdf/pdftemplate.html'  # the template

    def get(self, request, pk):
        data = {"mydata": "your data"}  # data that has to be renderd to pdf templete
        try:
            response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="loan-details.pdf",
                                       context=data,
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