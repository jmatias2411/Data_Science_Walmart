import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Pruebaa;Trusted_Connection=yes;')
    print("Conexion Exitosa")
    cursor = connection.cursor()

    # Calcular medidas estadísticas para 'Fuel_Price'
    cursor.execute("SELECT AVG(Fuel_Price) AS Media_Fuel_Price FROM Walmart_sales")
    media_fuel_price = cursor.fetchone()
    print(f"Media de Fuel_Price: {media_fuel_price[0]}")

    cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Fuel_Price) OVER () AS Mediana_Fuel_Price FROM Walmart_sales")
    mediana_fuel_price = cursor.fetchone()
    print(f"Mediana de Fuel_Price: {mediana_fuel_price[0]}")

    cursor.execute("SELECT TOP 1 WITH TIES Fuel_Price AS Moda_Fuel_Price FROM Walmart_sales ORDER BY COUNT(*) OVER (PARTITION BY Fuel_Price) DESC")
    moda_fuel_price = cursor.fetchone()
    print(f"Moda de Fuel_Price: {moda_fuel_price[0]}")

    cursor.execute("SELECT STDEV(Fuel_Price) AS Desviacion_Estandar_Fuel_Price FROM Walmart_sales")
    desviacion_fuel_price = cursor.fetchone()
    print(f"Desviación Estándar de Fuel_Price: {desviacion_fuel_price[0]}")

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()
