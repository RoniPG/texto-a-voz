# Texto a Voz

> Convierte artículos web en archivos de audio MP3 usando Python.

---

## 📌 Descripción

Este proyecto permite tomar un artículo desde cualquier `URL` y generar un archivo de audio reproducible en formato `MP3`. Utiliza herramientas de procesamiento de lenguaje natural y conversión de texto a voz.

El script puede funcionar sin `ffmpeg`, generando un MP3 por cada párrafo del artículo, o si `ffmpeg` está instalado, puede unir todas las partes en un único archivo final.

---

## 🛠️ Tecnologías utilizadas

- [Python 3.10](https://www.python.org/)
- [Newspaper3k](https://newspaper.readthedocs.io/) – Para extraer contenido de artículos web
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) – Para generar el audio en formato MP3
- [Conda](https://docs.conda.io/en/latest/) – Para manejar entornos virtuales
- Git y GitHub – Control de versiones

---

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/RoniPG/texto-a-voz.git
cd texto-a-voz
```
2. Crear y activar el environment de Conda:
```bash
conda env create -f environment.yml
conda activate texto_a_voz
```

3. Instalar paquetes adicionales (si aún no están):
```bash
pip install newspaper3k gtts
```

4. (Recomendado) Instalar `ffmpeg` si deseas un único archivo:
```
-Linux(Ubuntu/Debian):
sudo apt install ffmpeg

-macOS:
brew install ffmpeg
```

- Windows
Descargar desde [ffmpeg.org](https://ffmpeg.org/download.html) y añadir al `PATH`
---

## 📝 Uso


1. Ejecuta el script principal:

```bash
python src/texto_a_voz.py
```

2. Introduce la URL del artículo que deseas convertir.

3. Dependiendo de si tienes ffmpeg instalado:

- **Con ffmpeg** → Se generará un único archivo MP3 con todo el contenido del artículo.

- **Sin ffmpeg** → Se generará un MP3 por partes (cada párrafo), dejando los archivos temporales en la carpeta `audio/`.

4. Si se crearon archivos temporales mientras se generaba el audio, el script los limpia automáticamente al finalizar.

---

## 📂 Estructura del proyecto
```css
texto_a_voz/
├── src/
│   └── texto_a_voz.py
├── audio/
├── environment.yml
├── README.md
└── .gitignore
```