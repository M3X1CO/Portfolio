import cowsay
import pyttsx4
engine = pyttsx4.init()

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 100)

this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()


engine.stop()
