from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    try:
        data = {
            'name': request.GET['name'],
            'message': request.GET['message'],
        }
    except MultiValueDictKeyError:
        return render(request, 'rekruto/index.html')
    return render(request, 'rekruto/index.html', data)
