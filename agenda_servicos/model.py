import json

class Servico:
    def __init__(self, id, descricao, valor):
        self.__id = id
        self.__desc = descricao
        self.__v = valor
    def set_id(self, id):
        if id < 0: raise ValueError("ID não pode ser negativo.")
        self.__id = id
    def get_id(self):
        return self.__id
    def set_desc(self, descricao):
        if descricao == "": raise ValueError("Descrição não pode ser vazia.")
        self.__desc = descricao
    def get_desc(self):
        return self.__desc
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor não pode ser negativo.")
        self.__v = valor
    def get_valor(self):
        return self.__v
    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__desc,
            "valor": self.__v
        }
    @staticmethod
    def from_json(dict):
        return Servico(dict["id"], dict["descricao"], dict["valor"])
    def __str__(self):
        return f"{self.__id} - {self.__desc}\nValor: R${self.__v:.2f}"
    
class ServicoDAO:
    __servicos = []
    @classmethod
    def inserir(cls, s):
        cls.abrir()
        id = 0
        for serv in cls.__servicos:
            if serv.get_id() > id:
                id = serv.get_id()
        s.set_id(id+1)
        cls.__servicos.append(s)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__servicos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for servico in cls.__servicos:
            if servico.get_id() == id:
                return servico
        return None
    @classmethod
    def atualizar(cls, s):
        id = cls.listar_id(s.get_id())
        if id != None:
            cls.__servicos.remove(id)
            cls.__append(s)
            cls.salvar()
    @classmethod
    def excluir(cls, s):
        id = cls.listar_id(s.get_id())
        if id != None:
            cls.__servicos.remove(id)
            cls.salvar()
    @classmethod
    def abrir(cls):
        pass
    @classmethod
    def salvar(cls):
        pass