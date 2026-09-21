# -*- coding: utf-8 -*-
import copy
import time
import streamlit as st
from nucleo.cadena import (ASIENTOS, CONSORCIO, encadenar, verificar, coincidencias)
from nucleo.estilo import preparar, cabecera, caja, que_hace, ficha, pie

preparar("Reescribir la cadena")
cabecera("Sesión 4 · la grieta",
         "Reescribir la cadena",
         "En la página 1 vimos que alterar un asiento rompe la cadena. La pregunta de "
         "hoy es la siguiente: **¿y si quien lo altera no se detiene ahí?**", rojo=True)

que_hace("Altera un asiento, rehace la cuenta hacia delante y enseña que la cadena "
         "vuelve a cuadrar. Después multiplica el efecto por las diez copias del "
         "consorcio.",
         "No demuestra que reescribir sea fácil en la práctica: exige coordinación, "
         "deja rastro fuera de la cadena y probablemente constituye ilícito. Demuestra "
         "**dónde no está la garantía**.")

original = encadenar(ASIENTOS)

st.markdown("### 1 · Se altera un asiento")
c1, c2 = st.columns([1, 3])
with c1:
    elegido = st.selectbox("Asiento", [a["id"] for a in ASIENTOS], index=2)
idx = [a["id"] for a in ASIENTOS].index(elegido)
with c2:
    nuevo = st.text_input("Dato registrado", value=ASIENTOS[idx]["datos"])

alterados = copy.deepcopy(ASIENTOS)
alterados[idx]["datos"] = nuevo
cambiado = nuevo != ASIENTOS[idx]["datos"]

parcial = copy.deepcopy(original)
parcial[idx]["datos"] = nuevo
ok_parcial, donde = verificar(parcial)

if cambiado:
    st.error(f"Sin tocar nada más, la cadena **no cuadra** desde `{donde}`. "
             "Hasta aquí es exactamente lo de la sesión 2.")
else:
    st.info("Cambia un carácter del dato registrado para poner en marcha la página.")
    st.stop()

st.markdown("### 2 · Y ahora se rehace la cuenta")
t0 = time.perf_counter()
reescrita = encadenar(alterados)
ms = (time.perf_counter() - t0) * 1000
ok_re, _ = verificar(reescrita)

c1, c2, c3 = st.columns(3)
c1.metric("¿Cuadra la cadena reescrita?", "Sí" if ok_re else "No")
c2.metric("Asientos rehechos", len(ASIENTOS))
c3.metric("Tiempo empleado", f"{ms:.2f} ms")

st.caption(f"Al mismo ritmo, reescribir 100.000 asientos —un año entero de registro del "
           f"consorcio— costaría unos {ms / len(ASIENTOS) * 100_000 / 1000:.1f} segundos.")

caja("<b>La cadena reescrita verifica.</b> Es internamente coherente. Un perito que "
     "reciba solo esta cadena y la compruebe informará de que está íntegra, y "
     "tendrá razón: lo está.<br><br>"
     "<b>Coherencia interna no es autenticidad.</b> Una cadena verifica contra sí "
     "misma, no contra el mundo.", "rojo")

st.markdown("#### El único punto de comparación que queda")
st.markdown(
    f"<div class='lab-caja'><b>Último resumen, cadena original</b>"
    f"<div class='lab-mono'>{original[-1]['resumen']}</div><br>"
    f"<b>Último resumen, cadena reescrita</b>"
    f"<div class='lab-mono'>{reescrita[-1]['resumen']}</div></div>",
    unsafe_allow_html=True)
st.caption(f"Coinciden {coincidencias(original[-1]['resumen'], reescrita[-1]['resumen'])} "
           f"caracteres de 64; por puro azar saldrían unos 4. Quien conserve el resumen "
           f"anterior detecta la reescritura al instante. Quien no lo conserve, no tiene "
           f"con qué comparar.")

st.markdown("### 3 · Las diez copias")
st.markdown("El registro no está en un sitio: los diez miembros del consorcio conservan "
            "una copia. Reescribir la propia no sirve de nada… salvo que las demás hagan "
            "lo mismo.")

n = st.slider("Miembros que sustituyen su copia por la reescrita", 0, len(CONSORCIO), 0)
disidentes = CONSORCIO[n:]

if n == 0:
    st.success("Nadie ha sustituido nada. Las diez copias coinciden con la original.")
elif disidentes:
    st.warning(f"**Divergencia entre copias.** Conservan la original: "
               f"{', '.join(disidentes)}.")
    if len(disidentes) == 1:
        st.markdown(f"Queda **uno solo** frente a los demás, y resulta ser "
                    f"**{disidentes[0]}** — que está dentro del consorcio.")
    st.caption("La cadena no resuelve cuál de las dos versiones es la verdadera: solo "
               "informa de que hay dos. Quien decide cuál vale es alguien de fuera.")
else:
    st.error("**Las diez copias coinciden. No hay nada que detectar.** "
             "Ninguna comprobación interna al sistema puede distinguir esta cadena de "
             "la original.")

st.markdown("### 4 · La pregunta que se queda abierta")
st.markdown("Supongamos que mañana entra en el consorcio un miembro nuevo. ¿Puede "
            "comprobar por sí solo que lo anterior a su entrada no fue reescrito?")
st.markdown("""
Recibe una copia de la cadena, que verifica, y la palabra de los demás de que es la
original. No recibe ninguna prueba, interna a la cadena, de que no la reescribieran antes.
Le haría falta una de estas dos cosas, y **ninguna está dentro del sistema**:

- una copia anterior en poder de alguien ajeno al consorcio, o
- un anclaje de los resúmenes en un registro que el consorcio no controle.
""")
caja("Anótese la segunda: resolver el problema de una cadena **con un intermediario**. "
     "Vuelve en el Tema 4 y en el Tema 5.", "verde")

ficha("Que ningún miembro por sí solo pueda alterar el pasado sin que los demás lo "
      "detecten, y que cada asiento quede atribuido a una entidad identificada.",
      "De multiplicar copias, sostener una regla de consenso y una gobernanza del "
      "consorcio, y renunciar a la rectificación sencilla de un error honesto.",
      "La veracidad de lo asentado. La garantía frente a los miembros **actuando de "
      "común acuerdo**. Y la verificación del pasado por quien llega después.")

caja("En una cadena pública sin permiso, reescribir el pasado es caro por construcción. "
     "En una cadena de consorcio es barato, y lo que lo impide es un contrato, un acta y "
     "la amenaza de una responsabilidad. Es decir: <b>Derecho</b>.", "rojo")
pie()
