from . import views
from django.urls import path


urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('mainpage/',views.mainpage,name='mainpage'),
    path('data/',views.data,name='data'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('logout/',views.logout,name='logout'),
    path('update/<str:pk>/',views.update,name='update'),
    
]