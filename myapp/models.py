from django.db import models

###################### INSERI ##########################
class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
