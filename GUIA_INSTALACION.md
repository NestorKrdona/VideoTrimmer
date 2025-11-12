# 📖 Guía Completa de Instalación y Uso del Video Trimmer

Esta guía te llevará paso a paso desde la instalación de FFmpeg hasta la ejecución exitosa del script en **Windows**, **macOS** y **Linux**.

---

## 📑 Tabla de Contenidos

1. [Instalación de FFmpeg](#1-instalación-de-ffmpeg)
   - [Windows (Chocolatey)](#windows-con-chocolatey)
   - [macOS](#macos)
   - [Linux](#linux)
2. [Crear el Entorno Virtual de Python](#2-crear-el-entorno-virtual-de-python)
3. [Instalar Dependencias](#3-instalar-dependencias)
4. [Ejecutar el Script](#4-ejecutar-el-script)
5. [Solución de Problemas](#5-solución-de-problemas)

---

## 1. Instalación de FFmpeg

FFmpeg es un software necesario para procesar videos. Debes instalarlo antes de usar el script.

### Windows (con Chocolatey)

Chocolatey es un gestor de paquetes para Windows que facilita la instalación de software.

#### Paso 1: Instalar Chocolatey

1. **Abre PowerShell como Administrador:**
   - Presiona `Windows + X`
   - Selecciona **"Windows PowerShell (Administrador)"** o **"Terminal (Administrador)"**

2. **Ejecuta el siguiente comando:**
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

3. **Espera a que termine la instalación** (puede tomar 1-2 minutos)

4. **Cierra y abre de nuevo PowerShell** (como Administrador)

#### Paso 2: Instalar FFmpeg

```powershell
choco install ffmpeg -y
```

#### Paso 3: Verificar la instalación

Cierra y abre una nueva terminal (normal, no necesita ser Administrador) y ejecuta:

```powershell
ffmpeg -version
```

**Resultado esperado:**
```
ffmpeg version N-xxxxx-gxxxxxx Copyright (c) 2000-2024...
```

✅ **Si ves la versión de FFmpeg, la instalación fue exitosa!**

---

#### Alternativa: Instalación Manual de FFmpeg en Windows

Si prefieres no usar Chocolatey:

1. **Descarga FFmpeg:**
   - Ve a: https://www.gyan.dev/ffmpeg/builds/
   - Descarga: **ffmpeg-release-essentials.zip**

2. **Extrae el archivo:**
   - Extrae el contenido a: `C:\ffmpeg`
   - Deberías tener: `C:\ffmpeg\bin\ffmpeg.exe`

3. **Añade FFmpeg al PATH:**
   
   **Opción A - Por PowerShell (Administrador):**
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\ffmpeg\bin", "Machine")
   ```
   
   **Opción B - Manualmente:**
   - Presiona `Windows + R` → escribe `sysdm.cpl` → Enter
   - Pestaña **"Opciones avanzadas"** → **"Variables de entorno"**
   - En **"Variables del sistema"**, selecciona **"Path"** → **"Editar"**
   - Click **"Nuevo"** → añade: `C:\ffmpeg\bin`
   - **Aceptar** en todas las ventanas

4. **Reinicia la terminal y verifica:**
   ```cmd
   ffmpeg -version
   ```

---

### macOS

#### Opción 1: Usando Homebrew (Recomendado)

Homebrew es el gestor de paquetes más popular para macOS.

1. **Abrir Terminal:**
   - Presiona `Command + Espacio`
   - Escribe "Terminal" y presiona Enter

2. **Instalar Homebrew (si no lo tienes):**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Instalar FFmpeg:**
   ```bash
   brew install ffmpeg
   ```

4. **Verificar instalación:**
   ```bash
   ffmpeg -version
   ```

#### Opción 2: Usando MacPorts

```bash
sudo port install ffmpeg
```

---

### Linux

#### Ubuntu / Debian / Linux Mint

```bash
# Actualizar repositorios
sudo apt update

# Instalar FFmpeg
sudo apt install ffmpeg -y

# Verificar instalación
ffmpeg -version
```

#### Fedora / RHEL / CentOS

```bash
# Fedora 22+
sudo dnf install ffmpeg -y

# RHEL/CentOS (requiere repositorio EPEL)
sudo yum install epel-release -y
sudo yum install ffmpeg -y

# Verificar instalación
ffmpeg -version
```

#### Arch Linux / Manjaro

```bash
sudo pacman -S ffmpeg

# Verificar instalación
ffmpeg -version
```

---

## 2. Crear el Entorno Virtual de Python

El entorno virtual aísla las dependencias del proyecto del sistema.

### Windows (PowerShell o CMD)

#### Usando PowerShell:

```powershell
# Navegar a la carpeta del proyecto
cd C:\Users\TuUsuario\Desktop\VideoTrimmer

# Crear entorno virtual
python -m venv env

# Activar entorno virtual
.\env\Scripts\Activate.ps1
```

**Si obtienes un error de política de ejecución:**

```powershell
# Cambiar política temporalmente
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Luego activar
.\env\Scripts\Activate.ps1
```

#### Usando CMD (Command Prompt):

```cmd
# Navegar a la carpeta del proyecto
cd C:\Users\TuUsuario\Desktop\VideoTrimmer

# Crear entorno virtual
python -m venv env

# Activar entorno virtual
env\Scripts\activate.bat
```

**Verificar que está activo:**
Deberías ver `(env)` al inicio de tu línea de comandos:
```
(env) PS C:\Users\TuUsuario\Desktop\VideoTrimmer>
```

---

### macOS / Linux

```bash
# Navegar a la carpeta del proyecto
cd ~/Desktop/VideoTrimmer

# Crear entorno virtual
python3 -m venv env

# Activar entorno virtual
source env/bin/activate
```

**Verificar que está activo:**
```
(env) usuario@computadora:~/Desktop/VideoTrimmer$
```

---

## 3. Instalar Dependencias

Una vez que el entorno virtual está activo (verás `(env)` en la terminal):

### Todas las plataformas:

```bash
# Instalar desde requirements.txt
pip install -r requirements.txt
```

O instalar directamente:

```bash
pip install ffmpeg-python
```

**Verificar instalación:**

```bash
pip list
```

Deberías ver:
```
Package        Version
-------------- -------
ffmpeg-python  0.2.0
...
```

---

## 4. Ejecutar el Script

### Windows

#### PowerShell:

```powershell
# Asegúrate de estar en la carpeta del proyecto
cd C:\Users\Taller\Desktop\GRABACIONES\VideoTrimmer

# Activar entorno (si no está activo)
.\env\Scripts\Activate.ps1

# Ejecutar el script - Sintaxis básica
python .\video_trimmer.py "C:\ruta\al\video.mp4" 00:01:30 00:03:45

# Ejemplo real
python .\video_trimmer.py "C:\Users\Taller\Downloads\sesion3.mp4" 00:07:00 00:12:08

# Con nombre de salida personalizado
python .\video_trimmer.py "C:\Users\Taller\Downloads\sesion3.mp4" 00:07:00 00:12:08 -o "recorte_sesion3.mp4"
```

#### CMD (Command Prompt):

```cmd
cd C:\Users\Taller\Desktop\GRABACIONES\VideoTrimmer
env\Scripts\activate.bat
python video_trimmer.py "C:\Users\Taller\Downloads\sesion3.mp4" 00:07:00 00:12:08
```

**📝 Nota sobre rutas en Windows:**
- Si la ruta tiene espacios, usa comillas: `"C:\Mi Carpeta\video.mp4"`
- Puedes usar rutas relativas: `python video_trimmer.py video.mp4 00:00:00 00:01:00`

---

### macOS

```bash
# Navegar a la carpeta del proyecto
cd ~/Desktop/VideoTrimmer

# Activar entorno (si no está activo)
source env/bin/activate

# Ejecutar el script - Sintaxis básica
python3 video_trimmer.py /ruta/al/video.mp4 00:01:30 00:03:45

# Ejemplo real
python3 video_trimmer.py ~/Downloads/sesion3.mp4 00:07:00 00:12:08

# Con nombre de salida personalizado
python3 video_trimmer.py ~/Downloads/sesion3.mp4 00:07:00 00:12:08 -o recorte_sesion3.mp4

# Si el archivo está en la misma carpeta
python3 video_trimmer.py video.mp4 00:00:00 00:01:00
```

---

### Linux

```bash
# Navegar a la carpeta del proyecto
cd ~/Desktop/VideoTrimmer

# Activar entorno (si no está activo)
source env/bin/activate

# Ejecutar el script - Sintaxis básica
python3 video_trimmer.py /ruta/al/video.mp4 00:01:30 00:03:45

# Ejemplo real
python3 video_trimmer.py ~/Descargas/sesion3.mp4 00:07:00 00:12:08

# Con nombre de salida personalizado
python3 video_trimmer.py ~/Descargas/sesion3.mp4 00:07:00 00:12:08 -o recorte_sesion3.mp4

# Si el archivo está en la misma carpeta
python3 video_trimmer.py video.mp4 00:00:00 00:01:00
```

---

## 📝 Sintaxis Completa del Script

```bash
python video_trimmer.py <video_entrada> <tiempo_inicio> <tiempo_fin> [opciones]
```

### Parámetros:

- **video_entrada**: Ruta al archivo .mp4 (absoluta o relativa)
- **tiempo_inicio**: Formato `HH:MM:SS` (ejemplo: 00:01:30)
- **tiempo_fin**: Formato `HH:MM:SS` (ejemplo: 00:03:45)
- **-o, --output**: (Opcional) Nombre del archivo de salida

### Ejemplos de uso:

```bash
# Básico (salida automática: input_trimmed.mp4)
python video_trimmer.py video.mp4 00:01:30 00:03:45

# Con nombre de salida personalizado
python video_trimmer.py video.mp4 00:01:30 00:03:45 -o mi_clip.mp4

# Recortar los primeros 30 segundos
python video_trimmer.py video.mp4 00:00:00 00:00:30

# Con ruta absoluta (Windows)
python video_trimmer.py "C:\Videos\pelicula.mp4" 01:20:00 01:25:30 -o escena.mp4

# Con ruta absoluta (macOS/Linux)
python video_trimmer.py ~/Videos/pelicula.mp4 01:20:00 01:25:30 -o escena.mp4
```

### Ver ayuda completa:

```bash
python video_trimmer.py --help
```

---

## 5. Solución de Problemas

### ❌ Error: "ffmpeg: command not found" o "El sistema no puede encontrar el archivo"

**Causa:** FFmpeg no está instalado o no está en el PATH.

**Solución:**
1. Verifica la instalación: `ffmpeg -version`
2. Si no funciona, reinstala FFmpeg siguiendo la sección 1
3. Cierra y abre de nuevo la terminal después de instalar

---

### ❌ Error: "No module named 'ffmpeg'"

**Causa:** La librería ffmpeg-python no está instalada.

**Solución:**
```bash
# Activar entorno virtual primero
# Windows PowerShell:
.\env\Scripts\Activate.ps1

# macOS/Linux:
source env/bin/activate

# Luego instalar:
pip install ffmpeg-python
```

---

### ❌ Error: "execution of scripts is disabled" (Windows)

**Causa:** Política de ejecución de PowerShell.

**Solución 1 - Usar CMD en lugar de PowerShell:**
```cmd
cd C:\Users\Taller\Desktop\VideoTrimmer
env\Scripts\activate.bat
python video_trimmer.py video.mp4 00:00:00 00:01:00
```

**Solución 2 - Cambiar política temporalmente:**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\env\Scripts\Activate.ps1
```

---

### ❌ Error: "FileNotFoundError" o "El archivo no existe"

**Causa:** La ruta al video es incorrecta.

**Solución:**
1. Verifica que el archivo exista
2. Usa rutas absolutas o verifica que estás en la carpeta correcta
3. En Windows, usa comillas si la ruta tiene espacios:
   ```powershell
   python video_trimmer.py "C:\Mi Carpeta\video.mp4" 00:00:00 00:01:00
   ```

---

### ❌ Error: "El tiempo de fin debe ser mayor que el tiempo de inicio"

**Causa:** Los tiempos están en orden incorrecto.

**Solución:**
Asegúrate de que: `tiempo_inicio < tiempo_fin`

```bash
# ❌ Incorrecto:
python video_trimmer.py video.mp4 00:03:00 00:01:00

# ✅ Correcto:
python video_trimmer.py video.mp4 00:01:00 00:03:00
```

---

### ❌ Error: "Formato de tiempo inválido"

**Causa:** El formato de tiempo no es correcto.

**Solución:**
Usa siempre el formato `HH:MM:SS` con ceros:

```bash
# ❌ Incorrecto:
python video_trimmer.py video.mp4 1:30 3:45
python video_trimmer.py video.mp4 00:1:30 00:3:45

# ✅ Correcto:
python video_trimmer.py video.mp4 00:01:30 00:03:45
```

---

### 🔍 Verificar que todo está instalado correctamente:

```bash
# 1. Verificar Python
python --version    # Windows
python3 --version   # macOS/Linux

# 2. Verificar FFmpeg
ffmpeg -version

# 3. Verificar entorno virtual activo
# Deberías ver (env) en tu terminal

# 4. Verificar dependencias instaladas
pip list
# Debe aparecer: ffmpeg-python
```

---

## 📋 Resumen del Flujo Completo

### Windows (PowerShell/CMD):

```powershell
# 1. Instalar FFmpeg (una sola vez)
choco install ffmpeg -y

# 2. Navegar a la carpeta
cd C:\Users\TuUsuario\Desktop\VideoTrimmer

# 3. Crear entorno virtual (una sola vez)
python -m venv env

# 4. Activar entorno (cada sesión)
.\env\Scripts\Activate.ps1   # PowerShell
# O
env\Scripts\activate.bat      # CMD

# 5. Instalar dependencias (una sola vez)
pip install -r requirements.txt

# 6. Ejecutar script (cada vez que quieras recortar)
python video_trimmer.py "ruta\video.mp4" 00:01:30 00:03:45
```

---

### macOS/Linux:

```bash
# 1. Instalar FFmpeg (una sola vez)
brew install ffmpeg          # macOS
sudo apt install ffmpeg -y   # Ubuntu/Debian

# 2. Navegar a la carpeta
cd ~/Desktop/VideoTrimmer

# 3. Crear entorno virtual (una sola vez)
python3 -m venv env

# 4. Activar entorno (cada sesión)
source env/bin/activate

# 5. Instalar dependencias (una sola vez)
pip install -r requirements.txt

# 6. Ejecutar script (cada vez que quieras recortar)
python3 video_trimmer.py ~/ruta/video.mp4 00:01:30 00:03:45
```

---

## 🎯 Tips y Mejores Prácticas

1. **Siempre activa el entorno virtual** antes de ejecutar el script
2. **Usa rutas absolutas** si tienes problemas con rutas relativas
3. **El formato de tiempo es estricto**: siempre `HH:MM:SS`
4. **FFmpeg debe estar instalado** antes de usar el script
5. **Cierra y abre la terminal** después de instalar FFmpeg
6. **Usa comillas** en rutas con espacios (Windows)

---

## 📞 Soporte

Si encuentras algún problema no cubierto en esta guía:

1. Verifica que FFmpeg esté instalado: `ffmpeg -version`
2. Verifica que el entorno virtual esté activo: busca `(env)` en la terminal
3. Verifica que las dependencias estén instaladas: `pip list`
4. Revisa la sección de **Solución de Problemas**

---

## ✅ Checklist de Instalación

Antes de ejecutar el script por primera vez, verifica:

- [ ] FFmpeg instalado (`ffmpeg -version` funciona)
- [ ] Python 3.6+ instalado (`python --version`)
- [ ] Entorno virtual creado (carpeta `env` existe)
- [ ] Entorno virtual activado (ves `(env)` en la terminal)
- [ ] Dependencias instaladas (`ffmpeg-python` en `pip list`)
- [ ] Archivos del script en la carpeta correcta

**¡Listo para recortar videos! 🎬**
