from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'moderator']
    list_filter = ['moderator']

admin.site.register(Profile, ProfileAdmin) 