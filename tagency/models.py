from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

# Create your models here.
class Book(models.Model):
    destination= models.CharField(max_length=255, null=False, blank=True)
    agent = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    desc=models.TextField()
    img_url = models.TextField()

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    def __str__(self):
        return self.destination