from django.db import models
import datetime

def choice_year():
    return [(r, r) for r in range(1901, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

years = choice_year()

# Create your models here.
class VehicleBrand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.name)
    
class VehicleType(models.Model):
    name = models.CharField(max_length=255)
    brand_id = models.ForeignKey(VehicleBrand, related_name='type',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.name)

class VehicleModel(models.Model):
    name = models.CharField(max_length=255)
    type_id = models.ForeignKey(VehicleType, related_name='model', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.name)

class VehicleYear(models.Model):
    year = models.IntegerField('year', choices=years, default=current_year)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.year)

class PriceList(models.Model):
    code = models.CharField(max_length=8)
    price = models.IntegerField(default=100000000)
    year_id = models.ForeignKey(VehicleYear, on_delete=models.CASCADE)
    model_id = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.price)


