"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

class IJanela(ABC):    
    def fechar(self):
        raise NotImplementedError

class FixedJanela(IJanela):
    def mostrar_menu(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class MenulessJanela(IJanela):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(FixedJanela):
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(MenulessJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
