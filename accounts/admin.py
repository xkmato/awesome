from django.contrib import admin
from accounts.models import UserProfile, Respect, Contacts, Location

__author__ = 'kenneth'

admin.site.register(UserProfile)
admin.site.register(Respect)
admin.site.register(Contacts)
admin.site.register(Location)
