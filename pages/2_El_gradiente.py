# -*- coding: utf-8 -*-
import streamlit as st
from nucleo.estilo import preparar, cabecera, caja, que_hace, sin_solucion, pie

preparar("El gradiente")
cabecera("Sesión 3 · ejercicio C.4",
         "El gradiente de descentralización",
         "«Descentralizado» no es un sí o un no. Se puntúa por dimensiones, y cada "
         "dimensión señala a alguien distinto.")

que_hace("Puntúa las cuatro dimensiones de un sistema y enseña dónde queda "
         "concentrado el control.",
         "No imputa responsabilidad a nadie. Decir a quién se le reprocha qué es el "
         "ejercicio, y se evalúa la justificación, no el número.")

DIMENSIONES = {
    "nodos": ("¿Quién opera los nodos?",
              "Quien tiene la copia es a quien se le requiere exhibirla"),
    "orden": ("¿Quién valida y fija el orden?",
              "Quien decide qué entra y en qué orden decide qué consta"),
    "programa": ("¿Quién mantiene el programa?",
                 "Quien puede cambiar las reglas puede cambiar el resultado"),
    "acceso": ("¿Quién controla la entrada y la salida?",
               "Quien admite y expulsa gobierna quién puede escribir"),
}

st.markdown("### 1 · Puntuar el sistema")
st.caption("0 = una sola entidad lo controla · 3 = está repartido de hecho entre muchas.")

puntos, notas = {}, {}
for clave, (pregunta, porque) in DIMENSIONES.items():
    c1, c2 = st.columns([2, 3])
    with c1:
        puntos[clave] = st.slider(pregunta, 0, 3, 1, key=f"s_{clave}")
    with c2:
        notas[clave] = st.text_input("¿Quién, en este caso?", key=f"t_{clave}",
                                     placeholder="escribe el nombre de la entidad")
    st.caption(f"Por qué importa: {porque}")

total = sum(puntos.values())
st.markdown("### 2 · Lo que sale")

c1, c2 = st.columns([1, 3])
with c1:
    st.metric("Puntuación", f"{total} / 12")
with c2:
    if total <= 3:
        lectura = ("**Concentrado.** Hay un sujeto identificable detrás de casi todo. "
                   "El Derecho tiene a quién dirigirse, y la promesa de «que nadie "
                   "controle» no se sostiene.")
    elif total <= 8:
        lectura = ("**Mixto, que es el caso interesante.** Unas dimensiones están "
                   "repartidas y otras no. La pregunta jurídica se dirige a las que "
                   "**no** lo están.")
    else:
        lectura = ("**Repartido.** No hay un sujeto al que dirigirse por la vía "
                   "ordinaria, y ahí empieza el problema del Tema 5: cuando el Derecho "
                   "necesita un responsable y la arquitectura no lo da, lo designa.")
    st.markdown(lectura)

filas = ["| Dimensión | Puntuación | Quién manda ahí |", "|---|---|---|"]
for clave, (pregunta, _) in DIMENSIONES.items():
    quien = notas[clave].strip() or "_sin rellenar_"
    filas.append(f"| {pregunta} | {puntos[clave]} / 3 | {quien} |")
st.markdown("\n".join(filas))

bajas = [p for p, v in DIMENSIONES.items() if puntos[p] <= 1]
if bajas:
    nombres = ", ".join(DIMENSIONES[b][0].strip("¿?").lower() for b in bajas)
    caja(f"<b>Las dimensiones concentradas son las que hacen trabajo jurídico.</b> "
         f"Aquí lo están: {nombres}. Un escrito que quiera imputar algo tiene que "
         f"apoyarse en esas, no en la puntuación global.", "verde")

sin_solucion()
caja("<b>Recordatorio.</b> Este instrumento no decide: hace visible dónde está "
     "concentrado el control. Igual que en las cuatro preguntas, cambiar el peso de "
     "una dimensión cambiaría la lectura, y esa ponderación es una decisión que hay "
     "que declarar y justificar en el escrito.", "rojo")
pie()
