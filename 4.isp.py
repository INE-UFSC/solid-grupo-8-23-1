"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

class IJanela(ABC):    
    def fechar(self):
        raise NotImplementedError

    def minimizar(self):
        raise NotImplementedError

class FixedJanela(IJanela):
    def mostrar_menu(self):
        raise NotImplementedError

class MenulessJanela(IJanela):
    def maximizar(self):
        raise NotImplementedError
