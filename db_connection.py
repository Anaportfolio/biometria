# Bibliotecas: mysq-connector-python e python-dotenv
import mysql.connector as connector
import os
from dotenv import load_dotenv

load_dotenv()

class MySQLDatabase:

    #  Pegando as informações do arquivo .env
    def __init__(self):
        self._host = os.getenv("HOST")
        self._username = os.getenv("USER")
        self._passwd = os.getenv("PASSWORD")
        self._database = os.getenv("DATABASE")
        self._conn = self._connecting()

    #  Fazendo a conexão 
    def _connecting(self):
        return connector.connect(
            user = self._username,
            password = self._passwd,
            host = self._host,
            database = self._database
        )
    
    def _querying(self, query: str):
        
        # Verificando a conexão 
        try:
            if(not self._conn.is_connected()) or self._conn is None: 
                self._conn = self._connecting()

        except ConnectionError as err:
            raise f"Erro durante a conexão, Menssage: {err}"

        cursor = self._conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result
    
    # Lendo os dados da tabela 
    def get_lines_from_table(self, table):
        query = ' '.join(["SELECT * FROM", table])

        result = self._querying(query)
        for lista in result:
            keys = lista.keys()
            for k in keys:
                print(k + ':', lista[k])

        return result
    
    # Fechando a conexão
    def closing(self):
        if self._conn.is_connected():
            self._conn.close()