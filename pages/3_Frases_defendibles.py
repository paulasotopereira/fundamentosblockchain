# -*- coding: utf-8 -*-
import streamlit as st
from nucleo.estilo import preparar, cabecera, caja, que_hace, sin_solucion, pie

preparar("Frases defendibles")
cabecera("Sesión 3 · ejercicio C.5",
         "Frases defendibles",
         "Tres afirmaciones que se leen a diario y que un escrito no sostendría. "
         "Cada una falla por un motivo distinto.")

que_hace("Presenta las tres frases con una pista sobre **dónde** está el fallo, y un "
         "sitio para reescribirlas.",
         "No da la versión correcta. La reescritura es el ejercicio y se corrige en "
         "clase; publicarla aquí lo anularía.")

FRASES = [
    {
        "texto": "«El lote está certificado en blockchain, de modo que consta "
                 "acreditado que la temperatura de transporte no superó los 18 °C.»",
        "pista": "Mira el verbo. ¿Qué es exactamente lo que el registro acredita: el "
                 "hecho, o algo sobre el hecho? Repasa el hilo número uno del curso.",
        "familia": "Confunde acreditar el hecho con acreditar la declaración del hecho.",
    },
    {
        "texto": "«Al tratarse de una blockchain privada, el sistema no está sujeto a "
                 "las obligaciones del reglamento.»",
        "pista": "«Blockchain privada» no es una categoría del legislador europeo. "
                 "¿Qué habría que decir en su lugar para que la frase produzca algún "
                 "efecto jurídico?",
        "familia": "Usa una etiqueta del sector como si fuera una calificación jurídica.",
    },
    {
        "texto": "«El registro es inmutable, por lo que la anotación no puede "
                 "revertirse ni dejarse sin efecto.»",
        "pista": "Dos palabras distintas hacen aquí el mismo trabajo, y no significan "
                 "lo mismo. Una describe el registro; la otra, el efecto jurídico.",
        "familia": "Confunde inmutabilidad del soporte con irreversibilidad del efecto.",
    },
]

for i, f in enumerate(FRASES, start=1):
    st.markdown(f"### Frase {i}")
    caja(f"<i>{f['texto']}</i>", "rojo")
    with st.expander("Pista — dónde está el fallo"):
        st.markdown(f["pista"])
        st.caption(f"Familia del error: {f['familia']}")
    st.text_area("Tu versión defendible", key=f"frase_{i}", height=90,
                 placeholder="Reescríbela de modo que puedas sostenerla ante un juez.")
    st.divider()

st.markdown("### Cómo se corrige esto")
st.markdown("""
Una frase es defendible cuando **no afirma más de lo que el mecanismo permite** y
cuando **se puede sostener con la norma a la vista**. En la práctica, casi siempre
consiste en hacer tres cosas:

- Sustituir el verbo que afirma de más por el que describe lo que el mecanismo hace.
- Cambiar la etiqueta del sector por la descripción que el Derecho sí reconoce: quién
  escribe, con qué título y con qué responsabilidad pactada.
- Añadir expresamente el límite, en lugar de callarlo.
""")

caja("<b>La frase que gobierna la corrección de toda la asignatura:</b> reconocer por "
     "escrito lo que tu afirmación no resuelve suma; afirmar más de lo que el mecanismo "
     "permite resta.", "verde")

sin_solucion()
pie()
