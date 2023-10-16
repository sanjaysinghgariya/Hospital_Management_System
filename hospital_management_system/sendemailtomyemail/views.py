from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
from sendemailtomyemail.models import Contactus
from django.contrib import messages
from verify_email.email_handler import send_verification_email# Create your views here.
from sendemailtomyemail.utils import send_email_to_client
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def contact_us(request):
    if request.method =="POST":
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        all_users = User.objects.values()
        for k in all_users:
                if k['email'] == email:
                     messages.success(request, "email Already exists")
                     return redirect('contact')
                
                elif k['username'] == username:
                     messages.success(request, "username Already exists try different")
                     return redirect('contact')
                
        try:
            otp = send_email_to_client(email)
            messages.success(request, "please check your email")
            return render(request, 'sendemail/verify_otp.html', {'email':email, 'otp':otp, 'lname':lname, 'fname':fname, 'username':username, 'password':password})
        
        except Exception as e:
                      
            messages.error(request, str(e))
    
    return render(request, 'sendemail/contact.html')


@csrf_exempt
def verify_otp(request):
    if request.method =="POST":

        userotp = request.POST.get('otp')
        email = request.POST.get('email')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            form = User.objects.create_user(first_name = fname, last_name=lname, email=email, username=username, password=password)
            form.save()
            messages.success(request, "Sucessfully registred")
        except Exception as error:
            messages.success(request, error)
        
    return JsonResponse({'data':'data'}, status=200)


@csrf_exempt
def unverify_otp(request):
    if request.method =="POST":
        messages.success(request, "Otp is invalid please tryAgain")

    return JsonResponse({'data':'data'}, status=200)



def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return render(request, 'sendemail/main.html')
        else:
               messages.error(request, 'user not found')
    return render(request, 'sendemail/login.html')

def log_out(request):
    logout(request)
    return render(request, 'sendemail/contact.html')

@login_required(login_url="/login")
def main_page(request):
     return render(request, 'sendemail/main.html')


def forget_password(request):
     if request.method == "POST":
          email = request.POST['email']
          all_users = User.objects.values()
          exits = False
          for k in all_users:
                if k['email'] == email:
                     messages.success(request, "exist")
                     exits = True
                     break
          if exits == True:
                otp = send_email_to_client(email)
                
                messages.success(request, "please check your email")
                return render(request, 'sendemail/verify_OTP_pass.html',{'email':email, 'otp':otp} )
                
     return render(request, 'sendemail/forget_password.html')


@csrf_exempt
def verify_otp_pass(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        u = User.objects.filter(email=email).first()
       
        try:
            u.set_password(password)
            u.save()
            messages.success(request, "password changes sucesfully")
        except Exception as error:
            messages.success(request, error)
    return JsonResponse({'data':'data'}, status=200)

    
