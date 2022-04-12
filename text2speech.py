from gtts import gTTS
import os

# The text that you want to convert to audio
myText = 'Good morning everyone! This is MBS3523 AI and Programming class!' \
         'You need to submit the mini project on 23 May 2022.'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
output = gTTS(text=myText, lang=language, slow=True)

# Saving the converted audio in a mp3 file named "welcome"
output.save("text1.mp3")

# Playing the converted file
os.system("start text1.mp3")