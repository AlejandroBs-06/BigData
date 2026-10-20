from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = Path('data/processed')
CHARTS_DIR = Path('NevWorld/fase04/reports/charts')
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

hunts=pd.read_csv(DATA_DIR / 'hunts.csv')

if len(hunts['prey_type'])==0:
    print("No hay filas")
else:
    ordered=hunts.sort_values("tick")
    hunts_counts = hunts['prey_type'].value_counts()

    plt.figure(figsize=(8, 4))

    barras=hunts_counts.plot.bar(color='steelblue')
    plt.title('Presas cazadas')
    plt.xlabel('Presas')
    plt.ylabel('Cacerías completadas registradas')

    plt.locator_params(axis='y',integer=True)
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig(CHARTS_DIR / '05_hunts_by_prey.png')
    plt.close()

    suma=0
    for barra in barras.patches:
        altura=barra.get_height()
        suma+=altura
    if suma==len(hunts):
        print("La altura de la barra coincide con los recuentos de la actividad 3")
        