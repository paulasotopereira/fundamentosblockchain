# -*- coding: utf-8 -*-
import copy
import streamlit as st
from nucleo.cadena import ASIENTOS, encadenar, verificar, resumir, cuerpo
from nucleo.estilo import preparar, cabecera, caja, que_hace, ficha, sin_solucion, pie

preparar("La cadena rota")
cabecera("Sesión 2 · ejercicio B.5",
         "La cadena rota",
         "El encadenamiento hace que tocar un asiento delate la alteración **y diga "
         "dónde está**. Aquí se puede comprobar asiento por asiento.")

que_hace("Deja alterar cualquier asiento y muestra a partir de qué eslabón deja de "
         "cuadrar la cadena, y por qué.",
         "No dice si la alteración tiene relevancia jurídica, ni quién responde de "
         "ella. Eso es el ejercicio.")

cadena = encadenar(ASIENTOS)

st.markdown("### 1 · La cadena íntegra")
filas = ["| Asiento | Concepto | Actor | Dato registrado |", "|---|---|---|---|"]
for b in cadena:
    filas.append(f"| `{b['id']}` | {b['concepto']} | {b['actor']} | {b['datos']} |")
st.markdown("\n".join(filas))

st.markdown("### 2 · Alterar un asiento")
st.caption("Se edita el texto del asiento pero **se conservan los resúmenes ya "
           "registrados**: es lo que ocurre si alguien edita la base de datos y no "
           "toca nada más.")

col_a, col_b = st.columns([1, 3])
with col_a:
    elegido = st.selectbox("Asiento", [a["id"] for a in ASIENTOS], index=2)
idx = [a["id"] for a in ASIENTOS].index(elegido)
with col_b:
    nuevo = st.text_input("Dato registrado", value=ASIENTOS[idx]["datos"], key="dato")

alterada = copy.deepcopy(cadena)
alterada[idx]["datos"] = nuevo
cambiado = nuevo != ASIENTOS[idx]["datos"]

ok, donde = verificar(alterada)

if not cambiado:
    st.info("Todavía no se ha cambiado nada. Cambia un solo carácter y observa.")
elif ok:
    st.warning("La cadena sigue cuadrando: no se ha modificado el texto de verdad.")
else:
    st.error(f"**La cadena no cuadra.** Primera incoherencia en `{donde}`.")

st.markdown("### 3 · Dónde se rompe, exactamente")
registrado = alterada[idx]["resumen"]
recalculado = resumir(alterada[idx]["anterior"] + cuerpo(alterada[idx]))
st.markdown(
    f"<div class='lab-caja'><b>Resumen de {elegido} que consta registrado</b>"
    f"<div class='lab-mono'>{registrado}</div><br>"
    f"<b>Resumen que sale al rehacer la cuenta con el dato actual</b>"
    f"<div class='lab-mono'>{recalculado}</div></div>", unsafe_allow_html=True)

if cambiado:
    st.markdown(
        f"Los dos resúmenes no se parecen en nada aunque el cambio sea de un solo "
        f"carácter: es el **efecto avalancha**. Y como el resumen de `{elegido}` entra "
        f"en el cálculo del siguiente, **todos los asientos posteriores dejan también "
        f"de cuadrar**. Por eso la cadena no solo detecta la alteración: la localiza.")

st.markdown("### 4 · El estado de cada eslabón")
filas = ["| Asiento | ¿Cuadra? | Resumen registrado |", "|---|---|---|"]
roto = False
for b in alterada:
    propio = b["resumen"] == resumir(b["anterior"] + cuerpo(b))
    if not propio:
        roto = True
    estado = "sí" if propio and not roto else ("**NO — alterado**" if not propio
                                               else "**NO — arrastra el anterior**")
    filas.append(f"| `{b['id']}` | {estado} | `{b['resumen'][:32]}…` |")
st.markdown("\n".join(filas))

ficha("Que una alteración del registro se detecte, y que se pueda señalar el "
      "asiento concreto en el que se produjo.",
      "De rehacer la cuenta entera cada vez que se quiere verificar, y de no poder "
      "corregir un error honesto sin dejar rastro.",
      "Si el dato era cierto cuando se escribió. La cadena acredita la declaración "
      "y su antigüedad, no el hecho.")

sin_solucion()
pie()
