from abc import ABC, abstractmethod

class ServiceCRUDInterface(ABC):
    
    @abstractmethod
    def all():
        pass

    @abstractmethod    
    def get(self, id):
        pass

    abstractmethod
    def create(model):
        pass

    abstractmethod    
    def update():
        pass
