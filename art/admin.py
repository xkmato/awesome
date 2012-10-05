from django.contrib import admin
from art.models import ArtPiece, Credit, Like, Gallery

__author__ = 'kenneth'

admin.site.register(ArtPiece)
admin.site.register(Credit)
admin.site.register(Like)
admin.site.register(Gallery)
