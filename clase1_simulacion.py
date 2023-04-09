"""Clase 1: Simulación de Monte Carlo"""

from math import exp, sqrt
from random import seed, gauss

import numpy as np  # No lo vimos aun pero necesitamos números pseudoaleatorios Poisson
rng = np.random.default_rng()


def gbm(st, delta_t, mu, sigma):
    """Simula un paso de Geometric Brownian Motion.

    Parámetros:
        st -- valor del stock
        delta_t -- tamaño del paso (en fraccción de año)
        mu -- retorno anual promedio proyectado del stock
        sigma -- volatilidad anual proyectada del stock
    """
    st *= exp((mu - .5 * sigma ** 2) * delta_t +
              sigma * sqrt(delta_t) * gauss(0., 1.))

    return st


def mjd(st, delta_t, mu_s, sig_s, lamb, mu_j, sig_j):
    """Simula un paso de Merton Jump-Diffusion.

    Parámetros:
        st -- valor del stock
        delta_t -- tamaño del paso (en fraccción de año)
        mu_s -- retorno anual promedio proyectado del stock
        sig_s -- volatilidad anual proyectada del stock
        lamb -- frecuencia del salto (Poisson)
        mu_j -- promedio de la magnitud del salto (Poisson)
        sig_j -- volatilidad de la magnitud del salto (Poisson)
    """
    st *= exp((mu_s - .5 * sig_s ** 2) * delta_t +
              sig_s * sqrt(delta_t) * gauss(0., 1.) +
              (mu_j + sig_j * gauss(0., 1.)) * rng.poisson(lamb))
    return st


def create_path(s0, days, generator_func, **kwrags):
    """Crea una trayectoria de precios.

    Parámetros:
        s0 -- valor inicial del stock
        days -- días a simular
        generator_func -- función generadora de pasos
        kwrags -- parámetros de la función generadora
    """
    output = [s0]

    for _ in range(days):
        output.append(generator_func(output[-1], **kwrags))

    return output


if __name__ == '__main__':
    seed(1234) # Comentar esto para obtener aleatoriedad
    rng = np.random.default_rng(1234) # Comentar esto para obtener aleatoriedad

    st = 100.

    for _ in range(1000):
        st = gbm(st, 1/365, .1, .05)
        # st = mjd(st, 1/365, .1, .05, .3, 0., .02)

        if st >= 130.:
            print('Target alcanzado. Toma de ganancia.')
            break

    else:
        print('Target no alcanzado.')

    print(st)

    # from matplotlib.pyplot import plot

    # plot(create_path(100., 365, gbm, delta_t=1/365, mu=.1, sigma=.05))
    # plot(create_path(100., 365, mjd, delta_t=1/365, mu_s=.1, sig_s=.05, lamb=0.3, mu_j=0., sig_j=.02))
