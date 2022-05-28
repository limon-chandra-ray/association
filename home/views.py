
from asyncio.windows_events import NULL
from json import load
from multiprocessing import context
import re
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from auser.models import AssociationUser,ProfileImage,ProfileBackgroundImage
from django.contrib.auth.models import auth
from club.models import AssociationClub,ClubIn,ClubMember,Program,WebNetwork,HardWareHacking,SoftwareApp,Cultaral,Animation
from home.models import ClubNotice, ProjectImage,Project

# Create your views here.
def home(request):
      associtaion_club = AssociationClub.objects.all()
      club_notice = ClubNotice.objects.all().order_by('create_date').reverse()
      context={
            'associtaion_club' : associtaion_club,
            'club_notice':club_notice
      }
      return render(request,'home.html',context)

def coding(request):
      club_member = ClubMember.objects.filter(club__id =2)
      
      profile_image = []
      background_image=[]
      for member in club_member:
            if ProfileImage.objects.filter(member_id = member.member.id):
                  profile_image.append(ProfileImage.objects.filter(member_id = member.member.id).order_by('-id')[0])
      for member in club_member:
            if ProfileBackgroundImage.objects.filter(member_id = member.member.id):
                  background_image.append(ProfileBackgroundImage.objects.filter(member_id = member.member.id).order_by('-id')[0])    
            
            # profile_image.append(ProfileImage.objects.filter(member__id =member.id).order_by('-id')[0])
      print(profile_image)
      context={
            'club_member':club_member,
            'profile_image':profile_image,
            'background_image':background_image
      }
      return render(request,'pages/clubs/programming.html',context)

def animation(request):
      club_member = ClubMember.objects.filter(club__id =6)
      
      profile_image = []
      background_image=[]
      for member in club_member:
            if ProfileImage.objects.filter(member_id = member.member.id):
                  profile_image.append(ProfileImage.objects.filter(member_id = member.member.id).order_by('-id')[0])
      for member in club_member:
            if ProfileBackgroundImage.objects.filter(member_id = member.member.id):
                  background_image.append(ProfileBackgroundImage.objects.filter(member_id = member.member.id).order_by('-id')[0])    
      context={
            'club_member':club_member,
            'profile_image':profile_image,
            'background_image':background_image
      }
      return render(request,'pages/clubs/animation.html',context)
def softwaremobileapp(request):
      club_member = ClubMember.objects.filter(club__id =6)
      
      profile_image = []
      background_image=[]
      for member in club_member:
            if ProfileImage.objects.filter(member_id = member.member.id):
                  profile_image.append(ProfileImage.objects.filter(member_id = member.member.id).order_by('-id')[0])
      for member in club_member:
            if ProfileBackgroundImage.objects.filter(member_id = member.member.id):
                  background_image.append(ProfileBackgroundImage.objects.filter(member_id = member.member.id).order_by('-id')[0])    
            
            # profile_image.append(ProfileImage.objects.filter(member__id =member.id).order_by('-id')[0])
      # print(profile_image)
      context={
            'club_member':club_member,
            'profile_image':profile_image,
            'background_image':background_image
      }
      
      return render(request,'pages/clubs/software&mobile_app.html',context)

def ethicalHacking(request):
      club_member = ClubMember.objects.filter(club__id =4)
      
      profile_image = []
      background_image=[]
      for member in club_member:
            if ProfileImage.objects.filter(member_id = member.member.id):
                  profile_image.append(ProfileImage.objects.filter(member_id = member.member.id).order_by('-id')[0])
      for member in club_member:
            if ProfileBackgroundImage.objects.filter(member_id = member.member.id):
                  background_image.append(ProfileBackgroundImage.objects.filter(member_id = member.member.id).order_by('-id')[0])    
      context={
            'club_member':club_member,
            'profile_image':profile_image,
            'background_image':background_image
      }
      return render(request,'pages/clubs/ethical-hacking.html',context)
def math(request):
      club_member = ClubMember.objects.filter(club__id =7)
      
      profile_image = []
      background_image=[]
      for member in club_member:
            if ProfileImage.objects.filter(member_id = member.member.id):
                  profile_image.append(ProfileImage.objects.filter(member_id = member.member.id).order_by('-id')[0])
      for member in club_member:
            if ProfileBackgroundImage.objects.filter(member_id = member.member.id):
                  background_image.append(ProfileBackgroundImage.objects.filter(member_id = member.member.id).order_by('-id')[0])    
      context={
            'club_member':club_member,
            'profile_image':profile_image,
            'background_image':background_image
      }
      return render(request,'pages/clubs/math.html')
