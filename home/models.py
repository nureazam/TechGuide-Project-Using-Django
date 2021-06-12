from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.email