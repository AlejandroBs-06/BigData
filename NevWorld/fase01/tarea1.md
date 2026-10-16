# Radiografía de una partida de NevWorld

Has terminado una partida y el juego ha generado un archivo JSONL. Tu misión es abrirlo con pandas y preparar una ficha que permita a otra persona comprender qué contiene ese registro.

Utiliza **los datos de tu propia partida** y las operaciones vistas en el tema. No modifiques el archivo RAW.

## Teoría de apoyo

JSONL guarda un evento en cada línea. pandas lo carga con `pd.read_json(..., lines=True)` en un **DataFrame**, una tabla de filas y columnas. La variable `df` recibe ese nombre como abreviatura de DataFrame: cada fila representa un evento y cada columna, un campo.

| Para… | Utiliza… |
| --- | --- |
| Representar y comprobar la ruta | `Path(...)` y `exists()` |
| Ver los primeros eventos | `df.head()` |
| Obtener filas y columnas | `df.shape` |
| Consultar los nombres de los campos | `df.columns.tolist()` |
| Contar eventos de cada tipo | `df['type'].value_counts()` |
| Leer un valor de la primera fila | `df['campo'].iloc[0]` |
| Obtener los extremos de los ticks | `df['tick'].min()` y `max()` |

Los eventos pueden tener campos diferentes: un `NaN` representa una ausencia, no necesariamente un error ni un cero. El tick mide tiempo simulado; varios eventos pueden compartirlo.

## Enunciado

Crea `scripts/actividades/01_radiografia.py` en tu proyecto `bigdata-game`. Carga el JSONL que has guardado en `data/raw`, comprobando antes que la ruta existe. Puedes apoyarte en el script del tema.

Aplica las cuatro validaciones básicas del tema: que la tabla no esté vacía, que existan las columnas principales, que no se repita la pareja `run_id` y `event_index`, y que los ticks no retrocedan al ordenar por `event_index`. Hazlo antes de consultar la primera fila.

Después, muestra las primeras filas y obtén los datos necesarios para completar esta ficha:

| Dato de mi partida | Resultado |
| --- | --- |
| Nombre del archivo JSONL | nevworld_2121053672443607134_20261005_184808 |
| Número total de eventos | 2867 |
| Número de columnas | 37 |
| Nombres de las columnas | ['schema_version', 'run_id', 'seed', 'event_index', 'tick', 'type', 'started_at_utc', 'resource_type', 'amount_before', 'amount_after', 'amount_delta', 'building_id', 'building_type', 'cell_x', 'cell_y', 'width', 'height', 'villager_id', 'activity', 'prey_type', 'population', 'constructed_buildings', 'wood_stock', 'food_stock', 'gold_stock', 'day', 'actor_id', 'target_id', 'interaction_type', 'topic', 'relationship_actor_to_target_after', 'relationship_target_to_actor_after', 'need_type', 'state', 'name', 'cause', 'predator_type'] |
| Tipo del primer evento registrado | simulation_started |
| Tipo de evento más frecuente y cantidad | Tipo de evento: villager_activity_changed, cantidad: 1941|
| Recuento de todos los tipos de evento | {"type": "villager_activity_changed", "count": 1941}, {"type": "villager_need_changed", "count": 246}, {"type": "world_snapshot", "count": 240}, {"type": "resource_changed", "count": 174}, {"type": "social_interaction", "count": 91}, {"type": "construction_abandoned", "count": 50}, {"type": "villager_drank", "count": 48}, {"type": "villager_ate", "count": 37}, {"type": "hunt_completed", "count": 21}, {"type": "construction_expired", "count": 9}, {"type": "building_created", "count": 7}, {"type": "simulation_started", "count": 1}, {"type": "villager_created", "count": 1}, {"type": "villager_died", "count": 1} |
| `run_id`, semilla y versión del esquema de la primera fila | run_id: 20261005_184808_2121053672443607134_ed06445e606844ba9564c3bdac122867, semilla: 2121053672443607134, esquema: 2|
| Tick mínimo y tick máximo | Tick mínimo: 0, Tick máximo: 148800 |
| Resultado de las validaciones | OK |

Termina la ficha respondiendo con tus palabras:

1. ¿Qué te permite afirmar el recuento sobre tu partida? Nos permite afirmar el número de eventos y de columnas ¿Por qué el tipo más frecuente no tiene que ser el más importante? Porque son importantes para el buen funcionamiento
2. ¿Por qué una celda vacía no significa necesariamente que el registro esté mal? Porque no todos los eventos contienen los mismos datos
3. ¿Qué sabes ahora del archivo y qué pregunta sobre tu partida necesitaría un análisis posterior? Lo que se ahora del archivo es que pertenece a una única partida con 4 aldeanos que realizan diversas actividades. Alguna pregunta para un análisis posterior sería cuánto tiempo están realizando una actividad.  