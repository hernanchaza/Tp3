# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Coupons
from .forms import CouponForm
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods([ "POST"])
def coupon_apply(request):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupons.objects.get(
                code__iexact=code, expiration__gte=now, active=True)
            request.session['coupon_id'] = coupon_id
        except Coupons.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
