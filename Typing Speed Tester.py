import tkinter as tk
import time
import random

# Sentences for testing
sentences = [
    "Python is a great programming language",
    "Artificial intelligence is changing the world",
    "Tkinter makes GUI development easy",
    "Practice makes a person perfect",
    "Speed typing is a useful skill"
]

# Function to start test
def start_test():
    global start_time, test_sentence
    test_sentence = random.choice(sentences)
    sentence_label.config(text=test_sentence, fg=random.choice(["#FF5733", "#33FF57", "#3357FF", "#FF33A6"]))
    entry.delete(0, tk.END)
    result_label.config(text="")
    start_time = time.time()

# Function to calculate results
def calculate_results():
    end_time = time.time()
    typed_text = entry.get()
    time_taken = max(end_time - start_time, 1)
    words_typed = len(typed_text.split())
    wpm = round((words_typed / time_taken) * 60)
    
    correct_words = 0
    for i, word in enumerate(typed_text.split()):
        if i < len(test_sentence.split()) and word == test_sentence.split()[i]:
            correct_words += 1
    accuracy = round((correct_words / len(test_sentence.split())) * 100)

    result_label.config(
        text=f"Time: {time_taken:.1f}s | WPM: {wpm} | Accuracy: {accuracy}%",
        fg="#FFD700",
        font=("Helvetica", 14, "bold")
    )

# Tkinter window
window = tk.Tk()
window.title("Typing Speed Tester")
window.geometry("700x400")
window.config(bg="#222831")

# Heading
heading = tk.Label(window, text="💻 Typing Speed Tester 💨", font=("Helvetica", 22, "bold"), bg="#222831", fg="#00ADB5")
heading.pack(pady=15)

# Sentence to type
sentence_label = tk.Label(window, text="", font=("Helvetica", 16), wraplength=600, bg="#222831", fg="white")
sentence_label.pack(pady=20)

# Text entry
entry = tk.Entry(window, font=("Helvetica", 14), width=50, justify="center", bd=3, relief="solid")
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(window, bg="#222831")
btn_frame.pack(pady=20)

start_btn = tk.Button(btn_frame, text="Start Test", command=start_test, font=("Helvetica", 14, "bold"), bg="#00ADB5", fg="white", activebackground="#393E46", relief="raised", width=12)
start_btn.grid(row=0, column=0, padx=10)

submit_btn = tk.Button(btn_frame, text="Submit", command=calculate_results, font=("Helvetica", 14, "bold"), bg="#FF5722", fg="white", activebackground="#393E46", relief="raised", width=12)
submit_btn.grid(row=0, column=1, padx=10)

# Results
result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#222831", fg="white")
result_label.pack(pady=15)

window.mainloop()
