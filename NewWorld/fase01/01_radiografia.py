from pathlib import Path

import pandas as pd

DATASET=Path(
    'data/raw/nevworld_2121053672443607134_20261005_184808.jsonl'
)

if not DATASET.exists():
    raise FileNotFoundError(
        f'No se encuentra: {DATASET.resolve()}'
    )

df = pd.read_json(DATASET, lines=True)

required = [
    'run_id', 'event_index', 'tick', 'type'
]

assert not df.empty, 'El dataset está vacío'
assert all(column in df.columns for column in required), \
    'Faltan columnas principales'
assert not df.duplicated(['run_id', 'event_index']).any(), \
    'Hay eventos duplicados'

ordered = df.sort_values('event_index')
assert ordered['tick'].is_monotonic_increasing, \
    'Los ticks retroceden'

eventos, columnas = df.shape
print('Número de eventos:', eventos)
print('Número de columnas:', columnas)

print('\nNOMBRES DE LAS COLUMNAS')
print(df.columns.tolist())

print('\nTipo del primer evento registrado:',df['type'].iloc[0])

print('\nTipo de evento: ', df['type'].value_counts().index[0], ', cantidad: ', df['type'].value_counts().iloc[0])
print('\nEVENTOS POR TIPO')
print(df['type'].value_counts())



print('\n`run_id`, semilla y versión del esquema de la primera fila')
print('run_id:', df['run_id'].iloc[0])
print('semilla:', df['seed'].iloc[0])
print('esquema:', df['schema_version'].iloc[0])

print('\nTick mínimo:', df['tick'].min())
print('Tick máximo:', df['tick'].max())

print('\nRESULTADO DE LAS VALIDACIONES: OK')