from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Discover,Disease,Diseasetype,Doctor,Publicservant,Record,Users,Country,Specialize
from django.apps import apps
from django.urls import reverse
from django.template import loader
# Create your views here.

def index(request):
    database_list=['Discover','Disease','Diseasetype','Doctor','Publicservant','Record','Users','Country','Specialize']
    #all_patients=disease.objects.all()
    context={
        'database_list':database_list
    }
    return render(request,'index.html',context)



def deletecountry(request, cname):
  patient = Country.objects.get(cname=cname)
  if Discover.objects.filter(cname=cname).exists():
    disease=Disease.objects.filter(cname=cname)
    for dis in disease:
        dis.delete()
  if Record.objects.filter(cname=cname).exists():
    record=Record.objects.filter(cname=cname)
    for dis in record:
        dis.delete()  
  if Users.objects.filter(cname=cname).exists():
    record=Users.objects.filter(cname=cname)
    for dis in record:
        dis.delete()  
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('country'))

def deletediscover(request, cname,disease_code):
  patient = Discover.objects.get(cname=cname,disease_code=disease_code)
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('discover'))

def deletedisease(request,disease_code):
  patient = Disease.objects.get(disease_code=disease_code)
  if Record.objects.filter(disease_code=disease_code).exists():
    record=Record.objects.filter(disease_code=disease_code)
    for dis in record:
        dis.delete()
  if Discover.objects.filter(disease_code=disease_code).exists():
    rec=Discover.objects.filter(disease_code=disease_code)
    for dis in rec:
        dis.delete()
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('disease'))

def deletediseasetype(request,id):
  patient = Diseasetype.objects.get(id=id)
  if Disease.objects.filter(id=id).exists():
    disease=Disease.objects.filter(id=id)
    for dis in disease:
        dis.delete()
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('diseasetype'))

def deletedoctor(request,email):
  patient = Doctor.objects.get(email=email)
  if Specialize.objects.filter(email=email).exists():
    disease=Specialize.objects.filter(email=email)
    for dis in disease:
        dis.delete()
  if Users.objects.filter(email=email).exists():
    disease=Users.objects.filter(email=email)
    for dis in disease:
        dis.delete()
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('doctor'))

def deletepublicservant(request, email):
  patient = Publicservant.objects.get(email=email)
  if Record.objects.filter(email=email).exists():
    disease=Record.objects.filter(email=email)
    for dis in disease:
        dis.delete()
  if Users.objects.filter(email=email).exists():
    disease=Users.objects.filter(email=email)
    for dis in disease:
        dis.delete()
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('publicservant'))



def deletespecialize(request, email,disease_type_id):
  patient = Specialize.objects.get(email=email,disease_type=disease_type_id)
  patient.delete()
  return HttpResponseRedirect(reverse('specialize'))
  #return render(request,'users')

def deleterecord(request,cname,email,disease_code):
  record=Record.objects.get(cname=cname,email=email,disease_code=disease_code)
  record.delete()
  return HttpResponseRedirect(reverse('record'))

def deleteusers(request, email):
  patient = Users.objects.filter(email=email)
  if Specialize.objects.filter(email=email).exists():
    disease=Specialize.objects.filter(id=id)
    for dis in disease:
        dis.delete()
  if Record.objects.filter(email=email).exists():
    disease=Record.objects.filter(email=email)
    for dis in disease:
        dis.delete()  
  if Doctor.objects.filter(email=email).exists():
    disease=Doctor.objects.filter(email=email)
    for dis in disease:
        dis.delete()
  if Publicservant.objects.filter(email=email).exists():
    disease=Publicservant.objects.filter(email=email)
    for dis in disease:
       dis.delete()
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('users'))


def country(request):
    objects=Country.objects.all()
    return render(request,'country.html',{'objects':objects})

def discover(request):
    objects=Discover.objects.all()
    return render(request,'discover.html',{'objects':objects})

def disease(request):
    objects=Disease.objects.all()
    return render(request,'disease.html',{'objects':objects})

def diseasetype(request):
    objects=Diseasetype.objects.all()
    return render(request,'diseasetype.html',{'objects':objects})

