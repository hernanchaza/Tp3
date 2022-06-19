# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Coupons(models.Model):
    code = models.CharField(max_length=50, 
                            unique=True, default= 'No Data')
    percentage = models.IntegerField(validators=[MinValueValidator(0), 
                                                 MaxValueValidator(100)])
    telephone = models.IntegerField()
    expiration = models.DateField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.code