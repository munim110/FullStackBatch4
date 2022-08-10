from django.shortcuts import render
from Student.models import Student

# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, 'home/index.html', {'students': students})