import requests

from datetime import datetime
date_of_issue: str = '01.12.2014'
base_currency: str = 'UAH'


def get_currency_iso_code(currency: str) -> int:
    currency_dict = {
        'CHF': 756,
        'EUR': 978,
        'GBP': 826,
        'PLN': 985,
        'RUB': 643,
        'SEK': 752,
        'UAH': 980,
        'USD': 840,
        'XAU': 959,
        'CAD': 124,
    }
    try:
        return currency_dict[currency]
    except:
        raise KeyError('Currency not found! Update currencies information')

def sale_rate_NB(sale_nb:str):
    sale_nb_dict ={
        'CHF': 15.6389750,
        'EUR': 18.7949200,
        'GBP': 23.6324910,
        'PLN': 4.4922010,
        'RUB': 0.3052700,
        'SEK': 2.0283750,
        'UAH': 1.0000000,
        'USD': 15.0564130,
        'XAU': 17747.7470000,
        'CAD': 13.2107400,
    }
    try:
        return sale_nb_dict[sale_nb]
    except:
        raise KeyError('SaleRateNB not found! Update SaleRateNB information')

    def purchase_rate(purchase: int) ->float:
        purchase_dict = {
            'CHF': 15.5,
            'EUR': 19.2,
            'GBP': 24,
            'PLN': 4.2,
            'RUB': 0.28,
            'USD': 15.35,
            'CAD': 13,
        }
        try:
            return purchase_dict[purchase]
        except:
            raise KeyError('PurchaseRate not found! Update PurchaseRate information')

        def sale_rate(sale: int) ->float:
            sale_dict = {
                'CHF': 17,
                'EUR': 20,
                'GBP': 25.8,
                'PLN': 5,
                'RUB': 0.32,
                'USD': 15.7,
                'CAD': 15,
            }
            try:
                return sale_dict[sale]
            except:
                raise KeyError('SaleRate not found! Update SaleRate information')

def get_currency_exchange_rate(currency_a: str,
                               currency_b: str) -> str:
    currency_code_a = get_currency_iso_code(currency_a)
    currency_code_b= get_currency_iso_code(currency_b)

    response = requests.get('https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014')
    json = response.json()

    if response.status_code == 200:
        for i in range(len(json)):
            if json[i].get('currencyCodeA') == currency_code_a and json[i].get('currencyCodeB') == currency_code_b:
                date = datetime.fromtimestamp(
                    float(json[i].get('date'))
                ).strftime('%Y-%m-%d %H:%M:%S')
                rate_buy = json[i].get('rateBuy')
                rate_sell = json[i].get('rateSell')
                return f'exchange rate {currency_a} to {currency_b} for {date}: \n rate buy - {rate_buy} \n rate sell - {rate_sell}'
            return f'Not found: exchange rate {currency_a} to {currency_b}'
    else:
        return f"Api error {response.status_code}: {json.get('errorDescription')}"




print(get_currency_exchange_rate('USD', 'UAH'))
