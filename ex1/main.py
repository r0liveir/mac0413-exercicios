from decimal import Decimal
import sys

# Classes
class Produto: 
    def __init__(self, codigo: int, nome: str, preco: Decimal):
        self.codigo = codigo
        self.nome = nome 
        self.preco = preco

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto 
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self):
        self.lista_pedidos: dict[int, ItemPedido] = {}
    
    def adicionar_pedido(self, item_pedido: ItemPedido):
        if item_pedido.produto.codigo in self.lista_pedidos:
            item = self.lista_pedidos[item_pedido.produto.codigo]
            item.quantidade += item_pedido.quantidade
        else:
            self.lista_pedidos[item_pedido.produto.codigo] = item_pedido

    def calcular_subtotal(self):
        lista_precos = [item.subtotal() for _, item in self.lista_pedidos.items()]
        # for terminal being nitipicky about output 
        if not lista_precos:
            return Decimal('0.00')
        return sum(lista_precos)

    def calcular_desconto(self):
        subtotal = self.calcular_subtotal()
        if subtotal >= 100:
            return subtotal * Decimal('0.10')
        else: 
            return Decimal('0.00')
    
    def calcular_valor_total(self):
        return self.calcular_subtotal() - self.calcular_desconto()
    
produtos = {
    1: Produto(1, 'X-Salada', Decimal('20.00')),
    2: Produto(2, 'Suco', Decimal('7.50')),
    3: Produto(3, 'Batata Frita', Decimal('12.00')),
    4: Produto(4, 'Cafe', Decimal('5.00')),
    5: Produto(5, 'Pudim', Decimal('10.00')),
}

def pedido_valido(codigo: int, quantidade: int) -> bool:
    if not (1 <= codigo <= 5) or quantidade <= 0:
        return False
    
    return True

input = sys.stdin.readline
N = int(input())


# Process data
pedido = Pedido()
qnt_pedidos = 0

for _ in range(N):
    line = input().split()
    item, quantity = int(line[0]), int(line[1])

    if pedido_valido(item, quantity):
        item_pedido = ItemPedido(produto=produtos[item],quantidade=quantity)
        pedido.adicionar_pedido(item_pedido)
        qnt_pedidos += 1

# print data
print("PEDIDO")
if qnt_pedidos == 0:
    print("NENHUM ITEM VALIDO")
else:
    for _, p in pedido.lista_pedidos.items():
        print(f"{p.produto.nome} {p.quantidade} x {p.produto.preco:.2f} = {p.subtotal():.2f}")

print(f"SUBTOTAL: {pedido.calcular_subtotal():.2f}")
print(f"DESCONTO: {pedido.calcular_desconto():.2f}")
print(f"TOTAL: {pedido.calcular_valor_total():.2f}", end="")

