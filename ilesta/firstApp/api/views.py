# generics

from rest_framework import generics
from firstApp.models import BlogPost
from .serializers import BlogPostSerializer



class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    #queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()


   # def get_object(self):
    #    pk = self.kwargs.get("pk")
     #   return BlogPost.objects.get(pk=pk)




