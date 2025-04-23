#!/usr/bin/env python3
"""
Punto de entrada del compilador.
Ejemplo de uso:
    python main.py               # analiza input.txt por defecto
    python main.py programa.xyz  # analiza el archivo dado
"""
import sys
from pathlib import Path
from analizador_sintactico import analizar

def leer_archivo(ruta: Path) -> str:
    try:
        return ruta.read_text(encoding="utf-8")
    except FileNotFoundError:
        sys.exit(f"❌  Archivo no encontrado: {ruta}")

def main() -> None:
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.txt")
    codigo_fuente = leer_archivo(ruta)

    arbol = analizar(codigo_fuente)
    print("\n--- Árbol sintáctico ---")
    print(arbol)

if __name__ == "__main__":
    main()
