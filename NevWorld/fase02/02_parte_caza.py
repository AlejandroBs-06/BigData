from pathlib import Path

import pandas as pd

DATASET=Path(
    'data/raw/nevworld_2121053672443607134_20261005_184808.jsonl'
)

if not DATASET.exists():
    raise FileNotFoundError(
        f'No se encuentra: {DATASET.resolve()}'
    )

#Aquí definimos otra ruta:
OUTPUT_DIR = Path('data/processed')

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_json(DATASET, lines=True)

def event_table(event_type, columns):

    selected = ['run_id', 'event_index', 'tick', *columns]

    available = [
        column for column in selected
        if column in df.columns
    ]

    table = df.loc[
        df['type'] == event_type,
        available,
    ].copy()


    if not table.empty:
        table['simulation_day'] = table['tick'] // 12000

    return table

tables={
    'hunts': event_table('hunt_completed',[
        "villager_id", "prey_type"
    ])
}

for name, table in tables.items():
    output = OUTPUT_DIR / f'{name}.csv'

    table.to_csv(output, index=False)

    print(name, '->', len(table), 'filas')
    print('Ruta completa: ', output)

assert (df['type'] == 'hunt_completed').sum()==len(df[df['type']=='hunt_completed']), \
    'El número de filas no coincide'

assert not df.duplicated(['run_id', 'event_index']).any(), \
    'Hay eventos duplicados'

campos_obligatorios=['run_id', 'event_index', 'prey_type', 'villager_id', 'simulation_day']
assert table[campos_obligatorios].notna().all().all(), \
    'Hay algún valor nulo'

assert (table['simulation_day'] == table['tick'] // 12000).all(), \
    'Hay alguna división incorrecta'