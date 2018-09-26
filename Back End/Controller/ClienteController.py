# -*- coding: latin-1 -*-
import json
from Model.Client import Client
from Model.Database import Database

class ClientController(object):
    """Classe que controla os acessos ao cadastro de clientes."""    

    def GET(self, code = None):
        """Lista os clientes cadastradas no sistema."""
                
        #Se nenhum código de cliente foi informado        
        if code == None:            
            #Capturo a lista de clientes e faço um dump dos dicionários da lista
            return json.dumps([c.__dict__ for c in Client().selectAllClients()])                
        else:
            #Se um código de cliente foi informado, capturo o objeto e faço um dump de seu dicionario
            return json.dumps(Client().selectClient(code).__dict__)

    def PUT(self, strJson):
        """Inclui ou atualiza """
        
        if strJson != None:
            client = Client()
            client.__dict__ = json.loads(strJson)
            
            #Se é um novo registro, adiciono. Caso contrário, atualizo.            
            if client.isNew():
                client.insertClient()
            else:
                client.updateClient()                
        
        
    def DELETE(self, code = None):
        """Apaga um cliente do sistema."""   

        #Se o código informado não for nulo,
        if code != None:
            
            #Testo selecionar o cliente
            client = Client().selectClient(code)
            
            #Se ela realmente existir
            if client != None:                
                #Deleto-a
                client.deleteClient()