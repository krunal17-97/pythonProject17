from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home, name='home'),
    path('product/', views.product),
    path('user/', views.users),
    path('createorder', views.createOrder),
    path('updateorder/<str:pk>/', views.updateOrder, name= 'updateorder'),
    path('deleteorder/<str:pk>/',views.deleteOrder, name= 'deleteorder'),
]