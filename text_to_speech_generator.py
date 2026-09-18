from gtts import gTTS

text = "Coding is hard yet fun..(*cries low-key)"

tts = gTTS(text=text, lang="en")

tts.save("voice.mp3")
print("audio saved succesfully")