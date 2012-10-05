from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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

    def get_credits(self):
        return self.credit_set.all()

    def get_likes(self):
        return self.like_set.all()

class Credit(models.Model):
    name = models.CharField(max_length=100)
    register_user = models.ForeignKey(User)
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

#class ExtraAttributes(models.Model):
#    pass

class Comment(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey(User)
    commented_on_art = models.ForeignKey(ArtPiece,null=True)
    commented_on_gallery = models.ForeignKey('Gallery',null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.commented_on_art and self.commented_on_gallery:
            raise ValidationError('A comment can either be for an art Piece or Gallery but not both')


class Gallery(models.Model):
    owners = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    art_pieces = models.ManyToManyField(ArtPiece)
    added_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name