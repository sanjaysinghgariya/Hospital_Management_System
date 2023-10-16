from django.urls import path
from sendemailtomyemail import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('register', views.contact_us, name='contact'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('unverify_otp', views.unverify_otp, name='unverify_otp'),

    path('login', views.Login, name='login'),
    path('logout', views.log_out, name='logout'),
    path('forget_passsword', views.forget_password, name='forgetpassword'),
    path('verify_otp_pass', views.verify_otp_pass, name='verify_otp_pass')
    
]
