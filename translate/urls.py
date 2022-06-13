from django.urls import path

from . import views

app_name = 'translate'

urlpatterns = [
    path('', views.get_translated, name="get-translated"),
]
