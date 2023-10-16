from django.db import models

# Create your models here.
class Contactus(models.Model):
    fname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=False, blank=False)

    password = models.CharField( default='None', max_length=20)

    def __str__(self) -> str:
        return self.email + "--->" + self.name
 


