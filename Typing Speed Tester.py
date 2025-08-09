import tkinter as tk
import time
import random

# Sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a powerful programming language",
    "Typing speed tests are fun to practice",
    "Tkinter is used to create GUI applications",
    "Always practice to improve your typing skills"
]

start_time = None
current_sentence = ""

def start_test():
    global current_sentence, start_time
    current_sentence = random.choice(sentences)
    sentence_label.config(text=current_sentence)
    entry.delete(0, tk.END)
    result_label.config(text="")
    start_time = None

def start_timer(event):
    global start_time
    if start_time is None:
        start_time = time.time()

def calculate_result():
    global start_time
    if start_time is None:
        result_label.config(text="Please type the sentence first!")
        return
    
    end_time = time.time()
    time_taken = end_time - start_time
    typed_text = entry.get()
    
    # Calculate WPM
    words = len(typed_text.split())
    wpm = round((words / time_taken) * 60, 2)
    
    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(typed_text, current_sentence) if a == b)
    accuracy = round((correct_chars / len(current_sentence)) * 100, 2)
    
    result_label.config(text=f"Speed: {wpm} WPM | Accuracy: {accuracy}%")

# Create window
window = tk.Tk()
window.title("Typing Speed Tester")
window.geometry("600x300")

title_label = tk.Label(window, text="Typing Speed Tester", font=("Arial", 18))
title_label.pack(pady=10)

sentence_label = tk.Label(window, text="", font=("Arial", 14), wraplength=500)
sentence_label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width=50)
entry.pack(pady=10)
entry.bind("<KeyPress>", start_timer)

start_button = tk.Button(window, text="Start Test", font=("Arial", 12), command=start_test)
start_button.pack(pady=5)

submit_button = tk.Button(window, text="Submit", font=("Arial", 12), command=calculate_result)
submit_button.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
