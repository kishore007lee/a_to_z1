from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home',views.home,name='home'),
    path('sign_up',views.sign_up,name='sign_up' ),
    path('sign_in',views.sign_in,name='sign_in' ),
    path('sign_out', views.sign_out, name='sign_out'),
    path('details', views.details, name='details'),
    path('Add_cart', views.Add_cart, name='Add_cart'),

]