import streamlit as st
from openai import OpenAI

# Configuración del cliente OpenAI
client = OpenAI()

def transcribe_audio(audio_file):
    response = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file
    )
    # Inspecciona la respuesta para entender su estructura
    print(response)

    # Suponiendo que la respuesta tiene un atributo 'text', cambia la siguiente línea
    return response.text  # Cambia 'text' por el atributo correcto según la inspección


def summarize_text(text):
    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text}
      ]
    )
    # Inspecciona la respuesta para entender su estructura
    print(response)

    # Modifica la siguiente línea según la estructura correcta de la respuesta
    # Por ejemplo, si la respuesta es un objeto con un atributo 'content', usa response.content
    return response.choices[0].message.content  # Modifica esta línea según la estructura de la respuesta


# Diseño de la interfaz de Streamlit
st.title('Transcriptor y Resumidor de Voz')

uploaded_file = st.file_uploader("Sube un archivo de voz", type=['mp3', 'wav', 'ogg', 'm4a'])
if uploaded_file is not None:
    # Transcripción del archivo
    text = transcribe_audio(uploaded_file)
    st.text_area("Transcripción", text, height=250)

    # Generación y visualización del resumen
    summary = summarize_text("Haz un resumen de lo siguiente: " + text)
    st.text_area("Resumen", summary, height=150)
