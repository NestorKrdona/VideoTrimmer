#!/usr/bin/env python3
"""
Script para recortar videos manteniendo la calidad y códec originales.
Utiliza ffmpeg-python para operaciones eficientes de recorte.
"""

import os
import sys
import argparse
from datetime import datetime, timedelta
import ffmpeg


def time_to_seconds(time_str):
    """
    Convierte un string en formato HH:MM:SS a segundos.
    
    Args:
        time_str: String en formato "HH:MM:SS"
    
    Returns:
        float: Tiempo en segundos
    
    Raises:
        ValueError: Si el formato es inválido
    """
    try:
        # Parsear el tiempo
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        # Convertir a timedelta para obtener los segundos totales
        delta = timedelta(
            hours=time_obj.hour,
            minutes=time_obj.minute,
            seconds=time_obj.second
        )
        return delta.total_seconds()
    except ValueError:
        raise ValueError(f"Formato de tiempo inválido: '{time_str}'. Use formato HH:MM:SS")


def validate_video_file(filepath):
    """
    Valida que el archivo de video exista y sea accesible.
    
    Args:
        filepath: Ruta al archivo de video
    
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el archivo no tiene extensión .mp4
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"El archivo no existe: {filepath}")
    
    if not os.path.isfile(filepath):
        raise ValueError(f"La ruta no corresponde a un archivo: {filepath}")
    
    if not filepath.lower().endswith('.mp4'):
        raise ValueError(f"El archivo debe ser .mp4, se recibió: {filepath}")
    
    if not os.access(filepath, os.R_OK):
        raise PermissionError(f"No hay permisos de lectura para: {filepath}")


def get_video_duration(filepath):
    """
    Obtiene la duración del video en segundos.
    
    Args:
        filepath: Ruta al archivo de video
    
    Returns:
        float: Duración en segundos
    """
    try:
        probe = ffmpeg.probe(filepath)
        video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
        duration = float(probe['format']['duration'])
        return duration
    except Exception as e:
        raise RuntimeError(f"Error al obtener información del video: {str(e)}")


def validate_time_range(start_seconds, end_seconds, video_duration):
    """
    Valida que el rango de tiempo sea válido.
    
    Args:
        start_seconds: Tiempo de inicio en segundos
        end_seconds: Tiempo de fin en segundos
        video_duration: Duración total del video en segundos
    
    Raises:
        ValueError: Si el rango de tiempo es inválido
    """
    if start_seconds < 0:
        raise ValueError("El tiempo de inicio no puede ser negativo")
    
    if end_seconds <= start_seconds:
        raise ValueError(
            f"El tiempo de fin ({end_seconds}s) debe ser mayor que "
            f"el tiempo de inicio ({start_seconds}s)"
        )
    
    if start_seconds >= video_duration:
        raise ValueError(
            f"El tiempo de inicio ({start_seconds}s) excede la duración "
            f"del video ({video_duration}s)"
        )
    
    if end_seconds > video_duration:
        raise ValueError(
            f"El tiempo de fin ({end_seconds}s) excede la duración "
            f"del video ({video_duration}s)"
        )


def trim_video(input_path, output_path, start_time, end_time, accurate=True):
    """
    Recorta el video entre los tiempos especificados.

    Args:
        input_path: Ruta del video de entrada
        output_path: Ruta del video de salida
        start_time: Tiempo de inicio en formato "HH:MM:SS"
        end_time: Tiempo de fin en formato "HH:MM:SS"
        accurate: Si True, usa corte preciso (más lento pero exacto).
                 Si False, usa codec copy (rápido pero puede ser impreciso)
    """
    print("=" * 60)
    print("RECORTADOR DE VIDEOS")
    print("=" * 60)

    # Validar archivo de entrada
    print(f"\n[1/6] Validando archivo de entrada...")
    validate_video_file(input_path)
    print(f"✓ Archivo válido: {input_path}")

    # Convertir tiempos a segundos
    print(f"\n[2/6] Procesando tiempos...")
    try:
        start_seconds = time_to_seconds(start_time)
        end_seconds = time_to_seconds(end_time)
        duration_seconds = end_seconds - start_seconds
        print(f"✓ Inicio: {start_time} ({start_seconds}s)")
        print(f"✓ Fin: {end_time} ({end_seconds}s)")
        print(f"✓ Duración del recorte: {duration_seconds}s")
    except ValueError as e:
        print(f"✗ Error: {str(e)}")
        sys.exit(1)

    # Obtener duración del video
    print(f"\n[3/6] Analizando video...")
    try:
        video_duration = get_video_duration(input_path)
        print(f"✓ Duración total del video: {video_duration:.2f}s")
    except RuntimeError as e:
        print(f"✗ {str(e)}")
        sys.exit(1)

    # Validar rango de tiempo
    print(f"\n[4/6] Validando rango de tiempo...")
    try:
        validate_time_range(start_seconds, end_seconds, video_duration)
        print(f"✓ Rango de tiempo válido")
    except ValueError as e:
        print(f"✗ Error: {str(e)}")
        sys.exit(1)

    # Verificar si el archivo de salida ya existe
    if os.path.exists(output_path):
        response = input(f"\n⚠ El archivo '{output_path}' ya existe. ¿Sobrescribir? (s/n): ")
        if response.lower() != 's':
            print("Operación cancelada.")
            sys.exit(0)

    # Recortar el video
    print(f"\n[5/6] Recortando video...")
    if accurate:
        print("Modo: PRECISO (recodifica para exactitud)")
        print("Esto tomará más tiempo pero garantiza duración exacta...")
    else:
        print("Modo: RÁPIDO (puede ser impreciso en keyframes)")
        print("Esto puede tomar unos momentos...")

    try:
        if accurate:
            # Método preciso: usa corte en dos pasos
            # Paso 1: buscar keyframe antes del inicio (rápido)
            # Paso 2: recodificar desde el punto exacto
            stream = ffmpeg.input(input_path, ss=start_seconds)
            stream = ffmpeg.output(
                stream,
                output_path,
                t=duration_seconds,
                vcodec='libx264',  # Recodifica con H.264
                acodec='aac',      # Recodifica audio con AAC
                **{
                    'crf': '18',   # Calidad alta (0-51, menor = mejor)
                    'preset': 'medium'  # Balance velocidad/calidad
                }
            )
        else:
            # Método rápido: codec copy (puede ser impreciso)
            stream = ffmpeg.input(input_path, ss=start_seconds, t=duration_seconds)
            stream = ffmpeg.output(
                stream,
                output_path,
                codec='copy',
                avoid_negative_ts='make_zero'
            )

        # Ejecutar el comando con sobrescritura habilitada
        ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)

        print("✓ Video recortado exitosamente")

    except ffmpeg.Error as e:
        print(f"✗ Error al recortar el video:")
        print(f"  {e.stderr.decode() if e.stderr else 'Error desconocido'}")
        sys.exit(1)

    # Verificar archivo de salida
    print(f"\n[6/6] Verificando resultado...")
    if os.path.exists(output_path):
        output_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
        output_duration = get_video_duration(output_path)
        print(f"✓ Archivo guardado: {output_path}")
        print(f"✓ Tamaño: {output_size:.2f} MB")
        print(f"✓ Duración real: {output_duration:.2f}s (esperado: {duration_seconds}s)")

        # Advertencia si hay diferencia significativa
        diff = abs(output_duration - duration_seconds)
        if diff > 1.0:  # Más de 1 segundo de diferencia
            print(f"⚠ Diferencia de {diff:.2f}s detectada")
            if not accurate:
                print("  Sugerencia: usa --accurate para corte preciso")
    else:
        print(f"✗ Error: No se pudo crear el archivo de salida")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print("=" * 60)


def main():
    """Función principal del script."""
    parser = argparse.ArgumentParser(
        description='Recorta un video MP4 entre dos tiempos especificados.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python video_trimmer.py input.mp4 00:01:30 00:03:45
  python video_trimmer.py input.mp4 00:01:30 00:03:45 -o output.mp4
  python video_trimmer.py video.mp4 00:00:00 00:00:30 --output clip.mp4
  python video_trimmer.py video.mp4 00:00:00 00:00:30 --accurate
  python video_trimmer.py video.mp4 00:00:00 00:00:30 --fast

Modos de corte:
  --accurate: Corte preciso (recodifica, más lento pero exacto)
  --fast:     Corte rápido (codec copy, rápido pero puede ser impreciso)
  Por defecto se usa modo PRECISO para garantizar duración exacta.
        """
    )

    parser.add_argument(
        'input',
        help='Ruta del archivo de video de entrada (.mp4)'
    )
    parser.add_argument(
        'start',
        help='Tiempo de inicio (formato HH:MM:SS)'
    )
    parser.add_argument(
        'end',
        help='Tiempo de finalización (formato HH:MM:SS)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Ruta del archivo de salida (por defecto: input_trimmed.mp4)',
        default=None
    )
    parser.add_argument(
        '--accurate',
        action='store_true',
        help='Usar modo preciso (recodifica, por defecto)'
    )
    parser.add_argument(
        '--fast',
        action='store_true',
        help='Usar modo rápido (codec copy, puede ser impreciso)'
    )

    args = parser.parse_args()

    # Generar nombre de salida si no se especificó
    if args.output is None:
        base_name = os.path.splitext(args.input)[0]
        args.output = f"{base_name}_trimmed.mp4"

    # Determinar modo (por defecto: accurate)
    accurate = True
    if args.fast:
        accurate = False
    elif args.accurate:
        accurate = True

    try:
        trim_video(args.input, args.output, args.start, args.end, accurate=accurate)
    except KeyboardInterrupt:
        print("\n\n✗ Operación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error inesperado: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
