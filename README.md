# Video Trimmer - Recortador de Videos

Script de Python para recortar videos MP4 manteniendo la calidad y códec originales.

## Características

✅ Recorte preciso de videos entre tiempos específicos
✅ Mantiene el códec y calidad originales (sin recodificación)
✅ Validaciones completas de entrada
✅ Manejo robusto de errores
✅ Mensajes informativos de progreso
✅ Interfaz de línea de comandos intuitiva

## Requisitos Previos

### 1. FFmpeg
Debes tener FFmpeg instalado en tu sistema:

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Descarga desde [ffmpeg.org](https://ffmpeg.org/download.html) y añade a PATH

### 2. Python
Python 3.6 o superior

## Instalación

1. **Clona o descarga los archivos del proyecto**

2. **Instala las dependencias de Python:**
```bash
pip install -r requirements.txt
```

O instala directamente:
```bash
pip install ffmpeg-python
```

## Uso

### Sintaxis básica:
```bash
python video_trimmer.py <video_entrada> <tiempo_inicio> <tiempo_fin> [-o <video_salida>]
```

### Parámetros:

- `video_entrada`: Ruta al archivo MP4 de entrada
- `tiempo_inicio`: Tiempo de inicio en formato `HH:MM:SS`
- `tiempo_fin`: Tiempo de finalización en formato `HH:MM:SS`
- `-o, --output`: (Opcional) Nombre del archivo de salida. Por defecto: `input_trimmed.mp4`

### Ejemplos:

**1. Recortar del minuto 1:30 al 3:45:**
```bash
python video_trimmer.py mi_video.mp4 00:01:30 00:03:45
```
Salida: `mi_video_trimmed.mp4`

**2. Especificar nombre de salida:**
```bash
python video_trimmer.py mi_video.mp4 00:01:30 00:03:45 -o clip_corto.mp4
```
Salida: `clip_corto.mp4`

**3. Recortar los primeros 30 segundos:**
```bash
python video_trimmer.py video.mp4 00:00:00 00:00:30 --output intro.mp4
```

**4. Ver ayuda:**
```bash
python video_trimmer.py --help
```

## Validaciones Incluidas

El script realiza las siguientes validaciones:

✓ Verifica que el archivo de entrada exista y sea accesible
✓ Valida que sea un archivo .mp4
✓ Verifica el formato de los tiempos (HH:MM:SS)
✓ Comprueba que el tiempo de fin sea mayor que el de inicio
✓ Valida que los tiempos no excedan la duración del video
✓ Pregunta antes de sobrescribir archivos existentes

## Manejo de Errores

El script maneja errores comunes y proporciona mensajes claros:

- Archivo no encontrado
- Formato de tiempo incorrecto
- Rango de tiempo inválido
- Permisos insuficientes
- Errores de FFmpeg

## Salida de Ejemplo

```
============================================================
RECORTADOR DE VIDEOS
============================================================

[1/6] Validando archivo de entrada...
✓ Archivo válido: mi_video.mp4

[2/6] Procesando tiempos...
✓ Inicio: 00:01:30 (90.0s)
✓ Fin: 00:03:45 (225.0s)
✓ Duración del recorte: 135.0s

[3/6] Analizando video...
✓ Duración total del video: 600.00s

[4/6] Validando rango de tiempo...
✓ Rango de tiempo válido

[5/6] Recortando video...
Esto puede tomar unos momentos...
✓ Video recortado exitosamente

[6/6] Verificando resultado...
✓ Archivo guardado: mi_video_trimmed.mp4
✓ Tamaño: 45.32 MB

============================================================
PROCESO COMPLETADO EXITOSAMENTE
============================================================
```

## Ventajas de usar `codec='copy'`

El script utiliza `-codec copy` de FFmpeg, lo que significa:

- ⚡ Velocidad: El proceso es muy rápido (sin recodificación)
- 🎯 Calidad: No hay pérdida de calidad
- 💾 Eficiencia: Menor uso de CPU y recursos
- 📐 Dimensiones: Se mantienen las dimensiones originales

## Troubleshooting

### Error: "ffmpeg: command not found"
**Solución:** Instala FFmpeg en tu sistema (ver sección Requisitos Previos)

### Error: "No module named 'ffmpeg'"
**Solución:** Instala la biblioteca de Python:
```bash
pip install ffmpeg-python
```

### El video de salida no se reproduce correctamente
**Causa posible:** El punto de inicio no coincide con un keyframe
**Solución:** Ajusta ligeramente el tiempo de inicio (±1 segundo)

## Limitaciones

- Solo procesa archivos .mp4
- Los tiempos deben estar en formato exacto HH:MM:SS
- Requiere FFmpeg instalado en el sistema

## Licencia

Libre para uso personal y comercial.

## Autor

Script creado con Python y FFmpeg.
