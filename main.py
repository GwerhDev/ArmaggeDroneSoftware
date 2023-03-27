from config import API_OPENAI
import openai
import pyttsx3
import tkinter as tk

# Define tus credenciales de OpenAI
openai.api_key = API_OPENAI

# Configura la biblioteca de texto a voz
engine = pyttsx3.init()

# Crea la ventana principal
root = tk.Tk()
root.title("Chatbot")

# Crea una caja de texto para el input del usuario
user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=10)

# Define la variable para almacenar el contexto
last_chatbot_message = []

def generate_response():
  global last_chatbot_message
  # Obtiene el input del usuario
  user_message = user_input.get()

  # Define el prompt que quieres enviar a ChatGPT
  prompt = f"Usuario: {user_message}\nChatbot: {last_chatbot_message}"

  # Envía la solicitud a la API de ChatGPT
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=50,
      n=1,
      stop=None,
      temperature=0.5,
  )

  # Obtiene la respuesta generada por ChatGPT
  chatbot_message = response.choices[0].text.strip()

  # Actualiza el contexto del chatbot
  last_chatbot_message.append(chatbot_message)

  # Lee la respuesta en voz alta
  engine.say(chatbot_message)
  engine.runAndWait()

# Crea un botón para enviar el mensaje
send_button = tk.Button(root, text="Enviar", command=generate_response)
send_button.pack(padx=10, pady=10)

# Inicia la ventana principal
root.mainloop()
