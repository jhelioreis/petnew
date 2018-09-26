# -*- coding: latin-1 -*-
import traceback
import json
from Model.Database import Database

class Category(object):
    """Classe que descreve o objeto Categoria"""

    def __init__(self, code = 0, name = ""):
        """Construtor da classe"""
        if code == 0:
            self.code = nextCode()
        else:
            self.code = code
        self.code = code
        self.name = name        
        
    def insertCategory(self):
        """Insere uma nova categoria na base de dados."""
        
        #Se a categoria foi criada sem um c�digo, providencio um novo c�digo.
        if self.code == None or self.code <= 0:
            self.code = nextCode()
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a inser��o
            cursor.execute("INSERT INTO Category (code, name) VALUES (" + str(self.code) + ", '" + str(self.name) + "')")
            
            #Gravo as altera��es
            database.conn.commit()
            
            #Fecho o cursor
            cursor.close()
            
            #Retorno OK 
            return str(True)
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return str(False)
    
    def updateCategory(self):
        """Atualiza as informa��es de uma categoria."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo o update
            cursor.execute("UPDATE Category SET name = '" + str(self.name) + "' WHERE code = " + str(self.code) + " ")
            
            #Gravo as altera��es
            database.conn.commit()
            
            #Fecho o cursor
            cursor.close()
            
            #Retorno OK 
            return True
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    def deleteCategory(self):
        """Excluo uma categoria da base de dados."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a exclus�o
            cursor.execute("DELETE FROM Category WHERE code = " + str(self.code) + " ")                
            
            #Gravo as altera��es
            database.conn.commit()
                        
            #Fecho o cursor
            cursor.close()
            
            #Retorno OK 
            return True
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    def selectCategory(self, code):
        """Retorna informa��es de uma categoria"""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo a sele��o
            cursor.execute("SELECT code, name FROM Category WHERE code = " + str(code) + " ")
            
            #Preencho os dados do objeto com as informa��es retornadas
            for category in cursor:
                self.code = category[0]
                self.name = category[1]
                        
            #Fecho o cursor
            cursor.close()
            
            #Retorno o objeto
            return self
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    
    def selectAllCategories(self):
        """Recupera todas as categorias cadastradas no sistema"""        
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT code, name FROM Category")
            
            #Crio uma lista para armazenar os resultados
            categories = []
            
            #Preencho os dados do objeto com as informa��es retornadas
            for category in cursor:
                cat = Category(category[0], category[1])
                categories.append(cat)
                        
            #Fecho o cursor
            cursor.close()
            
            #Retorno a lista de objetos
            return categories
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
        
    def isNew(self):
        """Verifica se a categoria � nova."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT COUNT(*) FROM Category WHERE code = " + str(self.code) + " ")                
            
            #Guardo o n�mero de registros retornado
            count = cursor.fetchone()[0]
            
            #Fecho o cursor
            cursor.close()
            
            #Retorno a lista de objetos
            return count <= 0
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
        
        def nextCode(self):
            """Verifico qual � o pr�ximo c�digo de categoria dispon�vel."""
        
            #Instancio a classe banco
            database = Database()
            
            try:
                #Crio um cursor para acessar o banco de dados
                cursor = database.conn.cursor()
                
                #Executo o select
                cursor.execute("SELECT MAX(code) FROM Category")                
                
                #Guardo o n�mero de registros retornado
                count = cursor.fetchone()[0]
                
                #Fecho o cursor
                cursor.close()
                
                #Retorno a lista de objetos
                return count + 1
            except:
                #Capturo a mensagem de erro
                error = traceback.format_exc()
                print(error)
                return 0