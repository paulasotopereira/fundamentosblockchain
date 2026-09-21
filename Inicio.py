# -*- coding: utf-8 -*-
import streamlit as st
from nucleo.estilo import preparar, cabecera, caja, pie

preparar("Inicio")
cabecera("Tema 1 · Sesiones 2, 3 y 4",
         "Laboratorio de la asignatura",
         "Seis páginas para trabajar los mecanismos con las manos. Se abre en el "
         "navegador, no se instala nada y no hace falta ninguna cuenta.")

caja(
    "<b>Para qué sirve esto y para qué no.</b> Sirve para ver funcionar un "
    "mecanismo y comprobar qué garantiza, a costa de qué y qué deja fuera. "
    "No sirve para resolver los ejercicios: la calificación jurídica la haces tú, "
    "y es lo único que se evalúa.", "verde")

st.markdown("### Qué hay en cada página")

st.markdown("""
| | Página | De qué sesión viene | Qué se hace |
|---|---|---|---|
| **1** | La cadena rota | Sesión 2 · ejercicio B.5 | Localizar dónde se rompe una cadena y por qué el resto deja de cuadrar |
| **2** | El gradiente | Sesión 3 · ejercicio C.4 | Puntuar las cuatro dimensiones de la descentralización y ver a quién señalan |
| **3** | Frases defendibles | Sesión 3 · ejercicio C.5 | Reescribir tres afirmaciones que un escrito no sostendría |
| **4** | Reescribir la cadena | Sesión 4 · la grieta | Alterar un asiento, recalcular la cadena entera y multiplicarlo por las diez copias |
| **5** | Las cuatro preguntas | Sesión 4 | Puntuar el caso, y ver cómo la ponderación cambia la recomendación |
| **6** | El precio de reescribir | Sesión 4 · **voluntario** | Medir cuánto cuesta reescribir cuando no hay contrato que lo impida |
""")

st.markdown("### Tres advertencias")

st.markdown("""
1. **No hay que saber programar.** Todo se maneja con controles. El código está a la
   vista para quien quiera mirarlo, y mirarlo es ampliación voluntaria: suma y no resta.
2. **Nada de lo que se calcula aquí entra en la prueba objetiva.** No se pregunta por
   pasos de algoritmo, parámetros ni cifras. Se pregunta qué garantiza un mecanismo,
   qué supuesto necesita para funcionar y qué consecuencia jurídica tiene que ese
   supuesto falle.
3. **Ningún resumen está escrito en el código.** Todos se calculan en el momento, de
   modo que no puede haber ninguno inventado. Es la misma exigencia que se os pide a
   vosotros con las citas normativas.
""")

caja(
    "<b>Los datos del caso.</b> Todas las páginas trabajan sobre el lote "
    "<b>AOVE-2026-0148</b> del consorcio TrazaOliva, el mismo de la sesión 2. "
    "Si algún dato no coincide con el del aula, avisad en el foro: se corrige en un "
    "único sitio del código y queda corregido en toda la aplicación.")

pie()
