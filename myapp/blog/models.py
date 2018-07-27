from django.db import models
from django.utils import timezone
#from nntplib import author
from unittest.util import _MAX_LENGTH
from email.policy import default
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    publized_date=models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.publized_date=timezone.now()
        self.save()
        
    def _str_(self):
        return self.title