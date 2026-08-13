## Definições
class Veiculo:
    def __init__(self, placa, qnt_horas):
        self.placa = placa 
        self.qnt_horas = qnt_horas

    def calcularValor(self) -> float: # type:ignore
        """Subclasse deverá implementar isso"""
        ...

class Carro(Veiculo):
    def calcularValor(self) -> float:
        primeira_hora = 8.0
        hora_add = 4.0
        valor_max = 30.0
        if self.qnt_horas == 1:
            return primeira_hora
        
        qnt_add = self.qnt_horas-1
        total_value = (qnt_add * hora_add) + primeira_hora
        return min(total_value, valor_max)

class Motocicleta(Veiculo):
    def calcularValor(self) -> float:
        primeira_hora = 5.0
        hora_add = 2.0
        valor_max = 18.0
        if self.qnt_horas == 1:
            return primeira_hora
        
        qnt_add = self.qnt_horas-1
        total_value = (qnt_add * hora_add) + primeira_hora
        return min(total_value, valor_max)
    
class Estacionamento:
    def __init__(self):
        self.lista_veiculos: list[Veiculo] = []

    def registrarVeiculo(self, tipo, placa, horas):
        if horas <= 0:
            return 

        if tipo == 'C':
            veiculo = Carro(placa=placa, qnt_horas=horas)
            self.lista_veiculos.append(veiculo)
        elif tipo == 'M':
            veiculo = Motocicleta(placa=placa, qnt_horas=horas)
            self.lista_veiculos.append(veiculo)
    
    def calcularTotal(self):
        valor_total = 0
        for v in self.lista_veiculos:
            valor_total += v.calcularValor()
        
        return valor_total

    def calculatQntVeiculos(self):
        return len(self.lista_veiculos)

## Execução
N = int(input())
estacionamento = Estacionamento()

for _ in range(N):
    line = input().split()
    tipo, placa, qnt_horas = line[0], line[1], int(line[2])

    estacionamento.registrarVeiculo(tipo, placa, qnt_horas)

qnt_veiculos = estacionamento.calculatQntVeiculos()
print("ESTACIONAMENTO")
if qnt_veiculos == 0:
    print("NENHUM VEICULO VALIDO")
else:
    for v in estacionamento.lista_veiculos:
        tipo = 'CARRO' if isinstance(v, Carro) else "MOTO"
        print(f'{v.placa} - {tipo} - {v.qnt_horas} h - R$ {v.calcularValor():.2f}')

print(f'VEICULOS: {qnt_veiculos}')
print(f'TOTAL: R$ {estacionamento.calcularTotal():.2f}')
