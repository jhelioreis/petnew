# -*- coding: latin-1 -*-
import json
from Model.Producer import Producer
from Model.Database import Database

class ProducerController(object):
    """Classe que controla os acessos ao cadastro de fornecedores."""    

    def GET(self, code = None):
        """Lista os fornecedores cadastradas no sistema."""
                
        #Se nenhum código de fornecedor foi informado        
        if code == None:            
            #Capturo a lista de fornecedores e faço um dump dos dicionários da lista
            return json.dumps([c.__dict__ for c in Producer().selectAllProducers()])                
        else:
            #Se um código de fornecedor foi informado, capturo o objeto e faço um dump de seu dicionario
            return json.dumps(Producer().selectProducer(code).__dict__)

    def PUT(self, strJson):
        """Inclui ou atualiza """
        
        if strJson != None:
            producer = Producer()
            producer.__dict__ = json.loads(strJson)
            
            #Se é um novo registro, adiciono. Caso contrário, atualizo.            
            if producer.isNew():
                producer.insertProducer()
            else:
                producer.updateProducer()                
        
        
    def DELETE(self, code = None):
        """Apaga um fornecedor do sistema."""   

        #Se o código informado não for nulo,
        if code != None:
            
            #Tento selecionar o fornecedor
            producer = Producer().selectProducer(code)
            
            #Se ele realmente existir
            if producer != None:                
                #Deleto-o
                producer.deleteProducer()