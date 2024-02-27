
# Instala la biblioteca 'odbc' si no está instalada
if (!requireNamespace("odbc", quietly = TRUE)) {
  install.packages("odbc")
}

# Cargar la biblioteca 'odbc'
library(odbc)

# Configuración de la conexión a la base de datos
con <- dbConnect(odbc::odbc(), 
                 driver = "SQL Server", 
                 server = ".", 
                 database = "Pruebaa",
                 trusted_connection = TRUE)

# Realizar medidas estadísticas para 'Fuel_Price'
query <- "SELECT AVG(Fuel_Price) AS Media_Fuel_Price,
                  STDEV(Fuel_Price) AS Desviacion_Estandar_Fuel_Price
          FROM Walmart_sales"

result <- dbGetQuery(con, query)

# Imprimir los resultados
print(result)

# Cerrar la conexión
dbDisconnect(con)
