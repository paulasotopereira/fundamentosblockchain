# -*- coding: utf-8 -*-
"""Identidad visual del curso y piezas de interfaz que se repiten."""

import streamlit as st

VERDE_OSCURO = "#1F2D24"
VERDE = "#2C5F2D"
ROJO = "#B85042"
CREMA = "#F4F2EC"
VERDE_CLARO = "#E4ECE2"
ROJO_CLARO = "#F7E7E3"

CSS = f"""
<style>
  html, body, [class*="css"] {{ font-family: Calibri, Carlito, system-ui, sans-serif; }}
  h1, h2, h3 {{ font-family: Cambria, Caladea, Georgia, serif; color: {VERDE_OSCURO}; }}
  .lab-kicker {{ font-size: .78rem; font-weight: 700; letter-spacing: .06em;
                 text-transform: uppercase; color: {VERDE}; margin-bottom: .1rem; }}
  .lab-kicker-rojo {{ color: {ROJO}; }}
  .lab-caja {{ background: {CREMA}; border-radius: 4px; padding: .9rem 1.1rem;
               margin: .5rem 0 1rem 0; }}
  .lab-caja-verde {{ background: {VERDE_CLARO}; border-radius: 4px;
                     padding: .9rem 1.1rem; margin: .5rem 0 1rem 0; }}
  .lab-caja-roja {{ background: {ROJO_CLARO}; border-radius: 4px;
                    padding: .9rem 1.1rem; margin: .5rem 0 1rem 0; }}
  .lab-mono {{ font-family: Consolas, "DejaVu Sans Mono", monospace;
               font-size: .82rem; word-break: break-all; }}
  .lab-pie {{ color: #5A5F5C; font-size: .8rem; border-top: 1px solid #DDD;
              padding-top: .6rem; margin-top: 2rem; }}
</style>
"""


def preparar(titulo: str, icono: str = "⛓"):
    st.set_page_config(page_title=f"{titulo} · Laboratorio Blockchain",
                       page_icon=icono, layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)
    with st.sidebar:
        st.markdown(f"<div class='lab-kicker'>UNIE · Grado de Derecho</div>",
                    unsafe_allow_html=True)
        st.markdown("### Laboratorio")
        st.caption("Blockchain: Fundamentos Técnicos y Problemática Jurídica · 2026-27")
        st.divider()
        st.markdown(
            "**No hay que saber programar.** No se instala nada y no hace falta "
            "ninguna cuenta.\n\n"
            "**Nada de lo que aquí se calcula se pregunta en el examen.** Lo que se "
            "pregunta es, de cada mecanismo: qué garantiza, a costa de qué y qué "
            "deja fuera."
        )


def _html(texto: str) -> str:
    """Convierte el énfasis de Markdown a HTML, para los bloques que van en crudo."""
    import re
    texto = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", texto, flags=re.S)
    texto = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>",
                   texto, flags=re.S)
    return texto


def cabecera(kicker: str, titulo: str, entradilla: str = "", rojo: bool = False):
    clase = "lab-kicker lab-kicker-rojo" if rojo else "lab-kicker"
    st.markdown(f"<div class='{clase}'>{kicker}</div>", unsafe_allow_html=True)
    st.markdown(f"# {titulo}")
    if entradilla:
        st.markdown(entradilla)


def caja(texto: str, tono: str = "crema"):
    clase = {"crema": "lab-caja", "verde": "lab-caja-verde", "rojo": "lab-caja-roja"}[tono]
    st.markdown(f"<div class='{clase}'>{_html(texto)}</div>", unsafe_allow_html=True)


def que_hace(hace: str, no_hace: str):
    a, b = st.columns(2)
    with a:
        st.markdown(f"<div class='lab-caja-verde'><b>Qué hace</b><br>{_html(hace)}</div>",
                    unsafe_allow_html=True)
    with b:
        st.markdown(f"<div class='lab-caja-roja'><b>Qué NO hace</b><br>{_html(no_hace)}</div>",
                    unsafe_allow_html=True)


def ficha(garantiza: str, coste: str, fuera: str):
    st.markdown("#### Ficha del mecanismo")
    st.markdown(
        f"| | |\n|---|---|\n"
        f"| **Qué garantiza** | {garantiza} |\n"
        f"| **A costa de qué** | {coste} |\n"
        f"| **Qué deja fuera** | {fuera} |"
    )


def sin_solucion():
    caja(
        "<b>Esta página no da la respuesta.</b> Da el instrumento. La calificación "
        "jurídica la haces tú, y es lo único que se evalúa.", "rojo")


def pie():
    st.markdown(
        "<div class='lab-pie'>Laboratorio de la asignatura · "
        "Blockchain: Fundamentos Técnicos y Problemática Jurídica · "
        "Grado de Derecho · UNIE · Curso 2026-27</div>",
        unsafe_allow_html=True)
