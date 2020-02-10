from django.shortcuts import redirect


def redirect_kanobu(request):
    return redirect("materials_list_url", permanent=True)
