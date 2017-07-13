from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from bankapp.models import LoanDetail, LoanUserAddress, Branch, Review, Document, Pincode, User

class AddressAdmin(admin.TabularInline):
    model = LoanUserAddress
    readonly_fields = ('verified',)
    max_num = 5
    extra = 1
    template = 'template/tabular.html'

class ReviewsAdmin(admin.TabularInline):
    model = Review
    max_num = 50
    extra = 1

class DocumentsAdmin(admin.TabularInline):
    model = Document
    max_num = 10
    extra = 1

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('full_name', 'email', 'username', 'password',)}),
        (_('Status info'), {'fields': ('is_active', 'is_staff')}),
    )

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'ifsc_code')
    search_fields = ('name', 'address', 'ifsc_code')

class PincodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pincode', 'user')


class LoanDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_no', 'job_status', 'applicant_type', 'customer_name')

    fieldsets = (
        (_('Personal info'), {'fields': ('job_no', 'loan_account_no', 'loan_type', 'job_status', 'applicant_type')}),
        (_('Status info'), {'fields': ('customer_name', 'father_name', 'mother_name', 'spouse_name', 'martial_status')}),
        (_('Permissions'), {'fields': ('nationality', 'resident', )}),
        (_('Important dates'), {'fields': ('dob', 'sex', 'kyc_status', 'job_type', 'gross_annual_income', 'political_influence' )}),
        (_('Branch'), {'fields': ('branch',)}),
    )

    inlines = [
        AddressAdmin, DocumentsAdmin, ReviewsAdmin,
    ]
    search_fields = ('job_no', 'applicant_type', 'loan_account_no')

    ordering = ('id', )
    readonly_fields = ('created_date', 'modified_date', )


admin.site.register(LoanDetail, LoanDetailsAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Pincode, PincodeAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_title = 'eMaps Admin'
admin.site.site_header = 'eMaps Admin'