def doctor(request):
    objects=Doctor.objects.all()
    return render(request,'doctor.html',{'objects':objects})

def publicservant(request):
    objects=Publicservant.objects.all()
    return render(request,'publicservant.html',{'objects':objects})

def record(request):
    objects=Record.objects.all()
    return render(request,'record.html',{'objects':objects})

def specialize(request):
    objects=Specialize.objects.all()
    return render(request,'specialize.html',{'objects':objects})

def users(request):
    objects=Users.objects.all()
    return render(request,'users.html',{'objects':objects})


def updatecountry(request, cname):
  country=Country.objects.all()
  patient = Country.objects.get(cname=cname)
  template = loader.get_template('updatecountry.html')
  context = {
    'x': patient,
    'country':country
  }
  return HttpResponse(template.render(context, request))

def updatecountryrecord(request, cname):
  cname = request.POST['cname']
  population = request.POST['population']
  
  
  member = Country.objects.get(cname=cname)
  member.population = population
  member.cname=cname
  
  member.save()
  return HttpResponseRedirect(reverse('country'))

def updatediseasetype(request, id):
  patient = Diseasetype.objects.get(id=id)
  template = loader.get_template('updatediseasetype.html')
  context = {
    'x': patient,
  }
  return HttpResponse(template.render(context, request))



def updatediseasetyperecord(request, id):
  id = request.POST['id']
  description = request.POST['description']
  
  
  member = Diseasetype.objects.get(id=id)
  member.id = id
  member.description=description
  
  member.save()
  return HttpResponseRedirect(reverse('diseasetype'))


def updatediscover(request, cname,disease_code):
  country=Country.objects.all()
  dis_code=Disease.objects.all()
  patient = Discover.objects.get(cname=cname,disease_code=disease_code)
  template = loader.get_template('updatediscover.html')
  context = {
    'x': patient,
    'country':country,
    'dis_code':dis_code
  }
  return HttpResponse(template.render(context, request))

def updatediscoverrecord(request,cname,disease_code):
  cname = request.POST['cname']
  disease_code = request.POST['disease_code']
  first_enc_date=request.POST['first_enc_date']
  
  
  member = Discover.objects.get(cname=cname,disease_code=disease_code)
  member.cname_id=cname
  member.disease_code_id = disease_code
  member.first_enc_date=first_enc_date
  
  member.save()
  return HttpResponseRedirect(reverse('discover'))

def updatedisease(request, disease_code):
  dis_code=Disease.objects.all()
  idd=Diseasetype.objects.all()
  patient = Disease.objects.get(disease_code=disease_code)
  template = loader.get_template('updatedisease.html')
  context = {
    'x': patient,
    'dis_code':dis_code,
    'idd':idd
  }
  return HttpResponse(template.render(context, request))

def updatediseaserecord(request, disease_code):
  disease_code = request.POST['disease_code']
  pathogen = request.POST['pathogen']
  description=request.POST['description']
  id=request.POST['id']
  
  
  member = Disease.objects.get(disease_code=disease_code)
  member.disease_code=disease_code
  member.pathogen = pathogen
  member.description=description
  member.id_id=id
  
  member.save()
  return HttpResponseRedirect(reverse('disease'))

def updateuser(request, email):
  country=Country.objects.all()
  patient = Users.objects.get(email=email)
  template = loader.get_template('updateuser.html')
  context = {
    'x': patient,
    'country':country
  }
  return HttpResponse(template.render(context, request))

def updateuserrecord(request, email):
  email = request.POST['email']
  name = request.POST['name']
  surname=request.POST['surname']
  cname=request.POST['country']
  salary=request.POST['salary']
  phone=request.POST['phone']
  
  
  member = Users.objects.get(email=email)
  member.email=email
  member.name = name
  member.surname=surname
  member.cname_id=cname
  member.salary=salary
  member.phone=phone
  
  member.save()
  return HttpResponseRedirect(reverse('users'))


def updatepublicservant(request, email):
  patient = Publicservant.objects.get(email=email)
  template = loader.get_template('updatepublicservant.html')
  context = {
    'x': patient,
    'email':email
  }
  return HttpResponse(template.render(context, request))

