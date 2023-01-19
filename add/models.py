from django.db import models

# Create your models here.
class products(models.Model):
    Pname = models.CharField(max_length=100)
    Price = models.FloatField()
    Stock = models.IntegerField()

    def __str__(self):
        return self.Pname