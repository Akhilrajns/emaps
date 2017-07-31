from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from bankapp.models import LoanDetail, LoanUserAddress, Branch, Review, Document, Pincode, User, AddressType, LoanType

class AddressAdmin(admin.TabularInline):
    model = LoanUserAddress
    readonly_fields = ('verified', 'address_verifier', 'latitude', 'longitude', 'mark_borders')
    max_num = 10
    extra = 0
    min_num = 1
    #template = 'template/tabular.html'

class ReviewsAdmin(admin.TabularInline):
    model = Review
    max_num = 50
    extra = 0

class DocumentsAdmin(admin.TabularInline):
    model = Document
    max_num = 10
    extra = 0
    min_num = 1

class PincodeAdmin(admin.TabularInline):
    model = Pincode
    max_num = 100
    extra = 0
    min_num = 0

class AppUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ('id', 'username', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        (_('Personal info'), {'fields': ('full_name', 'phone', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
        (_('Important dates'), {'fields': ('last_login', 'created_date', 'modified_date', )})
    )
    search_fields = ('full_name', 'email', )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', )
        }),
    )

    inlines = [
        PincodeAdmin
    ]

    ordering = ('email', )
    readonly_fields = ('created_date', 'modified_date', )

# class UserAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'username', 'password')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
#     )

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'ifsc_code')
    search_fields = ('name', 'address', 'ifsc_code')

class PincodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pincode', 'user')


class LoanDetailsAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'job_no', 'loan_account_no', 'job_status', 'applicant_type')

    fieldsets = (
        (_('Personal info'), {'fields': ('job_no', 'loan_account_no', 'loan_type', 'job_status', 'applicant_type')}),
        (_('Status info'), {'fields': ('customer_name', 'father_name', 'mother_name', 'spouse_name', 'martial_status')}),
        (_('Permissions'), {'fields': ('nationality', 'resident', 'created_by')}),
        (_('Important datas'), {'fields': ('dob', 'sex', 'kyc_status', 'job_type', 'gross_annual_income', 'political_influence' )}),
        (_('Branch'), {'fields': ('branch',)}),
    )

    inlines = [
        AddressAdmin, DocumentsAdmin, ReviewsAdmin,
    ]
    search_fields = ('job_no', 'applicant_type', 'loan_account_no')

    ordering = ('job_no', )
    readonly_fields = ('created_date', 'modified_date', 'job_no', 'created_by')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('address_type', 'house_name', 'street', 'area', 'address_verifier', 'verified')

    fieldsets = (
        (_('Loan Linked to '), {'fields': ('loan',)}),
        (_('Address Verified by '), {'fields': ('address_verifier',)}),
        (_('Address'), {'fields': ('address_type', 'house_name', 'street', 'area', 'landmark')}),
        (_('Location'), {'fields': ('city', 'state', 'village', 'thaluk', 'survey_no', 'pincode')}),
        (_('Map cordinates'), {'fields': ('latitude', 'longitude', 'mark_borders')}),
        (_('Contact details'), {'fields': ('telephone', 'mobile_primary', 'mobile_secondary', 'email',)}),
    )

    readonly_fields = ('address_verifier', 'verified', 'latitude', 'longitude', 'mark_borders')


class AddressTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'address_type',)   


class LoanTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_type',)    


admin.site.register(LoanType, LoanTypeAdmin)
admin.site.register(AddressType, AddressTypeAdmin)
admin.site.register(LoanDetail, LoanDetailsAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Pincode, PincodeAdmin)
admin.site.register(User, AppUserAdmin)
admin.site.register(LoanUserAddress, UserAddressAdmin)
admin.site.site_title = 'eMaps Admin'
admin.site.site_header = 'eMaps Admin'