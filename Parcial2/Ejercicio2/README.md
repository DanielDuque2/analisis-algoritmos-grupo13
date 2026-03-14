# Ejercicio 2 — Non-overlapping Intervals

## Enlace al problema

https://leetcode.com/problems/non-overlapping-intervals/

---

# Justificación de la estrategia Greedy

La solución utiliza una estrategia greedy basada en ordenar los intervalos por su punto de fin y recorrerlos secuencialmente, conservando siempre el intervalo que termina más pronto. Al procesar los intervalos en este orden, la decisión local óptima consiste en comparar el inicio del intervalo actual con el fin del último intervalo conservado. Si existe solapamiento, se elimina el intervalo actual y se incrementa el contador de removidas. Si no hay solapamiento, el intervalo actual se conserva y pasa a ser el nuevo referente.

---

# Complejidad del algoritmo

## Complejidad temporal

El algoritmo consta de dos operaciones principales:

**1. Ordenamiento de los intervalos por punto de fin**

O(n log n)

**2. Recorrido lineal de los intervalos**

O(n)

En cada paso del recorrido se realiza una comparación de tiempo constante O(1), por lo que el costo total del recorrido es proporcional al número de intervalos.

Por lo tanto, la complejidad temporal total del algoritmo es:

**O(n log n)**

---

## Complejidad espacial

El algoritmo opera directamente sobre la lista de intervalos ordenada y solo mantiene una variable entera para el contador de remociones y otra para el fin del último intervalo conservado. No se utilizan estructuras de datos auxiliares proporcionales a la entrada.

**O(1)**
