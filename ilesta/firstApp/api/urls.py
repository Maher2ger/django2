from .views import BlogPostRudView,BlogPostAPIView
from django.conf.urls import url,include


from django.contrib import admin

urlpatterns = [
    url(r'^(?P<pk>\d+)', BlogPostRudView.as_view(),name='post-rud'),
    url(r'^$', BlogPostAPIView.as_view(),name='post-create'),
 ]