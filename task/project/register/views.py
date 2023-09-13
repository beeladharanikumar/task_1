from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers,status
from django.shortcuts import get_object_or_404,redirect
from django.conf import settings
from .serializers import *
from django.db import IntegrityError
import json
from django.core.mail import send_mail

# Create your views here.

def display(request):
    if request.method == 'POST':
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        un = request.POST.get('user_name')
        em = request.POST.get('email')
        pn = request.POST.get('phone_number')
        pwd = request.POST.get('password')
        gen = request.POST.get('gender')
        a = Register.objects.create(first_name = fn,last_name = ln,user_name =un,email = em,phone_number = pn,password = pwd,gender = gen)
        return render(request,'registeration.html')
    else:
        return render(request,'registeration.html')
    
def login_logout(request):
    if request.method == 'post' or 'get':
        user = request.POST.get('user_name')
        pwd = request.POST.get('password')
        # return render(request,'login.html')
        # k = Login.objects.create(user_name = user,password = pwd)
        res = Register.objects.filter(user_name = user)
        for i in res:
            if user == i.user_name:
                if pwd == i.password:
                    user = Login.objects.create(user_name = user,password = pwd,login_status = 'login succesfull')
                    context = {'user':i}
                    res_data = Register.objects.get(user_name = i.user_name)
                    # rev_data = registerSerializer(res_data)

                    return redirect('add-task',id = res_data.pk)
                else:
                    Login.objects.create(user_name = user,password = pwd,login_status = 'login failed')
                    return HttpResponse('please enter correct password')
            else:
                return HttpResponse('please register')
        return render(request,'login.html')
    else:
        return HttpResponse("hi")

# def add_task(request):
    


# crud operation using api
# c-create  [post]
class register_api(APIView):
    def post(self,request):
        try:
            fn = request.data.get('first_name')
            ln = request.data.get('last_name')
            un = request.data.get('user_name')
            em = request.data.get('email')
            pn = request.data.get('phone_number')
            pwd = request.data.get('password')
            gen = request.data.get('gender')

            a = Register.objects.create(first_name = fn,last_name = ln,user_name =un,email = em,phone_number = pn,password = pwd,gender = gen)
            return Response('registered successfully')
        except IntegrityError as e:
            return Response(str(e))

    def get(self,request):
        return Response('not allowed ......')

# r - read [get]----[post]

# class login_api(APIView):
@api_view(['post'])
def login_api(request):
        user = request.data.get('user_name')
        pwd = request.data.get('password')
        res = Register.objects.filter(user_name = user)
        # res = get_object_or_404(Register,user_name = user)
        if res.exists():
            for i in res:
                if pwd == i.password:
                    Login.objects.create(user_name=user, password=pwd, login_status='login successful')
                    return Response('successful login')
                else:
                    Login.objects.create(user_name=user, password=pwd, login_status='login failed')
                    return Response('login failed')
        else:
            return Response('User not found')

# u - update -[put]
class update_pwd(APIView):
    def put(self,request):
        user = request.data.get('user_name')
        pwd = request.data.get('password')
        new_pwd = request.data.get('new_password')
        res = get_object_or_404(Register,user_name = user)
        if res.password == pwd:
            res.password = new_pwd
            res.save()
            return Response('updated')
        else:
            return Response('wrong password')

# d - delete [del]
class remove_api(APIView):
    def delete(self,request):
        user = request.data.get('user_name')
        pwd = request.data.get('password')
        res= Register.objects.get(user_name = user)
        if res.password == pwd:
            res.delete()
            return Response('account deleted')
        else:
            return Response('please check your password')
        
class profile(APIView):
    def get(self,request):
        user_name = request.data.get('user_name')
        pwd = request.data.get('password')
        res = get_object_or_404(Register,user_name=user_name,password = pwd)
        data = {
            'first_name':res.first_name,
            "last_name":res.last_name,
            "email":res.email,

        }
        return Response(data)
    
class update_profile(APIView):
    def put(self,request):
        user_name = request.data.get('user_name')
        pwd = request.data.get('password')
        update_item = request.data.get('item')
        item_data = request.data.get("item_data")
        res = get_object_or_404(Register,user_name=user_name,password = pwd)
        if update_item == 'email':
            res.email = item_data
            res.save()
            return Response('email successfully changed')
        elif update_item == 'phone_number':
            res.phone_number = item_data
            res.save()
            return Response('phone number successfully updated')
        else:
            return Response('not changed')
        

class test_serializer(APIView):
    def post(self,request):
        user = request.data.get('name')
        num = request.data.get('number')
        a =temp.objects.filter(name = user)
        b = Register.objects.filter(user_name=user)
        if a.exists() and b.exists(): 
            temp_serialized = tempserializer(a , many=True) #mant = true means it return multiple opbjects(multiple rows)
            register_serialized = registerSerializer(b,many=True)
            serialized_data1 = temp_serialized.data  #here the serialized(dictionary) data deserialized to data 
            serialized_data2 = register_serialized.data
            response_data = {
                "data1": serialized_data1,
                "data2":serialized_data2
            }

            return Response(response_data)
        else:
            return Response('user not found')
        

