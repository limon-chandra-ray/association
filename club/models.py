

from django.db import models
from django.conf import settings

# Create your models here.
class ClubIn(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='clubs',blank=True,null=True)
    def __str__(self):
        return self.name



    




class AssociationClub(models.Model):
    club_name = models.CharField(max_length=100,unique=True)
    club_image = models.ImageField(upload_to="club",)
    club_url = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.club_name
    
    
class ClubMember(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    club = models.ForeignKey(AssociationClub,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.member.student_id +"-"+ self.club.club_name 
class Program(models.Model):
    student_id = models.CharField(max_length=39)
    batch_number =models.IntegerField()
    student_name = models.CharField(max_length=150)
    student_nickname=models.CharField(max_length=150,null=True,blank=True)
    club =models.ForeignKey(ClubIn, verbose_name="club name", on_delete=models.CASCADE)
    student_email = models.CharField(max_length=150)
    student_phone = models.CharField(max_length=11)
      
      
    def __str__(self):
        return self.student_id

class WebNetwork(models.Model):
    student_id = models.CharField(max_length=39)
    batch_number =models.IntegerField()
    student_name = models.CharField(max_length=150)
    student_nickname=models.CharField(max_length=150,null=True,blank=True)
    club =models.ForeignKey(ClubIn, verbose_name="club name", on_delete=models.CASCADE)
    student_email = models.CharField(max_length=150)
    student_phone = models.CharField(max_length=11)
      
      
    def __str__(self):
        return self.student_id     

class HardWareHacking(models.Model):
    student_id = models.CharField(max_length=39)
    batch_number =models.IntegerField()
    student_name = models.CharField(max_length=150)
    student_nickname=models.CharField(max_length=150,null=True,blank=True)
    club =models.ForeignKey(ClubIn, verbose_name="club name", on_delete=models.CASCADE)
    student_email = models.CharField(max_length=150)
    student_phone = models.CharField(max_length=11)
      
      
    def __str__(self):
        return self.student_id     

class Animation(models.Model):
    student_id = models.CharField(max_length=39)
    batch_number =models.IntegerField()
    student_name = models.CharField(max_length=150)
    student_nickname=models.CharField(max_length=150,null=True,blank=True)
    club =models.ForeignKey(ClubIn, verbose_name="club name", on_delete=models.CASCADE)
    student_email = models.CharField(max_length=150)
    student_phone = models.CharField(max_length=11)
      
      
    def __str__(self):
        return self.student_id
class Cultaral(models.Model):
    student_id = models.CharField(max_length=39)
    batch_number =models.IntegerField()
    student_name = models.CharField(max_length=150)
    student_nickname=models.CharField(max_length=150,null=True,blank=True)
    club =models.ForeignKey(ClubIn, verbose_name="club name", on_delete=models.CASCADE)
    student_email = models.CharField(max_length=150)
    student_phone = models.CharField(max_length=11)
      
      
    def __str__(self):
        return self.student_id
class SoftwareApp(models.Model):
    student_id = models.CharField(max_length=39)
    batch_number =models.IntegerField()
    student_name = models.CharField(max_length=150)
    student_nickname=models.CharField(max_length=150,null=True,blank=True)
    club =models.ForeignKey(ClubIn, verbose_name="club name", on_delete=models.CASCADE)
    student_email = models.CharField(max_length=150)
    student_phone = models.CharField(max_length=11)
      
      
    def __str__(self):
        return self.student_id