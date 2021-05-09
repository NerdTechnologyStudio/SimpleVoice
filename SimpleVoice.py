import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
#PyAudio è fondamentale nell'esecuzione di Speech_Recognition

class SimpleVoice:
    def __init__(self):
        sv = tk.Tk()  # Creazione GUi
        sv.title("SimpleVoice") # Titolo
        # Creazione Frame #
        button_frame = tk.Frame(sv)
        button_frame.grid(row=0, column=0)
        text_frame = tk.Frame(sv)
        text_frame.grid(row=1, column=0)

        self.text = tk.Text(text_frame)
        self.text.grid(row=0, column=0)
        text = self.text
        # Tasto Button #
        scrivi = tk.Button(button_frame, text="Vocal", command=self.vocal)
        scrivi.grid(row=0, column=0, padx=0, ipadx=25)

        sv.mainloop()
    # Funzione Speech_Recognition
    def vocal(self):
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                command = listener.recognize_google(voice, language="it-IT")
                self.text.insert(tk.INSERT, command)
        except Exception as e:
            print(e)
 # Loop #
if __name__ == "__main__":
    SimpleVoice()
