from newspaper import Article
from gtts import gTTS
import os
import shutil
from pathlib import Path


# Carpeta para guardar los audios
AUDIO_FOLDER = "./audio/"
os.makedirs(AUDIO_FOLDER, exist_ok=True)


def articulo_a_mp3(url, nombre_archivo="articulo", idioma="es"):
    """
    Convierte un artículo de URL a archivo MP3.
    """

    try:
        # 1️ Descargar y procesar el artículo
        articulo = Article(url, language=idioma)
        articulo.download()
        articulo.parse()
        # articulo.nlp() # --> Opcional: para resumen y keywords

        texto = articulo.text
        if not texto.strip():
            raise ValueError("No se pudo extraer texto del artículo.")

        # 2️ Dividir el texto en parrafos
        # parrafos = [p.strip() for p in texto.split("\n") if p.strip()]
        texto_parrafos = texto.split("\n\n")

        # 3 Convertir parrafos a voz
        ruta_completa = os.path.join(AUDIO_FOLDER, nombre_archivo)

        for i, parrafo in enumerate(texto_parrafos):
            tts = gTTS(text=parrafo, lang=idioma)
            tts.save(f"{ruta_completa}_{i}.mp3")

        # 4 Unificar toodos los archivos mp3 en uno solo. (necesita ffmpeg instalado)
        if not (shutil.which("ffmpeg")):
            print(f"✅ Archivos de audios generados en la carpeta: {AUDIO_FOLDER}")
        else:
            # Obtenemos todos los arhivos mp3 generados
            mp3s = sorted(Path(AUDIO_FOLDER).glob("*.mp3"))

            # Creamos un archivo temporal con la lista de archivos a unir
            tmp_file = f"{AUDIO_FOLDER}files.txt"
            with open(tmp_file, "w") as f:
                for mp3 in mp3s:
                    f.write(f"file '{mp3.name}'\n")

            # Comando para unir los archivos con ffmpeg
            os.system(f"ffmpeg -f concat -safe 0 -i {tmp_file} -c copy {ruta_completa}.mp3")

            # Borramos los archivos individuales
            for mp3 in mp3s:
                mp3.unlink()
                
            #Borramos el archivo temporal
            if Path(tmp_file).exists():
               Path(tmp_file).unlink()
            print(f"✅ Archivo de audio generado: {ruta_completa}")

    except Exception as e:
        print(f"❌ Error al procesar la URL: {e}")


if __name__ == "__main__":
    url = input("Introduce la URL del artículo: ")
    nombre_archivo = (
        input("Nombre del archivo MP3 (por defecto articulo): ") or "articulo"
    )
    articulo_a_mp3(url, nombre_archivo)
