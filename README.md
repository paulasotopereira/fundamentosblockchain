# Laboratorio · Blockchain: Fundamentos Técnicos y Problemática Jurídica

Aplicación de apoyo a la asignatura **Blockchain: Fundamentos Técnicos y Problemática
Jurídica** (Grado de Derecho, UNIE, curso 2026-27). Seis páginas para trabajar con las
manos los mecanismos del Tema 1.

Se abre en el navegador con una dirección web. **No se instala nada y no hace falta
ninguna cuenta**, que es lo que el documento de bienvenida de la asignatura promete en su
epígrafe 9.

---

## Qué hay dentro

| Página | De qué sesión viene | Qué se hace |
|---|---|---|
| La cadena rota | Sesión 2 · B.5 | Localizar dónde se rompe una cadena y por qué el resto deja de cuadrar |
| El gradiente | Sesión 3 · C.4 | Puntuar las cuatro dimensiones de la descentralización |
| Frases defendibles | Sesión 3 · C.5 | Reescribir tres afirmaciones que un escrito no sostendría |
| Reescribir la cadena | Sesión 4 · la grieta | Alterar, recalcular y multiplicar por las diez copias del consorcio |
| Las cuatro preguntas | Sesión 4 · B.7 | Puntuar el caso y ver cómo la ponderación invierte la recomendación |
| El precio de reescribir | Sesión 4 · voluntario | Medir el coste de reescribir sin contrato que lo impida |

## Dos reglas de diseño que no se negocian

1. **Ningún resumen SHA-256 está escrito en el código.** Todos se calculan en ejecución,
   de modo que no puede haber resúmenes inventados. Es la misma exigencia que la
   asignatura impone a los alumnos con las citas normativas.
2. **Ninguna página da la solución de un ejercicio.** Dan el instrumento; la calificación
   jurídica la hace el alumno. Publicar soluciones junto al enunciado anularía el
   ejercicio.

## Punto único de sincronización

Los seis asientos del lote `AOVE-2026-0148` viven en **`nucleo/cadena.py`**, en la lista
`ASIENTOS`. Toda la aplicación lee de ahí. Si el texto de los asientos no coincide
carácter por carácter con el material del aula, los resúmenes serán distintos de los que
se vieron en clase: basta sustituir esa lista.

Lo mismo con `CONSORCIO`, que fija los diez miembros y es un supuesto pendiente de
confirmar contra la ficha del caso.

---

## Puesta en marcha en local

```bash
git clone https://github.com/jftmames/blockchain-laboratorio.git
cd blockchain-laboratorio
python -m venv .venv && source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run Inicio.py
```

Se abre en `http://localhost:8501`.

## Publicación en Streamlit Community Cloud

Es gratuito para repositorios públicos y no requiere tarjeta.

1. **Crear el repositorio en GitHub** y subir este contenido:

   ```bash
   cd blockchain-laboratorio
   git init -b main
   git add .
   git commit -m "Laboratorio de la asignatura: seis páginas del Tema 1"
   git remote add origin https://github.com/jftmames/blockchain-laboratorio.git
   git push -u origin main
   ```

   Si el repositorio aún no existe, créalo antes en `github.com/new` como **público**,
   sin README ni .gitignore (ya están aquí).

2. **Desplegar**: entrar en `share.streamlit.io`, iniciar sesión con la cuenta de GitHub,
   *Create app* → *Deploy a public app from GitHub*, y rellenar:

   - Repository: `jftmames/blockchain-laboratorio`
   - Branch: `main`
   - Main file path: `Inicio.py`

3. Streamlit devuelve una dirección del tipo
   `https://blockchain-laboratorio.streamlit.app`. **Esa es la que se pega en el aula.**

Cada `git push` a `main` vuelve a desplegar la aplicación automáticamente.

### Si se prefiere no publicarla

La aplicación funciona igual en local con los tres comandos de arriba, y también en
cualquier otro alojamiento que ejecute Python. No necesita base de datos, ni claves, ni
conexión a ningún servicio externo: todo el cálculo ocurre en el proceso.

---

## Estructura

```
Inicio.py                         página de entrada
nucleo/cadena.py                  cálculo: hash, encadenamiento, verificación, datos del caso
nucleo/estilo.py                  identidad visual del curso y piezas de interfaz
pages/1_La_cadena_rota.py         …
pages/2_El_gradiente.py
pages/3_Frases_defendibles.py
pages/4_Reescribir_la_cadena.py
pages/5_Las_cuatro_preguntas.py
pages/6_El_precio_de_reescribir.py
.streamlit/config.toml            colores y tipografía del curso
requirements.txt                  una sola dependencia: streamlit
```

Para añadir una página nueva basta con crear un fichero en `pages/` con el prefijo
numérico que fije su orden en el menú.

---

## Aviso

Material docente. Los datos del consorcio TrazaOliva y del lote AOVE-2026-0148 son un
caso construido para la asignatura: no corresponden a ninguna entidad real.
