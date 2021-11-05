class Endereco(object):

    def __init__(self, endereco, cidade, cod_postal, pais = 'PT', numero_porta = None, nome_rua = None, regiao = None):
        self.__endereco = endereco
        self.__cidade = cidade
        self.__cod_postal = cod_postal
        self.__pais = pais
        self.__numero_porta = numero_porta
        self.__nome_rua = nome_rua
        self.__regiao = regiao
        self.__index = -1

    @property
    def id(self):
        return self.__id

    @property
    def endereco(self):
        return self.__endereco

    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def cod_postal(self):
        return self.__cod_postal
    
    @property
    def pais(self):
        return self.__pais

    @property
    def numero_porta(self):
        return self.__numero_porta

    @property
    def nome_rua(self):
        return self.__nome_rua

    @property
    def regiao(self):
        return self.__regiao