from django.urls import path
from .views import *

urlpatterns = [
    path('Register/', UserRegister.as_view()),
    path('Login/', UserLogin.as_view()),
    path('Logout/', UserLogout.as_view()),
    path('ItemPost/', ItemPost.as_view()),
    path('GetAllItems/', GetAllItems.as_view()),
    path('GetAllUser/', GetAllUser.as_view()),
    path('OrderItem/', OrderItemPost.as_view()),
    path('GetOrder/<int:UserId>/', GetAllOrderUser.as_view())
]
