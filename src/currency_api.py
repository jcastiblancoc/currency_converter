import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_currency_list():
    url = "https://api.freecurrencyapi.com/v1/currencies"
    params = {
        'apikey': os.getenv('CURRENCY_API_KEY')
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        currency_list = {}

        if 'data' in data:
            for code, details in data['data'].items():
                currency_list[code]= details['name']

    return currency_list


def get_exchange_rates(base_currency):
    url = "https://api.freecurrencyapi.com/v1/latest"

    params = {
        'apikey': os.getenv('CURRENCY_API_KEY'),
        'base_currency': base_currency or None
    }

    try:
        response = requests.get(url, params=params)
    except :
        return {}

    return response.json().get('data', {})


def get_custom_exchange_rates(base_currency, target_currencies):
    url = "https://api.freecurrencyapi.com/v1/latest"

    currencies= ','.join([currency.strip() for currency in target_currencies.split(',')])
    params = {
        'apikey': os.getenv('CURRENCY_API_KEY'),
        'base_currency': base_currency,
        'currencies': currencies
    }
    try:
        response = requests.get(url, params=params)
    except:
        return {}

    return response.json().get('data', {})


def get__exchange_value(base_currency, target_currency):
    url = "https://api.freecurrencyapi.com/v1/latest"

    params = {
        'apikey': os.getenv('CURRENCY_API_KEY'),
        'base_currency': base_currency,
        'currencies': target_currency
    }
    try:
        response = requests.get(url, params=params)
    except:
        return {}

    return response.json().get('data', {})
