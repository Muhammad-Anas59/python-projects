from win10toast import ToastNotifier
import pyttsx3

toast = ToastNotifier()
toast.show_toast("Reminder",
                 "Hey Anas, what the hell are doing ",
                 duration=5)

engine = pyttsx3.init()
engine.say("Hey Anas, drink water")
engine.runAndWait()


