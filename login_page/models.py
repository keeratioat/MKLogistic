from django.db import models

# Create your models here.
class Parcle(models.Model):
    email = models.CharField(max_length=60)
    ems = models.CharField(max_length=20)
    isSend = models.BooleanField()
    
    def __str__(self):
        return self.email
    