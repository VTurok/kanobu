from django.urls import path, include

from .views import materials_list

urlpatterns = [
    path('', materials_list, name='materials_list_url'),
]