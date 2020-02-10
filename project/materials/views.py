from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .models import Material, Comment
from .forms import MaterialForm, CommentForm


def materials_list(request):
    """
    Функция вывода материалов списком
    :param request:
    :return:
    """
    materials = Material.objects.all()
    paginator = Paginator(materials, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    name = "Главная"
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'name': name,
    }
    return render(
        request,
        "materials/materials_list.html",
        context=context,
    )


def material_detail(request, pk):
    """
    Функция вывода полной версии материала с комментариями
    :param request:
    :param pk:
    :return:
    """
    material = get_object_or_404(Material, pk=pk)
    comments = material.comment_set.all()
    paginator = Paginator(comments, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    form = CommentForm()
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'material': material,
        'page_object': page,
        'form': form,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
    }
    return render(
        request,
        "materials/material_detail.html",
        context=context,
    )


def comment_add(request, pk):
    """
    Функция, обрабатывающия добавление коментария
    :param request:
    :param pk: int
    :return:
    """
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
    """
    Класс для создания материала
    """
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
