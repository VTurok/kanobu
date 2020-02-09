from django.urls import path, include

from .views import *

urlpatterns = [
    path('', materials_list, name='materials_list_url'),
    path('material/create/', MaterialCreate.as_view(), name='material_create_url'),
]