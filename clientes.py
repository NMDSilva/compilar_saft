class Cliente(object):

    def __init__(self, id, nif, nome, contacto, endereco, cidade, cod_postal, pais):
        self.__id = id
        self.__nif = nif
        self.__nome = nome
        self.__contacto = contacto
        self.__endereco = endereco
        self.__cidade = cidade
        self.__cod_postal = cod_postal
        self.__pais = pais
        self.__index = -1

    @property
    def id(self):
        return self.__id

    @property
    def nif(self):
        return self.__nif

    @property
    def nome(self):
        return self.__nome
    
    @property
    def contacto(self):
        return self.__contacto
    
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