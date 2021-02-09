from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    stock = getStock()
    return render(request, 'www/index.html', {'stock': stock})
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






import re
import requests
def getStock():
    url = 'http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code=053610'
    req = requests.get(url).content

    CurJuka = re.search(r'CurJuka=\"[0-9,]+\"', str(req))
    CurJuka = CurJuka.group()
    CurJuka = CurJuka.replace('CurJuka=','')
    CurJuka = CurJuka.replace('"', '')

    kospiJisu = re.search(r'kospiJisu=\"[0-9.]+\"', str(req))
    kospiJisu = kospiJisu.group()
    kospiJisu = kospiJisu.replace('kospiJisu=','')
    kospiJisu = kospiJisu.replace('"', '')

    kosdaqJisu = re.search(r'kosdaqJisu=\"[0-9.]+\"', str(req))
    kosdaqJisu = kosdaqJisu.group()
    kosdaqJisu = kosdaqJisu.replace('kosdaqJisu=', '')
    kosdaqJisu = kosdaqJisu.replace('"', '')

    stock = {'CurJuka':CurJuka, 'kospiJisu':kospiJisu, 'kosdaqJisu':kosdaqJisu}
    return stock
