class Retangulo:
    def __init__(self, b, h):
        self.__b = b
        self.__h = h
    def get_b(self, b):
        if b < 0: raise ValueError("Base menor que zero.")
        b = self.__b
    def set_b(self):
        return self.__b
    def get_h(self, h):
        if h < 0: raise ValueError("Altura menor que zero.")
        h = self.__h
    def set_h(self):
        return self.__h
    def calc_area(self):
        return self.__b*self.__h
    def calc_diagonal(self):
        return (self.__b**2 + self.__h**2) ** 0.5
    def __str__(self):
        return f"Base = {self.__b}\nAltura = {self.__h}\nÁrea = {self.calc_area():.2f}\nDiagonal = {self.calc_diagonal():.2f}"

