import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Pruebaa;Trusted_Connection=yes;')
    print("Conexion Exitosa")
    cursor = connection.cursor()

    # Obtener solo los primeros 10 registros de 'Walmart_sales'
    cursor.execute("SELECT TOP 10 * FROM Walmart_sales")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()
