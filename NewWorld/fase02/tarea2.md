## 1. Investiga antes de elegir

Consulta los tipos de evento de tu partida con `df['type'].value_counts()`. Localiza el que registra una cacería completada y busca una de sus líneas originales en el JSONL. Puedes buscar el texto en el editor.

No te quedes solo con el nombre del evento: lee sus campos. Copia un ejemplo real en tu entrega e identifica qué información contiene y cuál no.

Si tu partida no contiene cacerías completadas, pide un registro de práctica al profesor para inspeccionar un ejemplo. Tu script debe admitir que tu propio archivo no contenga ninguna y generar un CSV vacío con sus cabeceras. No inventes filas para llenarlo.

Completa esta ficha **antes de escribir la llamada a `event_table()`**:

| Pregunta | Campo o valor elegido | Justificación |
| --- | --- | --- |
| ¿Qué evento demuestra que la cacería terminó? | "type"="hunt_completed" | Este campo registra el tipo de evento que se realiza |
| ¿Quién la completó? | "villager_id" | Es el identificador de cada jugador |
| ¿Qué presa aparece registrada? | "prey_type" | Este campo registra la presa de la cacería |
| ¿Cuándo ocurrió? | "tick":25569 | Refleja el momento exacto en el que se produce el evento |
| ¿A qué partida pertenece? | "run_id" | El run_id es el identificador de la sesión |
| ¿Cómo localizo el evento original sin confundirlo con otro? | A través del campo "event_index" | Este es el identificador único para cada evento |

Explica también por qué `activity`, `food_stock` y `amount_delta` no son necesarios para este parte. El campo 'activity' no es necesario porque ya indicamos cuál es la actividad con el campo "type", food_stock tampoco pertenece a las fotografías del mundo y amount_delta tampoco porque describe cambios de recursos ¿Permite el evento saber por sí solo cuánta comida produjo la cacería? No, el evento no sabe cuánta comida produjo la cacería porque no se registra

## 2. Construye la tabla

Crea `scripts/actividades/02_parte_caza.py` dentro de `bigdata-game`. Reutiliza la lectura del JSONL y la función `event_table()` del tema, copiando las partes necesarias a este script.

El programa debe: 

1. Leer el RAW y crear `data/processed` si hace falta.
2. Seleccionar únicamente cacerías completadas y los campos justificados en tu ficha.
3. Conservar `run_id`, `event_index` y `tick`, que la función añade automáticamente.
4. Añadir `simulation_day` mediante `tick // 12000`.
5. Guardar `data/processed/hunts.csv` sin exportar el índice de pandas.
6. Mostrar la ruta del archivo generado y su número de filas.

**Condición adicional:** el CSV debe tener las mismas cabeceras aunque no haya cacerías. Revisa estas dos partes de la función del tema: el filtro de columnas `available` y el `if not table.empty`. Una columna ausente de todo el JSONL y una tabla sin filas son situaciones distintas.

Puedes usar esta operación para fijar las columnas de salida:

```python
# Conserva ese orden y crea con valores vacíos las columnas que falten.
table = table.reindex(columns=columnas_de_salida)
```

Si hay eventos de caza pero falta un campo obligatorio, debes avisar con una validación; añadir la columna vacía no repara el dato.

## 3. Demuestra que funciona

Comprueba con `assert`:

- El número de filas coincide con el número de eventos del tipo elegido en el RAW.
- No se repite la pareja `run_id`, `event_index`.
- Si hay filas, los campos que identifican partida, evento, momento, aldeano y presa no tienen valores ausentes.
- `simulation_day` coincide con la división entera indicada.

Ayudas de sintaxis:

```python
# Cuenta cuántas filas cumplen una condición.
cantidad = (df['type'] == 'TIPO_ELEGIDO').sum()

# Comprueba que los campos obligatorios no tengan celdas ausentes.
assert table[campos_obligatorios].notna().all().all()
```

Abre el CSV exportado. Elige dos filas —o todas si hay menos de dos— y localiza sus eventos originales mediante `run_id` y `event_index`. Comprueba aldeano, presa y tick. Anota la comparación; si no hay filas, explica qué has podido comprobar y qué no.

Ejecuta desde la raíz de `bigdata-game`, con el entorno de Python que tenga pandas:

```powershell
python scripts/actividades/02_parte_caza.py
```

## 4. Detecta las conclusiones que los datos no sostienen

Responde justificando cada decisión:

1. «Hay seis filas, por tanto hay seis cazadores distintos». ¿Es necesariamente cierto? No es cierto porque un aldeano pudo cazar en un momento determinado a y otro momento en el que cazó a otra
2. «Una fila indica que ese aldeano estuvo cazando durante todo el día». ¿Qué registra realmente la fila? Que el aldeano cazó en un momento determinado
3. «Borro del DataFrame original todas las filas con algún `NaN` y después selecciono las cacerías». ¿Por qué puede desaparecer información válida? Porque aunque haya datos con NaN no significa que sea inválido
4. «El CSV está vacío, así que nadie intentó cazar». ¿Qué puedes afirmar realmente sobre el registro? Si el csv está vacío puede deberse a que se intentó cazar, pero no se logró


## Entrega y valoración

Mismos pasos que la Actividad 1. Entrega el script, `hunts.csv` y una ficha con el ejemplo RAW, tus decisiones de diseño, las comprobaciones y las cuatro respuestas. Si haces el reto, incluye también su CSV y justificación.