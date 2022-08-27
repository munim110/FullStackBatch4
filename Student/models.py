from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student_photos')

    def __str__(self):
        return self.name




# create a teacher model
# the model should have name, age, email, phone, address, photo, salary, subject
# the photo should be uploaded to the media folder