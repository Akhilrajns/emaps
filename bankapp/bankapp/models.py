from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

JOB_STATUS = (
    (1, 'Pending'),
    (2, 'Approved'),
    (3, 'Completed'),
)

APPLICANT_TYPE = (
    (1, 'Pending'),
    (2, 'Approved'),
    (3, 'Completed'),
)

MARTIAL_STATUS = (
    (1, 'Married'),
    (2, 'UnMarried'),
    (3, 'divorce'),
)

NATIONALITY = (
    (1, 'Indian'),
)

SEX = (
    (1, 'Male'),
    (2, 'Female'),
)

KYC_STATUS = (
    (1, 'Approved'),
    (2, 'Pending'),
    (3, 'Rejected'),
)

JOB_TYPE = (
    (1, 'Govt employee'),
    (2, 'Private'),
    (3, 'Self employed'),
)

ANNUAL_INCOME = (
    (1, 'Below 1 lakh'),
    (2, 'Above 1 lakh'),
    (3, 'Above 5 lakh'),
)

ADDRESS_TYPE = (
    (0, 'Select'),
    (1, 'Permenent Address'),
    (2, 'Current Address'),
)

DOC_TYPE = (
    (0, 'Select'),
    (1, 'Pancard'),
    (2, 'UID-Aadhar'),
    (3, 'Passport'),
    (4, 'Voters ID'),
    (5, 'Driving License'),
    (6, 'SSLC'),
    (7, 'Other ID'),
)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
            Creates and saves a User with the given username, email and password.
        """
        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', blank=False, db_index=True, max_length=255, unique=True)
    email = models.EmailField('Email', blank=True, null=True, db_index=True, unique=True)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    is_staff = models.BooleanField('Staff Status', default=False,
                                   help_text='Designates whether the user can log into this admin site.',
                                   db_index=True)
    is_active = models.BooleanField('Active', default=True,
                                    help_text=('Designates whether this user should be treated as '
                                               'active. Deselect this instead of deleting accounts.'), db_index=True)

    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True)
    phone = models.CharField('Phone Number', null=True, blank=True, max_length=15)
    date_of_birth = models.DateField('Date of Birth', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def get_short_name(self):
        """
            Returns the short name for the user.
        """
        return self.full_name


class Pincode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pincode = models.CharField('Pincode', null=False, max_length=10)
    name = models.CharField('Place', max_length=128)

    def __str__(self):
        return str(self.pincode)


class Branch(models.Model):
    name = models.CharField('Branch Name', max_length=128)
    address = models.TextField('Address', max_length=255, null=True, blank=True)
    city = models.CharField('City', max_length=128)
    district = models.CharField('District', max_length=128)
    pincode = models.CharField('Pincode', max_length=6)
    ifsc_code = models.CharField('IFSC code', max_length=12)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.address, self.ifsc_code)


class LoanType(models.Model):
    loan_type = models.CharField('Loan Type', max_length=128)

    class Meta:
        verbose_name = 'Loan type'
        verbose_name_plural = 'Loan Types'

    def __str__(self):
        return str(self.loan_type)        


class LoanDetail(models.Model):
    """docstring for LoanDetails"""
    job_no = models.AutoField('Job No', primary_key=True)
    loan_account_no = models.CharField('Loan account No', blank=True, max_length=128)
    loan_type = models.ForeignKey(LoanType)
    job_status = models.IntegerField('Job Status', choices=JOB_STATUS, default=1, db_index=True)
    applicant_type = models.IntegerField('Applicant type', choices=APPLICANT_TYPE, default=1, db_index=True)
    customer_name = models.CharField('Customer Name', max_length=128)
    father_name = models.CharField('Father Name', max_length=128)
    mother_name = models.CharField('Mother Name', max_length=128)
    spouse_name = models.CharField('Spouse Name', max_length=128)
    martial_status = models.IntegerField('Martial Status', choices=MARTIAL_STATUS, default=1,  db_index=True)
    nationality = models.IntegerField('Nationality', choices=NATIONALITY, default=1, db_index=True)
    resident = models.CharField('Resident', max_length=128)
    dob = models.DateField('Date of birth', null=True, blank=False)
    sex = models.IntegerField('Sex',  choices=SEX, default=1, db_index=True)
    kyc_status = models.IntegerField('KYC Status', choices=KYC_STATUS, default=1, db_index=True)
    job_type = models.IntegerField('Job type', choices=JOB_TYPE, default=1, db_index=True)
    gross_annual_income = models.IntegerField('Job type', choices=ANNUAL_INCOME, default=1, db_index=True)
    political_influence = models.CharField('Political Influenze', max_length=600, null=True, blank=True)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    created_by = models.ForeignKey(User)
    modified_date = models.DateTimeField('Modified Date', auto_now=True)
    branch = models.ForeignKey('Branch')

    class Meta:
        verbose_name = "Loan Detail"
        verbose_name_plural = "Loan Details"

    def __str__(self):
        return self.customer_name


class AddressType(models.Model):
    address_type = models.CharField('Address Type', max_length=128)

    def __str__(self):
        return str(self.address_type)


class LoanUserAddress(models.Model):

    loan = models.ForeignKey(LoanDetail, on_delete=models.CASCADE, related_name="loanuser")
    address_type = models.ForeignKey(AddressType)
    house_name = models.CharField('House/Flat/Name', max_length=128)
    street = models.CharField('Street', max_length=128)
    area = models.CharField('Area/Location', max_length=128)
    landmark = models.CharField('Landmark', blank=True, max_length=128)
    city = models.CharField('city', max_length=128)
    state = models.CharField('State', max_length=128)
    village = models.CharField('Village', blank=True, max_length=128)
    thaluk = models.CharField('Thaluk', blank=True, max_length=128)
    survey_no = models.CharField('Survey Number', blank=True, max_length=128)
    pincode = models.ForeignKey('Pincode')
    latitude = models.CharField('Latitude', blank=True, max_length=128)
    longitude = models.CharField('Longitude', blank=True, max_length=128)
    mark_borders = models.CharField('Mark borders', blank=True, max_length=600)
    telephone = models.CharField('Telephone', max_length=128)
    mobile_primary = models.CharField('Mobile Primary', max_length=128)
    mobile_secondary = models.CharField('Mobile Secondary',blank=True, max_length=128)
    email = models.CharField('Email', blank=True, max_length=128)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True)
    verified = models.BooleanField('Verified', default=False, db_index=True)
    address_verifier = models.ForeignKey(User, null=True, blank=True, related_name='loanuseraddress')

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.house_name

    def save(self, *args, **kwargs):
        try:
            userpincode = Pincode.objects.get(pincode=str(self.pincode))
            self.address_verifier = User.objects.get(pk=userpincode.user_id)
            super(LoanUserAddress , self).save(*args, **kwargs)
        except Exception as e:
            print(e)


class Review(models.Model):
    loan = models.ForeignKey('LoanDetail')
    reviews = models.TextField('Reviews', max_length=255, blank=True)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True)

    def __str__(self):
        return self.reviews


class Document(models.Model):
    loan = models.ForeignKey('LoanDetail')
    document_type = models.IntegerField('Document type', choices=DOC_TYPE, default=0, db_index=True)
    name = models.CharField('Document details', max_length=255, null=True, blank=True)
    document = models.FileField(upload_to='documents/')
    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True)

    def __str__(self):
        return self.name

