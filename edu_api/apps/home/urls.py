from django.urls import path

from home import views

urlpatterns = [
    path('banners/',views.BannerAPIView.as_view()),
    path('headers/',views.HeaderAPIView.as_view()),
    path('footers/',views.FooterAPIView.as_view()),
]