from rest_framework.generics import ListAPIView

from home.models import Banner, Nav
from home.serializers import BannerModelSerializer,NavModelSerializer


class BannerAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer


class HeaderAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, is_position=1).order_by("orders")
    serializer_class = NavModelSerializer


class FooterAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, is_position=2).order_by("orders")
    serializer_class = NavModelSerializer