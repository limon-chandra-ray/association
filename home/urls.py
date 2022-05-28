from unicodedata import name
from django.urls import path
from home import views
urlpatterns = [
      path('',views.home,name="home"),
      # path('association-admin/',views.association,name="association_admin"),
      path('registration/',views.registration,name='registration'),
      path('login/',views.logIn,name='login'),
      path("logout/",views.logOut,name="logout"),
      # Club
      path('programming/',views.coding,name='programming'),
      path('animation/',views.animation,name='animation'),
      path('software-mobile-apps',views.softwaremobileapp,name='softwaremobileapp'),
      path('hardware-hacking',views.ethicalHacking,name='ethicalHacking'),
      path('math',views.math,name='math'),
      path('cultural',views.cultural,name='cultural'),
      path('robotics',views.robotics,name='robotics'),
      path('sports',views.sports,name='sports'),
      path('web-design-development',views.webDesignDevelopment,name='webDesignDevelopment'),
      path('about-us',views.aboutUs,name='aboutUs'),
      path('contact',views.contact,name='contact'),
      path('gallery',views.gallery,name='gallery'),
      path('notice',views.notice,name='notice'),
      path('notice/<int:notice_id>',views.singleNotice,name='notice_id'),
      
      # club Member Profile Details
      path('member/<int:id>/<str:club_name>/<str:std_id>/',views.clubMemberDetails,name="memberDetails"),
      #profile
      path('profile/',views.myprofile,name="myprofile"),
      path('project/',views.myproject,name="myproject"),
      path('add-new-project/',views.addNewProject,name="addNewProject"),
      path('active-club/',views.myClub,name="myClub"),
      path('account-settings/',views.accountSettings,name="accountSettings"),
      path('add-profile-image/',views.addprofileImage,name='addprofileImage'),
      path('add-profile-background-image/',views.addprofileBackgroundImage,name="addprofileBackgroundImage"),
      
]
