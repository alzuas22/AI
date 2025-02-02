# -*- coding: utf-8 -*-
"""Pruebas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fp9P2hmGJdniyhfR213QNfBcwVkgxRV0

# Generación de Preguntas a partir de Textos

## Introducción

Nuestro objetivo es preparar un sistema especializado en la generación de preguntas a partir de textos, utilizando modelos de lenguaje preentrenados. Este proyecto tiene aplicaciones en la educación, la generación de contenido y sistemas de tutoría automática.

Para la generación de preguntas, empleamos modelos avanzados de lenguaje preentrenados disponibles en la biblioteca `transformers` de Hugging Face.

## Proceso

1. **Recopilación de Textos**:
   - Utilizamos textos en español como entrada para la generación de preguntas.
   
2. **Generación de Preguntas**:
   - Utilizamos un pipeline de generación de preguntas basado en el modelo T5 (Text-to-Text Transfer Transformer).

Instalamos las librerías necesarias.
"""

# Instalamos la biblioteca transformers de Hugging Face
!pip install transformers

"""Procedemos a la construcción de la pipeline."""

from transformers import pipeline

# Cargamos un pipeline de generación de preguntas
generator = pipeline('text2text-generation', model='t5-base')

# Texto de ejemplo
text ="""K'inich Janaab' Pakal o Pakal “el Grande” (23 de marzo de 603 - 28 de agosto de 683) fue un ahau o gobernante del ajawlel o señorío maya de B'aakal,
 cuya sede era Lakam Ha', ahora conocida como la zona arqueológica de Palenque, ubicada en el norte del estado mexicano de Chiapas.
Fue entronizado por su padre a la edad de doce años, gobernó desde el año 615 hasta el 683, convirtiéndose así en uno de los gobernantes
más longevos de la historia. Ascendió al poder después de que Palenque hubiera sufrido un período de adversidad. Durante las primeras décadas
 de su gobierno se vivió una época de paz y productividad. En el 659 inició una campaña militar que consolidó a Palenque como una de las ciudades
 más importantes de la región. El gobierno de Pakal se caracterizó por haber impulsado el crecimiento de la obra arquitectónica de Palenque y por
  haber iniciado los registros jeroglíficos de su historia dinástica."""

# Generamos preguntas
prompt = f"Genera preguntas a partir del siguiente texto: {text} Pregunta:"

questions = generator(prompt, max_length=512, num_beams=5, num_return_sequences=5)

for i, question in enumerate(questions):
    print(f"Pregunta {i+1}: {question['generated_text']}")

# Instalar las bibliotecas necesarias
!pip install transformers

from transformers import pipeline

# Cargar un pipeline especializado en generación de preguntas
generator = pipeline('text2text-generation', model='valhalla/t5-small-qg-hl')

# Texto de ejemplo
text = """K'inich Janaab' Pakal o Pakal “el Grande” (23 de marzo de 603 - 28 de agosto de 683) fue un ahau o gobernante del ajawlel o señorío maya de B'aakal,
cuya sede era Lakam Ha', ahora conocida como la zona arqueológica de Palenque, ubicada en el norte del estado mexicano de Chiapas.
Fue entronizado por su padre a la edad de doce años, gobernó desde el año 615 hasta el 683, convirtiéndose así en uno de los gobernantes
más longevos de la historia. Ascendió al poder después de que Palenque hubiera sufrido un período de adversidad. Durante las primeras décadas
de su gobierno se vivió una época de paz y productividad. En el 659 inició una campaña militar que consolidó a Palenque como una de las ciudades
más importantes de la región. El gobierno de Pakal se caracterizó por haber impulsado el crecimiento de la obra arquitectónica de Palenque y por
haber iniciado los registros jeroglíficos de su historia dinástica."""

# Añadir indicadores especiales al texto
text_with_hl = "generate questions: " + text.replace("Pakal", "<hl>Pakal<hl>")

# Generar preguntas
questions = generator(text_with_hl, max_length=512, num_beams=5, num_return_sequences=5)

for i, question in enumerate(questions):
    print(f"Pregunta {i+1}: {question['generated_text']}")

# Cargar un pipeline especializado en generación de preguntas
question_generator = pipeline('text2text-generation', model='valhalla/t5-small-qg-hl')

# Cargar un pipeline especializado en respuestas
answer_generator = pipeline('question-answering', model='deepset/roberta-base-squad2')

from transformers import pipeline

