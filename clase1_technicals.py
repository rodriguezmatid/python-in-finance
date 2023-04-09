"""Clase 1: Análisis Técnico"""


def bollinger_bands(todays_price, hist_data, calc_days):
    """Indicador de Bandas de Bollinger.
    https://www.investopedia.com/terms/b/bollingerbands.asp

    Parámetros:
        todays_price -- precio actual del activo
        hist_data -- list con precios ANTERIORES a todays_price
        calc_days -- días a considerar en la ventana (default: 20)

    Retorna:
        1 (compra) / -1 (venta) / 0 (no hacer nada)
    """
    pass


def rsi(todays_price, hist_data, calc_days, min_val, max_val):
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
    pass


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
    pass


if __name__ == '__main__':
    # 1. Importar los datos de 'data/crypto.json'
    # 2. Trabajar sobre la serie 'BTC'
    # 3. Considerar como precio actual el ubicado en la posición 100
    # 4. Ejecutar indicadores con parámetros por default

    pass
