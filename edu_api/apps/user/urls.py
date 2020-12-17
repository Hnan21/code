from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from user import views


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('captcha/', views.CaptchaAPIView.as_view()),
    path('users/', views.UserAPIView.as_view()),
    path('message/', views.SendMessageAPIView.as_view()),
    path("register/", views.UserAPIView.as_view()),
    path("phone/", views.Phone.as_view({'post': 'phone'})),
    path("login_phone/", views.PhoneModelViewSet.as_view({'post': 'login_phone'})),  # 短信登录
    path("phone_code/", views.PhonesModelViewSet.as_view({'post': 'phone_code'})),#登录检测手机号
]