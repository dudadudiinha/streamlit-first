from datetime import datetime
class Paciente:
    def __init__(self, nome, cpf, tel, nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__tel = tel
        self.__nasc = nasc
    def get_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio.")
        self.__nome = nome
    def set_nome(self):
        return self.__nome
    def get_cpf(self, cpf):
        if cpf == "": raise ValueError("CPF não pode ser vazio.")
        self.__cpf = cpf
    def set_nome(self):
        return self.__cpf
    def get_tel(self, tel):
        if tel == "": raise ValueError("Telefone não pode ser vazio.")
        self.__tel = tel
    def set_tel(self):
        return self.__tel
    def get_nasc(self, nasc):
        if nasc > datetime.today(): raise ValueError("Data de nascimento não pode ser maior que zero.")
        self.__nasc = nasc
    def set_nasc(self):
        return self.__nasc
    def idade(self):
        hoje = datetime.today()
        anos = hoje.year - self.__nasc.year
        meses = hoje.month - self.__nasc.month
        return f"{anos} anos e {meses} meses"
    def __str__(self):
        return f"Olá, {self.__nome}! Você tem {self.idade()}"