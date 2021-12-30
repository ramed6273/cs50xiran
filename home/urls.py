from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
#     path('about-us', about_us),
    path('ai', ai),
    path('android', android),
    path('pack', pack),
#     path('team-us', team_us),
    path('web', web),
    path('term', term),
    path('payment', payment),
    path('verify_coupon', verify_coupon),
    path('validate_payment', validate_payment),
    path('payment_result', payment_result),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('profile', profile, name='profile'),
    path('AI_class', ai_class, name='ai_class'),
    path('android_class', android_class, name='android_class'),
    path('web_class', web_class, name='web_class'),
    path("ai_sessions/<int:session_id>/", ai_class_sessions, name="ai_class_sessions"),
    path("web_sessions/<int:session_id>/", web_class_sessions, name="web_class_sessions"),
    path("android_sessions/<int:session_id>/", android_class_sessions, name="android_class_sessions"),
    path('AI_class/ai_guide', ai_guide)
]
