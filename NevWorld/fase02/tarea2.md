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


## 2. Conclusiones que los datos no sostienen

Responde justificando cada decisión:

1. «Hay seis filas, por tanto hay seis cazadores distintos». ¿Es necesariamente cierto? No es cierto porque un aldeano pudo cazar en un momento determinado a y otro momento en el que cazó a otra
2. «Una fila indica que ese aldeano estuvo cazando durante todo el día». ¿Qué registra realmente la fila? Que el aldeano cazó en un momento determinado
3. «Borro del DataFrame original todas las filas con algún `NaN` y después selecciono las cacerías». ¿Por qué puede desaparecer información válida? Porque aunque haya datos con NaN no significa que sea inválido
4. «El CSV está vacío, así que nadie intentó cazar». ¿Qué puedes afirmar realmente sobre el registro? Si el csv está vacío puede deberse a que se intentó cazar, pero no se logró