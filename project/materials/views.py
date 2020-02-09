from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

from .models import Material
from .forms import MaterialForm


def materials_list(request):
    materials = Material.objects.all()
    name = 'Главная'
    return render(request, 'materials/materials_list.html', context={'materials': materials, 'name': name})

def material_detail(request, pk):
    material = Material.objects.get(pk=pk)
    return render(request, 'materials/material_detail.html', context={'material': material})

class MaterialCreate(View):
    def get(self, request):
        form = MaterialForm()
        return render(request, 'materials/material_create_form.html', context={'form': form})

    def post(self, request):
        bound_form = MaterialForm(request.POST)
        if bound_form.is_valid():
            new_material = bound_form.save()
            return redirect(new_material)
        return render(request, 'materials/material_create_form.html', context={'form': bound_form})