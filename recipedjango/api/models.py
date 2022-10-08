from django.db import models

# Create your models here.

class base(models.Model):
    domainName = models.CharField(max_length=200)
    ipAddr = models.CharField(max_length=200)

    def __str__(self):
        return (self.domain + self.ip)