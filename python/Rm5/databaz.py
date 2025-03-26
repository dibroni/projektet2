import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",      
            password="your_password",  
            database="your_database"   
        )
        print("Lidhja me bazën e të dhënave u krye me sukses!")
        return connection
    except mysql.connector.Error as e:
        print(f"Gabim gjatë lidhjes: {e}")
        return None

def insert_record(connection, table, data):
    cursor = connection.cursor()
    
    # Kreoni një pyetje INSERT dinamikisht
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table} VALUES ({placeholders})"
    
    values = tuple(data)
    try:
        cursor.execute(query, values)
        connection.commit()
        print(f"Regjistri u shtua me sukses në tabelën {table}.")
    except mysql.connector.Error as e:
        print(f"Gabim gjatë shtimit të regjistrit: {e}")
    finally:
        cursor.close()

# Testimi i lidhjes dhe insertimit
def test_insert():
    connection = connect_to_database()
    if connection:
        data = ('example_value_1', 'example_value_2', 'example_value_3')  # Ndryshoni sipas nevojës
        insert_record(connection, 'your_table_name', data)  # Vendosni emrin e tabelës suaj
        connection.close()

if __name__ == "__main__":
    test_insert()
