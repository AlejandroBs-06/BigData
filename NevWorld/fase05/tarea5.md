# El parte de caza también habla SQL

## 1. Tamaños de los archivos en bytes
hunts.csv: 2064 bytes
hunts.parquet: 4593 bytes

## 2. Comparación con la Actividad 03 y el gráfico de la Actividad 04
Los resultados obtenidos en la consulta SQL coinciden de forma exacta con los resultados de la actividad 03 y de la suma de los valores de las barras del gráfico de la actividad 04.

## 3. Cuestiones Teóricas
1. ¿Qué representa una fila del resultado? Una fila del resultado representa el número de cacerías completas de cada presa. ¿Cuenta cacerías o unidades de comida? Cuenta cacerías
2. ¿Qué hace `AS hunt_count`? Cuenta cuántas veces aparece una presa en la tabla. Si lo cambias por `AS total_cacerias`, ¿qué referencias posteriores debes actualizar? Si lo cambiase por `AS total_cacerias` tendría que quitar de la consulta la agrupación por `prey_type` y la solicitud de la columna `prey_type`.
3. ¿Qué archivo ocupa menos en tu partida? El archivo de mi partida que ocupa menos es el csv ¿Demuestra eso que ese formato será siempre mejor? No, debido a que paquet es muy bueno para el análisis de datos.