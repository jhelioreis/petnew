# -*- coding: latin-1 -*-
import json
from Model.Client import Client
from Model.Database import Database

class ClientController(object):
    """Classe que controla os acessos ao cadastro de clientes."""    

    def GET(self, code = None):
        """Lista os clientes cadastradas no sistema."""
                
        #Se nenhum c�digo de cliente foi informado        
        if code == None:            
            #Capturo a lista de clientes e fa�o um dump dos dicion�rios da lista
            return json.dumps([c.__dict__ for c in Client().selectAllClients()])                
        else:
            #Se um c�digo de cliente foi informado, capturo o objeto e fa�o um dump de seu dicionario
            return json.dumps(Client().selectClient(code).__dict__)

    def PUT(self, strJson):
        """Inclui ou atualiza """
        
        if strJson != None:
            client = Client()
            client.__dict__ = json.loads(strJson)
            
            #Se � um novo registro, adiciono. Caso contr�rio, atualizo.            
            if client.isNew():
                client.insertClient()
            else:
                client.updateClient()                
        
        
    def DELETE(self, code = None):
        """Apaga um cliente do sistema."""   

        #Se o c�digo informado n�o for nulo,
        if code != None:
            
            #Testo selecionar o cliente
            client = Client().selectClient(code)
            
            #Se ela realmente existir
            if client != None:                
                #Deleto-a
                client.deleteClient()