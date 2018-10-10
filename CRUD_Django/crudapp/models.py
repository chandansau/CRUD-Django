from django.db import models

# Create your models here.
class products(models.Model):
    pname=models.CharField(max_length=15)
    pcost = models.DecimalField(max_digits=10, decimal_places=4)
    quantity=models.IntegerField()

    def __str__(self):
        return self.pname

