from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserAttached(models.Model):
    user = models.ForeignKey(User)
    class Meta:
        abstract = True

class UserProfile(UserAttached):
    pass

class Contacts(UserAttached):
    pass

class Location(UserAttached):
    pass

class Respect(models.Model):
    pass