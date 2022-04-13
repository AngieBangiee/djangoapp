from django.shortcuts import render

def home(request):
    return render(request, 'modeltermpapers/home.html')  


def prices(request): 
    return render(request, 'modeltermpapers/prices.html') 


def about(request): 
    return render(request, 'modeltermpapers/about.html')


def services(request): 
    return render(request, 'modeltermpapers/services.html')


def guarantees(request): 
    return render(request, 'modeltermpapers/guarantees.html')


def termpapers(request): 
    return render(request, 'modeltermpapers/custom-term-papers.html')

def order(request): 
    return render(request, 'modeltermpapers/order.html')