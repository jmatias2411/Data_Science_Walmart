import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

try:
    # Conexión
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Pruebaa;Trusted_Connection=yes;')
    print("Conexion Exitosa")

    # Consultas SQL
    query_media = "SELECT AVG(Fuel_Price) AS Media_Fuel_Price FROM Walmart_sales"
    query_mediana = "SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Fuel_Price) OVER () AS Mediana_Fuel_Price FROM Walmart_sales"
    query_moda = "SELECT TOP 1 WITH TIES Fuel_Price AS Moda_Fuel_Price FROM Walmart_sales ORDER BY COUNT(*) OVER (PARTITION BY Fuel_Price) DESC"
    query_desviacion = "SELECT STDEV(Fuel_Price) AS Desviacion_Estandar_Fuel_Price FROM Walmart_sales"

    # Ejecutar las consultas y obtener resultados en DataFrames
    media_result = pd.read_sql(query_media, connection)
    mediana_result = pd.read_sql(query_mediana, connection)
    moda_result = pd.read_sql(query_moda, connection)
    desviacion_result = pd.read_sql(query_desviacion, connection)

    # Crear un DataFrame consolidado con los resultados
    data = {
        'Medida Estadística': ['Media', 'Mediana', 'Moda', 'Desviación Estándar'],
        'Valor': [
            media_result['Media_Fuel_Price'][0],
            mediana_result['Mediana_Fuel_Price'][0],
            moda_result['Moda_Fuel_Price'][0],
            desviacion_result['Desviacion_Estandar_Fuel_Price'][0]
        ]
    }
    df_resultados = pd.DataFrame(data)

    # Visualizar como gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_resultados['Medida Estadística'], df_resultados['Valor'], color='blue')
    plt.title('Medidas Estadísticas de Fuel_Price')
    plt.xlabel('Medida Estadística')
    plt.ylabel('Valor')
    plt.show()

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()
