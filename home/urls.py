from django.urls import path

from . import views
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
    path('dashbord', dashbord, name='dashbord'),
    path('profile/', profile, name='profile'),
    path('profile_edite/', profile_edite, name='profile_edite'),
    path('AI_class', ai_class, name='ai_class'),
    path('android_class', android_class, name='android_class'),
    path('web_class', web_class, name='web_class'),
    path("ai_sessions/<int:session_id>/", ai_class_sessions, name="ai_class_sessions"),
    path("web_sessions/<int:session_id>/", web_class_sessions, name="web_class_sessions"),
    path("android_sessions/<int:session_id>/", android_class_sessions, name="android_class_sessions"),
    path("ai_sessions/<int:session_id>/description", ai_class_sessions_description,
         name="ai_class_sessions_drescription"),
    path("ai_sessions/<int:session_id>/question", ai_class_sessions_question,
         name="ai_class_sessions_question"),

    path("web_sessions/<int:session_id>/description", web_class_sessions_description,
         name="web_class_sessions_drescription"),
    path("web_sessions/<int:session_id>/question", web_class_sessions_question,
         name="web_class_sessions_question"),

    path("android_sessions/<int:session_id>/description", android_class_sessions_description,
         name="android_class_sessions_drescription"),
    path("android_sessions/<int:session_id>/question", android_class_sessions_question,
         name="android_class_sessions_question"),
    # password urls# urlpatterns += staticfiles_urlpatterns()
    path('change_password', change_password, name="change_password"),
    # path('password_reset', views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset/done', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
