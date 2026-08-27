from abc import abstractmethod, ABC


class Cobravel(ABC):
    @abstractmethod
    def calcular_custo(self,) -> float:
        pass

class Faturamento:

    def calcular_total(self, entregas: list[Cobravel]) -> float:
        total = 0.0

        for entrega in entregas:
            total += entrega.calcular_custo()

        return total
    
class Entrega(Cobravel):
    
    def __init__(self, codigo: str, distancia_km: float):
        self.codigo = codigo
        self.distancia_km = distancia_km 
        
class EntregaPadrao(Entrega):
    def calcular_custo(self) -> float:
        return 8.00 + 1.50 * self.distancia_km

class EntregaExpressa(Entrega):
    def calcular_custo(self) -> float:
        return 12.00 + 2.50 * self.distancia_km

class EntregaRefrigerada(Entrega):
    
    def __init__(self, codigo: str, distancia_km: float, horas_refrigeracao: float) -> None:
        super().__init__(codigo, distancia_km)
        self.horas_refrigeracao = horas_refrigeracao
        
    def calcular_custo(self) -> float:
        return (10.00 + 1.80 * self.distancia_km + 5.00 * self.horas_refrigeracao)