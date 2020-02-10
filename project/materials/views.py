from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.shortcuts import redirect

from .models import Material, Comment
from .forms import MaterialForm, CommentForm


def materials_list(request):
    materials = Material.objects.all()
    name = "Главная"
    return render(
        request,
        "materials/materials_list.html",
        context={"materials": materials, "name": name},
    )


def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)
    # material = Material.objects.get(pk=pk)
    comments = material.comment_set.all()
    form = CommentForm()
    return render(
        request,
        "materials/material_detail.html",
        context={"material": material, "comments": comments, "form": form},
    )


def comment_add(request, pk):
    bound_form = CommentForm(request.POST)
    material = get_object_or_404(Material, pk=pk)
    if bound_form.is_valid():
        comment = Comment()
        comment.material = material
        comment.author = bound_form.cleaned_data["author"]
        comment.body = bound_form.cleaned_data["body"]
        comment.save()
    return redirect(material.get_absolute_url())


class MaterialCreate(View):
    def get(self, request):
        form = MaterialForm()
        return render(
            request, "materials/material_create_form.html", context={"form": form}
        )

    def post(self, request):
        bound_form = MaterialForm(request.POST)
        if bound_form.is_valid():
            new_material = bound_form.save()
            return redirect(new_material)
        return render(
            request, "materials/material_create_form.html", context={"form": bound_form}
        )