def updatepublicrecord(request, email):
  email = request.POST['email']
  department=request.POST['department']
  
  
  member = Publicservant.objects.get(email=email)
  member.email_id=email
  member.department=department
  
  member.save()
  return HttpResponseRedirect(reverse('publicservant'))

def updatedoctor(request, email):
  patient = Doctor.objects.get(email=email)
  template = loader.get_template('updatedoctor.html')
  context = {
    'x': patient,
  }
  return HttpResponse(template.render(context, request))

def updatedoctorrecord(request, email):
  email = request.POST['email']
  degree=request.POST['degree']
  
  
  member = Doctor.objects.get(email=email)
  member.email_id=email
  member.degree=degree
  
  member.save()
  return HttpResponseRedirect(reverse('doctor'))

def updaterecordmodel(request, email,cname,disease_code):
  patient = Record.objects.get(email_id=email,cname_id=cname,disease_code_id=disease_code)
  template = loader.get_template('updaterecord.html')
  context = {
    'x': patient,
  }
  return HttpResponse(template.render(context, request))

def updaterecrecord(request, email):
  email = request.POST['email']
  cname=request.POST['cname']
  disease_code=request.POST['disease_code']
  total_deeaths=request.POST['total_deaths']
  total_patients=request.POST['total patients']
  
  
  member = Record.objects.get(email=email,cname=cname,disease_code=disease_code)
  member.email_id=email
  member.cname=cname
  member.disease_code=disease_code
  member.total_deaths=total_deeaths
  member.total_patients=total_patients
  
  member.save()
  return HttpResponseRedirect(reverse('record'))

def updatespecialize(request, disease_type,email):
  dis_type=Diseasetype.objects.all()
  patient = Specialize.objects.get(email_id=email,disease_type_id=disease_type)
  template = loader.get_template('updatespecialize.html')
  context = {
    'x': patient,
    'dis_type':dis_type
  }
  return HttpResponse(template.render(context, request))

def updatespecializerecord(request, disease_type,email):
  email = request.POST['email']
  disease_type=request.POST['disease_type']
  
  old_dis=request.get_full_path().disease_type
  old_email=request.email
  member = Specialize.objects.get(email_id=old_email,disease_type_id=old_dis)
  member.delete()
  member=Specialize(disease_type_id=disease_type,email_id=email)
  member.save()
  return HttpResponseRedirect(reverse('specialize'))

def registercountry(request):
  if request.method=='POST':
      cname=request.POST.get('cname')
      #populatiom=request.POST.get('population')
      population=request.POST.get('population')
      patient=Country(cname=cname,population=population)
      if not Country.objects.filter(cname=cname).exists():
        patient.save()
        return redirect('country')
  return render(request,'registercountry.html')

def registerdiseasetype(request):
  if request.method=='POST':
    id=request.POST.get('id')
    descriptiion=request.POST.get('description')
    diseasetype=Diseasetype(id=id,description=descriptiion)
    if not Diseasetype.objects.filter(id=id).exists():
      diseasetype.save()
      return redirect('diseasetype')
  return render(request,'registerdiseasetype.html')

def registerdisease(request):
  dis_type=Diseasetype.objects.all()
  context={
      'dis_type':dis_type
    }
  if request.method=='POST':
    id=request.POST.get('id')
    descriptiion=request.POST.get('description')
    disease_code=request.POST.get('disease_code')
    pathogen=request.POST.get('pathogen')
    if Diseasetype.objects.filter(id=id).exists():
      disease=Disease(id_id=id,description=descriptiion,disease_code=disease_code,pathogen=pathogen)
      if not Disease.objects.filter(disease_code=disease_code).exists():
        disease.save()
        return redirect('disease')
    else:
      return redirect('registerdisease')

  return render(request,'registerdisease.html',context)

