
import pyodbc
try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Pruebaa;Trusted_Connection=yes;')
    print("Conexion Exitosa")
    cursor = connection.cursor()

    # Obtener los últimos 10 registros de 'Walmart_sales'
    cursor.execute("SELECT TOP 10 * FROM Walmart_sales ORDER BY Store DESC")
    # Reemplaza 'Store' con la columna por la cual quieres ordenar por ejemplo 'Date' 
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()