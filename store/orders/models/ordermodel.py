from django.db import models

class Order(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    shipping = models.DecimalField(max_digits = 10, decimal_places = 2)
    total = models.DecimalField(max_digits = 10, decimal_places = 2)