



from asyncio.windows_events import NULL
from dataclasses import fields
from tkinter.ttk import Style
from unittest.mock import DEFAULT
from django.forms import ValidationError
from rest_framework import serializers
from club.models import ClubIn,ClubMember,Program,WebNetwork,HardWareHacking,SoftwareApp,Cultaral,Animation,AssociationClub
from auser.models import AssociationUser
from rest_framework.authtoken.models import Token

# class RegistrationSerializer(serializers.ModelSerializer):
#       club_admin = serializers.CharField()
#       class Meta:
#             model = AssociationUser
#             # fields="__all__"
#             fields =("user_name","email","full_name","student_id","batch_no","linkend_id","password","club_admin")
#       #   fields = ('id', 'username', 'password', 'email',)
#             extra_kwargs = {'password': {"write_only": True, 'required': True}}

#       def create(self, validated_data):
#             user = AssociationUser.objects.create_member(**validated_data)
#             Token.objects.create(user=user)
#             return user


class RegistrationSerializer(serializers.ModelSerializer):
      password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
      
      class Meta:
            model =AssociationUser
            fields=["user_name","email","full_name","student_id","batch_no","linkend_id","password","password2"]
            extra_kwargs={
                  'password':{'write_only':True}
            }
            
      def save(self, **kwargs):
            member = AssociationUser(
                  user_name=self.validated_data['user_name'],
                  email =self.validated_data['email'],
                  full_name=self.validated_data['full_name'],
                  student_id =self.validated_data['student_id'],
                  batch_no=self.validated_data['batch_no'],
                  linkend_id =self.validated_data['linkend_id'],
            )
            password= self.validated_data['password']
            password2= self.validated_data['password2']
            if password != password2:
                  raise serializers.ValidationError({'password':'Password must match.'})

            member.set_password(password2)
            member.save()
            return member
class AssociationUserSerializer(serializers.ModelSerializer):
      class Meta:
            model = AssociationUser
            fields = "__all__"
            depth=1

class AssociationClubSerializer(serializers.ModelSerializer):
      class Meta:
            model = AssociationClub
            fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):
      class Meta:
            model= ClubIn
            fields="__all__"
            

class ProgrammingSerializer(serializers.ModelSerializer):
      class Meta:
            model=Program
            fields= "__all__"
            depth = 1
            
class WebNetworkSerializer(serializers.ModelSerializer):
      class Meta:
            model=WebNetwork
            fields= "__all__"
            depth = 1
            
class HardWareHackingSerializer(serializers.ModelSerializer):
      class Meta:
            model=HardWareHacking
            fields= "__all__"
            depth = 1

class SoftwareAppSerializer(serializers.ModelSerializer):
      class Meta:
            model=SoftwareApp
            fields= "__all__"
            depth = 1
class CultaralSerializer(serializers.ModelSerializer):
      class Meta:
            model=Cultaral
            fields= "__all__"
            depth = 1
class AnimationSerializer(serializers.ModelSerializer):
      class Meta:
            model=Animation
            fields= "__all__"
            depth = 1
class ClubMemberSerializer(serializers.ModelSerializer):
      class Meta:
            model=ClubMember
            fields= "__all__"
            depth = 1