# Texto de ejemplo
text = """In Tijuana, Gina sees a pickup truck carrying a bull, which she surmises belongs to Shawn's grandfather. Shawn gets into the bed of the truck and discovers that the bull can talk and that the bull believes his encounter with Shawn is part of an ancient bovine prophecy. The bull agrees to teach him Spanish, which he calls "the language that will thwart evil."

The truck stops in the fictional ghost town of La Zorra as the bull continues on in the truck to his fate as a bull in a bullfight. Exploring the town, Shawn meets Tío Juan, his uncle, who is now an "exporter" to the United States and has "unfinished business" with Miguel's father in Ensenada. He offers Shawn a ride to Ensenada in his jeep and helps him learn Spanish along the way.

Shawn and Tío Juan reach Ensenada, and Juan states that he will not be able to bring Shawn back to the United States. Miguel returns Shawn's DS, and as Shawn walks away from Miguel's house, a group of six cars pulls up on the front driveway.

As gunfire can be heard in the background, the game sets up a potential sequel by explaining that Juan left a box for Shawn filled with "many puffy dolls", an airplane ticket, and a message asking Shawn to deliver the package to his "friend", Gustave Charlot, in France."""

# Añadir indicadores especiales al texto para la generación de preguntas
text_with_hl = "generate questions: " + text.replace("Shawn", "<hl>Shawn<hl>")

# Generar preguntas
questions = question_generator(text_with_hl, max_length=512, num_beams=5, num_return_sequences=5)

# Generar respuestas para las preguntas
for i, question in enumerate(questions):
    question_text = question['generated_text']
    answer = answer_generator(question=question_text, context=text)
    print(f"Pregunta {i+1}: {question_text}")
    print(f"Respuesta {i+1}: {answer['answer']}")
    print()

# Texto de ejemplo
text = """In Tijuana, Gina sees a pickup truck carrying a bull, which she surmises belongs to Shawn's grandfather. Shawn gets into the bed of the truck and discovers that the bull can talk and that the bull believes his encounter with Shawn is part of an ancient bovine prophecy. The bull agrees to teach him Spanish, which he calls "the language that will thwart evil."

The truck stops in the fictional ghost town of La Zorra as the bull continues on in the truck to his fate as a bull in a bullfight. Exploring the town, Shawn meets Tío Juan, his uncle, who is now an "exporter" to the United States and has "unfinished business" with Miguel's father in Ensenada. He offers Shawn a ride to Ensenada in his jeep and helps him learn Spanish along the way.

Shawn and Tío Juan reach Ensenada, and Juan states that he will not be able to bring Shawn back to the United States. Miguel returns Shawn's DS, and as Shawn walks away from Miguel's house, a group of six cars pulls up on the front driveway.

As gunfire can be heard in the background, the game sets up a potential sequel by explaining that Juan left a box for Shawn filled with "many puffy dolls", an airplane ticket, and a message asking Shawn to deliver the package to his "friend", Gustave Charlot, in France."""

# Generar preguntas utilizando el texto directamente
prompt = f"generate questions: {text} Pregunta:"

# Generar preguntas
questions = question_generator(prompt, max_length=512, num_beams=5, num_return_sequences=5)

# Generar respuestas para las preguntas
for i, question in enumerate(questions):
    question_text = question['generated_text']
    answer = answer_generator(question=question_text, context=text)
    print(f"Pregunta {i+1}: {question_text}")
    print(f"Respuesta {i+1}: {answer['answer']}")
    print()

# Texto de ejemplo
text = """La aleatoriedad se refiere a eventos, procesos o modelos en los que algunos de los resultados son esencialmente imprevisibles, por efectos relacionados con el azar. El concepto admite diferentes caracterizaciones en matemáticas, ciencia, filosofía o historia.

Por ejemplo, en matemáticas sólo una secuencia infinita puede ser realmente aleatoria (para secuencias finitas siempre es posible encontrar una fórmula determinista que la reproduzca). En física, se cree que existe una aleatoriedad profunda, como podría existir en física cuántica y una aleatoriedad práctica, como es el lanzamiento de dados (si bien macroscópicamente está gobernado por leyes de movimiento deterministas en la práctica es difícil de predecir el resultado). El resultado de todo suceso aleatorio no puede determinarse en ningún caso antes de que este se produzca. El estudio de los fenómenos aleatorios queda dentro del ámbito de la teoría de la probabilidad y, en un marco más amplio, en el de la estadística.

La palabra aleatorio se usa para expresar una aparente carencia de propósito, causa, u orden. En cambio, el término aleatoriedad se usa a menudo como sinónimo con un número de propiedades estadísticas medibles, tales como la carencia de tendencias o correlación, es decir, que no haya patrones que se puedan identificar."""

