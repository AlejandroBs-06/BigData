from pathlib import Path

import duckdb
import pandas as pd

DATA_DIR = Path('data/processed')
PARQUET_DIR = DATA_DIR / 'parquet'
csv_path=DATA_DIR / 'hunts.csv'
table=pd.read_csv(csv_path)

hunts_type=table["prey_type"].value_counts()

assert {"prey_type"}.issubset(table.columns), \
    'La columna `prey_type` no existe'
assert table["prey_type"].notna().all().all(), \
    'Hay algún valor en la columna `prey_type` que es nulo'
hunts_parquet=PARQUET_DIR / 'hunts.parquet'
table.to_parquet(hunts_parquet, engine='pyarrow', index=False)
print('  CSV:', csv_path.stat().st_size, 'bytes')
print('  Parquet:', hunts_parquet.stat().st_size, 'bytes')

connection = duckdb.connect()

resource_query = """
    SELECT
        prey_type,
        COUNT("prey_type") as hunt_count
    FROM read_parquet('data/processed/parquet/hunts.parquet')
    GROUP BY prey_type
    ORDER BY hunt_count DESC
"""

resource_summary = connection.execute(
    resource_query
).fetchdf()

print('\nRECURSOS CONSULTADOS CON SQL')
print(resource_summary)

suma=0
barras=hunts_type.plot.bar(color='steelblue')
for barra in barras.patches:
    altura=barra.get_height()
    suma+=altura
assert resource_summary["hunt_count"].sum()==len(table), \
    'La suma de `hunt_count` no coincide con el número de filas del CSV. '
assert resource_summary["hunt_count"].sum()==suma, \
    'La suma de `hunt_count` no coincide con la longitud de las barras del gráfico de la actividad 4. '


Path('NevWorld/fase05/reports').mkdir(exist_ok=True)

resource_summary.to_csv(
    'NevWorld/fase05/reports/hunts_by_prey_sql.csv',
    index=False
)
connection.close()