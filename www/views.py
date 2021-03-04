from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
import time

# Create your views here.
def index(request):
    stock=finance()
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
def notice(request):
    return render(request, 'www/notice.html', {'message': 'notice'})
def stock(request):
    return render(request, 'www/stock.html', {'message': 'stock'})
def product(request):
    return render(request, 'www/product.html', {'message': 'product'})



def finance():
    url = 'https://finance.naver.com/item/main.nhn?code=053610'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    _nowVal = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    _nowVal = _nowVal.text
    print(_nowVal)

    url = 'https://finance.naver.com/sise'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    _kospi = soup.select_one('#KOSPI_now')
    _kospi = _kospi.text
    print(_kospi)
    _kosdaq = soup.select_one('#KOSDAQ_now')
    _kosdaq = _kosdaq.text
    print(_kosdaq)

    stock = {'nowVal': _nowVal, 'kosdaq': _kosdaq, 'kospi': _kospi}
    return stock
