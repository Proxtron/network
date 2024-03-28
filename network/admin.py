from django.contrib import admin
from .models import User, Post


#class UserAdmin(admin.ModelAdmin):
    

class PostAdmin(admin.ModelAdmin):
    list_display = ['message', 'author', 'timePosted']

#admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)