import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Pruebaa;Trusted_Connection=yes;')
    print("Conexion Exitosa")
    cursor = connection.cursor()

    # Calcular medidas estadísticas para 'Temperature'
    cursor.execute("SELECT AVG(Temperature) AS Media_Temperature FROM Walmart_sales")
    media_temperatura = cursor.fetchone()
    print(f"Media de Temperature: {media_temperatura[0]}")

    cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Temperature) OVER () AS Mediana_Temperature FROM Walmart_sales")
    mediana_temperatura = cursor.fetchone()
    print(f"Mediana de Temperature: {mediana_temperatura[0]}")

    cursor.execute("SELECT TOP 1 WITH TIES Temperature AS Moda_Temperature FROM Walmart_sales ORDER BY COUNT(*) OVER (PARTITION BY Temperature) DESC")
    moda_temperatura = cursor.fetchone()
    print(f"Moda de Temperature: {moda_temperatura[0]}")

    cursor.execute("SELECT STDEV(Temperature) AS Desviacion_Estandar_Temperature FROM Walmart_sales")
    desviacion_temperatura = cursor.fetchone()
    print(f"Desviación Estándar de Temperature: {desviacion_temperatura[0]}")

    # Calcular medidas estadísticas para 'Unemployment'
    cursor.execute("SELECT AVG(Unemployment) AS Media_Unemployment FROM Walmart_sales")
    media_desempleo = cursor.fetchone()
    print(f"Media de Unemployment: {media_desempleo[0]}")

    cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Unemployment) OVER () AS Mediana_Unemployment FROM Walmart_sales")
    mediana_desempleo = cursor.fetchone()
    print(f"Mediana de Unemployment: {mediana_desempleo[0]}")

    cursor.execute("SELECT TOP 1 WITH TIES Unemployment AS Moda_Unemployment FROM Walmart_sales ORDER BY COUNT(*) OVER (PARTITION BY Unemployment) DESC")
    moda_desempleo = cursor.fetchone()
    print(f"Moda de Unemployment: {moda_desempleo[0]}")

    cursor.execute("SELECT STDEV(Unemployment) AS Desviacion_Estandar_Unemployment FROM Walmart_sales")
    desviacion_desempleo = cursor.fetchone()
    print(f"Desviación Estándar de Unemployment: {desviacion_desempleo[0]}")

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()
