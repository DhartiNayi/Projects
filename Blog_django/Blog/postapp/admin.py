from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=('title','image','des')
    
admin.site.register(Blog,BlogAdmin)    


# Register your models here.
