# code  for time  in   different   timezones
# importing modules
import pendulum
import pyttsx3  # for speaking purpose


# function for speaking
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)  # rate of speaking
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()


speak("Hello ! I will convert time in desired timezones.")
# current details
d1 = pendulum.now()
# splitting for getting date and time only
dt1 = str(d1).split(".")
speak("Here is your current timezones with current date and time")
print(f"current timezone:{d1.timezone_name}")  # for displaying timezone
print(f"current date and time: {dt1[0]}")  # as we split time and timezone
speak("bhai kaha ka time dekna h teko bta ")
i = input("enter here: ")
# details for inputed timezones
try:
    d2 = pendulum.now(i)
    dt2 = str(d2).split(".")
    speak("here is the details")
    print(f"Current date and time for {d2.timezone_name} :{dt2[0]}")
except Exception as e:
    speak("looks like you have entered incorrect timezone!")
    speak("Please check it and try again!")
