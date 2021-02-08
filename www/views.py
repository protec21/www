from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'www/index.html', {'message': 'index'})
def company(request):
    return render(request, 'www/company.html', {'message': 'company'})
def vision(request):
    return render(request, 'www/vision.html', {'message': 'vision'})
def history(request):
    return render(request, 'www/history.html', {'message': 'history'})
def orgnation(request):
    return render(request, 'www/orgnation.html', {'message': 'orgnation'})
def certificate(request):
    return render(request, 'www/certificate.html', {'message': 'certificate'})
def map(request):
    return render(request, 'www/map.html', {'message': 'map'})
def stocknotice(request):
    return render(request, 'www/stocknotice.html', {'message': 'stocknotice'})
def stock(request):
    return render(request, 'www/stock.html', {'message': 'stock'})
def product(request):
    return render(request, 'www/product.html', {'message': 'product'})
