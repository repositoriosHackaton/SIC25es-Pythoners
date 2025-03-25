# Clasificador Inteligente de Residuos Reciclables

Conclusiones del proyecto

## Tabla de contenidos

1. [Nombre](#Nombre)
2. [Descripción](#descripción)
3. [Arquitectura](#Arquitectura)
4. [Proceso](#Proceso)
5. [Funcionalidades](#Funcionalidades)
6. [Estado del proyecto](#EstadoDelProyecto)

### Nombre
* Clasificador Inteligente de Residuos Reciclables

### Descripción
Este proyecto consiste en el desarrollo de un modelo de clasificación de residuos utilizando técnicas de Machine Learning. Se implementará un modelo basado en Random Forest para clasificar imágenes de residuos en tres categorías principales: cartón, papel y metal. El objetivo es facilitar la separación de residuos reciclables mediante un sistema automatizado que pueda ser aplicado en aplicaciones web. Para el entrenamiento del modelo, se utilizará un dataset de imágenes de residuos previamente etiquetadas.

![ProyectoGIF](img/ProyectoGIF.gif)

### Arquitectura
- La arquitectura del proyecto se puede visualizar a través del siguiente diagrama:
    ![Arquitectura](img/Arquitectura.png)

- El funcionamiento del proyecto se puede visualizar a través del siguiente diagrama de flujo:
    ![Flujograma](img/Flujograma.png)

### Proceso
* **Fuente de los datasets:** https://huggingface.co/datasets/garythung/trashnet

* **Limpieza de datos:**
    ![LimpiezaDeDatos](img/LimpiezaDeDatos.png)

* **Manejo de excepciones / control de errores:**
    - Se debe subir un archivo de imagen si se desea realizar la predicción, si se usa el botón "Subir y Predecir":
        ![ManejoExcepciones](img/ManejoExcepciones1.png)
    - Otra excepcion...
        ![ManejoExcepciones](img/ManejoExcepciones2.png)
    - Otra excepcion...
        ![ManejoExcepciones](img/ManejoExcepciones3.png)


* **Estadísticos (Valores, gráficos, …):**
    1. Metricas y graficos del modelo de clasificación de residuos reciclables:
        - Cálculo de la precisión del modelo (75%):
            ![CalculoPrecision](img/CalculoPrecision.png)
        - Accuracy, Precision, Recall, F1-Score, Support:
            ![Valores](img/ValoresRR.png)
        - Grafico de Valores (Precision, Recall, F1-Score):
            ![GraficoValores](img/GraficoValores.png)
        - Matriz de confusión:
            ![MatrizConfusion](img/MatrizConfusionRR.png)
        - Curva ROC:
            ![CurvaROC](img/CurvaROC.png)
    
    2. Metricas y graficos del modelo de chatbot:
        - Distribución de categorías:
            ![DistribucionCategorias](img/DistribucionCategorias.png)
        - Accuracy, Precision, Recall, F1-Score, Support:
            ![Valores](img/ValoresCB.png)
        - Matriz de confusión:
            ![MatrizConfusion](img/MatrizConfusionCB.png)
        - Curva de aprendizaje:
            ![CurvaDeAprendizaje](img/CurvaDeAprendizaje.png)

### Funcionalidades

- **Integración de un chatbot:**
    - Tecnología / Herramientas usadas: 
- **Uso de cámara para la detección de residuos reciclables:**
    - Tecnología / Herramientas usadas:
- **Integración del proyecto en una página web:**
    - Enlace: (pendiente)
    - Tecnología / Herramientas usadas: HTML, CSS, Tailwind, Flask, Render.
    - Arquitectura (img): La arquitectura del proyecto junto con la integración en una página web se puede visualizar a través del siguiente diagrama:
        ![ArquitecturaWeb](img/ArquitecturaWeb.png)

### EstadoDelProyecto
En proceso de desarrollo