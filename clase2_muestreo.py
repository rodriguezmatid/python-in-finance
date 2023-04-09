"""Clase 2: Muestreo y limpieza de datos."""

# %%
# Imports
from collections import namedtuple
from datetime import datetime, timedelta
from math import prod
from random import choices, seed
from statistics import mean
from typing import Callable

import yfinance as yf


# %%
# Definiciones
Metrics = namedtuple('Metrics', ['mean', 'percentil_025', 'percentil_975'])


def compute_returns(prices: list) -> list:
    '''Calcula la serie de retornos dada una serie de precios'''

    return [t / t_1 - 1. for t, t_1 in zip(prices[1:], prices[:-1])]
    #return [(sample[i] / sample[i - 1]) - 1.0 for i in range(1, len(sample))]


def percentile(returns: list, q: float) -> float:
    '''Retorna observación de corte para un percentil q de una serie de retornos'''

    n = len(returns)
    p = int(n * (q / 100))

    sorted_returns = sorted(returns)

    return sorted_returns[p]


def remove_outliers(sample: list) -> list:
    '''Remueve los outliers de una muestra de datos por el método IQR'''
    q1 = percentile(sample, 25)
    q3 = percentile(sample, 75)

    iqr = q3 - q1

    return [s for s in sample if s > q1 - 1.5 * iqr and s < q3 + 1.5 * iqr]


def bootstrap(aggregation_function: Callable[[list], float], returns: list,
              n_boostraps: int, bootstrap_size: int, **kwargs) -> Metrics:
    '''Retorna promedios de una función de agregación por bootstraping

    Parámetros:
        aggregation_function -- función de agregación
        returns -- serie de retornos
        n_bootstraps -- cantidad de bootstraps a realizar
        bootstrap_size -- tamaño de cada bootstrap
        kwargs -- argumentos adicionales para la función de transformación
    '''
    results = []

    for _ in range(n_boostraps):
        s = choices(returns, k=bootstrap_size)
        agg_result = aggregation_function(s, **kwargs)
        results.append(agg_result)

    m = mean(results)
    pl = percentile(results, 2.5)
    pu = percentile(results, 97.5)

    return Metrics(m, pl, pu)


# %%
# Obtengo los datos
yahoo_data = yf.download('MSFT', start=datetime.today() - timedelta(days=180),
                         end=datetime.today(), progress=False)

prices = yahoo_data.loc[:, 'Close'].tolist()  # Pandas DataFrame que NO vimos aún!


# %%
# Realizo el análisis
returns = compute_returns(prices)
returns_clean = remove_outliers(returns)

seed(1234)
orig_metrics = bootstrap(lambda x: prod(1 + r for r in x) - 1., returns, 1_000, 100)
clean_merics = bootstrap(lambda x: prod(1 + r for r in x) - 1., returns_clean, 1_000, 100)


print('--- Bootstrapped (1000 corridas de 100 observaciones) Returns Statistics ---')

print('Original sample')
print(f'  Mean:             {orig_metrics.mean:8.4%}')
print(f'   2.5% Percentile: {orig_metrics.percentil_025:8.4%}')
print(f'  97.5% Percentile: {orig_metrics.percentil_975:8.4%}')

print('\nCleaned sample')
print(f'  Mean:             {clean_merics.mean:8.4%}')
print(f'   2.5% Percentile: {clean_merics.percentil_025:8.4%}')
print(f'  97.5% Percentile: {clean_merics.percentil_975:8.4%}')
