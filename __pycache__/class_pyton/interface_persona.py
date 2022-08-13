from abc import ABCMeta
from abc import abstractmethod

class InterfacePersona(metaclass=ABCMeta):

    @abstractmethod
    def get_full_name(self)->str:
        pass

    @abstractmethod
    def set_name(self, name:str)->str:
        pass

    @abstractmethod
    def set_lastName(self, lastName:str)->str:
        pass

