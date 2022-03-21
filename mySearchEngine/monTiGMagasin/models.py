from django.db import models

# Create your models here.
class InfoProduct(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tig_id = models.IntegerField(default='-1')
    name = models.CharField(max_length=100, blank=True, default='')
    category = models.IntegerField(default='-1')
    price = models.FloatField(default='0')
    unit = models.CharField(max_length=20, blank=True, default='')
    availability = models.BooleanField(default=True)
    sale = models.BooleanField(default=False)
    discount = models.FloatField(default='0')
    comments = models.CharField(max_length=100, blank=True, default='')
    owner = models.CharField(max_length=20, blank=True, default='tig_orig')
    quantityInStock = models.IntegerField(default='0')
    percentage_reduc = models.FloatField(default='0')
    quantitySold = models.IntegerField(default='0')

    class Meta:
        ordering = ('name',)

class DonneeHisto(models.Model):
    nameProd = models.CharField(max_length=100, blank=True, default='')
    category = models.IntegerField(default='-1')
    quantityT = models.IntegerField(default='0')
    dateT = models.DateField(auto_now_add=True)
    typeT = models.CharField(max_length=100, blank=True, default='')
    valeurT = models.FloatField(default='0')

    class Meta:
        ordering = ('dateT',)
