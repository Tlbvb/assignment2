from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('country',views.country,name='country'),
    path('discover',views.discover,name='discover'),
    path('disease',views.disease,name='disease'),
    path('diseasetype',views.diseasetype,name='diseasetype'),
    path('doctor',views.doctor,name='doctor'),
    path('publicservant',views.publicservant,name='publicservant'),
    path('record',views.record,name='record'),
    path('specialize',views.specialize,name='specialize'),
    path('users',views.users,name='users'),
    #path('Discover',views.discover,)

    path('deletediscover/<str:cname>/<str:disease_code>', views.deletediscover, name='deletediscover'),
    path('deletediseasetype/<int:id>', views.deletediseasetype, name='deletediseasetype'),
    path('deletecountry/<str:cname>', views.deletecountry, name='deletecountry'),
    path('deletedisease/<str:disease_code>', views.deletedisease, name='deletedisease'),
    path('deletedoctor/<str:email>', views.deletedoctor, name='deletedoctor'),
    path('deletepublicservant/<str:email>', views.deletepublicservant, name='deletepublicservant'),
    path('deleterecord/<str:email>/<str:cname>/<str:disease_code>', views.deleterecord, name='deleterecord'),
    path('deletespecialize/<str:email>/<int:disease_type_id>', views.deletespecialize, name='deletespecialize'),
    path('deleteusers/<str:email>', views.deleteusers, name='deleteusers'),

    path('updatecountry/<str:cname>', views.updatecountry, name='updatecountry'),
    path('updatecountry/updaterecord/<str:cname>', views.updatecountryrecord, name='updatecountryrecord'),
    path('register/country',views.registercountry,name='registercountry'),
    path('register/diseasetype',views.registerdiseasetype,name='registerdiseasetype'),
    path('register/disease',views.registerdisease,name='registerdisease'),
    path('register/discover',views.registerdiscover,name='registerdiscover'),
    path('register/user',views.registeruser,name='registeruser'),
    path('register/doctor',views.registerdoctor,name='registerdoctor'),
    path('register/publicservant',views.registerpublicservant,name='registerpublicservant'),
    path('register/specialize',views.registerspecialize,name='registerspecialize'),
    path('register/record',views.registerrecord,name='registerrecord'),

    path('updatediscover<str:cname>,<str:disease_code>', views.updatediscover, name='updatediscover'),
    path('updaterecord<str:cname>,<str:disease_code>', views.updatediscoverrecord, name='updatediscoverrecord'),

    path('updatedisease<str:disease_code>', views.updatedisease, name='updatedisease'),
    path('updaterecord<str:disease_code>', views.updatediseaserecord, name='updatediseaserecord'),

    path('updatecountry/<str:cname>', views.updatecountry, name='updatecountry'),
    path('updaterecord/<str:cname>', views.updatecountryrecord, name='updatecountryrecord'),

    path('updatediseasetype<int:id>', views.updatediseasetype, name='updatediseasetype'),
    path('updaterecord/<int:id>', views.updatediseasetyperecord, name='updatediseasetyperecord'),

    path('updateuser<str:email>', views.updateuser, name='updateuser'),
    path('updateuserrecord/<str:email>', views.updateuserrecord, name='updateuserrecord'),

    path('updatepublicservant<str:email>', views.updatepublicservant, name='updatepublicservant'),
    path('updatepublicrecord/<str:email>', views.updatepublicrecord, name='updatepublicrecord'),

    path('updatedoctor<str:email>', views.updatedoctor, name='updatedoctor'),
    path('updatedoctorrecord/<str:email>', views.updatedoctorrecord, name='updatedoctorrecord'),
    
    path('updatespecialize<int:disease_type><str:email>', views.updatespecialize, name='updatespecialize'),
    path('updatespecializerecord/<int:disease_type><str:email>', views.updatespecializerecord, name='updatespecializerecord'),

    path('updaterecordmod<str:email><str:cname><str:disease_code>', views.updaterecordmodel, name='updaterecprd'),
    path('updaterecrecord<str:email><str:cname><str:disease_code>', views.updaterecrecord, name='updaterecrecord'),


]