from django.urls import path

from cart import views

urlpatterns = [
    path("option/", views.CartViewSet.as_view({"post": "add_cart", "get": "list_cart",
                                               "delete": "delete_course","patch":"patch_course",'put':'put_cart'})),
    path("order/", views.CartViewSet.as_view({"get": "get_select_courses"})),


]
