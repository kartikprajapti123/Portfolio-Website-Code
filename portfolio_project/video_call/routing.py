from django.urls import re_path
from video_call.consumer import ChatConsumer,VideoCallConsumer
from django.urls import path

websocket_urlpatterns = [
    # repath(r'ws/video-call/$', ChatCounsumer.as_asgi()),
    path("ws/chat/<str:id>/",ChatConsumer.as_asgi()),
    path("ws/video-call/<str:id>/",VideoCallConsumer.as_asgi()),
    
    
]
