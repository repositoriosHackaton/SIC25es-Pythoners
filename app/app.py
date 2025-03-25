from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import cv2
import numpy as np
import base64
import os
import random

# Configuración inicial de la aplicación
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  # Lee la clave
CORS(app)

# Configuración de rutas importantes
app.config.update({
    'MODEL_PATH': os.path.join(app.root_path, 'data', 'modelo_random_forest.pkl'),
    'IMG_SIZE': (512, 384)
})

# Cargar el modelo de ML al iniciar
try:
    with open(app.config['MODEL_PATH'], "rb") as model_file:
        clf = pickle.load(model_file)
    print("✅ Modelo cargado correctamente desde:", app.config['MODEL_PATH'])
except Exception as e:
    print(f"❌ Error cargando el modelo: {str(e)}")
    clf = None

def base64_to_image(base64_str):
    """Convierte una cadena base64 a imagen OpenCV"""
    try:
        img_data = base64.b64decode(base64_str)
        np_arr = np.frombuffer(img_data, np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except Exception as e:
        print(f"Error procesando imagen: {str(e)}")
        return None

def predecir_imagen(img_base64):
    """Realiza la predicción con el modelo"""
    if not clf:
        return None
        
    img = base64_to_image(img_base64)
    if img is None:
        return None
        
    # Preprocesamiento
    img = cv2.resize(img, app.config['IMG_SIZE'])
    img = img / 255.0  # Normalización
    img_flat = img.flatten().reshape(1, -1)
    
    return clf.predict(img_flat)[0]

# Rutas de la aplicación
@app.route('/')
def home():
    """Sirve la página principal"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint para predicciones"""
    if not clf:
        return jsonify({'error': 'Modelo no disponible'}), 500
        
    try:
        data = request.json
        img_base64 = data['image']
        
        categoria = {
            0: "cartón",
            1: "papel",
            2: "plastico"
        }
        
        prediccion = predecir_imagen(img_base64)
        if prediccion is None:
            return jsonify({'error': 'Error procesando imagen'}), 400
            
        return jsonify({
            'categoria': categoria.get(prediccion, 'desconocido'),
            'codigo': int(prediccion)
        })
        
    except Exception as e:
        print(f"Error en /predict: {str(e)}")
        return jsonify({'error': str(e)}), 500


# Cargar el modelo y el vectorizador
ruta_modelo = os.path.join(os.getcwd(), "app", "chatbot_model.pkl")
ruta_vectorizer = os.path.join(os.getcwd(), "app", "vectorizer.pkl")

with open(ruta_modelo, "rb") as model_file:
    model = pickle.load(model_file)

with open(ruta_vectorizer, "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').lower()
    
    # Vectorizar el mensaje del usuario
    user_message_vectorized = vectorizer.transform([user_message])
    
    # Predecir la categoría
    prediction = model.predict(user_message_vectorized)
    
    # Respuestas basadas en la predicción
    responses = {
        "saludo": [
        "¡Hola! ¿Sabías que reciclar puede salvar el planeta? ¿Cómo te puedo ayudar hoy?",
        "¡Hola! ¿Te interesa saber más sobre el reciclaje y cómo hacerlo correctamente?",
        "¡Buen día! Si tienes preguntas sobre reciclaje, estoy aquí para ayudarte.",
        "¡Saludos! ¿Te gustaría aprender sobre el impacto positivo del reciclaje?",
        "¡Hola! ¿Sabías que pequeños cambios en tu rutina pueden hacer una gran diferencia en el medio ambiente?"
    ],
    
    "identidad": [
        "Soy un chatbot creado para ayudarte a entender más sobre reciclaje y su importancia.",
        "Soy un asistente virtual especializado en ayudarte a hacer un cambio positivo a través del reciclaje.",
        "Soy un chatbot que te orienta sobre cómo mejorar tus hábitos de reciclaje y contribuir al planeta.",
        "Soy un asistente digital con la misión de ayudarte a comprender y practicar el reciclaje.",
        "Soy un chatbot ecológico que busca promover hábitos de reciclaje para cuidar el medio ambiente."
    ],
    
    "despedida": [
        "¡Hasta luego! Recuerda que reciclar es un pequeño gesto que tiene un gran impacto en el planeta.",
        "¡Adiós! Gracias por preocuparte por el reciclaje. ¡Nos vemos pronto!",
        "¡Hasta la próxima! No olvides separar tus residuos y reciclar siempre que puedas.",
        "¡Nos vemos! Reciclar hoy es cuidar el futuro del planeta.",
        "¡Adiós! Gracias por ser parte del cambio. ¡Recuerda reciclar y hacer tu parte!"
    ],

    "reciclaje": [
        "Puedes encontrar zonas de reciclaje en centros como Recicla503 y otros puntos estratégicos. Consulta el Ministerio de Medio Ambiente para más información.",
    ],
    "quereciclar":[
        "Puedes reciclar papel, cartón, plástico, vidrio, metales y más. Asegúrate de separar los materiales correctamente.","Materiales como electrónicos viejos, baterías, envases de vidrio, plástico y papel pueden ser reciclados. Consulta con tu centro local de reciclaje para más detalles.","Recicla residuos como botellas de plástico, latas de metal, papel usado, y recuerda separar los materiales orgánicos de los inorgánicos.", "Es importante reciclar cosas como cartón, vidrio y plástico. Para electrónicos y baterías, verifica los puntos de recolección especializados."
    ],
    "importanciareciclaje":[
        "Reciclar ayuda a reducir la contaminación, ahorrar recursos naturales y construir un futuro más sostenible.","Es esencial reciclar para disminuir la contaminación, ahorrar energía y proteger los ecosistemas del planeta.","El reciclaje reduce la cantidad de desechos que terminan en vertederos y ayuda a conservar los recursos naturales.","Al reciclar, contribuyes a reducir las emisiones de gases de efecto invernadero y a crear un ciclo más sostenible de consumo."
    ],
    "comoreciclar":[
        "Empieza separando tus residuos en orgánicos e inorgánicos. Busca centros de acopio cercanos para llevar tus materiales reciclables.", "Puedes encontrar zonas de reciclaje en centros como Recicla503 y otros puntos estratégicos. Consulta el <a href='https://www.ambiente.gob.sv/se-parte-de-la-cadena-del-reciclaje/' target='_blank' style='font-weight: bold; text-decoration: underline;'>Ministerio de Medio Ambiente</a> para más información.","Lava los envases reciclables como latas y botellas antes de llevarlos al punto de recolección. Mantén todo bien organizado."
    ],
    "circular":[
        "Es un modelo que busca reutilizar materiales y reducir el desperdicio, promoviendo el reciclaje y la sostenibilidad.", "La economía circular busca reutilizar materiales y productos en lugar de desecharlos, reduciendo el desperdicio y promoviendo la sostenibilidad.", "A diferencia del modelo 'usar y tirar', la economía circular busca maximizar el valor de los recursos prolongando su uso.", "Es una forma de diseñar y consumir de manera más consciente, priorizando el reciclaje y la reducción de desechos para cuidar el planeta."
    ],

    }
    
    response = random.choice(responses.get(prediction[0], ["Lo siento, no entiendo tu mensaje."]))

    return jsonify({'response': response})



if __name__ == '__main__':
    # Configuración para desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)