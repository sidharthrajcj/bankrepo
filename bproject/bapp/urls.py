from django.urls import path
from . import views
app_name='bapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>/', views.district_dropdown, name='district_dropdown'),
]
