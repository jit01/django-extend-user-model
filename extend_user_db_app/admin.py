from django.contrib import admin
from extend_user_db_app.models import UserProfile


class userprofileadmin(admin.ModelAdmin):
    list_display = ['user', 'location']


admin.site.register(UserProfile, userprofileadmin)