def cultural(request):
      club_member = ClubMember.objects.filter(club__id =5)
      
      profile_image = []
      background_image=[]
      for member in club_member:
            if ProfileImage.objects.filter(member_id = member.member.id):
                  profile_image.append(ProfileImage.objects.filter(member_id = member.member.id).order_by('-id')[0])
      for member in club_member:
            if ProfileBackgroundImage.objects.filter(member_id = member.member.id):
                  background_image.append(ProfileBackgroundImage.objects.filter(member_id = member.member.id).order_by('-id')[0])    
      context={
            'club_member':club_member,
            'profile_image':profile_image,
            'background_image':background_image
      }
      return render(request,'pages/clubs/cultural.html',context)
def robotics(request):
      return render(request,'pages/clubs/robotics.html')
def sports(request):
      return render(request,'pages/clubs/sports.html')
def webDesignDevelopment(request):
      club_member = ClubMember.objects.filter(club__id =1)
      
      profile_image = []
      background_image=[]
      for member in club_member:
            if ProfileImage.objects.filter(member_id = member.member.id):
                  profile_image.append(ProfileImage.objects.filter(member_id = member.member.id).order_by('-id')[0])
      for member in club_member:
            if ProfileBackgroundImage.objects.filter(member_id = member.member.id):
                  background_image.append(ProfileBackgroundImage.objects.filter(member_id = member.member.id).order_by('-id')[0])    
            
            # profile_image.append(ProfileImage.objects.filter(member__id =member.id).order_by('-id')[0])
      # print(profile_image)
      context={
            'club_member':club_member,
            'profile_image':profile_image,
            'background_image':background_image
      }
      return render(request,'pages/clubs/web-design&Development.html',context)

def aboutUs(request):
      return render(request,'pages/aboutus.html')
def contact(request):
      return render(request,'pages/contact.html')
def gallery(request):
      return render(request,'pages/gallery.html')
def notice(request):
      return render(request,'notice.html')
def singleNotice(request,notice_id):
      get_notice = ClubNotice.objects.get(id=notice_id)
      context={
            'notice':get_notice
      }
      return render(request,'notice.html',context)



def registration(request):
      clubs = AssociationClub.objects.all()
      if request.method == "POST":
            stdId = request.POST['studentId']
            stdName = request.POST['name']
            stdUserName = request.POST['user_name']
            stdemail = request.POST['email']
            stdsocialmedia = NULL
            stdbatch = request.POST['batch']
            reclubs=request.POST.getlist('recommendationClub')
            password1 =request.POST['password1']
            password2 = request.POST['password1']
            members = AssociationUser.objects.filter(student_id =stdId)
            countmember = members.count()
            matchCLub = []
            for i in reclubs:
                  club = AssociationClub.objects.get(club_name=i)
                  matchCLub.append(club.id)
            # for j in matchCLub:
            #       print(j['name'])
            print(matchCLub)
            
            print("Count " +str(countmember) )
            if countmember != 0:
                  print("All ready signup")
            
            elif password1 and password2 and password2 == password1 :
                  member = AssociationUser.objects.create_member(
                        user_name =stdUserName,
                        email=stdemail,
                        full_name = stdName,
                        student_id=stdId,
                        batch_no=str(stdbatch),
                        linkend_id=stdsocialmedia,
                        club_admin=NULL,
                        password=password2   
                  )
                  member.save()
                  
                  
                  profile= ProfileImage()
                  profile.member = member
                  
                  profile.save()
                  backgroundprofile= ProfileBackgroundImage()
                  backgroundprofile.member = member
                  
                  backgroundprofile.save()
                  
                  for cl in matchCLub:
                        club_member = ClubMember()
                        club_member.member = member
                        club_member.club = AssociationClub.objects.get(id=cl)
                        club_member.save()
                  
                  return HttpResponseRedirect('/')
            else:
                  print('password not match')

            
      
      
      
      
      context={
            'clubs':clubs,
            
      }
      return render(request,'registration.html',context)

