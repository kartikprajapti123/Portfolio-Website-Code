from django.contrib import admin
from video_call.models import VideoRoom,ChatMessage,ChatRoom
# Register your models here.
admin.site.register(VideoRoom)
admin.site.register(ChatMessage)
admin.site.register(ChatRoom)
