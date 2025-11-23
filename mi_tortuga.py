# Reto 1: Simular la tortuga usando solo texto, print() e input()

def mover_derecha(pasos):
    """Imprime una flecha hacia la derecha según pasos."""
    print("-" * pasos + ">")

def mover_izquierda(pasos):
    """Imprime una flecha hacia la izquierda según pasos."""
    print("<" + "-" * pasos)

def mover_arriba(pasos):
    """Imprime un movimiento hacia arriba en vertical."""
    for _ in range(pasos):
        print("^")

def mover_abajo(pasos):
    """Imprime un movimiento hacia abajo en vertical."""
    for _ in range(pasos):
        print("v")

# --- Programa principal ---
print("Simulador de movimientos de la tortuga (versión texto)")
print("Opciones: derecha, izquierda, arriba, abajo")

direccion = input("¿Hacia dónde quieres mover la tortuga? ").strip().lower()
pasos = int(input("¿Cuántos pasos quieres mover? "))

print("\nResultado del movimiento:\n")

if direccion == "derecha":
    mover_derecha(pasos)
elif direccion == "izquierda":
    mover_izquierda(pasos)
elif direccion == "arriba":
    mover_arriba(pasos)
elif direccion == "abajo":
    mover_abajo(pasos)
    print("Dirección no válida. Intenta con: derecha, izquierda, arriba o abajo.")
  # Reto 2: Tortuga bajando con solo print() e input()

print("Simulador: Tortuga moviéndose hacia abajo")

# Pedimos cuántos pasos debe bajar
pasos = int(input("¿Cuántos pasos quieres que la tortuga baje? "))

print("\nRastro generado:\n")

# Imprime una línea vertical hacia abajo
for _ in range(pasos):
    print("|")

print("v")  # Flecha final indicando la dirección hacia abajo

# Reto 3: Girar y dibujar usando solo print() e input()
# Dibujar una "L" como en la versión gráfica de turtle

print("Simulación de una tortuga que avanza y luego gira hacia abajo\n")

# Pedimos los valores al usuario
horizontal = int(input("¿Cuántos pasos debe avanzar hacia la derecha? "))
vertical = int(input("¿Cuántos pasos debe avanzar hacia abajo? "))

print("\nDibujo generado:\n")

# --- Tramo horizontal ---
print("-" * horizontal + ">")

# --- Tramo vertical ---
# El primer segmento vertical empieza alineado al final del horizontal
for _ in range(vertical - 1):
    print(" " * horizontal + "|")

# Flecha final hacia abajo
print(" " * horizontal + "v")



