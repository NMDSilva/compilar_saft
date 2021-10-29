class Produto(object):

    def __init__(self, codigo, tipo, descricao, numero):
        self.__codigo = codigo
        self.__tipo = tipo
        self.__descricao = descricao
        self.__numero = numero
        self.__index = -1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def numero(self):
        return self.__numero