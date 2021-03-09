from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import datetime
import json
from .models import Notice

def index(request):
    url = 'https://finance.naver.com/item/main.nhn?code=053610'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    _nowVal = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    _nowVal = _nowVal.text
    #print(_nowVal)
    url = 'https://finance.naver.com/sise'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    _kospi = soup.select_one('#KOSPI_now')
    _kospi = _kospi.text
    #print(_kospi)
    _kosdaq = soup.select_one('#KOSDAQ_now')
    _kosdaq = _kosdaq.text
    #print(_kosdaq)
    stock = {'nowVal': _nowVal, 'kosdaq': _kosdaq, 'kospi': _kospi}
    return render(request, 'www/index.html', {'stock': stock})
def company_intro(request):
    return render(request, 'www/company_intro.html', {'message': 'company'})
def company_vision(request):
    return render(request, 'www/company_vision.html', {'message': 'vision'})
def company_history(request):
    return render(request, 'www/company_history.html', {'message': 'history'})
def company_orgnation(request):
    return render(request, 'www/company_orgnation.html', {'message': 'orgnation'})
def company_certificate(request):
    return render(request, 'www/company_certificate.html', {'message': 'certificate'})
def company_map(request):
    return render(request, 'www/company_map.html', {'message': 'map'})
def product_dispenser(request):
    return render(request, 'www/product_dispenser.html', {'message': 'dispenser'})
def product_diebonder(request):
    return render(request, 'www/product_diebonder.html', {'message': 'diebonder'})
def product_attach(request):
    return render(request, 'www/product_attach.html', {'message': 'attach'})


def finance_notice(request):
    notices = Notice.objects.all().order_by('-date')
    return render(request, 'www/finance_notice.html', {'notices': notices})



def finance_disclosure(request):
    with open("secret.json") as f:
        secrets = json.loads(f.read())
    DART_KEY = secrets['DART_KEY']
    date_ago = datetime.datetime.now() - datetime.timedelta(days=365)
    print(date_ago.strftime("%Y%m%d"))
    startDate = date_ago.strftime("%Y%m%d")
    url = 'https://opendart.fss.or.kr/api/list.json?crtfc_key='+DART_KEY+'&corp_code=00325112&bgn_de='+startDate
    response = requests.get(url)
    response.raise_for_status()
    return render(request, 'www/finance_disclosure.html', {'message': response.json()['list']})
