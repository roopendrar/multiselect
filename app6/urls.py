from django.urls import path
from app6 import views
app_name="app6"


urlpatterns = [
    path('register/',views.register,name="register"),
    path('img/',views.img_upld,name="img"),
]
