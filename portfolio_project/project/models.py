from django.db import models

# Create your models here.
class Project(models.Model):
    project_name=models.CharField(max_length=255,null=True)
    client_name=models.CharField(max_length=255,null=True)
    project_title=models.CharField(max_length=255,null=True)
    project_description=models.TextField(null=True)
    project_image=models.FileField(upload_to='project_image')
    project_thumbnail=models.FileField(upload_to='project_image',null=True)
    project_video=models.FileField(upload_to="project_video")
    project_category=models.CharField(max_length=255,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    external_link=models.CharField(max_length=255,null=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    deleted=models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return self.project_name
    
    