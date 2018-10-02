# generics
from django.db.models import   Q
from rest_framework import generics, mixins
from firstApp.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly


class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    #queryset = BlogPost.objects.all()

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title=query)|
                Q(content=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request,*args, **kwargs):
        return self.create(request, *args, **kwargs)



   # def get_object(self):
    #    pk = self.kwargs.get("pk")
     #   return BlogPost.objects.get(pk=pk)






class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    premissions_classes = [IsOwnerOrReadOnly]
    #queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()


   # def get_object(self):
    #    pk = self.kwargs.get("pk")
     #   return BlogPost.objects.get(pk=pk)




