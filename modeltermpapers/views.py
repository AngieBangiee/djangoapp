from django.shortcuts import render

def home(request):
    return render(request, 'modeltermpapers/home.html')  


def prices(request, name='prices'):
    name = name
    return render(request, 'modeltermpapers/prices.html', {'context': name}) 