def registerdiscover(request):
  country=Country.objects.all()
  disease_code=Disease.objects.all()
  context={
    'country':country,
    'disease_code':disease_code
  }
  if request.method=='POST':
    cname=request.POST.get('cname')
    disease_code=request.POST.get('disease_code')
    first_enc_date=request.POST.get('first_enc_date')
    if Country.objects.filter(cname=cname).exists() and Disease.objects.filter(disease_code=disease_code).exists():
      discover=Discover(cname_id=cname,disease_code_id=disease_code,first_enc_date=first_enc_date)
      if not Discover.objects.filter(disease_code_id=disease_code,cname_id=cname).exists():
        discover.save()
        return redirect('discover')
    else:
      return redirect('registerdiscover')
  return render(request,'registerdiscover.html',context)

def registeruser(request):
  country=Country.objects.all()
  context={
    'country':country
  }
  if request.method=='POST':
    cname=request.POST.get('cname')
    email=request.POST.get('email')
    name=request.POST.get('name')
    surname=request.POST.get('surname')
    salary=request.POST.get('salary')
    phone=request.POST.get('phone')
    if Country.objects.filter(cname=cname).exists():
      user=Users(cname_id=cname,email=email,name=name,surname=surname,salary=salary,phone=phone)
      if not Users.objects.filter(email=email).exists():
        user.save()
        return redirect('users')
    else:
      return redirect('registeruser')
  return render(request,'registeruser.html',context)

def registerdoctor(request):
  emailus=Users.objects.raw('SELECT DISTINCT users.email FROM publicservant,users,doctor WHERE users.email!=publicservant.email AND users.email!=doctor.email')
  #exclude(Publicservant.objects.filter(email=email))
  context={
    'email':emailus
  }
  if request.method=='POST':
    email=request.POST.get('email')
    degree=request.POST.get('degree')
    if  Users.objects.filter(email=email).exists():
      doctor=Doctor(email_id=email,degree=degree)
      if not Doctor.objects.filter(email_id=email).exists():
        doctor.save()
        return redirect('doctor')
    else:
      return redirect('registerdoctor')
  return render(request,'registerdoctor.html',context)

def registerspecialize(request):
  id=Diseasetype.objects.all()
  email=Doctor.objects.all()
  context={
    'id':id,
    'email':email
  }
  if request.method=='POST':
    email=request.POST.get('email')
    disease_type=request.POST.get('disease_type')
    if  Doctor.objects.filter(email=email).exists() and Diseasetype.objects.filter(disease_type=disease_type).exists():
      specialize=Specialize(email_id=email,disease_type_id=disease_type)
      if not Specialize.objects.filter(email_id=email).exists():
        specialize.save()
        return redirect('specialize')
    else:
      return redirect('registerspecialize')
  return render(request,'registerspecialize.html',context)                

def registerpublicservant(request):
  emailus=Users.objects.raw('SELECT DISTINCT users.email FROM publicservant,users,doctor WHERE users.email!=publicservant.email AND users.email!=doctor.email')
  #exclude(Publicservant.objects.filter(email=email))
  context={
    'email':emailus
  }
  if request.method=='POST':
    email=request.POST.get('email')
    department=request.POST.get('department')
    if  Users.objects.filter(email=email).exists():
      publicservant=Publicservant(email_id=email,department=department)
      if not Publicservant.objects.filter(email_id=email).exists():
        publicservant.save()
        return redirect('publicservant')
    else:
      return redirect('registerpublicservant')
  return render(request,'registerpublicservant.html',context)

def registerrecord(request):
  cname=Country.objects.all()
  email=Publicservant.objects.all()
  disease_code=Disease.objects.all()
  context={
    'cname':cname,
    'email':email,
    'disease_code':disease_code
  }
  if request.method=='POST':
    email=request.POST.get('email')
    cname=request.POST.get('cname')
    disease_code=request.POST.get('disease_code')
    total_deaths=request.POST.get('total_deaths')
    total_patients=request.POST.get('total_patients')
    if  Publicservant.objects.filter(email=email).exists() and Disease.objects.filter(disease_code=disease_code).exists() and Country.objects.filter(cname=cname).exists():
      record=Record(email_id=email,disease_code_id=disease_code,cname_id=cname,total_deaths=total_deaths,total_patients=total_patients)
      if not Record.objects.filter(email_id=email,cname_id=cname,disease_code_id=disease_code).exists():
        record.save()
        return redirect('record')
    else:
      return redirect('registerrecord')
  return render(request,'registerrecord.html',context)


