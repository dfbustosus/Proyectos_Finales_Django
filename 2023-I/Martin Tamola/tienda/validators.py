from typing import Any
from django.forms import ValidationError

#Funcion o Clase

class MaxSizeFileValidaor:
    
    def __init__(self, max_file_size=5):
        self.max_file_size = max_file_size
        
    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size * 1058576
        
        if size > max_size:
            raise ValidationError(f"El tamaño máximo del archivo deber {self.max_file_size} MB")
        
        return value