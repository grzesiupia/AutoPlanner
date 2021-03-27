from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'users'
