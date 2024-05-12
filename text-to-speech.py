# pip install pyttsx3 #
import pyttsx3

# Load the lib #
engine = pyttsx3.init()

# Text that the engine will speak #
engine.say('Hello how are you?')
engine.say('What language do you program in?')

# Execute #
engine.runAndWait()
