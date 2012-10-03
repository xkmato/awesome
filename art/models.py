from django.contrib.auth.models import User
from django.db import models

# Create your models here.
ART_CHOICES = ((u'Film',u'Film'),(u'Music',u'Music'),(u'FineArt',u'FineArt'),
               (u'Sculpture',u'Sculpture'),(u'Photography',u'Photography'),(u'TV',u'TV'))
class ArtPiece(models.Model):
    owners = models.ManyToManyField(User)
    art_type = models.CharField(max_length=50,choices=ART_CHOICES)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    art_piece = models.FileField(upload_to='media/%s'%art_type)
    added_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Credits(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    art_piece = models.ForeignKey(ArtPiece)

    def __unicode__(self):
        return self.name

class Like(models.Model):
    liker = models.ForeignKey(User)
    liked = models.ForeignKey(ArtPiece)
    liked_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.liker.username

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    art_pieces = models.ManyToManyField(ArtPiece)
    added_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name