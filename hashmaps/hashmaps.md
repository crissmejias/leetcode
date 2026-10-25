# LeetCode: Hashmaps para principiantes

Resumen de la sesión de práctica: problemas resueltos, patrones comunes y pendientes.

## Problemas resueltos

| Problema | Estructura | Qué guardas | Idea clave |
|---|---|---|---|
| Two Sum | `dict` | número → índice | Buscar el complemento **antes** de guardar |
| Contains Duplicate | `set` | solo lo visto | ¿Ya vi esto? |
| Valid Anagram | `dict` | carácter → conteo | Sumar con `s`, restar con `t`, cortar si baja de 0 |
| Group Anagrams | `dict` | clave calculada → lista | Letras ordenadas como clave común |
| Top K Frequent | `dict` | número → conteo | Contar y luego ordenar con `key=hashmap.get` |

## Patrones comunes de hashmap

1. **"¿Ya lo vi?" (existencia).** Un `set` o un `dict`, consultando antes de insertar. Aparece en Two Sum y Contains Duplicate.
2. **Contar frecuencias.** El patrón `.get(x, 0) + 1`. Cuando veas "cuántas veces", piensa en esto.
3. **Guardar el complemento o lo que "falta".** Dejas pistas de lo que ya pasó para que el elemento actual encuentre su pareja en O(1).
4. **Agrupar por clave calculada.** Transformas cada elemento en una "firma" igual para los equivalentes (aquí, letras ordenadas) y usas `setdefault(clave, []).append(...)`. La clave debe ser hashable, por eso `"".join(...)` en vez de la lista que devuelve `sorted`.
5. **Contar y luego ordenar o seleccionar.** El hashmap resume los datos y después trabajas sobre el resumen, como en Top K.

## Snippets de referencia

```python
# Contar frecuencias
conteos[item] = conteos.get(item, 0) + 1

# Crear la lista la primera vez que aparece una clave
grupos.setdefault(clave, []).append(valor)

# Ordenar claves por su valor, de mayor a menor
sorted(conteos, key=conteos.get, reverse=True)
```

## Ideas transversales

- **Por qué bajan la complejidad:** buscar, insertar y consultar es O(1) en promedio, así que reemplazan un segundo ciclo anidado (O(n²)) por una consulta (O(n) total).
- **El orden de las operaciones importa:** en Two Sum, guardar antes de buscar hace que un número se encuentre a sí mismo como complemento.
- **Razonar con invariantes:** en Valid Anagram, longitudes iguales más ningún conteo negativo implica que todos terminan en 0. Si a un carácter le sobra algo en `s`, a otro le falta en `t`, y ese dispara el corte.
- **Claves hashables:** las listas no sirven como clave; strings y tuplas sí.
- **Hábitos a mantener:** type hints, nombres claros (`word`, no `str`), y probar casos borde (vacío, un elemento, duplicados, negativos).

## Complejidad de cada solución

| Problema | Tiempo | Espacio |
|---|---|---|
| Two Sum | O(n) | O(n) |
| Contains Duplicate | O(n) | O(n) |
| Valid Anagram | O(n) | O(k), con k = caracteres distintos |
| Group Anagrams | O(n · k log k), con k = longitud de cada palabra | O(n · k) |
| Top K Frequent (con `sorted`) | O(n + m log m), con m = elementos únicos | O(m) |




