# El parte de caza, de un vistazo

## 1. Decisiones iniciales

* **¿Qué representa cada barra?** Representa el número de veces que se cazó a cada presa.
* **¿Qué cantidad y unidad aparecerán en el eje vertical?** En el eje vertical aparecen las posibles cantidades de cacerías completadas.
* **¿Por qué usar barras y no una línea que conecte las presas?** Porque se quiere comparar el número de veces que se cazó una presa en la partida y con la línea se comprueba la variedad de valores durante la partida
* **Título elegido:** "Presas cazadas"


## 2. Comparación con los recuentos

Gracias al comando: `altura=barra.get_height()` que nos sirve para sacar la altura de una barra del gráfico y de hacer un sumatorio de todas ellas se puede comprobar que la altura de las barras coincide con los recuentos obtenidos en la actividad 3 con un total de 21 cacerías completadas


## 3. Tres frases finales

1. **Observación:** La única presa que cuenta con cacerías completas registradas es `sheep` con 21 cacerías.
2. **Límite:** El gráfico no muestra cuánto tiempo se dedicó a cazar ni cuánta comida produjo cada presa debido a que la información la sacamos a través de este comando: `hunts['prey_type'].value_counts()` que nos muestra el número de registros que tiene cada presa, pero no muestra ni el tiempo empleado ni la comida producida.
3. **Pregunta pendiente:** Una pregunta que no puedo responder con este gráfico sería: ¿Cuánto tiempo se empleó para completar cada cacería? Para ello necesitaría los valores de la columna `ticks`