# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'expiration', 'percentage', 'telephone']
    search_fields = ['code']

    def get_queryset(self, request):
				qs = super(CouponAdmin, self).get_queryset(request)
				return qs

admin.site.register(Coupons, CouponAdmin)