# Generar preguntas utilizando el texto directamente
prompt = f"generate questions: {text} Pregunta:"

# Generar preguntas
questions = question_generator(prompt, max_length=512, num_beams=5, num_return_sequences=5)

# Generar respuestas para las preguntas
for i, question in enumerate(questions):
    question_text = question['generated_text']
    answer = answer_generator(question=question_text, context=text)
    print(f"Pregunta {i+1}: {question_text}")
    print(f"Respuesta {i+1}: {answer['answer']}")
    print()

# Texto de ejemplo
text = """La aleatoriedad se refiere a eventos, procesos o modelos en los que algunos de los resultados son esencialmente imprevisibles, por efectos relacionados con el azar. El concepto admite diferentes caracterizaciones en matemáticas, ciencia, filosofía o historia.

Por ejemplo, en matemáticas sólo una secuencia infinita puede ser realmente aleatoria (para secuencias finitas siempre es posible encontrar una fórmula determinista que la reproduzca). En física, se cree que existe una aleatoriedad profunda, como podría existir en física cuántica y una aleatoriedad práctica, como es el lanzamiento de dados (si bien macroscópicamente está gobernado por leyes de movimiento deterministas en la práctica es difícil de predecir el resultado). El resultado de todo suceso aleatorio no puede determinarse en ningún caso antes de que este se produzca. El estudio de los fenómenos aleatorios queda dentro del ámbito de la teoría de la probabilidad y, en un marco más amplio, en el de la estadística.

La palabra aleatorio se usa para expresar una aparente carencia de propósito, causa, u orden. En cambio, el término aleatoriedad se usa a menudo como sinónimo con un número de propiedades estadísticas medibles, tales como la carencia de tendencias o correlación, es decir, que no haya patrones que se puedan identificar."""

# Añadir indicadores especiales al texto para la generación de preguntas
text_with_hl = "generate questions: " + text.replace("aleatoriedad", "<hl>aleatoriedad<hl>")

# Generar preguntas
questions = question_generator(text_with_hl, max_length=512, num_beams=5, num_return_sequences=5)

# Generar respuestas para las preguntas
for i, question in enumerate(questions):
    question_text = question['generated_text']
    answer = answer_generator(question=question_text, context=text)
    print(f"Pregunta {i+1}: {question_text}")
    print(f"Respuesta {i+1}: {answer['answer']}")
    print()

# Instalar las bibliotecas necesarias
!pip install transformers

from transformers import pipeline

# Cargar un pipeline especializado en generación de preguntas
question_generator = pipeline('text2text-generation', model='valhalla/t5-base-qg-hl')

# Cargar un pipeline especializado en respuestas
answer_generator = pipeline('question-answering', model='deepset/roberta-base-squad2')

# Texto de ejemplo dividido en segmentos más pequeños
segments = [
    "La aleatoriedad se refiere a eventos, procesos o modelos en los que algunos de los resultados son esencialmente imprevisibles, por efectos relacionados con el azar. El concepto admite diferentes caracterizaciones en matemáticas, ciencia, filosofía o historia.",
    "En matemáticas sólo una secuencia infinita puede ser realmente aleatoria (para secuencias finitas siempre es posible encontrar una fórmula determinista que la reproduzca).",
    "En física, se cree que existe una aleatoriedad profunda, como podría existir en física cuántica y una aleatoriedad práctica, como es el lanzamiento de dados (si bien macroscópicamente está gobernado por leyes de movimiento deterministas en la práctica es difícil de predecir el resultado).",
    "El resultado de todo suceso aleatorio no puede determinarse en ningún caso antes de que este se produzca.",
    "El estudio de los fenómenos aleatorios queda dentro del ámbito de la teoría de la probabilidad y, en un marco más amplio, en el de la estadística.",
    "La palabra aleatorio se usa para expresar una aparente carencia de propósito, causa, u orden.",
    "El término aleatoriedad se usa a menudo como sinónimo con un número de propiedades estadísticas medibles, tales como la carencia de tendencias o correlación, es decir, que no haya patrones que se puedan identificar.",
    "La aleatoriedad ocupa un lugar importante en la ciencia, la filosofía y la historia."
]

# Generar preguntas y respuestas para cada segmento
for segment in segments:
    # Resaltar la palabra clave "aleatoriedad"
    segment_with_hl = segment.replace("aleatoriedad", "<hl>aleatoriedad<hl>")
    prompt = f"generate questions: {segment_with_hl} Pregunta:"

    # Generar preguntas
    questions = question_generator(prompt, max_length=512, num_beams=10, num_return_sequences=2)

    for i, question in enumerate(questions):
        question_text = question['generated_text']
        answer = answer_generator(question=question_text, context=segment)
        print(f"Pregunta {i+1}: {question_text}")
        print(f"Respuesta {i+1}: {answer['answer']}")
        print()

