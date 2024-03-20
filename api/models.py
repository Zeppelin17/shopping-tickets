from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    date = models.DateField()
    shop = models.ForeignKey(Shop, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.shop}"
