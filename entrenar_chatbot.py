# train_chatbot.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Datos de entrenamiento
data = [
# saludo
("hola", "saludo"),
("como estas?", "saludo"),
("buenos dias", "saludo"),
("buenas tardes", "saludo"),
("buenas noches", "saludo"),
("que tal?", "saludo"),
("como te va?", "saludo"),
("que onda!", "saludo"),
("hola, que tal!", "saludo"),
# despedida
("adios", "despedida"),
("nos vemos", "despedida"),
("hasta luego", "despedida"),
("hasta pronto", "despedida"),
("chao", "despedida"),
("cuidate", "despedida"),
("nos vemos pronto", "despedida"),
("hasta manana", "despedida"),
("que tengas un buen dia", "despedida"),
("adios, cuidate!", "despedida"),
# identidad
("quien eres?", "identidad"),
("eres un humano o un robot?", "identidad"),
("como puedes ayudarme con el reciclaje?", "identidad"),
("cual es tu proposito?", "identidad"),
("por que fuiste creado?", "identidad"),
("sabes sobre el medio ambiente?", "identidad"),
("eres un asistente ecologico?", "identidad"),
("tienes un nombre?", "identidad"),
("por que promueves el reciclaje?", "identidad"),
("como aprendiste sobre reciclaje?", "identidad"),
# quereciclar
("que puedo reciclar?", "quereciclar"),
("que cosas se pueden reciclar?", "quereciclar"),
("que materiales son reciclables?", "quereciclar"),
("que tipo de residuos se pueden reciclar?", "quereciclar"),
("que elementos puedo separar para reciclar?", "quereciclar"),
("cuales son los productos que se pueden reciclar?", "quereciclar"),
("como se que se puede reciclar?", "quereciclar"),
("que materiales puedo reciclar?", "quereciclar"),
("cuales son los materiales que puedo reciclar?", "quereciclar"),
("que tipo de materiales pueden ser reciclados?", "quereciclar"),
("que materiales se pueden reutilizar a traves del reciclaje?", "quereciclar"),
("como se que materiales puedo reciclar?", "quereciclar"),
("cuales son los materiales reciclables mas comunes?", "quereciclar"),
("que materiales estan permitidos para reciclar?", "quereciclar"),
# importancia reciclaje
("por que es importante reciclar?", "importanciareciclaje"),
("por que el reciclaje es tan relevante?", "importanciareciclaje"),
("cual es la importancia del reciclaje?", "importanciareciclaje"),
("por que debemos reciclar?", "importanciareciclaje"),
("que impacto tiene el reciclaje en el medio ambiente?", "importanciareciclaje"),
("como ayuda reciclar al planeta?", "importanciareciclaje"),
("en que nos beneficia reciclar?", "importanciareciclaje"),
# comoreciclar
("como", "comoreciclar"),
("como puedo empezar a reciclar?", "comoreciclar"),
("como iniciar con el reciclaje?", "comoreciclar"),
("cual es el primer paso para reciclar?", "comoreciclar"),
("como puedo comenzar a separar mi basura para reciclar?", "comoreciclar"),
("como hacer que el reciclaje sea un habito?", "comoreciclar"),
("que debo hacer para empezar a reciclar en casa?", "comoreciclar"),
("como puedo aprender a reciclar correctamente?", "comoreciclar"),
# circular
("que es la economia circular?", "circular"),
("como se define la economia circular?", "circular"),
("a que se refiere el concepto de economia circular?", "circular"),
("que significa economia circular?", "circular"),
("cual es la idea principal de la economia circular?", "circular"),
("como funciona la economia circular?", "circular"),
("que diferencia hay entre la economia circular y el reciclaje?", "circular"),
# reciclaje
("donde estan las zonas de reciclaje en el salvador?", "reciclaje"),
("donde puedo encontrar centros de reciclaje en el salvador?", "reciclaje"),
("donde estan los puntos de reciclaje en el pais?", "reciclaje"),
("en que lugares de El Salvador puedo reciclar?", "reciclaje"),
("donde se ubican las estaciones de reciclaje en el salvador?", "reciclaje"),
("como encuentro sitios para reciclar en el salvador?", "reciclaje"),
("que lugares reciben material reciclable en el salvador?", "reciclaje"),

]

# Separar los mensajes y las etiquetas
X, y = zip(*data)

# Vectorizar los mensajes
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Entrenar el modelo
model = MultinomialNB()
model.fit(X_vectorized, y)

# Guardar el modelo y el vectorizador
with open("app/chatbot_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("app/vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Modelo y vectorizador guardados.")
