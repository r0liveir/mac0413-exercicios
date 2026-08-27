from enum import Enum


class TipoEntrega(Enum):
    PADRAO = 1
    EXPRESSA = 2
    REFRIGERADA = 3


class Entrega:

    def __init__(
        self,
        codigo,
        tipo,
        distancia_km,
        horas_refrigeracao=0.0,
    ):
        self.codigo = codigo
        self.tipo = tipo
        self.distancia_km = distancia_km
        self.horas_refrigeracao = horas_refrigeracao

    def calcular_custo(self):
        if self.tipo == TipoEntrega.PADRAO:
            return 8.00 + 1.50 * self.distancia_km

        if self.tipo == TipoEntrega.EXPRESSA:
            return 12.00 + 2.50 * self.distancia_km

        if self.tipo == TipoEntrega.REFRIGERADA:
            return (
                10.00
                + 1.80 * self.distancia_km
                + 5.00 * self.horas_refrigeracao
            )

        raise ValueError("Tipo de entrega desconhecido")


class Faturamento:

    def calcular_total(self, entregas):
        total = 0.0

        for entrega in entregas:
            total += entrega.calcular_custo()

        return total
