from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    show = notice.objects.all().order_by('cr_date')
    context = {'show':show}
    return render(request, 'index.html', context)

def fulldetails(request, id):
    details = notice.objects.filter(notice_id = id)
    return render(request, 'details.html', {'details':details[0]})

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        branch = request.POST['branch']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

    #Validations

    # if len(username)>10:
    #     messages.error(request, "Enter a valid username")
    #     return redirect('home')
    
    # if pass1 != pass2:
    #     messages.error(request, "Password do not match")
    #     return redirect('home')

    #Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        myuser.branch = branch
        myuser.save()
        messages.success(request, "Your Account has been created successfully")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')


def handlelogin(request):
    # loginusername and loginpassowrd comes from input fields in html filehomeform
    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']

    user = authenticate(username = loginusername, password=loginpassword)
    if user is not None:
        login(request, user)
        messages.success(request, "Login Successfully")
        return redirect('home')

    else:
        messages.error(request, "Enter Username and password correctly")
        return redirect('home')


def handlelogout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('home')







