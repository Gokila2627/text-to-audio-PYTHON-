import gtts as gt
import os

# Prompt the user to enter the text to be converted to audio
a = input("Enter the text: ")

# Create a gTTS object with the input text and language set to English
tts = gt.gTTS(text=a, lang="en")

# Save the generated audio to a file named "english-audio.mp3"
tts.save("english-audio.mp3")

# Play the saved audio file using the default system player
os.system("english-audio.mp3")
