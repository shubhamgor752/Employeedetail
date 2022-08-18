from django.db import models

# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)







class Company(models.Model):
    cName = models.CharField(primary_key='true',max_length=50,unique='true')
    cEmail = models.EmailField()
    cLogo = models.ImageField(upload_to="images", blank=True)
    cUrl = models.CharField(max_length=50)
    class Meta:
        db_table = "company"

class Employee(models.Model):
    eFname = models.CharField(primary_key='true',max_length=50,unique='true')
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"
    

    