@api_view(['POST'])
def post_data_into_temp(request):
    seri = tempserializer(data = request.data) #requested data srialized (convert into data format) if it is valid then save
    if seri.is_valid():
        seri.save()
        return Response(seri.data)
    else:
        return Response('not updated')
    
# @login_required(login_url='login')  # Requires login to access this view
# @api_view(['post'])
# def add_task(request):
#     # Here, you can access the present login user credentials
#     user = Login.objects.get(user_name = request.user.username)
#     # password = request.user.password

#     if user:
#         data = loginserializer(user )
#         return Response(data.data)
#         task = request.data.get('task')
#         task = tasks.objects.create(user = data.data,task = task)
#         return Response('task completed')

# @api_view(['POST'])
# def add_task(request):
#     # Here, you can access the present login user credentials
#     try:
#         user = Login.objects.get(user_name=request.user.username)
#     except Login.DoesNotExist:
#         return Response('User not found')  # Return appropriate response if user not found

#     data = loginserializer(user)
#     task_data = request.data.get('task')

#     if task_data:
#         task = tasks.objects.create(user=user, task=task_data)
#         return Response('Task added successfully')
#     else:
#         return Response('Task data not provided')

# here we add task by particular user when login with right crdentials
# @api_view(['post'])
def add_task(request,id):
    if request.method == "POST" or 'get':
        user = Register.objects.get(id = id)
        task = request.POST.get('task')
        user1 = registerSerializer(user)
        parsed_data =user1.data
        if task:
        # res_data = json.loads(parsed_data)    
        # Create the Task instance associated with the user
            task = tasks.objects.create(user_id=id, task=task)
        task1_viewer = tasks.objects.filter(user_id = id)
                # Rdirect to a success page or task list page
            # return redirect('task_list')
        return render(request,"task.html",{"id":task1_viewer})
        
    
    # else:
    #     return Response("task page fails")


class ParentToChildView(APIView):
    def post(self, request):
        parent_serializer = ParentModelSerializer(data=request.data)
        if parent_serializer.is_valid():
            parent_instance = parent_serializer.save()  # Save the parent instance

            # Get the description from the request
            description = request.data.get('description')

            # Create a new child instance referencing the parent instance
            child_instance = ChildModel.objects.create(parent=parent_instance, description=description)

            # Serialize the child instance to include parent data as a reference
            child_serializer = ChildModelSerializer(child_instance)

            return Response(child_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# in this we add data in child table as relevant to parent table
class childtoparentview(APIView):
    def post(self, request):
        parent_serializer = ParentModelSerializer(data=request.data)
        if parent_serializer.is_valid():
            parent_instance = parent_serializer.save() # Save the parent instance

            # Get the description from the request
            description = request.data.get('description')

            # Create a new child instance referencing the parent instance
            child_instance = ChildModel.objects.create(parent=parent_instance, description=description)

            # Serialize the child instance using ChildModelSerializer with nested representation
            child_serializer = ChildModelSerializer(child_instance)

            return Response(child_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# upload a file in your browser those files stored in uploaded_files folder in our local storage
def upload_file(request):
    file = request.FILES.get('file')
    upload_instance = file_upload.objects.create(file = file)
    return render(request,'file.html')


def task_html(request):
    return render(request,"task.html")

class serializer_test(APIView):
    def post(self,request):
        b = request.data.get("user")
        a = Register.objects.get(user_name = b)
        a1 = registerSerializer(a).data

        return Response(a1.get('id'))
    
class gmail(APIView):
    def post(self,request):
        user_email = request.data.get('email')
        rec_email = [user_email,]
        sender_mail = settings.EMAIL_HOST_USER
        a = send_mail('kumars project' ,'thanks fro register to my website',sender_mail,rec_email)
        return Response(a)
    
@api_view(['post' or 'get'])
def Chat(request):
        to_msg = request.data.get('number')
        # return HttpResponse(to_msg)
        receiver = Register.objects.get(phone_number = to_msg)
        receiver_id = registerSerializer(receiver).data
        return redirect ('chat_message',id = receiver_id.get('id'))
        # return render(request,'chat.html')

@api_view(['post' or 'get' or 'put'])
def chat_message(request,id):
    id_check  = chat.objects.filter(person2 = id)
    send_message =  request.data.get('message')
    if id_check.exists():
        a = get_object_or_404(chat,person2 = id)
        a.p1_msg = send_message
        a.save()
        res_data ={
            "data1" : a.p1_msg,
            "data2" : a.p2_msg
        }
        return Response(res_data)
        
    else:
        
        a1= chat.objects.create(person1 = 100,person2=id,p1_msg = send_message,p2_msg = '')
        # a = chat.objects.filter(id = a1)
        # res=a
        # res = chatserializer(a.id).data
        # return Response(res.get('id'))
        return redirect('chat_message',id)

# def chat(request):
#         if request.method =='post' or 'get':
#             to_msg = request.POST.get('phone_number')
#             # return HttpResponse(to_msg)
#             receiver = Register.objects.filter(phone_number = to_msg)
#             receiver_id = registerSerializer(receiver).data
#             return render(request,'chat.html')
        

