from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from contact.models import Contact

class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields=[
            "id",
            "name",
            "phone",
            "email",
            "select_website",
            "message",
        ]
        
    def validate(self, attrs):
        phone = attrs.get("phone")
        email = attrs.get("email")    
        message = attrs.get("message")    
        select_website = attrs.get("select_website")    
        
        # Check if both phone and email are empty
        if (phone is None or phone == "") and (email is None or email == ""):
            raise serializers.ValidationError("Phone or email, one of them is required to contact")
        
        # Check if message is empty
        if message is None or message == "":
            raise serializers.ValidationError("Message is required")
        
        # Check message length
        if len(message) < 30:
            raise serializers.ValidationError("Message length should be more than 30 characters")
        
        # Check if a website is selected
        if select_website is None or select_website == "":
            raise serializers.ValidationError("Please select a website")
        
        return attrs
    
                    
            
            