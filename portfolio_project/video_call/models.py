from django.db import models
from django.conf import settings
from django.utils.timezone import now
from uuid import uuid4
from user.models import User
# Create your models here.

class VideoRoom(models.Model):
    choice_status=[
        ("Portfolio","Portfolio"),
        ("Custom","Custom"),
        ("Ecommerce","Ecommerce"),
        ("Other","Other"),
    ]
    uuid=models.CharField(max_length=255,null=True)
    message=models.CharField(max_length=255,null=True)
    requirement=models.CharField(choices=choice_status,max_length=255,null=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="package_model_created",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="package_model_updated",
    )
    deleted = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.uuid
    
    
class ChatRoom(models.Model):
    uuid=models.CharField(default=uuid4,null=True,max_length=100)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_chatroom")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    def __str__(self):
        return self.uuid
    
class ChatMessage(models.Model):
    chatroom=models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name="chatroom_chatmessage",default="",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_chatmessage")
    message=models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    
    
    
    