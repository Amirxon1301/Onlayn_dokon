from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# class ProfilAdmin(UserAdmin):
#     model = Profil
#     fieldsets = UserAdmin.fieldsets + (
#         ('Profil ustunlari', {
#             'fields': ('ism', 'davlat', "jins", "shahar")
#         }),
#     )
admin.site.register(Profil)
