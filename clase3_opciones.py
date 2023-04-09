"""Clase 3: Arrancano con POO"""

class Opcion:
    def __init__(self, tipo_de_opcion, strike):
        self._type = tipo_de_opcion
        self._strike = strike

    def __repr__(self):
        return f'{self._type} @ {self._strike:,.2f}'


class Call(Opcion):
    def __init__(tipo_de_opcion, strike):
        super().__init__('Call', strike)

    def get_payoff(self, spot):
        return max(spot - self._strike, 0)


class Put(Opcion):
    def __init__(self, strike):
        super().__init__('Put', strike)

    def get_payoff(self, spot):
        return max(self._strike - spot, 0)


if __name__ == '__main__':
    call = Call(10)
    print(call)
    print(call.get_payoff(12))

    put = Put(10)
    print(put)
    print(put.get_payoff(12))
