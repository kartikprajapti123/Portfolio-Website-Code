from django.urls import path
from render import views

urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("change-password/",views.change_password,name="change_password"),
    path("forgot-password/<str:token>/",views.forgot_password,name="forgot_password"),
    path("forgot-password-mail-request/",views.forgot_password_mail,name="forgot_password_mail"),
    path("change-password/",views.change_password,name="change_password"),
    path("project-detail/<str:name>/",views.project_detail,name="project-detail"),
    path("pricing/",views.pricing,name="pricing"),
    path("contact-us/",views.contact_us,name="pricing"),
    path("development-process/",views.development_process,name="development_process"),
    path("service/",views.service,name="service"),
    path("why-me/",views.why_me,name="why_me"),
    path("video-call/<str:link>/",views.video_call,name="video_call"),
    path("profile/",views.profile,name="profile"),
    path("policy/",views.policy,name="policy"),
    path("terms_and_condition/",views.terms_and_condition,name="policy"),
    
    
    
    
    
    
    
    

    
]
