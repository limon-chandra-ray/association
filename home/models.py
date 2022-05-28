

from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from club.models import AssociationClub, ClubIn
# Create your models here.
class ClubNotice(models.Model):
      club_name = models.ForeignKey(AssociationClub,on_delete=models.CASCADE)
      club_notice = models.TextField()
      create_date = models.DateTimeField(auto_now_add=True)
      update_date = models.DateTimeField(auto_now=True)
      
      def __str__(self):
          return self.club_name.club_name
      
class Project(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    club = models.ForeignKey(AssociationClub,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    github= models.URLField()
    project_url = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.name+" - "+self.member.user_name
    
    
class ProjectImage(models.Model):
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='project')
    
    def __str__(self):
        return self.project_name.name
    
    
    