from rest_framework.serializers import ModelSerializer
from project.models import Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model=Project
        fields=[
            "id",
            "project_name",
            "project_title",
            "project_description",
            "project_image",
            "client_name",
            "project_video",
            "project_thumbnail",
            "external_link",
            "project_category",
            "created_at",
            "updated_at"
        ]
        
        
        