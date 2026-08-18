
class Item:
    def __init__(self, item, preco, quantidade):
        self.item = item
        self.preco = preco
        self.quantidade = quantidade
        
    def calculaDescontoItem(self):
        if self.item == "LIVRO":
            return self.preco * self.quantidade * 0.05
        elif self.item == "ELETRONICO":
            return self.preco * self.quantidade * 0.02
        return 0.0

class Cliente:
    def __init__(self, tipo=""):
        self.tipo = tipo
        
    def calculaDescontoCliente(self, subtotal):
        if (self.tipo == "PREMIUM"):
            return subtotal * 0.10
        return 0.0

class Entrega:
    def __init__(self, tipo=""):
        self.tipo = tipo
        
    def calculaFrete(self, total):
        if ((self.tipo == "NORMAL") and (total < 150.0)):
            return 12.0
        elif (self.tipo == "EXPRESSA"):
            return 25.0
        return 0.0

class Pedido:
    def __init__(self, cliente, entrega):
        self.cliente = cliente
        self.entrega = entrega
        self.carrinho = []

    def calculaSubtotal(self):
        subtotal = 0.0
        desconto = 0.0
        for item in self.carrinho:
            subtotal += item.preco * item.quantidade
            desconto += item.calculaDescontoItem()
        return subtotal, desconto

    def checkout(self):
        
        subtotal, descontoItens = self.calculaSubtotal()
        descontoCliente = self.cliente.calculaDescontoCliente(subtotal - descontoItens)
        desconto = descontoItens + descontoCliente
        frete = self.entrega.calculaFrete(subtotal - desconto)
        total = subtotal - desconto + frete
        
        return subtotal, desconto, frete, total

def main():

    cliente = input().strip()
    entrega = input().strip()
    
    pedido = Pedido(Cliente(cliente), Entrega(entrega))

    quantidadeItens = int(input().strip())

    for _ in range(quantidadeItens):
        compra = input().split()
        pedido.carrinho.append(Item(compra[0], float(compra[1]), int(compra[2])))

    subtotal, desconto, frete, total = pedido.checkout()
    
    print(f"SUBTOTAL={subtotal:.2f}")
    print(f"DESCONTO={desconto:.2f}")
    print(f"FRETE={frete:.2f}")
    print(f"TOTAL={total:.2f}")
    return

if __name__ == "__main__":
    main()