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

        read_only_fields = ['user']


    def validate_tilte(self,value):
        qs = BlogPost.objects.filter(title_iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")