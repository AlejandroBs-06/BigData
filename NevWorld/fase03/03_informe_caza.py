from pathlib import Path

import pandas as pd


DATA_DIR = Path('data/processed')
REPORTS_DIR = Path('NewWorld/fase03/reports')
REPORTS_DIR.mkdir(exist_ok=True)

hunts=pd.read_csv(DATA_DIR / "hunts.csv")
resources=pd.read_csv(DATA_DIR / "resources.csv")

if hunts.empty:
    print("No hay cacerías completadas registradas.")

hunts_counts=len(hunts)
print("\nCACERÍAS COMPLETADAS")
print(hunts_counts)

hunts_groups=hunts['prey_type'].value_counts()
print("\nNÚMERO DE CACERÍAS SEGÚN LA PRESA")
print(hunts_groups)

hunts_proportions=hunts['prey_type'].value_counts(normalize=True)
hunts_percents=(hunts_proportions*100).round(1)
print("\nPORCENTAJES")
print(hunts_percents)

hunts_days=hunts.groupby('simulation_day').size()
print("\nNÚMERO DE CACERÍAS POR DÍA")
print(hunts_days)

food_stock=resources[resources["resource_type"]=="food"]
if food_stock.empty:
    print("No hay eventos de comida")
incrementos=food_stock[food_stock['amount_delta'] > 0]
disminucion=food_stock[food_stock['amount_delta'] < 0].copy()
disminucion['amount_delta']=disminucion["amount_delta"].abs()
print("\nINCREMENTOS REGISTRADOS")
print(incrementos["amount_delta"].sum())
print("\nDESCENSOS REGISTRADOS")
print(disminucion["amount_delta"].sum())
print("\nBALANCE NETO")
print(food_stock['amount_delta'].sum())

assert (hunts_groups.sum()==hunts_counts), \
    'La suma del número de cacerías por presa no coincide con el número de cacerías completas'
assert (hunts_days.sum()==hunts_counts), \
    'La suma del número de cacerías por día no coincide con el número de cacerías completas'
assert ((incrementos["amount_delta"].sum() - disminucion["amount_delta"].sum())==food_stock['amount_delta'].sum()), \
    'La diferencia entre el incremento y el descenso de comida no coincide con el balance neto'
if len(hunts)>0:
    assert(abs((hunts_proportions.sum()*100) - 100) < 0.000001) ,\
        'La suma de los porcentajes no da 100'

summary=pd.DataFrame([
    {'metric':'hunt_events', 'value':len(hunts)},
    {'metric':'food_change_events', 'value':len(resources[resources["resource_type"]=="food"])},
    {'metric':'food_gains', 'value':incrementos["amount_delta"].sum()},
    {'metric':'food_reductions', 'value':disminucion["amount_delta"].sum()},
    {'metric':'food_net_change', 'value':food_stock['amount_delta'].sum()}
])

summary.to_csv(REPORTS_DIR / 'hunting_summary.csv', index=False)