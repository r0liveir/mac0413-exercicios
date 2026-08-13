produtos: dict[int, list] = {
    1: ["X-Salada", 20.0],
    2: ["Suco", 7.5],
    3: ["Batata Frita", 12.0],
    4: ["Cafe", 5.0],
    5: ["Pudim", 10.0]
}

class Produto:
    
    def __init__(self, codigo):
                
        self.codigo = codigo
        self.nome = produtos[codigo][0]
        self.preco = produtos[codigo][1]

class ItemPedido:
    
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
    
class Pedido:
    
    def __init__(self):
        self.itens = []
        self.map = {}
        
    def adicionarProduto(self, produto, quantidade):
        
        if (quantidade <= 0):
            return
        
        if (produto.nome not in self.map):
            self.map[produto.nome] = len(self.itens)
            self.itens.append(ItemPedido(produto, quantidade))
            
        else:
            self.itens[self.map[produto.nome]].quantidade += quantidade

    def calcularSubtotal(self):
        subtotal = 0
        for item in self.itens:
            subtotal += item.produto.preco * item.quantidade
        return subtotal

    def calcularDesconto(self):
        subtotal = self.calcularSubtotal()
        if (subtotal >= 100):
            return subtotal * 0.1
        return 0.0
    
    def calcularTotal(self):
        subtotal = self.calcularSubtotal()
        desconto = self.calcularDesconto()
        if (desconto):
            return subtotal - desconto
        return subtotal
    
    def cashout(self):
        if (len(self.itens) == 0):
            print("PEDIDO\nNENHUM ITEM VALIDO\nSUBTOTAL: 0.00\nDESCONTO: 0.00\nTOTAL: 0.00", end="")
            return
        
        print("PEDIDO")
        
        for produto in self.itens:
            quantidade = produto.quantidade
            preco = produto.produto.preco
            print(f"{produto.produto.nome} {quantidade} x {preco:.2f} = {quantidade * preco:.2f}")
        
        print(f"SUBTOTAL: {self.calcularSubtotal():.2f}")
        print(f"DESCONTO: {self.calcularDesconto():.2f}")
        print(f"TOTAL: {self.calcularTotal():.2f}", end="")
    
def main():
    
    numPedidos = int(input())
    pedido = Pedido()
    
    while (numPedidos > 0):
        
        comando = str(input()).split()
        
        if (0 < int(comando[0]) < 6):
            produto = Produto(int(comando[0]))
            quantidade = int(comando[1])
            pedido.adicionarProduto(produto, quantidade)
        
        numPedidos -= 1
        
    pedido.cashout()
    return

main()