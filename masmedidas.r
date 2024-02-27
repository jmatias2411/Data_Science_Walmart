 #Instala los paquetes necesarios si no están instalados
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

# Calcula algunas medidas estadísticas para las columnas seleccionadas
media_temperature <- mean(walmart_data$Temperature, na.rm = TRUE)
mediana_temperature <- median(walmart_data$Temperature, na.rm = TRUE)
desviacion_temperature <- sd(walmart_data$Temperature, na.rm = TRUE)

media_weekly_sales <- mean(walmart_data$Weekly_Sales, na.rm = TRUE)
mediana_weekly_sales <- median(walmart_data$Weekly_Sales, na.rm = TRUE)
desviacion_weekly_sales <- sd(walmart_data$Weekly_Sales, na.rm = TRUE)

media_cpi <- mean(walmart_data$CPI, na.rm = TRUE)
mediana_cpi <- median(walmart_data$CPI, na.rm = TRUE)
desviacion_cpi <- sd(walmart_data$CPI, na.rm = TRUE)

media_fuel_price <- mean(walmart_data$Fuel_Price, na.rm = TRUE)
mediana_fuel_price <- median(walmart_data$Fuel_Price, na.rm = TRUE)
desviacion_fuel_price <- sd(walmart_data$Fuel_Price, na.rm = TRUE)

# Imprime las medidas estadísticas
cat("Medidas estadísticas para Temperature:\n")
cat("  Media:", media_temperature, "\n")
cat("  Mediana:", mediana_temperature, "\n")
cat("  Desviación Estándar:", desviacion_temperature, "\n\n")

cat("Medidas estadísticas para Weekly_Sales:\n")
cat("  Media:", media_weekly_sales, "\n")
cat("  Mediana:", mediana_weekly_sales, "\n")
cat("  Desviación Estándar:", desviacion_weekly_sales, "\n\n")

cat("Medidas estadísticas para CPI:\n")
cat("  Media:", media_cpi, "\n")
cat("  Mediana:", mediana_cpi, "\n")
cat("  Desviación Estándar:", desviacion_cpi, "\n\n")

cat("Medidas estadísticas para Fuel_Price:\n")
cat("  Media:", media_fuel_price, "\n")
cat("  Mediana:", mediana_fuel_price, "\n")
cat("  Desviación Estándar:", desviacion_fuel_price, "\n")

# Cerrar la conexión
dbDisconnect(con)
