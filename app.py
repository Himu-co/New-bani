import pyttsx3
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, OptionMenu, Text
from tkinter.scrolledtext import ScrolledText

def speak_text():
    """Convert text to speech."""
    text = text_area.get("1.0", "end").strip()
    if text:
        engine.say(text)
        engine.runAndWait()
        status_label.config(text="Speaking...", fg="blue")
    else:
        status_label.config(text="Please enter text to speak.", fg="red")

def save_audio():
    """Save the converted speech to an audio file."""
    text = text_area.get("1.0", "end").strip()
    if text:
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                 filetypes=[("Audio Files", "*.mp3")],
                                                 title="Save As")
        if file_path:
            engine.save_to_file(text, file_path)
            engine.runAndWait()
            status_label.config(text=f"Audio saved to {file_path}", fg="green")
    else:
        status_label.config(text="Please enter text to save.", fg="red")

def update_voice():
    """Update the voice based on user selection."""
    selected_voice = voice_var.get()
    if selected_voice == "Male":
        engine.setProperty('voice', voices[0].id)
    elif selected_voice == "Female":
        engine.setProperty('voice', voices[1].id)

def update_rate():
    """Update the speaking rate based on user input."""
    try:
        rate = int(rate_entry.get())
        engine.setProperty('rate', rate)
        status_label.config(text=f"Speaking rate set to {rate}", fg="green")
    except ValueError:
        status_label.config(text="Invalid rate. Please enter a number.", fg="red")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Set up the GUI
root = Tk()
root.title("Professional Text-to-Speech App")
root.geometry("500x500")
root.configure(bg="#f4f4f4")

# Title
Label(root, text="Text-to-Speech Converter", font=("Arial", 18, "bold"), bg="#f4f4f4").pack(pady=10)

# Text Area
Label(root, text="Enter Text:", font=("Arial", 14), bg="#f4f4f4").pack(anchor="w", padx=20)
text_area = ScrolledText(root, font=("Arial", 12), height=8, width=50, wrap="word")
text_area.pack(padx=20, pady=10)

# Buttons
Button(root, text="Speak", font=("Arial", 12), command=speak_text, bg="#4CAF50", fg="white").pack(pady=5)
Button(root, text="Save as MP3", font=("Arial", 12), command=save_audio, bg="#2196F3", fg="white").pack(pady=5)

# Voice Selection
Label(root, text="Select Voice:", font=("Arial", 12), bg="#f4f4f4").pack(anchor="w", padx=20)
voice_var = StringVar(root)
voice_var.set("Male")  # Default voice
voice_menu = OptionMenu(root, voice_var, "Male", "Female", command=lambda _: update_voice())
voice_menu.config(font=("Arial", 12))
voice_menu.pack(padx=20, pady=5)

# Speaking Rate Adjustment
Label(root, text="Set Speaking Rate (Default 200):", font=("Arial", 12), bg="#f4f4f4").pack(anchor="w", padx=20)
rate_entry = Entry(root, font=("Arial", 12), width=10)
rate_entry.insert(0, "200")  # Default rate
rate_entry.pack(padx=20, pady=5)
Button(root, text="Set Rate", font=("Arial", 12), command=update_rate, bg="#FF9800", fg="white").pack(pady=5)

# Status Label
status_label = Label(root, text="", font=("Arial", 10), bg="#f4f4f4")
status_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
