"""Funciones para consultar Binance"""
import json
from datetime import timedelta, datetime

import requests


_URL = 'https://api.binance.com'


def get_available_pairs():
    """Retorna lista de pares disponibles en Binance."""
    try:
        req = requests.get(_URL + '/api/v3/ticker/price')

        return sorted([r['symbol'] for r in req.json()])

    except Exception as e:
        raise RuntimeError('Error en la consulta')


def get_last_price(symbol):
    """Retorna precios de Binance.\n
    Parámetros:\n
        symbol -- (str o list[str]) par/es a solicitar
    """
    if isinstance(symbol, str):
        _params={'symbol': symbol}
    elif isinstance(symbol, list):
        _params={'symbols': json.dumps(symbol).replace(', ', ',')}
    else:
        raise RuntimeError('El parámetro symbol debe ser un str o list[str]')

    try:
        req = requests.get(_URL + '/api/v3/ticker/price', params=_params)

        if isinstance(symbol, str):
            return float(req.json()['price'])
        else:
            return {r['symbol']: float(r['price']) for r in req.json()}

    except:
        raise RuntimeError('Error en la consulta')


def get_price(symbol, tgt_date):
    """Retorna precio cierre de Binance para un par en una fecha dada.\n
    Parámetros:\n
        symbol -- (str) par a solicitar\n
        tgt_date -- (str o datetime) Fecha de formato ISO (ej. 'YYYY-MM-DD') o datetime
    """
    t_date = datetime.fromisoformat(tgt_date) if isinstance(tgt_date, str) else tgt_date

    try:
        data = get_historical_prices(symbol, t_date - timedelta(days=1), t_date)
        return data[-1][1]

    except:
        raise RuntimeError('Error en la consulta')


def get_historical_prices(symbol, start_date, end_date):
    """Retorna precios históricos de cierre de Binance para un par.\n
    Parámetros:\n
        symbol -- (str) par a solicitar\n
        start_dt -- (str o datetime) Fecha de formato ISO (ej. 'YYYY-MM-DD') o datetime\n
        end_dt -- (str o datetime) Fecha de formato ISO (ej. 'YYYY-MM-DD') o datetime
    """
    s_date = datetime.fromisoformat(start_date) if isinstance(start_date, str) else start_date
    e_date = datetime.fromisoformat(end_date) if isinstance(end_date, str) else end_date

    _params = {'symbol': symbol, 'interval': '1d', 'limit': 1000,
               'startTime': int(s_date.timestamp() * 1000),
               'endTime': int(e_date.timestamp() * 1000)}

    try:
        req = requests.get(_URL + '/api/v3/klines', params=_params)
        return [(datetime.utcfromtimestamp(r[6] / 1000), float(r[4]))
                for r in req.json()]

    except:
        raise RuntimeError('Error en la consulta')


if __name__ == '__main__':

    print(get_last_price('BTCUSDT'))
    print(get_last_price(['BTCUSDT', 'ETHUSDT']))
    print(get_historical_prices('BTCUSDT', datetime(2022, 1, 1), datetime(2022, 1, 31)))
    print(get_price('BTCUSDT', '2022-10-25'))
    # print(get_available_pairs())
