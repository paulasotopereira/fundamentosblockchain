# -*- coding: utf-8 -*-
import streamlit as st
from nucleo.cadena import buscar, medir_ritmo, legible, cuerpo, ASIENTOS
from nucleo.estilo import preparar, cabecera, caja, pie

preparar("El precio de reescribir")
cabecera("Sesión 4 · hilo hacia el Tema 2",
         "El precio de reescribir")

caja("<b>Ampliación voluntaria: suma y no resta. No entra en la prueba objetiva.</b>", "rojo")

st.markdown("""
En la página anterior vimos que reescribir la cadena del consorcio cuesta milisegundos, y
que lo que lo impide no es la matemática sino un acuerdo entre nueve entidades.

Queda entonces la pregunta que abre el Tema 2: si un acuerdo entre nueve conocidos puede
reescribir el pasado, **¿cómo consigue una cadena pública —donde no hay consorcio, ni
contrato, ni nadie a quien demandar— que reescribirlo sea imposible en la práctica?**

La respuesta corta: **poniéndole precio**.
""")

ASIENTO = cuerpo(ASIENTOS[2])

st.markdown("### 1 · Añadir una condición al resumen")
st.markdown("La idea consiste en no aceptar cualquier resumen: solo vale si empieza por un "
            "número determinado de ceros. Como el resumen no se puede dirigir, la única "
            "forma de conseguirlo es probar. **Cada cero adicional multiplica por dieciséis "
            "el número esperado de intentos.** Eso es todo el mecanismo, y es aritmética.")

ceros = st.slider("Ceros exigidos", 1, 5, 4)
if st.button("Buscar un resumen que cumpla la condición", type="primary"):
    with st.spinner("Probando números…"):
        n, r, seg = buscar(ASIENTO, ceros)
    if n is None:
        st.warning("No se ha encontrado dentro del tope de intentos. Prueba con menos ceros.")
    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Intentos", f"{n:,}".replace(",", "."))
        c2.metric("Esperados de media", f"{16 ** ceros:,}".replace(",", "."))
        c3.metric("Segundos", f"{seg:.2f}")
        st.markdown(f"<div class='lab-caja'><b>Resumen obtenido</b>"
                    f"<div class='lab-mono'>{r}</div></div>", unsafe_allow_html=True)
        st.caption("Una sola búsqueda tiene suerte o no la tiene. Lo que no oscila es la "
                   "media esperada, y es exactamente 16 por cada cero añadido.")

st.markdown("### 2 · La curva del precio")
st.caption("No hace falta medir más: basta multiplicar. Se toma el ritmo real de la "
           "máquina donde corre esta aplicación.")

if st.button("Medir el ritmo de esta máquina y extrapolar"):
    with st.spinner("Midiendo…"):
        ritmo = medir_ritmo()
    st.markdown(f"Ritmo medido: **{ritmo:,.0f} resúmenes por segundo**."
                .replace(",", "."))
    filas = ["| Ceros | Intentos esperados | Tiempo en esta máquina |", "|---|---|---|"]
    for k in range(4, 13):
        esperados = 16 ** k
        filas.append(f"| {k} | {esperados:,} |".replace(",", ".") +
                     f" {legible(esperados / ritmo)} |")
    st.markdown("\n".join(filas))
    st.caption("Léase la columna de la derecha despacio. No hay ningún truco: es el mismo "
               "cálculo, repetido más veces.")
    caja("Nada de esto hace el pasado <b>imposible</b> de reescribir. Lo hace <b>caro</b>. "
         "Y un coste es una magnitud económica, no una garantía jurídica ni una propiedad "
         "matemática.", "rojo")

st.markdown("### 3 · La consecuencia jurídica, que es la única que importa")
st.markdown("""
En una cadena pública sin permiso, reescribir el asiento número tres de seis obliga a
rehacer también el cuarto, el quinto y el sexto, porque cada uno incluye el resumen del
anterior. Y mientras se rehacen, los demás siguen añadiendo asientos por delante: hay que
alcanzarlos. **Cuanto más antiguo es un asiento, más caro es tocarlo.**
""")

caja("Al valorar un asiento en cadena pública, <b>cuánto tiempo lleva ahí</b> es un dato "
     "relevante. En una cadena de consorcio, en cambio, la antigüedad no aporta "
     "resistencia adicional: reescribir el asiento de hace tres años cuesta lo mismo que "
     "reescribir el de ayer.", "verde")

st.markdown("### 4 · Las dos formas de sostener el pasado")
st.markdown("""
| | Cadena pública sin permiso | Cadena permisionada de consorcio |
|---|---|---|
| **Qué impide reescribir** | Un coste que crece con la antigüedad | Un contrato, un acta y una responsabilidad |
| **Naturaleza de la garantía** | Económica | Jurídica y organizativa |
| **Frente a quién protege** | Frente a todos, incluidos los que la operan | Frente a cada miembro aislado, **no** frente a todos juntos |
| **Quién responde si falla** | Nadie identificable | Los miembros del consorcio, por su nombre |
| **Quién asume el coste** | Quien valida, retribuido por el sistema | Los miembros, en su presupuesto |
""")

st.markdown("La última fila es la que suele sorprender: **la cadena pública no es gratis**. "
            "Alguien paga ese coste, y hay que entender con qué incentivo lo paga. Esa es, "
            "literalmente, la pregunta viva del Tema 2.")

caja("<b>¿Se puede fabricar acuerdo entre desconocidos que pueden mentir, sin que nadie "
     "arbitre?</b>", "verde")

pie()
