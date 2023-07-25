from rest_framework import serializers
from .models import *


class tempserializer(serializers.ModelSerializer):
    class Meta:
        model = temp
        fields = '__all__'

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id','first_name','last_name','email']

class taskSerializer(serializers.ModelSerializer):    
    class Meta:
        model = tasks
        fields = '__all__'

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model =Login
        fileds = ['id']
        exclude = ['user_name','password','login_status','login_time']

class ParentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = '__all__'

class ChildModelSerializer(serializers.ModelSerializer):
    Parent = ParentModelSerializer(read_only =True)
    class Meta:
        model = ChildModel
        fields = '__all__'