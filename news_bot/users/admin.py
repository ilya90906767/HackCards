from django.contrib import admin


from .models import UserProfile, UserPhoto

admin.site.register(UserProfile)
admin.site.register(UserPhoto)

# Register your models here
