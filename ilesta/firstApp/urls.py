from django.conf.urls import url, include
from firstApp import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)




urlpatterns= [
    url(r'^$', views.index,name="maher"),
    url(r'^', include(router.urls)),

]
