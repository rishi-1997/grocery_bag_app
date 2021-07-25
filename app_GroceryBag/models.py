from django.db import models

# Create your models here.

Item_status_choices = (
    ('1', 'PENDING'),
    ('2', 'BOUGHT'),
    ('3', 'NOT AVAILABLE'),
)


class GrossBag(models.Model):
    Item_Name = models.CharField(max_length=100)
    Item_Quantity = models.IntegerField()
    Item_status = models.CharField(max_length=25, choices=Item_status_choices)
    Date = models.DateField()
