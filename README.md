# Texto a Voz

> Convierte artículos web en archivos de audio MP3 usando Python.

---

## 📌 Descripción

Este proyecto permite tomar un artículo desde cualquier URL y generar un archivo de audio reproducible en formato MP3. Utiliza herramientas de procesamiento de lenguaje natural y conversión de texto a voz.

---

## 🛠️ Tecnologías utilizadas

- [Python 3.10](https://www.python.org/)
- [Newspaper3k](https://newspaper.readthedocs.io/) – Para extraer contenido de artículos web
- [NLTK](https://www.nltk.org/) – Para procesamiento de texto
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) – Para generar el audio en formato MP3
- [Conda](https://docs.conda.io/en/latest/) – Para manejar entornos virtuales
- Git y GitHub – Control de versiones

---

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone git@github.com:TU_USUARIO/texto-a-voz.git
cd texto-a-voz
```
2. Crear y activar el environment de Conda:
```bash
conda env create -f environment.yml
conda activate texto_a_voz
```

3. Crear y activar el environment de Conda:
```bash
pip install newspaper3k nltk gtts
```

4. Crear y activar el environment de Conda:
```bash
import nltk
nltk.download('punkt')
```

---

## 📝 Uso


1. Ejecuta el script principal:

```bash
python src/texto_a_voz.py
```

2. Introduce la URL del artículo que deseas convertir.

3. Se generará un archivo MP3 en la carpeta audio/ con el contenido del artículo.

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