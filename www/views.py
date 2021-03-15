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
def investment_disclosure(request):
    with open("secret.json") as f:
        secrets = json.loads(f.read())
    DART_KEY = secrets['DART_KEY']
    date_ago = datetime.datetime.now() - datetime.timedelta(days=365)
    print(date_ago.strftime("%Y%m%d"))
    startDate = date_ago.strftime("%Y%m%d")
    url = 'https://opendart.fss.or.kr/api/list.json?crtfc_key='+DART_KEY+'&corp_code=00325112&bgn_de='+startDate
    response = requests.get(url)
    response.raise_for_status()
    return render(request, 'www/investment_disclosure.html', {'message': response.json()['list']})




def investment_stock(request):
    url = 'https://finance.naver.com/item/sise.nhn?code=053610'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    _현재가 = soup.select_one('#_nowVal').text
    _전일대비 = soup.select_one('#_diff').text
    _전일대비 = _전일대비.replace("상승", "▲")
    _전일대비 = _전일대비.replace("하락", "▼")
    _등락률 = soup.select_one('#_rate').text
    _시가 = soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(4) > span:nth-child(1)').text
    _고가52 = soup.select_one('#_high').text
    _저가52 = soup.select_one('#_low').text
    _거래량 = soup.select_one('#_quant').text
    _전일가 = soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(4) > span:nth-child(1)').text
    _최고 = soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(11) > td:nth-child(2) > span:nth-child(1)').text
    _최저 = soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(11) > td:nth-child(4) > span:nth-child(1)').text
    _상한가    =   soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(2) > span:nth-child(1)').text
    _하한가    =   soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(9) > td:nth-child(2) > span:nth-child(1)').text
    _PER = soup.select_one('#_sise_per').text
    _액면가    =   soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2) > span:nth-child(1)').text
    _상장주식수  =   soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(12) > td:nth-child(4) > span:nth-child(1) > span:nth-child(1)').text
    _시가총액   =   soup.select_one('.type_tax > tbody:nth-child(2) > tr:nth-child(12) > td:nth-child(2) > span:nth-child(1)').text





    url = 'http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code=053610'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    dailystocks = {}
    for dailystock in soup.findAll('dailystock'):
        day = {}
        day['day_date'] = dailystock['day_date']
        day['day_dungrak'] = dailystock['day_dungrak']
        day['day_endprice'] = dailystock['day_endprice']
        day['day_getamount'] = dailystock['day_getamount']
        day['day_getdebi'] = dailystock['day_getdebi']
        day['day_high'] = dailystock['day_high']
        day['day_low'] = dailystock['day_low']
        day['day_start'] = dailystock['day_start']
        day['day_volume'] = dailystock['day_volume']
        dailystocks[dailystock['day_date']] = day
    print(dailystocks)

    url = 'https://finance.naver.com/item/main.nhn?code=053610'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    매도1 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(2) > td:nth-child(1)').text
    매도2 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(3) > td:nth-child(1)').text
    매도3 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(4) > td:nth-child(1)').text
    매도4 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(5) > td:nth-child(1)').text
    매도5 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(6) > td:nth-child(1)').text

    매수1 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(2) > td:nth-child(3)').text
    매수2 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(3) > td:nth-child(3)').text
    매수3 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(4) > td:nth-child(3)').text
    매수4 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(5) > td:nth-child(3)').text
    매수5 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(6) > td:nth-child(3)').text

    매도1거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(2) > td:nth-child(2) > em:nth-child(1)').text
    매도2거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(3) > td:nth-child(2) > em:nth-child(1)').text
    매도3거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(4) > td:nth-child(2) > em:nth-child(1)').text
    매도4거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(5) > td:nth-child(2) > em:nth-child(1)').text
    매도5거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(6) > td:nth-child(2) > em:nth-child(1)').text

    매수1거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(2) > td:nth-child(4) > em:nth-child(1)').text
    매수2거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(3) > td:nth-child(4) > em:nth-child(1)').text
    매수3거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(4) > td:nth-child(4) > em:nth-child(1)').text
    매수4거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(5) > td:nth-child(4) > em:nth-child(1)').text
    매수5거래량 = soup.select_one('div.section:nth-child(9) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(5) > tr:nth-child(6) > td:nth-child(4) > em:nth-child(1)').text


    stock = {
        '현재가': _현재가, '전일대비': _전일대비, '등락률': _등락률, '시가': _시가, '고가52': _고가52, '저가52': _저가52, '거래량': _거래량,
        '전일가': _전일가, "최고": _최고, "최저": _최저, '상한가': _상한가, '하한가': _하한가, 'PER': _PER, '액면가': _액면가, '상장주식수': _상장주식수, '시가총액': _시가총액,
    }

    frgn = {
        '매도1': 매도1, '매도2': 매도2, '매도3': 매도3, '매도4': 매도4, '매도5': 매도5,
        '매수1': 매수1, '매수2': 매수2, '매수3': 매수3, '매수4': 매수4, '매수5': 매수5,
        '매도1거래량': 매도1거래량, '매도2거래량': 매도2거래량, '매도3거래량': 매도3거래량, '매도4거래량': 매도4거래량, '매도5거래량': 매도5거래량,
        '매수1거래량': 매수1거래량, '매수2거래량': 매수2거래량, '매수3거래량': 매수3거래량, '매수4거래량': 매수4거래량, '매수5거래량': 매수5거래량
    }

    return render(request, 'www/investment_stock.html', {'stock': stock, 'frgn': frgn, 'dailystocks': dailystocks})

def investment_finance(request):
    return render(request, 'www/investment_finance.html', {'finance': 'finance'})
def investment_notice(request):
    notices = Notice.objects.all().order_by('-date')
    return render(request, 'www/investment_notice.html', {'notices': notices})
