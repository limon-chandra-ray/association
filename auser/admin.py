from django.contrib import admin
from .models import AssociationUser,ProfileImage,ProfileBackgroundImage
# Register your models here.
admin.site.register(AssociationUser)
admin.site.register(ProfileImage)
admin.site.register(ProfileBackgroundImage)