from django.shortcuts import render
from django.views.generic import View

from .models import Material


def materials_list(request):
    materials = Material.objects.all()
    name = 'Главная'
    return render(request, 'materials/materials_list.html', context={'materials': materials, 'name': name})