from transformers import pipeline

# Cargar los pipelines necesarios
translator_es_to_en = pipeline('translation_es_to_en', model='Helsinki-NLP/opus-mt-es-en')
translator_en_to_es = pipeline('translation_en_to_es', model='Helsinki-NLP/opus-mt-en-es')
question_generator = pipeline('text2text-generation', model='valhalla/t5-small-qg-hl')
answer_generator = pipeline('question-answering', model='deepset/roberta-base-squad2')

# Texto de ejemplo en español
text_es = """La aleatoriedad se refiere a eventos, procesos o modelos en los que algunos de los resultados son esencialmente imprevisibles, por efectos relacionados con el azar. El concepto admite diferentes caracterizaciones en matemáticas, ciencia, filosofía o historia.

Por ejemplo, en matemáticas sólo una secuencia infinita puede ser realmente aleatoria (para secuencias finitas siempre es posible encontrar una fórmula determinista que la reproduzca). En física, se cree que existe una aleatoriedad profunda, como podría existir en física cuántica y una aleatoriedad práctica, como es el lanzamiento de dados (si bien macroscópicamente está gobernado por leyes de movimiento deterministas en la práctica es difícil de predecir el resultado). El resultado de todo suceso aleatorio no puede determinarse en ningún caso antes de que este se produzca. El estudio de los fenómenos aleatorios queda dentro del ámbito de la teoría de la probabilidad y, en un marco más amplio, en el de la estadística.

La palabra aleatorio se usa para expresar una aparente carencia de propósito, causa, u orden. En cambio, el término aleatoriedad se usa a menudo como sinónimo con un número de propiedades estadísticas medibles, tales como la carencia de tendencias o correlación, es decir, que no haya patrones que se puedan identificar. La aleatoriedad ocupa un lugar importante en la ciencia, la filosofía y la historia."""

# Traducir el texto de español a inglés
text_en = translator_es_to_en(text_es)[0]['translation_text']

# Añadir indicadores especiales al texto para la generación de preguntas
text_with_hl_en = "generate questions: " + text_en.replace("randomness", "<hl>randomness<hl>")

# Generar preguntas
questions_en = question_generator(text_with_hl_en, max_length=512, num_beams=10, num_return_sequences=5)

# Generar respuestas para las preguntas
qa_pairs = []
for question in questions_en:
    question_text_en = question['generated_text']
    answer_en = answer_generator(question=question_text_en, context=text_en)
    qa_pairs.append((question_text_en, answer_en['answer']))

# Traducir preguntas y respuestas de inglés a español
qa_pairs_es = [(translator_en_to_es(question)[0]['translation_text'], translator_en_to_es(answer)[0]['translation_text']) for question, answer in qa_pairs]

# Imprimir preguntas y respuestas en español
for i, (question_es, answer_es) in enumerate(qa_pairs_es):
    print(f"Pregunta {i+1}: {question_es}")
    print(f"Respuesta {i+1}: {answer_es}")
    print()

from transformers import pipeline

# Cargar un pipeline especializado en traducción
translator_es_to_en = pipeline('translation_es_to_en', model='Helsinki-NLP/opus-mt-es-en')
translator_en_to_es = pipeline('translation_en_to_es', model='Helsinki-NLP/opus-mt-en-es')

# Cargar un pipeline especializado en generación de preguntas en inglés
question_generator = pipeline('text2text-generation', model='valhalla/t5-small-qg-hl')

# Cargar un pipeline especializado en respuestas en inglés
answer_generator = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

# Texto de ejemplo en español
text_es = """La aleatoriedad se refiere a eventos, procesos o modelos en los que algunos de los resultados son esencialmente imprevisibles, por efectos relacionados con el azar. El concepto admite diferentes caracterizaciones en matemáticas, ciencia, filosofía o historia.

Por ejemplo, en matemáticas sólo una secuencia infinita puede ser realmente aleatoria (para secuencias finitas siempre es posible encontrar una fórmula determinista que la reproduzca). En física, se cree que existe una aleatoriedad profunda, como podría existir en física cuántica y una aleatoriedad práctica, como es el lanzamiento de dados (si bien macroscópicamente está gobernado por leyes de movimiento deterministas en la práctica es difícil de predecir el resultado). El resultado de todo suceso aleatorio no puede determinarse en ningún caso antes de que este se produzca. El estudio de los fenómenos aleatorios queda dentro del ámbito de la teoría de la probabilidad y, en un marco más amplio, en el de la estadística.

La palabra aleatorio se usa para expresar una aparente carencia de propósito, causa, u orden. En cambio, el término aleatoriedad se usa a menudo como sinónimo con un número de propiedades estadísticas medibles, tales como la carencia de tendencias o correlación, es decir, que no haya patrones que se puedan identificar. La aleatoriedad ocupa un lugar importante en la ciencia, la filosofía y la historia."""

