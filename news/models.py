from django.db import models
from django.conf import settings
# Create your models here.
#--headline (title,image,url)
#-- user_profile (user,last_scrap)

class Headline(models.Model):
    title = models.CharField(max_length=120)
    image =models.ImageField(null=True,blank=True)
    url =models.URLField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    last_scrape=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return "{} - {}".format(self.user,self.last_scrape)