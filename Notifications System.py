from win10toast import ToastNotifier
import pyttsx3

# --- Notification ---
toast = ToastNotifier()
toast.show_toast("Reminder",
                 "Hey Anas, drink water 💧",
                 duration=5)

# --- Voice Speech ---
engine = pyttsx3.init()
engine.say("Hey Anas, drink water")
engine.runAndWait()
