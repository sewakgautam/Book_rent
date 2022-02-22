from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index" ),
    path('login/', Login.as_view(), name="login" ),
    path('logout/', Logout_view, name="logout" ),
    path('cart/', Cart.as_view(), name="cart" ),
    path('items/<int:pk>/', ItemView.as_view(), name="item" ),
]
