"""Clase 1: Análisis Técnico"""

from statistics import mean, stdev


def bollinger_bands(todays_price, hist_data, calc_days=20):
    """Indicador de Bandas de Bollinger.
    https://www.investopedia.com/terms/b/bollingerbands.asp

    Parámetros:
        todays_price -- precio actual del activo
        hist_data -- list con precios ANTERIORES a todays_price
        calc_days -- días a considerar en la ventana (default: 20)

    Retorna:
        1 (compra) / -1 (venta) / 0 (no hacer nada)
    """
    data = hist_data[-calc_days:]
    ma = mean(data)
    std = stdev(data)

    BOLU = ma + 2 * std
    BOLD = ma - 2 * std

    if todays_price >= BOLU:
        return -1
    elif todays_price <= BOLD:
        return 1
    else:
        return 0


def rsi(todays_price, hist_data, calc_days=20, min_val=30, max_val=70):
    """Indicador de RSI.
    https://www.investopedia.com/terms/r/rsi.asp

    Parámetros:
        todays_price -- precio actual del activo
        hist_data -- list con precios ANTERIORES a todays_price
        calc_days -- días a considerar en la ventana (default: 20)
        min_val -- umbral mínimo (default: 30)
        max_val -- umbral máximo (default: 70)

    Retorna:
        1 (compra) / -1 (venta) / 0 (no hacer nada)
    """
    data = [hist_data[t+1] / hist_data[t] - 1 for t in range(-calc_days-1, -1)]

    rs = sum(r for r in data if r > 0) / sum(-r for r in data if r < 0)
    # NOTAS: a) -r es porque la perdida se debe tomar con signo positivo
    #        b) sum es lo mismo que mean en este caso porque ambas medias tienen
    #           el mismo denominador y se pueden simplificar.

    rsi = 100 - (100 / (1 + rs))

    if rsi >= max_val:
        return -1
    elif rsi <= min_val:
        return 1
    else:
        return 0


def fast_stochastic(todays_price, hist_data, min_val=20, max_val=80):
    """Indicador de Fast Stochastic.
    https://www.investopedia.com/terms/s/stochasticoscillator.asp

    Parámetros:
        todays_price -- precio actual del activo
        hist_data -- list con precios ANTERIORES a todays_price
        min_val -- umbral mínimo (default: 20)
        max_val -- umbral máximo (default: 80)

    Retorna:
        1 (compra) / -1 (venta) / 0 (no hacer nada)
    """
    # NOTA: Para este indicador haremos caso omiso de high/low prices, usaremos
    #       el precio de cierre unicamente.
    data = hist_data[-14:]
    L14 = min(data)
    M14 = max(data)

    K = (todays_price - L14) / (M14 - L14) * 100

    if K >= max_val:
        return -1
    elif K <= min_val:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # 1. Importar los datos de 'data/crypto.json'
    import json

    data = json.load(open('./data/crypto.json'))

    # 2. Trabajar sobre la serie 'BTC'
    tgt_series = data['BTC']

    # 3. Considerar como precio actual el ubicado en la posición 100
    todays_price = tgt_series[100]
    hist_data = tgt_series[:100]

    # 4. Ejecutar indicadores con parámetros por default
    print('Bollinger       :', bollinger_bands(todays_price, hist_data))
    print('RSI             :', rsi(todays_price, hist_data))
    print('Fast Stochastic :', fast_stochastic(todays_price, hist_data))
