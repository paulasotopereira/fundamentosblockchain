# -*- coding: utf-8 -*-
import streamlit as st
from nucleo.estilo import preparar, cabecera, caja, que_hace, sin_solucion, pie

preparar("Las cuatro preguntas")
cabecera("Sesión 4 · ejercicio B.7",
         "Las cuatro preguntas",
         "Se les pone número y se deja que el instrumento recomiende. Y después se "
         "cambia la ponderación sin tocar un solo dato del caso.")

que_hace("Puntúa las cuatro preguntas, da una recomendación y dice **qué respuesta "
         "está sosteniendo el resultado**.",
         "No decide. Un instrumento de puntuación no sustituye al criterio: hace "
         "visible qué pregunta está haciendo el trabajo.")

PREGUNTAS = {
    "P1": ("¿Hay varias partes que necesiten escribir en un mismo registro?",
           "Si hay una sola, no hay problema"),
    "P2": ("¿Desconfían entre sí lo bastante como para no aceptar el registro de una de ellas?",
           "Si se fían, sobra el aparato"),
    "P3": ("¿Importan el orden y la antigüedad de los asientos?",
           "Si da igual cuándo, basta una lista"),
    "P4": ("¿FALTA un tercero de confianza disponible, aceptado por todos y proporcionado en coste?",
           "Si lo hay, hay que justificarse"),
}

SUPUESTOS = {
    "TrazaOliva · consorcio del aceite": {"P1": 3, "P2": 2, "P3": 3, "P4": 0},
    "Nueve navieras sin autoridad común": {"P1": 3, "P2": 3, "P3": 3, "P4": 3},
    "Almacén interno de una sola empresa": {"P1": 0, "P2": 0, "P3": 2, "P4": 0},
}

st.markdown("### 1 · Puntuar")
supuesto = st.selectbox("Supuesto de partida", list(SUPUESTOS), index=0)
base = SUPUESTOS[supuesto]
st.caption("Cada pregunta, de 0 a 3. Si en clase acordasteis otras puntuaciones, "
           "cambiadlas: eso es exactamente lo que hay que hacer con un instrumento así.")

puntos = {}
for k, (texto, mide) in PREGUNTAS.items():
    puntos[k] = st.slider(f"**{k}** · {texto}", 0, 3, base[k], key=f"p_{k}_{supuesto}",
                          help=f"Qué está midiendo: {mide}")

st.markdown("### 2 · La ponderación, que también es una decisión")
peso_p4 = st.slider("Peso de P4 — la existencia de un tercero de confianza", 1.0, 3.0,
                    1.0, step=0.5, format="×%.1f",
                    help="Hasta ahora las cuatro pesaban igual. Eso también era una decisión.")
pesos = {"P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": peso_p4}

total = sum(puntos[k] * pesos[k] for k in PREGUNTAS)
maximo = sum(3 * pesos[k] for k in PREGUNTAS)
umbral = maximo / 2
justificado = total >= umbral

c1, c2, c3 = st.columns(3)
c1.metric("Puntuación", f"{total:.1f} / {maximo:.1f}")
c2.metric("Umbral", f"{umbral:.1f}")
c3.metric("Recomendación", "Justificado" if justificado else "No justificado")

st.markdown("### 3 · ¿Qué respuesta sostiene el resultado?")
lineas = ["| | Pregunta | Puntos | Peso | ¿Puede volcar el resultado? |",
          "|---|---|---|---|---|"]
for k, (texto, _) in PREGUNTAS.items():
    vuelca = []
    for alt in range(4):
        if alt == puntos[k]:
            continue
        t = sum((alt if j == k else puntos[j]) * pesos[j] for j in PREGUNTAS)
        if (t >= umbral) != justificado:
            vuelca.append(str(alt))
    veredicto = f"sí, si pasa a {' o '.join(vuelca)}" if vuelca else "**no**"
    corto = texto if len(texto) < 62 else texto[:59] + "…"
    lineas.append(f"| {k} | {corto} | {puntos[k]} | ×{pesos[k]:.1f} | {veredicto} |")
st.markdown("\n".join(lineas))

if puntos["P4"] == 0 and justificado and peso_p4 == 1.0:
    caja("<b>Léase la fila de P4 despacio.</b> Ya puntúa cero y el total sigue pasando "
         "el umbral: no hay nada que P4 pueda hacer para cambiar la recomendación. "
         "Las otras tres la neutralizan.<br><br>"
         "Ese es el defecto del instrumento con pesos iguales, y no es un defecto de "
         "programación: <b>la pregunta que decide el caso está neutralizada por las "
         "otras tres</b>. Sube el peso de P4 y mira qué pasa.", "rojo")
elif peso_p4 > 1.0:
    caja(f"Mismos hechos, mismas respuestas, mismo instrumento. Solo ha cambiado el peso "
         f"de P4, y con ×{peso_p4:.1f} la recomendación es "
         f"<b>{'justificado' if justificado else 'no justificado'}</b>.<br><br>"
         f"La ponderación únicamente cambia el resultado <b>donde las preguntas se "
         f"contradicen entre sí</b>, que es donde hacen falta juristas.", "verde")

st.markdown("### 4 · Lo que hay que escribir")
caja("<b>Regla para el escrito:</b> cuando una recomendación dependa de una ponderación, "
     "la ponderación se declara y se justifica en el propio escrito. No se esconde dentro "
     "del número.<br><br>"
     "Dicho de otra forma, y sirve literalmente para la Parte D de la Entrega 1: "
     "<i>la recomendación depende de la ponderación elegida, que es una decisión y no un "
     "hallazgo</i>.", "verde")

st.markdown("""
Y por eso la respuesta profesional a TrazaOliva no es ni sí ni no, sino una
**delimitación del objeto**: la cadena aporta sobre lo que el consejo regulador *no*
certifica —temperatura de transporte, tiempos, custodia intermedia— y añade coste sin
añadir garantía sobre lo que *sí* certifica.
""")

sin_solucion()
pie()
