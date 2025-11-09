# Mi-primera-pagina
---
title: "Primera entrada — Introducción y Fundamentos de Programación"
description: Variables, tipos de datos, operadores, cadenas, E/S, funciones (incluida recursión) y un panorama de GitHub como plataforma.
tags: [unidad1, fundamentos, python, variables, funciones, recursión, github]
---

# Unidad 1 — Introducción y Fundamentos de Programación

La Unidad 1 pone el foco en **variables** y **principales estructuras de datos en Python**, y aterriza cómo el software conversa con el hardware. Aquí va el mapa de ruta y ejemplos prácticos.

---

## 1) El Hardware
> *Sección en construcción.*  
Incluye recursos (videos) para entender cómo funciona el hardware moderno, por ejemplo la **estructura microscópica de una memoria SSD**. Piensa en una “**Medellín-SSD**”: una ciudad de celdas donde cada “barrio” guarda bits; las avenidas internas (bus/datos) mueven información con latencias muy distintas a la RAM o la CPU.

## 2) Software
Puente entre la lógica y lo físico. El **software** es la secuencia de instrucciones que, al ejecutarse, activa compuertas y mueve electrones de forma controlada. Dicho empresarialmente: **procesos repetibles** que convierten entradas en resultados.

## 3) Los Lenguajes de Programación (con Python de puerta de entrada)
**Lenguajes formales** (programación, matemáticas) vs **lenguajes naturales** (español). Un lenguaje de programación existe para **expresar cómputos** con precisión.
- Hoy, los **LLM** permiten escribir instrucciones en lenguaje natural; **aprender Python sigue siendo clave** para el **pensamiento computacional**.
- Cinco pilares que siempre aparecen: **Entrada**, **Salida**, **Matemáticas**, **Ejecución condicional** y **Repetición**.

## 4) Variables, Valores y Operadores
- **Variable**: nombre que referencia un **valor** en memoria.
- **Tipos de datos**: `int` (enteros), `float` (decimales), `str` (texto), `bool` (lógicos).
- **Almacenamiento en memoria**: un entero se representa en **binario** (bits con pesos).  
- **Funciones útiles**: `type()` para conocer el tipo y `id()` para ver un **identificador único** del objeto en memoria.
- **Optimización (nota técnica)**: Python puede **reutilizar** objetos inmutables (p. ej., algunos enteros pequeños). Es un detalle de implementación; **no programes dependiendo de ello**.
- **Asignación vs igualdad**:  
  - `=` **asigna** (toma el valor de la derecha y lo guarda en la variable de la izquierda).  
  - `==` **compara** y devuelve `True/False`.

**Operadores**  
- **Aritméticos**: `+ - * / // % **`  
- **Comparación**: `== != > < >= <=`  
- **Lógicos**: `and or not`  
- **Precedencia**: paréntesis → `**` → `* / // %` → `+ -` → comparaciones → lógicos.  
  *Asociatividad*: usualmente izquierda a derecha, excepto `**` (derecha a izquierda).

## 5) Operaciones con cadenas de texto
- `+` **concatena** textos.  
- `*` **repite** una cadena.  
Esto es **sobrecarga de operadores**: el mismo símbolo (`+`, `*`) significa cosas distintas según el tipo.

## 6) Lectura y escritura de valores
- **Salida**: `print()`, con **f-strings** para formatear: `print(f"Hola {nombre}")`.  
- **Entrada**: `input()` devuelve siempre `str`; convierte a número con `int()` o `float()` si hace falta.

## 7) Funciones
Bloques de código **reutilizables**.
- Definición: `def nombre(parámetros): ... return resultado`
- **Sangría importa**: en Python la indentación **define** bloques.  
- **Alcance**: variables **locales** (dentro de la función) y **globales** (afuera). `global` permite escribir sobre una global (úsalo con criterio).

## 8) Llamar funciones desde funciones
La **modularidad** parte problemas grandes en piezas pequeñas, reutilizables.

## 9) Condicionales: `if`, `elif`, `else`
Estructura para **decidir**: se ejecuta **solo** el primer bloque cuya condición sea verdadera.

## 10) Recursión
Una función que **se llama a sí misma**.  
- Necesita **caso base** (condición para detener) + **llamada recursiva** (resuelve un subproblema).  
- Ejemplo clásico: **factorial**.  
- Sin caso base → bucle infinito → 
---
# ejemplo phyton 
def demo():
    nombre = input("Nombre: ") or "Natalia"
    n = int((input("Número (0-10): ") or 5))
    # Variables y tipos
    x, y = 2, 3.5
    print(f"Hola, {nombre}. x+y={x+y} (tipo: {type(x+y).__name__})")
    # Cadenas: + (concatena), * (repite)
    print("Python " + "para todos " * 2)
    # Condicional
    print("n es par" if n % 2 == 0 else "n es impar")
    # Bucle for (suma 1..n)
    s = 0
    for i in range(1, n + 1):
        s += i
    print(f"Suma 1..{n} = {s}")
    # Funciones y composición
    def cuadrado(k): return k * k
    def hip(a, b): return (cuadrado(a) + cuadrado(b)) ** 0.5
    print("hip(3,4) =", hip(3, 4))

if __name__ == "__main__":
    demo()
    # Reflexión personal 
    Esta clase me ayudó a cuadrar la cancha: lo que escribo como símbolos en Python termina moviendo electrones con disciplina. Diferenciar = (asignación) de == (igualdad) y observar la precedencia me quitó ruido mental. Ver type() e id() me dio intuición sobre valores y objetos; ya no imagino “la memoria” como una caja negra, sino como una Medellín-SSD con barrios bien referenciados.
Para el próximo sprint, priorizaré: escribir funciones pequeñas y claras, practicar recursión con casos base sólidos y seguir usando IA como revisor crítico (no como piloto). KPI personal: menos errores por tipos/precedencia y más legibilidad en mis funciones.
# Referencia 
contenido generado con apoyo de IA (ChatGPT) y curado por Natalia 
