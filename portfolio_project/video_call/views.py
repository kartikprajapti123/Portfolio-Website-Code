from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import VideoRoom
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from video_call.models import ChatMessage,ChatRoom
from video_call.serializers import ChatMessageSerializer,ChatRoomSerializer

class RoomViewSet(ModelViewSet):
    queryset = VideoRoom.objects.filter(deleted=0)
    serializer_class = RoomSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    filter_backends=[SearchFilter,OrderingFilter]
    
    search_fields=[
        "uuid",
            "message",
            "requirement",
    ]   
    ordering_fields=[
        "uuid",
            "message",
            "requirement",
    ] 
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        no_pagination = request.query_params.get("no_pagination")

        if no_pagination:
            serializer = self.serializer_class(queryset, many=True)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        data["created_by"]=request.user.id
        data["user_username"]=request.user.username
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"success": True, "message": "Room deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
        
    
    @action(detail=False,methods=["POST",],url_path="check-uuid")
    def check_uuid(self,request,*agrs,**kwargs):
        uuid=request.data.get("uuid")
        if not uuid:
            return Response ({"success":False,"message":"uuid is required"},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            room_instanse=VideoRoom.objects.get(uuid__exact=uuid)
            
        except VideoRoom.DoesNotExist:
            return Response ({"success":False,"message":"Invliad Link"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer=self.serializer_class(room_instanse)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK,
        )


class ChatRoomViewSet(ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["uuid", "created_by__username"]
    ordering_fields = ["uuid", "created_at", "updated_at"]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        no_pagination = request.query_params.get("no_pagination")

        if no_pagination:
            serializer = self.serializer_class(queryset, many=True)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        data = request.data
        data["created_by"] = request.user.id

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK,
        )


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"success": True, "message": "Chat room deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class ChatMessageViewSet(ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["message", "user__username",
            "chatroom_uuid",]
    ordering_fields = ["created_at", "updated_at","chatroom",
            "chatroom_uuid"]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        no_pagination = request.query_params.get("no_pagination")

        if no_pagination:
            serializer = self.serializer_class(queryset, many=True)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        data = request.data
        data["user"] = request.user.id

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
            
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK,
        )


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"success": True, "message": "Chat message deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


    @action(detail=False,methods=["POST",],url_path="get-chat-message-uuid")
    def get_chat_message_from_uuid(self,request,*args,**kwargs):
        print(request.data)
        uuid=request.data.get("uuid")
        if not uuid:
            return Response({"success":False,"message":"UUID is required"},status=status.HTTP_400_BAD_REQUEST)
        
        chat_message_instance=ChatMessage.objects.filter(chatroom__uuid=uuid)
        
        serilaizer=ChatMessageSerializer(chat_message_instance,many=True)
        return Response({"success": True, "data": serilaizer.data},
            status=status.HTTP_200_OK,)
        
        
        