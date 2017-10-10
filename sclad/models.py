from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    full_name = models.CharField(
    		max_length=120)

    def __str__(self):              # __unicode__ on Python 2
        return self.full_name

class Tovar(models.Model):
    full_name = models.CharField(
    		max_length=120)
    category  = models.ForeignKey('Category')

    def __str__(self):              # __unicode__ on Python 2
        return self.full_name

class ScladTov(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    tovars = models.ForeignKey(
    		'Tovar',  null=True)

    MONTH = (
        ('1', '01'),
        ('2', '02'),
        ('3', '03'),
        ('4', '04'),
        ('5', '05'),
        ('6', '06'),
        ('7', '07'),
        ('8', '08'),
        ('9', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    srokmes = models.CharField(max_length=2, choices=MONTH, blank=False, default=MONTH[0])

    MY_YEARS = (
        ('18', '2018'),
        ('19', '2019'),
        ('20', '2020'),
        ('21', '2021'),
        ('22', '2022'),
        ('23', '2023'),
        ('24', '2024'),
        ('25', '2025'),
    )

    srokgod = models.CharField(max_length=2, choices=MY_YEARS, blank=False, default=MY_YEARS[2])
    kol = models.IntegerField(default=1)
    def __str__(self):              # __unicode__ on Python 2
        return self.tovars,self.srokmes+'/'+self.srokgod
