from django.urls import path
from . import views

urlpatterns = [
    path("",views.register,name="register"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("home/",views.home,name="home"),
    path("add/",views.add_item,name="add"),
    path("edit/",views.edit_item,name="edit"),
    path("driver/",views.edit_driver,name="edit_driver"),
    path('update/<int:item_id>/',views.update_item,name='update'),
    path('update_driver/<int:driver_id>/',views.update_driver,name='update_driver'),
    path("delete/<int:id>/",views.delete_item,name="delete"),
    path('delete_d/<int:id>/',views.delete_driver, name='delete_d'),
    path("category/",views.category,name="category"),
    path("trip/",views.trip,name="trip"),
    path("point/",views.point,name="point"),
    path("password/",views.password,name="password"),
    path("vehicle/",views.vehicle,name="vehicle"),
    path("add_driver/",views.add_driver,name="add_driver"),
    path("home2/",views.home2,name="home2"),
    path("add_d/",views.add_d,name="add_d"),
    #trip
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/add/', views.add_trip, name='add_trip'),
    path('trips/edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),
    path('trips/delete/<int:trip_id>/', views.delete_trip, name='delete_trip'),
    
    ] 


