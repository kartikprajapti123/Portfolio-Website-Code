from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from decouple import config
from .models import VideoRoom,ChatMessage,ChatRoom
from uuid import uuid4
from utils.send_mail import send_email_with_template
import threading
class RoomSerializer(ModelSerializer):
    user_username=serializers.CharField(required=False,allow_null=True)
    class Meta:
        model = VideoRoom
        fields = [
            "id",
            "uuid",
            "message",
            "requirement",
            "user_username",
            "created_by",
        ]
        
    def create(self, validated_data):
        main_uuid=uuid4()
        validated_data["uuid"]=main_uuid
        subject=f"A New Video Call Room Created by ${validated_data['user_username']} "
        to="kartikprajapati26122004@gmail.com",
        template="send-email-room-created.html",
        context={
            "uuid":validated_data["uuid"],
            "created_by":validated_data["user_username"],
            "message":validated_data["message"],
            "requirement":validated_data["requirement"],
            "room_link":f"{config('HOST_URL')}/video-call/{main_uuid}/"
            
        }
        validated_data.pop("user_username")
        mail_thread = threading.Thread(
                    target=send_email_with_template, 
                    args=(subject, to, template, context)
                )
        
        
        ChatRoom.objects.create(uuid=validated_data["uuid"],created_by=validated_data["created_by"])
        mail_thread.start()
        return super().create(validated_data)
    
    
    
class ChatRoomSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = ChatRoom
        fields = [
            "id",
            "uuid",
            "created_by",
            "created_by_username",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "uuid", "created_at", "updated_at"]

    def create(self, validated_data):
        # Additional logic during creation, if necessary
        return super().create(validated_data)


class ChatMessageSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username", read_only=True)
    user_profile_picture = serializers.CharField(source="user.profile_picture", read_only=True)
    
    chatroom_uuid= serializers.UUIDField(source="chatroom.uuid", read_only=True)

    class Meta:
        model = ChatMessage
        fields = [
            "id",
            "user",
            "user_username",
            "user_profile_picture",
            
            "chatroom",
            "chatroom_uuid",
            "message",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        # Additional logic during creation, if necessary
        return super().create(validated_data)
