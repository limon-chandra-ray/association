from xml.etree.ElementInclude import include
from django.urls import path,include
from associationapi import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router= routers.DefaultRouter()
router.register(r'club', views.ClubView)
router.register(r'members-of-coder',views.ProgrammerView)
router.register(r'members-of-web-and-network',views.WebNetworkView)
router.register(r'association-club', views.AssociationClubView)
router.register(r'members-of-hardware-ethical-hacking', views.HardWareHackingView)
router.register(r'members-of-software-and-mobile-apps',views.SoftwareAppView)
router.register(r'members-of-sport-cultural',views.CultaralView)
router.register(r'members-of-animation', views.AnimationView)
router.register(r'club-members', views.ClubMemberView)
router.register(r'association-user', views.AssociationUserView)

urlpatterns = [
    path('',include(router.urls)),
    # path('registration/',views.RegistrationNow.as_view()),
    path('registration/',views.registration_view,name="registration"),
    path('login/',obtain_auth_token,name="name")
]
