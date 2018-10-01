from rest_framework import serializers

from firstApp.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields= [
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]