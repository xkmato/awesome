from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserAttached(models.Model):
    user = models.ForeignKey(User)
    class Meta:
        abstract = True

class Respect(models.Model):
    respecter = models.ForeignKey(User,related_name='respecter')
    respected = models.ForeignKey(User,related_name='respected')

class UserProfile(UserAttached):
    about_you = models.TextField()

    def __unicode__(self):
        return self.user.username

    def get_respects(self):
        return  Respect.objects.filter(respected=self.user)

    def get_users_respected(self):
        return Respect.objects.filter(respecter=self.user)

    def get_art_pieces(self):
        pass

    def get_credits(self):
        return self.user.credit_set.all()

    def get_art_liked(self):
        return self.like_set.all()


class Contacts(UserAttached):
    other_email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    website = models.URLField()

    def __unicode__(self):
        return self.user.username

class Location(UserAttached):
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

    def __unicode__(self):
        return self.country

