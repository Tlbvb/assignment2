from django.db import models

# Create your models here.

class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Discover(models.Model):
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname', blank=True, null=True)
    disease_code = models.ForeignKey('Disease', models.CASCADE, db_column='disease_code', blank=True, null=True)
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    id = models.ForeignKey('Diseasetype', models.CASCADE, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseasetype'


class Doctor(models.Model):
    email = models.OneToOneField('Users', models.CASCADE, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Publicservant(models.Model):
    email = models.OneToOneField('Users', models.CASCADE, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicservant'


class Record(models.Model):
    email = models.ForeignKey(Publicservant, models.CASCADE, db_column='email', blank=True, null=True)
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname', blank=True, null=True)
    disease_code = models.ForeignKey(Disease, models.CASCADE, db_column='disease_code', blank=True, null=True)
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)


class Specialize(models.Model):
    disease_type = models.ForeignKey(Diseasetype, models.CASCADE, blank=True, null=True)
    email = models.ForeignKey(Doctor, models.CASCADE, db_column='email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialize'
        unique_together = (('disease_type', 'email'),)


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