# Traducir el texto de español a inglés
text_en = translator_es_to_en(text_es)[0]['translation_text']

# Añadir indicadores especiales al texto para la generación de preguntas
text_with_hl_en = "generate questions: " + text_en.replace("randomness", "<hl>randomness<hl>")

# Generar preguntas
questions_en = question_generator(text_with_hl_en, max_length=512, num_beams=5, num_return_sequences=5)

# Generar respuestas para las preguntas
qa_pairs = []
for question in questions_en:
    question_text_en = question['generated_text']
    answer_en = answer_generator(question=question_text_en, context=text_en)
    qa_pairs.append((question_text_en, answer_en['answer']))

# Traducir preguntas y respuestas de inglés a español
qa_pairs_es = [(translator_en_to_es(question)[0]['translation_text'], translator_en_to_es(answer)[0]['translation_text']) for question, answer in qa_pairs]

# Imprimir preguntas y respuestas en español
for i, (question_es, answer_es) in enumerate(qa_pairs_es):
    print(f"Pregunta {i+1}: {question_es}")
    print(f"Respuesta {i+1}: {answer_es}")
    print()

from transformers import pipeline

# Cargar un pipeline especializado en generación de preguntas
question_generator = pipeline('text2text-generation', model='valhalla/t5-small-qg-hl')

# Cargar un pipeline especializado en respuestas
answer_generator = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

# Texto de ejemplo en inglés
text_en = """The fields of mathematics, probability, and statistics use formal definitions of randomness, typically assuming that there is some 'objective' probability distribution. In statistics, a random variable is an assignment of a numerical value to each possible outcome of an event space. This association facilitates the identification and the calculation of probabilities of the events. Random variables can appear in random sequences. A random process is a sequence of random variables whose outcomes do not follow a deterministic pattern, but follow an evolution described by probability distributions. These and other constructs are extremely useful in probability theory and the various applications of randomness."""

# Añadir indicadores especiales al texto para la generación de preguntas
text_with_hl_en = "generate questions: " + text_en.replace("randomness", "<hl>randomness<hl>")

# Generar preguntas
questions_en = question_generator(text_with_hl_en, max_length=512, num_beams=5, num_return_sequences=5)

# Generar respuestas para las preguntas
qa_pairs = []
for question in questions_en:
    question_text_en = question['generated_text']
    answer_en = answer_generator(question=question_text_en, context=text_en)
    qa_pairs.append((question_text_en, answer_en['answer']))

# Imprimir preguntas y respuestas en inglés
for i, (question_en, answer_en) in enumerate(qa_pairs):
    print(f"Pregunta {i+1}: {question_en}")
    print(f"Respuesta {i+1}: {answer_en}")
    print()

# Instala la biblioteca de OpenAI si no la tienes instalada
!pip install openai

import os
from openai import OpenAI
from google.colab import userdata
# Configura tu clave API de OpenAI
os.environ["OPENAI_API_KEY"] = userdata.get('OPEN_AI_TOKEN')


# Inicializa el cliente de OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Texto proporcionado
texto = """
The fields of mathematics, probability, and statistics use formal definitions of randomness, typically assuming that there is some 'objective' probability distribution. In statistics, a random variable is an assignment of a numerical value to each possible outcome of an event space. This association facilitates the identification and the calculation of probabilities of the events. Random variables can appear in random sequences. A random process is a sequence of random variables whose outcomes do not follow a deterministic pattern, but follow an evolution described by probability distributions. These and other constructs are extremely useful in probability theory and the various applications of randomness.
"""

# Función para generar preguntas y respuestas
def generar_preguntas_respuestas(texto, n_preguntas=5):
    prompt = f"Generate {n_preguntas} questions and answers based on the following text:\n\n{texto}"
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )
    return response['choices'][0]['message']['content'].strip()

# Generar preguntas y respuestas
qa_text = generar_preguntas_respuestas(texto)
print(qa_text)