import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones CORS desde otro dominio/puerto

# Asigna tu clave de OpenAI desde las variables de entorno (recomendado)
# Ejemplo: export OPENAI_API_KEY='tu_api_key'

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        # Tomamos el prompt (pregunta) que envía el frontend
        prompt = request.json.get("prompt", "")

        # Llamada a la API de OpenAI
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Usa el modelo que tengas disponible
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Obtenemos la respuesta
        answer = completion.choices[0].message.content
        
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Ejecutamos el servidor Flask en el puerto 5001 (por ejemplo)
    app.run(port=5001, debug=True)