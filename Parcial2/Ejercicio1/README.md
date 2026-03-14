# Ejercicio 1 — Assign Cookies

## Enlace al problema

https://leetcode.com/problems/assign-cookies/

---

# Justificación de la estrategia Greedy

La solución utiliza una estrategia greedy basada en ordenar tanto los factores de avaricia de los niños como los tamaños de las galletas de menor a mayor, y luego emparejarlos secuencialmente con dos punteros. Al procesar ambas listas en orden ascendente, la decisión local óptima consiste en intentar satisfacer primero al niño menos exigente con la galleta más pequeña que pueda contentarlo. Si la galleta actual no es suficiente para el niño actual, se descarta y se prueba la siguiente galleta más grande. Si sí es suficiente, el niño queda satisfecho y ambos punteros avanzan. Esta estrategia es óptima porque nunca conviene asignar una galleta grande a un niño fácil de satisfacer cuando esa misma galleta podría ser la única capaz de satisfacer a un niño más exigente. Al emparejar la galleta mínima necesaria con el niño menos exigente posible, se maximiza el número de niños contentos sin desperdiciar recursos.

---

# Complejidad del algoritmo

## Complejidad temporal

El algoritmo consta de dos operaciones principales:

**1. Ordenamiento de los niños y las galletas**

O(n log n + m log m)

Donde `n` es el número de niños y `m` es el número de galletas. Dado que el término dominante es el mayor de los dos ordenamientos, se simplifica a:

O(n log n)

**2. Recorrido con dos punteros**

O(n + m)

En el peor caso, ambos punteros recorren sus listas completas sin que se pueda satisfacer a ningún niño o hasta que se agoten las galletas.

Por lo tanto, la complejidad temporal total del algoritmo es:

**O(n log n)**

---

## Complejidad espacial

El algoritmo ordena las listas en su lugar (`sort` in-place) y solo utiliza dos variables enteras como punteros auxiliares. No se requiere ninguna estructura de datos adicional proporcional a la entrada.

**O(1)**