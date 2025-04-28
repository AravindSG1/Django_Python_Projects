from django.db import models

# Create your models here.
class Visitor(models.Model):
    id = models.BigAutoField(primary_key=True,blank=False,null=False)
    category = models.CharField(verbose_name='category',max_length=100)
    name = models.CharField(verbose_name='name',max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(verbose_name='phone_number',max_length=20)
    address = models.CharField(verbose_name='address',max_length=400)
    apartment_number = models.IntegerField(verbose_name="apartment_number")
    floor = models.CharField(verbose_name='floor',max_length=10)
    to_meet = models.CharField(verbose_name='to_meet',max_length=100)
    reason = models.CharField(verbose_name='reason',max_length=100)
    date_time = models.DateTimeField(verbose_name='datetime',auto_now=True)
    status = models.CharField(verbose_name='status',default='In',max_length=3)

class Pass(models.Model):
    id = models.BigAutoField(primary_key=True,blank=False,null=False)
    category = models.CharField(verbose_name='category',max_length=100)
    name = models.CharField(verbose_name='name',max_length=100)
    phone_number = models.CharField(verbose_name='phone_number',max_length=20)
    address = models.CharField(verbose_name='address',max_length=400)
    apartment_number = models.IntegerField(verbose_name="apartment_number")
    floor = models.CharField(verbose_name='floor',max_length=10)
    from_date = models.DateField()
    to_date = models.DateField()
    pass_desc = models.CharField(verbose_name='pass_desc',max_length=100)
    created_datetime = models.DateTimeField(verbose_name='datetime',auto_now=True)