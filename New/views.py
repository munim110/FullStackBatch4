from django.http import HttpResponse
from django.shortcuts import render
from Student.models import Student
from django.db import connection

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        type
        print(name, age, email, phone, address)
        print(photo.url)
        student = Student(name=name, age=age, email=email, phone=phone, address=address, photo=photo)
        student.save()
        students = Student.objects.all()
        return render(request, 'home/index.html', {'students': students})
    else:
        students = Student.objects.all()
        return render(request, 'home/index.html', {'students': students})