from win10toast import ToastNotifier
import pyttsx3

toast = ToastNotifier()
toast.show_toast("Reminder",
                 "Hey Anas, drink water ",
                 duration=5)

engine = pyttsx3.init()
engine.say("Hey Anas, drink water")
engine.runAndWait()
