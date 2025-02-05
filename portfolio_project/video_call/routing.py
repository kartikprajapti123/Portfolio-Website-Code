from django.urls import re_path
from video_call.consumer import ChatConsumer,VideoCallConsumer
from django.urls import path

websocket_urlpatterns = [
    re_path(r"^ws/chat/(?P<id>[^/]+)/$", ChatConsumer.as_asgi()),
    re_path(r"^ws/video-call/(?P<id>[^/]+)/$", VideoCallConsumer.as_asgi()),
]
