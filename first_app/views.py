from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app.models import User 
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpage_list} 
    return render(request,'first_app/index.html', context=date_dict)

def template2(request):
    return render(request,'first_app/template2.html')

def userview(request):
    user_dict = {}
    users = User.objects.order_by('name')
        
    user_dict['users']= users

    print(user_dict)    

    return render(request,'first_app/user.html', context=user_dict)    