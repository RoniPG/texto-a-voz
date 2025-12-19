from newspaper import Article
from gtts import gTTS
import nltk
import os

# Descargar recursos NLTK (solo la primera vez)
nltk.download('punkt_tab')

# Carpeta para guardar los audios
AUDIO_FOLDER = "./audio/"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def articulo_a_mp3(url, nombre_archivo="articulo.mp3", idioma="es"):
    """
    Convierte un artículo de URL a archivo MP3.
    """
    
    try:
        # 1️ Descargar y procesar el artículo
        articulo = Article(url, language=idioma)
        articulo.download()
        articulo.parse()
        articulo.nlp()

        texto = articulo.text
        if not texto.strip():
            raise ValueError("No se pudo extraer texto del artículo.")

        # 2️ Convertir texto a voz
        tts = gTTS(text=texto, lang=idioma)
        ruta_completa = os.path.join(AUDIO_FOLDER, nombre_archivo)
        tts.save(ruta_completa)

        print(f"✅ Archivo de audio generado: {ruta_completa}")
    except Exception as e:
        print(f"❌ Error al procesar la URL: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del artículo: ")
    nombre_archivo = input("Nombre del archivo MP3 (por defecto articulo.mp3): ") or "articulo.mp3"
    articulo_a_mp3(url, nombre_archivo)
