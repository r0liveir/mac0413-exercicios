from dataclasses import dataclass


@dataclass(frozen=True)
class Edicao:
    isbn: str
    titulo: str
    autor: str
    capa: tuple


class FabricaEdicoes:
    def __init__(self):
        self.map = {}

    def obter(self, isbn, titulo, autor, capa):
        
        isbn = self.limpar_isbn(isbn)
        capa = tuple(capa)
        
        if (isbn in self.map):
            
            livro = self.map[isbn]
            if (livro.titulo == titulo and livro.autor == autor and livro.capa == capa):
                return livro

            raise ValueError()
            
        livro = Edicao(isbn, titulo, autor, capa)
        self.map[isbn] = livro
        return livro

    def quantidade_edicoes(self):
        return len(self.map)
    
    def limpar_isbn(self, isbn):
        isbn = isbn.replace("-", "").replace(" ", "")
        if len(isbn) == 13 and all("0" <= caractere <= "9" for caractere in isbn):
            return isbn
        raise ValueError()


class Exemplar:
    
    def __init__(self, tombo, localizacao, edicao):
        self._tombo = tombo
        self._localizacao = localizacao
        self._edicao = edicao
        self._emprestado = False

    @property
    def tombo(self):
        return self._tombo

    @property
    def localizacao(self):
        return self._localizacao

    @property
    def edicao(self):
        return self._edicao

    @property
    def emprestado(self):
        return self._emprestado 

    def mover(self, nova_localizacao):
        self._localizacao = nova_localizacao

    def emprestar(self):
        if (self._emprestado):
            return False
        self._emprestado = True
        return True

    def devolver(self):
        if (self._emprestado):
            self._emprestado = False
            return True
        return False
