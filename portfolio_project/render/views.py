from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def forgot_password_mail(request):
    return render(request,"forgot_password_mail_request.html")

def forgot_password(request,token):
    return render(request,"forgot-password.html")
    
def change_password(request):
    return render(request,"change-password.html")

def project_detail(request,name):
    return render(request,"project-detail.html")


def pricing(request):
    return render(request,"pricing.html")

def contact_us(request):
    return render(request,"contact-us.html")
    
    
def custom_404_view(request, exception):
    return render(request, 'error-404.html', status=404)


def development_process(request):
    return render(request, 'development-process.html', status=404)
    

def service(request):
    return render(request, 'services.html', status=404)
    

def why_me(request):
    return render(request, 'why-me.html')
    
def profile_edit(request):
    return render(request,"profile-edit.html")

   
def video_call(request,link):
    return render(request,"video-call.html")



def profile(request):
    return render(request,"profile.html")