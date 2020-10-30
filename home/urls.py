from django.urls import path
from . import views

# urls in association with the home app
urlpatterns = [
    path('', views.index, name='home'),
    path('location', views.location, name='location')
]
