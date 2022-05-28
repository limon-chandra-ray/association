from __future__ import annotations
from django.contrib import admin

# Register your models here.
from club.models import AssociationClub,Program,WebNetwork,HardWareHacking,Animation,SoftwareApp,ClubIn,Cultaral,ClubMember
admin.site.register(AssociationClub)
admin.site.register(Program)
admin.site.register(WebNetwork)
admin.site.register(HardWareHacking)
admin.site.register(SoftwareApp)
admin.site.register(Animation)
admin.site.register(ClubIn)
admin.site.register(Cultaral)
admin.site.register(ClubMember)