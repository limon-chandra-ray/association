
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
#Token models use
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class AssociationUserBaseManager(BaseUserManager):
      def create_member(self,user_name,email,full_name,student_id,batch_no,club_admin,linkend_id,password=None):
            
            member = self.model(
                  user_name =user_name,
                  email=self.normalize_email(email),
                  full_name = full_name,
                  student_id=student_id,
                  batch_no=batch_no,
                  linkend_id=linkend_id,
                  club_admin=club_admin,
                  
            )
            member.is_member=True
            member.set_password(password)
            
            member.save()
            return member
      def create_clubAdmin(self,user_name,email,full_name,student_id,batch_no,club_admin,linkend_id,password=None):
            member = self.create_member(
                  user_name =user_name,
                  email=self.normalize_email(email),
                  full_name = full_name,
                  student_id=student_id,
                  batch_no=batch_no,
                  linkend_id=linkend_id,
                  club_admin=club_admin,
                  password=password
            )
            member.is_staff=True
            member.is_member=True
            member.save()
            return member
      
      
      def create_superuser(self,user_name,email,student_id,password=None):
            member = self.create_member(
                  user_name =user_name,
                  email=self.normalize_email(email),
                  full_name = NULL,
                  student_id=student_id,
                  batch_no=NULL,
                  linkend_id=NULL,
                  club_admin=NULL,
                  password=password
            )
            member.is_admin=True
            member.is_staff=True
            member.is_member=True
            member.save()
            return member
            

class AssociationUser(AbstractBaseUser):
      user_name = models.CharField(max_length=150)
      email = models.EmailField(_('email address'))
      full_name = models.CharField(_('full name'),max_length=250,blank=True,null=True)
      student_id =models.CharField(_('student id'),max_length=150,unique=True)
      batch_no =models.CharField(_('batch no'),max_length=40)
      linkend_id = models.URLField(_("linkend id"),null=True,blank=True) 
      club_admin =models.CharField(_('club admin'),null=True,blank=True,max_length=50)
      is_staff = models.BooleanField(default=False)
      is_admin = models.BooleanField(default=False)
      is_member=models.BooleanField(default=True)
      join_date =models.DateTimeField(auto_now_add=True)
      last_login= models.DateTimeField(auto_now=True)
      
      USERNAME_FIELD ='student_id'
      REQUIRED_FIELDS= ['user_name','email',]
      objects= AssociationUserBaseManager()
      def __str__(self):
          return self.student_id+ " - "+ self.batch_no
    
      def has_perm(self,perm,obj=None):
            return True

      def has_module_perms(self,app_label):
            return True
      
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,*args, **kwargs):
      if created:
            Token.objects.create(user=instance)
            
            
            
class ProfileImage(models.Model):
      member =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
      image = models.ImageField(upload_to='profile',default="deafult_user.png")
      
      def __str__(self):
          return self.member.student_id
    
class ProfileBackgroundImage(models.Model):
      member =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
      image = models.ImageField(upload_to='profile',default="water-dropsjpg.jpg")
      
      def __str__(self):
          return self.member.student_id
      
      
      