## Justificación ejercicio 3

La propiedad clave es que si podemos llegar a una posición **i**, entonces podemos intentar extender nuestro alcance desde allí.

No es necesario explorar todas las combinaciones de saltos (como haría programación dinámica). Basta con mantener el **máximo índice alcanzable**.

El algoritmo es correcto porque:

- Si alguna posición **i** queda fuera del alcance máximo, ninguna secuencia de saltos anterior puede llegar a ella.
- Si logramos extender **max_reach** hasta el último índice, entonces existe al menos una secuencia válida de saltos.

Esto demuestra que la decisión local (**maximizar el alcance actual**) conduce a la **solución global**.

---

## Complejidad

**Tiempo:** `O(n)`  
Se recorre el arreglo una sola vez.

**Espacio:** `O(1)`  
Solo se usan variables auxiliares.

---

## Análisis de complejidad

### Complejidad temporal (Time Complexity)

**O(n)**  
Donde **n** es el numero de elementos en el arrelgo `nums`.

El algoritmo recorre el arreglo una sola vez usando un ciclo `for`.  
En cada iteración se realizan operaciones de tiempo constante:

- Comparar `i > max_reach`
- Calcular `max(max_reach, i + nums[i])`
- Comparar con el último índice

Ninguna de estas operaciones depende del tamaño del arreglo.

Por lo tanto, el tiempo total es:
    T(n)=n⋅O(1)=O(n)


---

### Complejidad espacial (Space Complexity)

**O(1)**

El algoritmo utiliza unicamente vbles auxiliares constantes:

- `max_reach`
- `i` (índice del bucle)

No se crean estructuras adicionales como arreglos, listas o tablas de DP.

Por lo tanto, el espacio utilizado no crece con el tamaño del input.

---

## Enlace al problema

https://leetcode.com/problems/jump-game/description/
