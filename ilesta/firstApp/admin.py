from django.contrib import admin
from firstApp.models import AccessRecord,Topic,Webpage,BlogPost

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(BlogPost)