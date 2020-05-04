from django.contrib import admin
#
# from apps.users.models import UserProfile
# class UserProfileAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(UserProfile, UserProfileAdmin)

#因为用户表相对来说都是系统中存在的，Django内置了一个队显示用户信息的优化
from apps.users.models import UserProfile
from django.contrib.auth.admin import UserAdmin
admin.site.register(UserProfile, UserAdmin)