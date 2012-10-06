from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
ART_CHOICES = ((u'Film',u'Film'),(u'Music',u'Music'),(u'FineArt',u'FineArt'),
               (u'Craft',u'Craft'),(u'Photography',u'Photography'),(u'TV',u'TV'),(u'Literature',u'Literature'))
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

    def get_extra_attributes(self):
        for attribute in list(self.extraattribute_set.all()):
            if attribute.user_involved:
                yield (attribute.attribute,attribute.user_involved)
            elif attribute.other_details:
                yield (attribute.attribute,attribute.other_details)

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

class ExtraAttribute(models.Model):
    art = models.ForeignKey(ArtPiece)
    attribute = models.CharField(max_length=100)
    user_involved = models.ForeignKey(User,null=True,help_text="this is only applicable if the attribute is about a user")
    other_details = models.TextField(blank=True)

    def clean(self):
        if self.user_involved and self.other_details:
            raise ValidationError('An Extra attribute can\'t have both user and other details set')

        if not (self.user_involved and self.other_details):
            raise ValidationError('One of other details or user involved must be set for an attribute')

    def __unicode__(self):
        return self.art.name

class Comment(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey(User)
    commented_on_art = models.ForeignKey(ArtPiece,null=True)
    commented_on_gallery = models.ForeignKey('Gallery',null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.commented_on_art and self.commented_on_gallery:
            raise ValidationError('A comment can either be for an art Piece or Gallery but not both')

        elif not(self.commented_on_art and self.commented_on_gallery):
            raise ValidationError('What is this comment for?')

class Gallery(models.Model):
    owners = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    art_pieces = models.ManyToManyField(ArtPiece)
    added_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name