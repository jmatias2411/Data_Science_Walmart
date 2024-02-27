import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Pruebaa;Trusted_Connection=yes;')
    print("Conexion Exitosa")
    cursor = connection.cursor()

    # Calcular medidas estadísticas para 'Weekly_Sales'
    cursor.execute("SELECT AVG(Weekly_Sales) AS Media_Weekly_Sales FROM Walmart_sales")
    media_ventas = cursor.fetchone()
    print(f"Media de Weekly_Sales: {media_ventas[0]}")

    cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Weekly_Sales) OVER () AS Mediana_Weekly_Sales FROM Walmart_sales")
    mediana_ventas = cursor.fetchone()
    print(f"Mediana de Weekly_Sales: {mediana_ventas[0]}")

    cursor.execute("SELECT TOP 1 WITH TIES Weekly_Sales AS Moda_Weekly_Sales FROM Walmart_sales ORDER BY COUNT(*) OVER (PARTITION BY Weekly_Sales) DESC")
    moda_ventas = cursor.fetchone()
    print(f"Moda de Weekly_Sales: {moda_ventas[0]}")

    cursor.execute("SELECT STDEV(Weekly_Sales) AS Desviacion_Estandar_Weekly_Sales FROM Walmart_sales")
    desviacion_ventas = cursor.fetchone()
    print(f"Desviación Estándar de Weekly_Sales: {desviacion_ventas[0]}")

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()