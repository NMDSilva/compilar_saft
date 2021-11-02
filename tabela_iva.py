class IVA(object):

    def __init__(self, tipo, pais, code, descricao, percentagem):
        self.__tipo = tipo
        self.__pais = pais
        self.__code = code
        self.__descricao = descricao
        self.__percentagem = percentagem
        self.__index = -1

    @property
    def tipo(self):
        return self.__tipo

    @property
    def pais(self):
        return self.__pais

    @property
    def code(self):
        return self.__code
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def percentagem(self):
        return self.__percentagem