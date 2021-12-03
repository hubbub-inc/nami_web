from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    item_Main_Img = models.ImageField(upload_to='images/')
# Create your models here.
