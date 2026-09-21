# -*- coding: utf-8 -*-
"""Núcleo de cálculo del laboratorio.

Todo lo que esta aplicación muestra sobre cadenas se calcula aquí, en ejecución.
No hay ningún resumen escrito a mano en el código: no puede haber resúmenes
inventados. Solo se usa la biblioteca estándar de Python.
"""

import hashlib
import time

GENESIS = "0" * 64

# ---------------------------------------------------------------------------
# PUNTO ÚNICO DE SINCRONIZACIÓN
#
# Los seis asientos del lote AOVE-2026-0148, los de la sesión 2. Si estas
# cadenas de texto no coinciden carácter por carácter con las del material de
# clase, los resúmenes que salgan aquí serán distintos de los que se vieron en
# el aula. Toda la aplicación lee de esta lista: basta sustituirla.
# ---------------------------------------------------------------------------

ASIENTOS = [
    {"id": "E1", "fecha": "2026-10-12T07:40", "actor": "Oleum Bética, S.C.A.",
     "concepto": "Recolección",
     "datos": "9.480 kg aceituna picual - finca Los Llanos, pol. 14 parc. 22"},
    {"id": "E2", "fecha": "2026-10-12T19:05", "actor": "Oleum Bética, S.C.A.",
     "concepto": "Molturación",
     "datos": "1.520 L AOVE - temperatura de batido 24 C"},
    {"id": "E3", "fecha": "2026-10-15T11:20", "actor": "Laboratorio Agroalimentario del Sur",
     "concepto": "Analítica",
     "datos": "acidez 0,21 % - índice de peróxidos 8,4 meq O2/kg"},
    {"id": "E4", "fecha": "2026-10-18T09:15", "actor": "Oleum Bética, S.C.A.",
     "concepto": "Envasado",
     "datos": "3.000 botellas de 500 ml - lote AOVE-2026-0148"},
    {"id": "E5", "fecha": "2026-10-20T06:00", "actor": "Transportes Guadalquivir, S.L.",
     "concepto": "Transporte",
     "datos": "temperatura máxima registrada 17,8 C - precinto 4471"},
    {"id": "E6", "fecha": "2026-10-24T14:30", "actor": "Nordwest Feinkost GmbH",
     "concepto": "Entrada en almacén",
     "datos": "3.000 botellas conformes - almacén Hamburgo HH-3"},
]

# Los diez miembros del consorcio. Los nueve primeros escriben asientos; el
# consejo regulador no escribe —certifica fuera de la cadena— pero conserva copia.
# SUPUESTO A CONFIRMAR con la ficha del caso.
CONSORCIO = [
    "Oleum Bética", "Almazara Sierra Mágina", "Almazara La Loma",
    "Almazara Cazorla", "Almazara Segura", "Almazara Úbeda",
    "Laboratorio Agroalimentario del Sur",
    "Transportes Guadalquivir", "Logística Bética Sur",
    "Consejo Regulador DOP",
]


def resumir(texto: str) -> str:
    """Resumen SHA-256 del texto, codificado en UTF-8. 64 caracteres hexadecimales."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def cuerpo(asiento: dict) -> str:
    """El texto del asiento que se somete a resumen."""
    return "|".join([asiento["id"], asiento["fecha"], asiento["actor"],
                     asiento["concepto"], asiento["datos"]])


def encadenar(asientos: list) -> list:
    """Calcula la cadena: el resumen de cada asiento incluye el del anterior."""
    cadena, anterior = [], GENESIS
    for a in asientos:
        r = resumir(anterior + cuerpo(a))
        cadena.append({**a, "anterior": anterior, "resumen": r})
        anterior = r
    return cadena


def verificar(cadena: list):
    """(True, None) si cuadra; (False, id) del primer asiento que no cuadra."""
    anterior = GENESIS
    for b in cadena:
        if b["anterior"] != anterior:
            return False, b["id"]
        if b["resumen"] != resumir(anterior + cuerpo(b)):
            return False, b["id"]
        anterior = b["resumen"]
    return True, None


def coincidencias(a: str, b: str) -> int:
    """Caracteres que coinciden en la misma posición. Por azar salen unos 4 de 64."""
    return sum(1 for x, y in zip(a, b) if x == y)


# --- Prueba de esfuerzo, solo para la página de ampliación voluntaria ---------

def buscar(texto: str, ceros: int, tope: int = 40_000_000):
    """Busca un número que haga que el resumen empiece por `ceros` ceros."""
    objetivo = "0" * ceros
    inicio = time.perf_counter()
    for n in range(tope):
        r = resumir(f"{texto}|{n}")
        if r.startswith(objetivo):
            return n, r, time.perf_counter() - inicio
    return None, None, time.perf_counter() - inicio


def medir_ritmo(n: int = 300_000) -> float:
    """Resúmenes por segundo de la máquina donde corre la aplicación."""
    t0 = time.perf_counter()
    for i in range(n):
        resumir(str(i))
    return n / (time.perf_counter() - t0)


UNIDADES = ((1, "segundos"), (60, "minutos"), (3600, "horas"),
            (86400, "días"), (86400 * 365, "años"))


def legible(seg: float) -> str:
    elegida, nombre = UNIDADES[0]
    for div, nom in UNIDADES:
        if seg >= div:
            elegida, nombre = div, nom
    return f"{seg / elegida:,.1f} {nombre}".replace(",", ".")
