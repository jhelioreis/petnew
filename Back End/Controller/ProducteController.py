# -*- coding: latin-1 -*-
import json
from Model.Product import Product
from Model.Database import Database

class ProductController(object):
    """Classe que controla os acessos ao cadastro de produtos."""    

    def GET(self, code = None):
        """Lista os produtos cadastradas no sistema."""        
        #Se nenhum código de produto foi informado        
        if code == None:            
            #Capturo a lista de produtos e faço um dump dos dicionários da lista
            return json.dumps([p.__dict__ for p in Product().selectAllProducts()])                
        else:
            #Se um código de produto foi informado, capturo o objeto e faço um dump de seu dicionario
            return json.dumps(Product().selectProduct(code).__dict__)

    def PUT(self, strJson):
        """Inclui ou atualiza """
        
        if strJson != None:
            product = Product()
            product.__dict__ = json.loads(strJson)
            
            #Se é um novo registro, adiciono. Caso contrário, atualizo.            
            if product.isNew():
                product.insertProduct()
            else:
                product.updateProduct()
        
        
    def DELETE(self, code = None):
        """Apaga um produto do sistema."""   
                        
        #Se o código informado não for nulo,
        if code != None:
            
            #Testo selecionar a categoria
            product = Product().selectProduct(code)
            
            #Se ela realmente existir
            if product != None:
                #Deleto-a
                product.deleteProduct()