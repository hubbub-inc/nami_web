from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    instructions = models.TextField()
    
    def __str__(self):
        return self.name
        
class TestModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self):
        return self.name

