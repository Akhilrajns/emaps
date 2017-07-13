# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-25 07:00
from __future__ import unicode_literals

import bankapp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Username')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(blank=True, max_length=128, null=True)),
                ('is_staff', models.BooleanField(db_index=True, default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff Status')),
                ('is_active', models.BooleanField(db_index=True, default=True, help_text='Designates whether this user should be treated as active. Deselect this instead of deleting accounts.', verbose_name='Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', bankapp.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Branch Name')),
                ('address', models.TextField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('city', models.CharField(max_length=128, verbose_name='City')),
                ('district', models.CharField(max_length=128, verbose_name='District')),
                ('pincode', models.IntegerField(verbose_name='Pincode')),
                ('ifsc_code', models.IntegerField(verbose_name='IFSC code')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Document details')),
                ('document_type', models.IntegerField(choices=[(0, 'Select'), (1, 'Pancard'), (2, 'UID-Aadhar'), (3, 'Passport'), (4, 'Voters ID'), (5, 'Driving License'), (6, 'SSLC'), (7, 'Other ID')], db_index=True, default=0, verbose_name='Document type')),
                ('document', models.FileField(upload_to='documents/')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
            ],
        ),
        migrations.CreateModel(
            name='LoanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.IntegerField(verbose_name='Job No')),
                ('loan_account_no', models.IntegerField(verbose_name='Loan account No')),
                ('loan_type', models.IntegerField(choices=[(1, 'Home loan'), (2, 'Car Loan')], db_index=True, default=1, verbose_name='Loan type')),
                ('job_status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Completed')], db_index=True, default=1, verbose_name='Job Status')),
                ('applicant_type', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Completed')], db_index=True, default=1, verbose_name='Applicant type')),
                ('customer_name', models.CharField(max_length=128, verbose_name='Customer Name')),
                ('father_name', models.CharField(max_length=128, verbose_name='Father Name')),
                ('mother_name', models.CharField(max_length=128, verbose_name='Mother Name')),
                ('spouse_name', models.CharField(max_length=128, verbose_name='Spouse Name')),
                ('martial_status', models.IntegerField(choices=[(1, 'Married'), (2, 'UnMarried'), (3, 'divorce')], db_index=True, default=1, verbose_name='Martial Status')),
                ('nationality', models.IntegerField(choices=[(1, 'Indian')], db_index=True, default=1, verbose_name='Nationality')),
                ('resident', models.CharField(max_length=128, verbose_name='Resident')),
                ('dob', models.DateField(null=True, verbose_name='Date of birth')),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], db_index=True, default=1, verbose_name='Sex')),
                ('kyc_status', models.IntegerField(choices=[(1, 'Approved'), (2, 'Pending'), (3, 'Rejected')], db_index=True, default=1, verbose_name='KYC Status')),
                ('job_type', models.IntegerField(choices=[(1, 'Govt employee'), (2, 'Private'), (3, 'Self employed')], db_index=True, default=1, verbose_name='Job type')),
                ('gross_annual_income', models.IntegerField(choices=[(1, 'Below 1 lakh'), (2, 'Above 1 lakh'), (3, 'Above 5 lakh')], db_index=True, default=1, verbose_name='Job type')),
                ('political_influence', models.CharField(blank=True, max_length=600, null=True, verbose_name='Political Influenze')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('branch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bankapp.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='LoanUserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.IntegerField(choices=[(0, 'Select'), (1, 'Permenent Address'), (2, 'Current Address')], db_index=True, default=0, verbose_name='Address type')),
                ('house_name', models.CharField(max_length=128, verbose_name='House/Flat/Name')),
                ('street', models.CharField(max_length=128, verbose_name='Street')),
                ('area', models.CharField(max_length=128, verbose_name='Area/Location')),
                ('landmark', models.CharField(max_length=128, verbose_name='Landmark')),
                ('city', models.CharField(max_length=128, verbose_name='city')),
                ('state', models.CharField(max_length=128, verbose_name='State')),
                ('village', models.CharField(max_length=128, verbose_name='Village')),
                ('thaluk', models.CharField(max_length=128, verbose_name='Thaluk')),
                ('survey_no', models.CharField(max_length=128, verbose_name='Survey Number')),
                ('latitude', models.CharField(max_length=128, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=128, verbose_name='Longitude')),
                ('telephone', models.CharField(max_length=128, verbose_name='Telephone')),
                ('mobile_primary', models.CharField(max_length=128, verbose_name='Mobile Primary')),
                ('mobile_secondary', models.CharField(max_length=128, verbose_name='Mobile Secondary')),
                ('email', models.CharField(max_length=128, verbose_name='Email')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.LoanDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField(verbose_name='Pincode')),
                ('name', models.CharField(max_length=128, verbose_name='Place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField(blank=True, max_length=255, null=True, verbose_name='Reviews')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.LoanDetail')),
            ],
        ),
        migrations.AddField(
            model_name='loanuseraddress',
            name='pincode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.Pincode'),
        ),
        migrations.AddField(
            model_name='document',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.LoanDetail'),
        ),
    ]
