from db_connection import MySQLDatabase

if __name__ == '__main__':

    db = MySQLDatabase()

    # Leitura dos dados 
    db.get_lines_from_table('pro_rurais') 