# El informe de caza: de las tablas a las conclusiones

## 1. Prepara las preguntas y los datos

| Pregunta | Tabla y columnas necesarias | Operación y motivo |
|---|---|---|
| ¿Cuántas cacerías completadas se registraron? | Tabla: hunts.csv Columnas: Todas las registradas | len(hunts). He usado esta operación debido a que la tabla hunts solo contiene las cacerías que fueron completadas |
| ¿Cuántas corresponden a cada tipo de presa? | Tabla: hunts.csv Columna: "prey_type" | hunts['prey_type'].value_counts(). El motivo por el que se usa esta operación es para conocer el número de presas que hay y las veces que han sido cazadas |
| ¿Qué porcentaje representa cada presa? | Tabla: hunts.csv Columna: "prey_type" | hunts_proportions=hunts['prey_type'].value_counts(normalize=True) y hunts_percents=(hunts_proportions*100).round(1). El motivo de la primera operación es para conocer la proporción de caza de cada presa y así en la segunda solo tener que multiplicar esa proporción por 100|
| ¿Cuántas cacerías se registraron en cada día observado? | Tabla: hunts.csv Columna: "simulation_day" | hunts.groupby('simulation_day').size(). El motivo de esta operación es para conocer cuántos días se cazó y el número de veces que se cazó cada día |
| ¿Cuánto aumentó, disminuyó y cambió en términos netos la comida? | Tabla: resources.csv Columna: "resource_type" | food_stock=resources[resources["resource_type"]=="food"], incrementos=food_stock[food_stock['amount_delta'] > 0], disminucion=food_stock[food_stock['amount_delta'] < 0].copy(), disminucion['amount_delta']=disminucion["amount_delta"].abs() y food_stock['amount_delta'].sum(). El motivo de la primera operación es obtener todos los registros en los que el tipo de registro sea `food` para, posteriormente, obtener los registros en los que la comida ha incrementado que son las filas en las que la columna "amount_delta" es positivo, los registros en los que la comida ha disminuido que son las filas en las que la columna "amount_delta" es negativa, pero con el comando .abs() lo ponemos positivo y por último obtenemos el balance neto sumando todas los valores de la columna "amount_delta" |

## 2. Resume el parte de caza

Muestra en la consola:

1. El total de cacerías completadas registradas.
2. El recuento por `prey_type`, de mayor a menor frecuencia.
3. El porcentaje de cada tipo de presa, redondeado a un decimal.
4. El recuento por `simulation_day`, ordenado por día, no por frecuencia.

* Total de cacerías completadas registradas: 21
* Recuento por presa: sheep tiene 21 cazas
* Porcentajes por presa: sheep tiene el 100.0 % de la cacería
* Recuento por día:
simulation_day = 0. 1 caza completada  
simulation_day = 1. 3 cazas completadas
simulation_day = 2. 6 cazas completadas
simulation_day = 3. 3 cazas completadas
simulation_day = 6. 2 cazas completadas
simulation_day = 7. 4 cazas completadas
simulation_day = 8. 2 cazas completadas

Explica qué representa una fila de `hunts.csv` y cuál es el denominador de los porcentajes.

Una fila de hunts.csv representa el momento en el que un aldeano cazó una presa y el denominador de los porcentajes es el número de cacerías completas, que en este caso es el número de columnas de la tabla

## 3. Examina los cambios de comida

Filtra las filas de `resources` cuyo `resource_type` sea `food`. Después calcula:

- **Incrementos registrados:** suma de los `amount_delta` positivos.
- **Reducciones registradas:** suma de las magnitudes de los `amount_delta` negativos; muéstrala como número positivo.
- **Balance neto:** suma de todos los `amount_delta` de comida.

Ejemplo inventado: +12, −5 y +3 producen incrementos de 15, reducciones de 5 y balance de +10. No es el resultado que debes entregar: usa tus datos.

Si no hay eventos de comida, las tres sumas serán cero, pero muestra también un aviso. Ese cero significa que no hay variaciones registradas que sumar; no demuestra que el mundo no tuviera comida.

## 4. Comprueba y guarda el informe

Utiliza `assert` para comprobar que:

- La suma de los recuentos por presa coincide con el total de cacerías.
- La suma de los recuentos por día coincide con el total de cacerías.
- Los incrementos menos las reducciones coinciden con el balance neto de comida.

Si hay cacerías, comprueba que los porcentajes sin redondear suman aproximadamente 100. Los porcentajes redondeados pueden no sumar exactamente 100. Para comparar números decimales puedes usar `abs(a - b) < 0.000001`: aquí `abs()` es una función de Python que mide la magnitud de la diferencia.

Crea un DataFrame de resumen con las columnas `metric` y `value` y las siguientes cinco filas:

| metric | value |
|---|---|
| `hunt_events` | Total de cacerías completadas registradas |
| `food_change_events` | Número de eventos de cambio de comida |
| `food_gains` | Incrementos de comida registrados |
| `food_reductions` | Reducciones de comida como cantidad positiva |
| `food_net_change` | Balance neto de comida |

Guarda el resultado en `reports/hunting_summary.csv`, sin índice. Reutiliza `pd.DataFrame` con una lista de diccionarios como en la teoría. Los recuentos por presa y día y los porcentajes se incorporarán a la ficha, junto con la salida de las comprobaciones.

Ejecuta el programa desde la raíz de `bigdata-game`:

```powershell
python scripts/actividades/03_informe_caza.py
```

## 5. Defiende tus conclusiones

1. ¿Qué presa o presas tienen el mayor recuento? Si hay empate, indícalo. Si no hay datos, explica por qué no puedes responder. La presa con el mayor recuento es `sheep` porque, en mi caso, es la única registrada
2. ¿El porcentaje de una presa representa un porcentaje de cacerías, de aldeanos o de tiempo? Justifica tu respuesta. El porcentaje de una presa representa el número de veces que se cazó una presa respecto al total de cacerías, el denominador para calcular el porcentaje de caza de una presa es el número total de cacerías porque si tenemos 21 cacerías registradas y queremos averiguar el de una presa concreta, cogemos el número de veces que se cazó esa presa, la dividimos entre el número de cacerías registradas y lo multiplicamos por 100
3. ¿El día con más cacerías fue necesariamente el día en que se dedicó más tiempo a cazar? Explica por qué. No, lo que indica es que durante el día hubo muchos momentos en los que se cazó una presa, pero pudo haber otros en los que se cazó a una presa empleando mucho más tiempo que otro en el se cazaron varias
4. ¿El balance neto indica las existencias finales de comida? No, lo que indica es la diferencia de comida que hubo cuando finalizó la cacería ¿Qué información faltaría? La información que faltaría por conocer sería cuanta comida había al comienzo del periodo
5. ¿Puedes demostrar que todos los incrementos de comida se deben a la caza? No, puede deberse a otro evento ¿Qué vínculo entre eventos necesitarías para justificarlo? Para vincularlo necesitaría algún identificador común que relacione la cacería con los incrementos de comida