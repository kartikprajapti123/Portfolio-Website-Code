from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from project.models import Project
from project.serializers import ProjectSerializer
from utils.pagination import mypagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.filter(deleted=0).order_by("-id")
    serializer_class = ProjectSerializer
    pagination_class = mypagination
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]
    
    search_fields=[
        "project_name",
            "project_title",
            "project_description",
            "project_image",
            "project_video",
            "project_category",
            "created_at",
            "updated_at"
    ]
    ordering_fields=[
        "project_name",
            "project_title",
            "project_description",
            "project_image",
            "project_video",
            "project_category",
            "created_at",
            "updated_at"
    ]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        no_pagination = request.query_params.get("no_pagination")
        page_url=request.query_params.get("page_url")
        print(page_url)
        if page_url:
           queryset=queryset.filter(page_url=page_url)
        
        if no_pagination:
            print(queryset)
            serializer = self.serializer_class(queryset, many=True)
            print(serializer.data)
            return Response({"success": True, "data": serializer.data})

       

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(
                {"success": True, "data": serializer.data}
            )

        serializer = self.serializer_class(queryset, many=True)
        return self.get_paginated_response({"success": True, "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # Perform a hard delete. Use soft delete if needed.
        return Response(
            {"success": True, "message": "Project deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
        
    @action(detail=False,methods=['GET',],url_path="project_by_username")
    def project_by_username(self,request,*args,**kwargs):
        project_name=request.query_params.get("project_name")
        
        if project_name:
            try:
                project_instance=Project.objects.get(project_name=project_name)
                
            except Project.DoesNotExist:
                return Response({"success":True,"message":"No Project Found with this detail"},status=status.HTTP_400_BAD_REQUEST)
            
        else:
                return Response({"success":True,"message":"project name is required"},status=status.HTTP_400_BAD_REQUEST)
            
        serializer=ProjectSerializer(project_instance)
        return Response({"success":True,"data":serializer.data},status=status.HTTP_200_OK)
    
