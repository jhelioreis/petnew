# -*- coding: latin-1 -*-
import json
from Model.Category import Category
from Model.Database import Database

class CategoryController(object):
    """Classe que controla os acessos ao cadastro de categorias."""    

    def GET(self, code = None):
        """Lista as categorias cadastradas no sistema."""        
        #Se nenhum código de categoria foi informado        
        if code == None:            
            #Capturo a lista de categorias e faço um dump dos dicionários da lista
            return json.dumps([c.__dict__ for c in Category().selectAllCategories()])                
        else:
            #Se um código de categoria foi informado, capturo o objeto e faço um dump de seu dicionario
            return json.dumps(Category().selectCategory(code).__dict__)

    def PUT(self, strJson):
        """Inclui ou atualiza """
        if strJson != None:
            category = Category()
            category.__dict__ = json.loads(strJson)
            
            #Se é um novo registro, adiciono. Caso contrário, atualizo.            
            if category.isNew():
                category.insertCategory()
            else:
                category.updateCategory()                
        
        
    def DELETE(self, code = None):
        """Apaga uma categoria do sistema."""   
                
        #Se o código informado não for nulo,
        if code != None:
            
            #Testo selecionar a categoria
            category = Category().selectCategory(code)
            
            #Se ela realmente existir
            if category != None:                
                #Deleto-a
                category.deleteCategory()