from django.urls import path
from . import views

### goes to the hellow function/method inside views.py ###  
urlpatterns = [
path('', views.hello, name="hello"),
]


