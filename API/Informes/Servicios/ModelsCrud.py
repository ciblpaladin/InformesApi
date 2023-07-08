from .ServicesCrud import ServicesCrud
from django.db import models

class ModelsCrud(ServicesCrud):

    def __init__(self, _model:models.Model) -> None:
       
       self.model = _model
    
    def all(self):
        
        return  list(self.model.objects.all())  
    
        
    def get(self, id):

       return self.model.objects.get(id=id)


    def create(self,model):
        
        model = self.model.objects.create(**model)
        model.save()
    
    def update(self, data_model):
        
        data_model.save()

    @staticmethod
    def create_model_crud(model: models.Model) -> ServicesCrud:

       return ModelsCrud(_model=model)    
    