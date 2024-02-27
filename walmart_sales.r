# Instala los paquetes necesarios si no están instalados
if (!requireNamespace("odbc", quietly = TRUE)) {
  install.packages("odbc")
}

# Cargar la biblioteca odbc
library(odbc)

# Configuración de la conexión a la base de datos
con <- dbConnect(odbc::odbc(), 
                 driver = "SQL Server", 
                 server = ".", 
                 database = "Pruebaa",
                 trusted_connection = TRUE)

# Consulta para obtener todos los datos de la tabla 'Walmart_sales'
query <- "SELECT * FROM Walmart_sales"
walmart_data <- dbGetQuery(con, query)

# Muestra los primeros 10 registros
head(walmart_data, 10)

# Calcula algunas medidas estadísticas para 'Fuel_Price'
media_fuel_price <- mean(walmart_data$Fuel_Price, na.rm = TRUE)
mediana_fuel_price <- median(walmart_data$Fuel_Price, na.rm = TRUE)
desviacion_fuel_price <- sd(walmart_data$Fuel_Price, na.rm = TRUE)

# Imprime las medidas estadísticas
cat("Media de Fuel_Price:", media_fuel_price, "\n")
cat("Mediana de Fuel_Price:", mediana_fuel_price, "\n")
cat("Desviación Estándar de Fuel_Price:", desviacion_fuel_price, "\n")

# Cerrar la conexión
dbDisconnect(con)
