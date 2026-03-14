# Ejercicio 5 — Merge Intervals

## Enlace al problema

https://leetcode.com/problems/merge-intervals/

---

# Justificación de la estrategia Greedy

La solución utiliza una estrategia greedy basada en ordenar los intervalos por su punto de inicio y recorrerlos secuencialmente fusionando aquellos que se solapan. Al procesar los intervalos en orden, cualquier intervalo que pueda solaparse con otro aparecerá inmediatamente después en la lista ordenada. Esto permite comparar cada intervalo únicamente con el último intervalo agregado al resultado. Si existe solapamiento, el algoritmo fusiona ambos intervalos extendiendo el final hasta el valor máximo posible, garantizando que el nuevo intervalo cubra completamente el rango de los intervalos solapados. Esta decisión local es óptima porque no afecta negativamente las decisiones posteriores y asegura que todos los puntos cubiertos por los intervalos originales se mantengan representados en el resultado final.

---

# Complejidad del algoritmo

## Complejidad temporal

El algoritmo consta de dos operaciones principales:

**1. Ordenamiento de los intervalos**

O(n log n)

**2. Recorrido de los intervalos**

O(n)

Por lo tanto, la complejidad temporal total del algoritmo es:

**O(n log n)**

---

## Complejidad espacial

El algoritmo utiliza una lista adicional para almacenar los intervalos fusionados. En el peor caso, cuando ningún intervalo se solapa, la lista resultante puede contener todos los intervalos originales.

**O(n)**