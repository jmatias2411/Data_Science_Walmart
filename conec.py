import pyodbc
try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Pruebaa;Trusted_Connection=yes;')
    print("Conexion Exitosa")
    cursor = connection.cursor()

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()