def logIn(request):
      if request.method =="POST":
            student_id = request.POST['student_Id']
            password = request.POST['password']
            
            current_user=auth.authenticate(username = student_id,password = password)
            if current_user:
                  auth.login(request,current_user)
                  if current_user.is_member:

                        return redirect('/')
                  # elif current_user.is_superuser and current_user.is_staff :

                  #       return redirect('/user-admin')      
                  # else:
                  #       return redirect('/')
            else:
                  return redirect('/registration')
            
def logOut(request):
      auth.logout(request)
      return redirect('/')




#club Member Profile Details

def clubMemberDetails(request,id,club_name,std_id):
      profile = AssociationUser.objects.get(id = id)
      profile_image=[]
      if ProfileImage.objects.filter(member_id =id):
            profile_image.append( ProfileImage.objects.filter(member_id =id).order_by('-id')[0])
      profile_background_image=[]
      if ProfileBackgroundImage.objects.filter(member_id =id):
            profile_background_image.append( ProfileBackgroundImage.objects.filter(member_id =id).order_by('-id')[0])
            
            
      project =Project.objects.filter(member__id=id,club__club_name=club_name)
      project_image = ProjectImage.objects.filter(project_name__member__id = id)
      context={
            'profile':profile,
            'project':project,
            'project_image':project_image,
            'profile_image':profile_image,
            'profile_background_image':profile_background_image
            
            
      }
      return render(request,'profile_details.html',context)


#Account Views.py

def myprofile(request):
      profile_image=[]
      if ProfileImage.objects.filter(member__id =request.user.id):
            profile_image.append(ProfileImage.objects.filter(member__id =request.user.id).order_by('-id')[0])
            
      background_image=[]
      if ProfileBackgroundImage.objects.filter(member__id =request.user.id):
            background_image.append(ProfileBackgroundImage.objects.filter(member__id =request.user.id).order_by('-id')[0]) 
            
      context={
           'background_image':background_image, 
           'profile_image':profile_image,
      }
      
      return render(request,'account/my_account.html',context)

def myproject(request):
      project = Project.objects.filter(member__id=request.user.id)
      project_image = ProjectImage.objects.filter(project_name__member__id=request.user.id)
      context={
            'project':project,
            'projectImage':project_image
            
      }
      return render(request,'account/my_project.html',context)
def myClub(request):
      myclub =ClubMember.objects.filter(member__student_id= request.user.student_id)
      context={
            'myclub':myclub
      }
      return render(request,'account/my_club.html',context)
def addNewProject(request):
      clubs = AssociationClub.objects.all()
      
      
      if request.method == "POST":
            name = request.POST['projectName']
            club = request.POST['selectedClub']
            github = request.POST['githublink']
            domain = request.POST['domainName']
            image1=request.FILES['image1']
            image2=request.FILES['image2']
            image3=request.FILES['image3']
            image4=request.FILES['image4']
            images =[image1,image2,image3,image4]
            print(images)
            project = Project.objects.create(
                  member = AssociationUser.objects.get(id=request.user.id),
                  club = AssociationClub.objects.get(club_name=club),
                  name = name,
                  github=github,
                  project_url = domain
            )
            project.save()
            for image in images:
                  projectImage = ProjectImage(project_name=project,
                  image=image)
                  projectImage.save()
            return redirect('/project')
      
      context={
            'clubs':clubs
      }
      return render(request,'account/add_new_project.html',context)
def accountSettings(request):
      return render(request,'account/account_settings.html')
def addprofileImage(request):
      if request.method =="POST":
            image = request.FILES['profile_image']
            
            profile_image = ProfileImage(
                  member = AssociationUser.objects.get(id = request.user.id),
                  image= image
            )
            profile_image.save()
            return HttpResponseRedirect(redirect_to='/profile')
def addprofileBackgroundImage(request):
      if request.method =="POST":
            image = request.FILES['profile_background_image']
            
            profile_image = ProfileBackgroundImage(
                  member = AssociationUser.objects.get(id = request.user.id),
                  image= image
            )
            profile_image.save() 
            return HttpResponseRedirect(redirect_to='/profile')           
            
