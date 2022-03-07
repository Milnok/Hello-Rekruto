from django.shortcuts import render


def home(request):
    data = {
        'name': request.GET['name'],
        'message': request.GET['message'],
    }
    return render(request, 'rekruto/index.html', data)
