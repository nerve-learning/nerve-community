# Reto 4 (FINAL): La Fábrica de Noticias 📰

Felicidades, llegaste al reto integrador. Eres el sistema de análisis de noticias de un periódico digital. Recibes noticias en bruto y debes procesarlas en tres etapas, usando un pipeline de generadores.

## El Escenario

Tienes estas noticias en bruto:

```python
noticias_brutas = [
    "  DEPORTES: el equipo local gano el campeonato  ",
    "  POLITICA: nueva ley aprobada por el congreso  ",
    "  DEPORTES: jugador estrella firma contrato millonario  ",
    "  ECONOMIA: el peso se fortalece ante el dolar  ",
    "  DEPORTES: el torneo comienza el proximo lunes  ",
    "  POLITICA: candidatos debaten temas de seguridad  ",
    "  ECONOMIA: inflacion baja por tercer mes consecutivo  ",
    "  DEPORTES: seleccion nacional convoca 23 jugadores  ",
]
```

## Instrucciones Paso a Paso:

Construye un pipeline de **3 etapas** y conéctalas igual que en el ejemplo:

**Etapa 1 — `limpiar_noticia(noticias)`:**
- Función generadora con `yield`.
- Limpia cada noticia: quita los espacios con `.strip()` y pone la primera letra en mayúscula con `.title()`.

**Etapa 2 — `filtrar_categoria(noticias_limpias, categoria)`:**
- Función generadora con `yield`.
- Solo produce las noticias que **empiecen con** la categoría buscada.
- Usa `if noticia.startswith(categoria)` — `.startswith(texto)` devuelve `True` si el string empieza con ese texto.
- Filtra por la categoría `"Deportes:"` (así queda después de `.title()`).

**Etapa 3 — `formatear_titular(noticias_filtradas)`:**
- Función generadora con `yield`.
- Produce cada noticia formateada así: `"🏆 [TITULAR] → publicada"`.
- Usa `.upper()` para poner el titular en mayúsculas.

Luego:
4. Conecta las 3 etapas en pipeline: `formatear_titular(filtrar_categoria(limpiar_noticia(noticias_brutas), "Deportes:"))`.
5. Recorre el pipeline con un `for` e imprime cada titular.
6. Al final, imprime cuántos titulares de deportes se publicaron (lleva un contador dentro del `for`).

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `def`, `yield`, `for`, `if`, `.strip()`, `.title()`, `.upper()`, `.startswith()`, f-strings, `print()`, contador con `+`.
❌ **Conceptos Prohibidos:** Listas intermedias entre etapas, `import`, expresiones generadoras como solución (usa `def` + `yield` para las 3 etapas).

## Resultado Esperado en tu Terminal:

```text
=== Titulares de Deportes — Edición de Hoy ===

🏆 DEPORTES: EL EQUIPO LOCAL GANO EL CAMPEONATO → publicada
🏆 DEPORTES: JUGADOR ESTRELLA FIRMA CONTRATO MILLONARIO → publicada
🏆 DEPORTES: EL TORNEO COMIENZA EL PROXIMO LUNES → publicada
🏆 DEPORTES: SELECCION NACIONAL CONVOCA 23 JUGADORES → publicada

Total de titulares de Deportes publicados hoy: 4
```

Crea tu código en `reto.py`. Si cambias `"Deportes:"` por `"Politica:"` en tu filtro y obtienes 2 titulares sin tocar más código, completaste el módulo.
