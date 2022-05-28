
# Authentication system
from asyncio.windows_events import NULL
from lib2to3.pgen2 import token
import re
from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
#End Authentication system
from django import views
from django.shortcuts import render
from rest_framework import viewsets
from club.models import ClubIn,Program,ClubMember,WebNetwork,AssociationClub,HardWareHacking,SoftwareApp,Cultaral,Animation
from .serializers import AnimationSerializer,AssociationUserSerializer, ClubSerializer,ProgrammingSerializer,WebNetworkSerializer,AssociationClubSerializer
from .serializers import HardWareHackingSerializer,ClubMemberSerializer,SoftwareAppSerializer,CultaralSerializer,AssociationClubSerializer
# Create your views here.
from auser.models import AssociationUser

# class RegistrationNow(APIView):
#       def post(self,request):
#             serializers = RegistrationSerializer(data=request.data)
#             if(serializers.is_valid()):
#                   serializers.save()
#                   return Response({'error':False,"message":'Your Registretion Complite','data':serializers.data})
#             return Response({'error':True,"message":'Your Registretion not complite'})
@api_view(['POST'])
def registration_view(requset):
      
      if requset.method == "POST":
            serializer = RegistrationSerializer(data=requset.data)
            data={}
            if serializer.is_valid():
                  member = serializer.save()
                  data['response'] = "Successfully registered a new user."
                  data['user_name']=member.user_name
                  data['email'] = member.email
                  data['full_name'] = member.full_name
                  data['student_id']=member.student_id
                  data['batch_no'] = member.batch_no
                  data['linkend_id'] = member.linkend_id
                  data['club_admin'] = NULL
                  token = Token.objects.get(user=member).key
                  data['token'] =token
            else:
                  data=serializer.errors
            return Response(data)

class AssociationUserView(viewsets.ModelViewSet):
      queryset = AssociationUser.objects.all()
      serializer_class = AssociationUserSerializer


class AssociationClubView(viewsets.ModelViewSet):
      queryset = AssociationClub.objects.all()
      serializer_class = AssociationClubSerializer

class ClubView(viewsets.ModelViewSet):
      queryset = ClubIn.objects.all()
      serializer_class = ClubSerializer
      

class ProgrammerView(viewsets.ModelViewSet):
      queryset=Program.objects.all()
      serializer_class= ProgrammingSerializer
      
      
class WebNetworkView(viewsets.ModelViewSet):
      queryset = WebNetwork.objects.all()
      serializer_class = WebNetworkSerializer
      
class HardWareHackingView(viewsets.ModelViewSet):
      queryset = HardWareHacking.objects.all()
      serializer_class = HardWareHackingSerializer
      
class SoftwareAppView(viewsets.ModelViewSet):
      queryset= SoftwareApp.objects.all()
      serializer_class=SoftwareAppSerializer
      
class CultaralView(viewsets.ModelViewSet):
      queryset = Cultaral.objects.all()
      serializer_class = CultaralSerializer
      
class AnimationView(viewsets.ModelViewSet):
      queryset = Animation.objects.all()
      serializer_class = AnimationSerializer
      
      
class ClubMemberView(viewsets.ModelViewSet):
      queryset = ClubMember.objects.all()
      serializer_class = ClubMemberSerializer