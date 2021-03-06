from django.urls import path, include

from .views import *

urlpatterns = [
    path("", materials_list, name="materials_list_url"),
    path("material/create/", MaterialCreate.as_view(), name="material_create_url"),
    path("material/<int:pk>/", material_detail, name="material_detail_url"),
    path("comments/<int:pk>/", comment_add, name="comment_add_url"),
    path("votes/", include("votes.urls")),
]
