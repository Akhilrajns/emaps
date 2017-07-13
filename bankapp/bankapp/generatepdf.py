from django.views.generic.base import View
from wkhtmltopdf.views import PDFTemplateResponse


class MyPDFView(View):
    template = 'pdf/pdftemplate.html'  # the template

    def get(self, request):
        data = {"mydata": "your data"}  # data that has to be renderd to pdf templete

        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="hello.pdf",
                                       context=data,
                                       show_content_in_browser=False,
                                       cmd_options={'margin-top': 10,
                                                    "zoom": 1,
                                                    "viewport-size": "1366 x 513",
                                                    'javascript-delay': 1000,
                                                    'footer-center': '[page]/[topage]',
                                                    "no-stop-slow-scripts": True},
                                       )
        return response