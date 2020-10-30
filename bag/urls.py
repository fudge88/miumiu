from django.urls import path
from . import views

# urls in association with the bag app
urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('edit/<item_id>/', views.edit_bag, name='edit_bag'),
    path('remove/<item_id>/', views.remove_item, name='remove_item'),
]