# def association(request):
#       clubs = ClubIn.objects.all()
#       if request.method == "POST":
#             stdId = request.POST['studentId']
#             stdName = request.POST['name']
#             stdUserName = request.POST['user_name']
#             stdemail = request.POST['email']
#             stdPhone = request.POST['phone']
#             stdbatch = request.POST['batch']
            
#             reclubs=request.POST.getlist('recommendationClub')
            
#             for reclub in reclubs:
#                   if reclub == "Program":
#                         program_data1= Program.objects.create(student_id= stdId,
#                                                             batch_number=stdbatch,student_name=stdName,
#                                                             student_nickname=stdUserName,
#                                                             club= ClubIn.objects.get(name="Program"),
#                                                             student_email=stdemail,
#                                                             student_phone=stdPhone)
#                         program_data1.save()
#                   elif reclub == "Web Design & Development":
#                         program_data2= WebNetwork.objects.create(student_id= stdId,
#                                                                 batch_number=stdbatch,
#                                                                 student_name=stdName,
#                                                                 student_nickname=stdUserName,
#                                                                 club= ClubIn.objects.get(name="Web Design & Development"),
#                                                                 student_email=stdemail,
#                                                                 student_phone=stdPhone)
#                         program_data2.save()
                  
#                   elif reclub == "Networking":
#                         program_data3= WebNetwork.objects.create(student_id= stdId,
#                                                              batch_number=stdbatch,
#                                                              student_name=stdName,
#                                                              student_nickname=stdUserName,
#                                                              club= ClubIn.objects.get(name="Networking"),
#                                                              student_email=stdemail,
#                                                              student_phone=stdPhone)
#                         program_data3.save()
#                   elif reclub == "Software & Mobile Application":
#                         program_data4= SoftwareApp.objects.create(student_id= stdId,
#                                                              batch_number=stdbatch,
#                                                              student_name=stdName,
#                                                              student_nickname=stdUserName,
#                                                              club=ClubIn.objects.get(name="Software & Mobile Application"),
#                                                              student_email=stdemail,
#                                                              student_phone=stdPhone)
#                         program_data4.save() 
#                   elif reclub == "Ethical Hacking":
#                         program_data5= HardWareHacking.objects.create(student_id= stdId,
#                                                              batch_number=stdbatch,
#                                                              student_name=stdName,
#                                                              student_nickname=stdUserName,
#                                                              club=ClubIn.objects.get(name="Ethical Hacking"),
#                                                              student_email=stdemail,
#                                                              student_phone=stdPhone)
#                         program_data5.save() 
#                   elif reclub == "Robotics":
#                         program_data6= HardWareHacking.objects.create(student_id= stdId,
#                                                              batch_number=stdbatch,
#                                                              student_name=stdName,
#                                                              student_nickname=stdUserName,
#                                                              club= ClubIn.objects.get(name="Robotics"),
#                                                              student_email=stdemail,
#                                                              student_phone=stdPhone)
#                         program_data6.save() 
#                   elif reclub == "Sports":
#                         program_data7= Cultaral.objects.create(student_id= stdId,
#                                                              batch_number=stdbatch,
#                                                              student_name=stdName,
#                                                              student_nickname=stdUserName,
#                                                              club= ClubIn.objects.get(name="Sports"),
#                                                              student_email=stdemail,
#                                                              student_phone=stdPhone)
#                         program_data7.save() 
#                   elif reclub == "Cultural":
#                         program_data8= Cultaral.objects.create(student_id= stdId,
#                                                              batch_number=stdbatch,
#                                                              student_name=stdName,
#                                                              student_nickname=stdUserName,
#                                                              club= ClubIn.objects.get(name="Cultural"),
#                                                              student_email=stdemail,
#                                                              student_phone=stdPhone)
#                         program_data8.save() 
#                   elif reclub == "Animation":
#                         program_data9= Animation.objects.create(student_id= stdId,
#                                                              batch_number=stdbatch,
#                                                              student_name=stdName,
#                                                              student_nickname=stdUserName,
#                                                              club= ClubIn.objects.get(name="Animation"),
#                                                              student_email=stdemail,
                         
#                                                             student_phone=stdPhone)
#                         program_data9.save() 
                 
                  
#             return HttpResponseRedirect("/")
            

      
      
      
      
#       context={
#             'clubs':clubs
#       }
#       return render(request,'association.html',context)
            


      