#!/usr/bin/env python3
"""
Script de ejemplo para probar el recortador de videos.
Este script muestra cómo usar el módulo video_trimmer programáticamente.
"""

from video_trimmer import trim_video

def ejemplo_basico():
    """Ejemplo básico de uso."""
    print("Ejemplo 1: Uso básico")
    print("-" * 50)
    
    # Parámetros de entrada
    input_video = "mi_video.mp4"
    output_video = "video_recortado.mp4"
    start_time = "00:01:30"  # 1 minuto 30 segundos
    end_time = "00:03:45"    # 3 minutos 45 segundos
    
    # Recortar el video
    try:
        trim_video(input_video, output_video, start_time, end_time)
    except Exception as e:
        print(f"Error: {e}")


def ejemplo_multiples_clips():
    """Ejemplo de creación de múltiples clips desde un mismo video."""
    print("\n\nEjemplo 2: Crear múltiples clips")
    print("-" * 50)
    
    input_video = "video_largo.mp4"
    
    # Lista de clips a crear (inicio, fin, nombre_salida)
    clips = [
        ("00:00:00", "00:00:30", "clip_intro.mp4"),
        ("00:05:00", "00:06:00", "clip_medio.mp4"),
        ("00:09:30", "00:10:00", "clip_final.mp4"),
    ]
    
    for i, (start, end, output) in enumerate(clips, 1):
        print(f"\n--- Procesando clip {i}/{len(clips)} ---")
        try:
            trim_video(input_video, output, start, end)
        except Exception as e:
            print(f"Error al procesar clip {i}: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("EJEMPLOS DE USO DEL RECORTADOR DE VIDEOS")
    print("=" * 60)
    print("\nNOTA: Estos ejemplos son demostrativos.")
    print("Asegúrate de tener videos reales para probar.\n")
    
    # Descomenta el ejemplo que quieras ejecutar:
    
    # ejemplo_basico()
    # ejemplo_multiples_clips()
    
    print("\nPara ejecutar estos ejemplos:")
    print("1. Descomenta la función de ejemplo que desees")
    print("2. Asegúrate de tener un video .mp4 disponible")
    print("3. Ejecuta: python ejemplo_uso.py")
