import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar variables desde .env
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# Validación para evitar errores silenciosos
if not clave_api:
    raise ValueError("No se encontró GEMINI_API_KEY. Revisa tu archivo .env y que esté en la raíz del proyecto.")

# 2. Inicializar el cliente con la API Key
client = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...🚈")
    try:
        # 3. Llamada al modelo
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Preséntate brevemente como un asistente de IA configurado para apoyar el curso de 'Desarrollo de aplicaciones con IA.'"
        )

        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")

    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")

if __name__ == "__main__":
    ejecutar_consulta()
