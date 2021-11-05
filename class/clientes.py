
class Cliente(object):

    def __init__(self, id, nif, nome, contacto, endereco):
        self.__id = id
        self.__nif = nif
        self.__nome = nome
        self.__contacto = contacto
        self.__endereco = endereco,
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