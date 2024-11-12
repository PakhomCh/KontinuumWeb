from django.shortcuts import redirect


def initial(request):
    return redirect('ru/', permanent=True)
