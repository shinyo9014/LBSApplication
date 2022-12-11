from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('map/', views.leaflet_map, name='map'),
    path('password/', views.change_password, name='password'),

]
