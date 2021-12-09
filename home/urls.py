from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about-us', about_us),
    path('ai', ai),
    path('android', android),
    path('pack', pack),
    path('team-us', team_us),
    path('web', web),

    path('payment', payment),
    path('verify_coupon', verify_coupon),
    path('/winter/validate_payment', validate_payment),
    path('payment_result', payment_result)
]
