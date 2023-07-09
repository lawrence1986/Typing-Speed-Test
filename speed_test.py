#!/usr/bin/python3
import random
import time
import tkinter as tk
from tkinter import messagebox

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.texts = [
            "In the beginning was the word and the word was with God and the word was God.",
            "I look up to the heavens from where comes my help.",
            "Innovation drives technological advancements.",
            "Software development is a collaborative process.",
            "Debugging is a crucial part of programming.",
            "Algorithms form the basis of computer science.",
            "Computers have revolutionized our lives.",
            "Automation simplifies repetitive tasks.",
            "Data is the new oil in today's world.",
            "Cybersecurity is essential to protect data.",
            "Cloud computing enables scalable applications.",
            "Programming is good, it takes time, dedication to master.",
            "I love coding and building cool projects.",
            "Wherever you go, you can always find good people.",
            "Although he was rich, he was still unhappy.",
            "The future is full of possibilities with AI."
            "When she was younger, she believed in Santa Claus.",
            "My name is Lawrence Maduabuchi, I am from Anambra State Nigeria",
            "Although it was very long, the movie was still entertaining.",
            "I enjoyed the apple pie that you bought for me.",
            "If the dog goes to the county fair, he will eat popcorn.",
            "The football match was cancelled because it was raining.",
            "Is Chelsea Football team doing a total Overhauling or Over Flushing.",
            "Since we are already late, we don’t have time to stop.",
            "If you have found the page, please begin reading.",
            "Because my coffee was too cold, I heated it in the microwave.",
            "Although the Justice League was very long, the movie was still enjoyable.",
            "Although I’m not very good, I really enjoy playing chess with my girlfriend.",
            "Even though they were millionaires, they drive old cars.",
            "Learning new things is always exciting.",
            "Programming helps solve complex problems.",
            "The internet is a vast source of information.",
            "Artificial Intelligence is transforming industries.",
            "Practice makes perfect in programming.",
            "Coding is a valuable skill in the digital age.",
        ]
        self.current_text = ""
        self.user_input = ""
        self.start_time = 0
        self.elapsed_time = 0
        self.words_typed = 0
        self.accuracy = 0.0

        self.create_widgets()

    def create_widgets(self):
        self.text_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.text_label.pack(pady=10)

        self.input_entry = tk.Entry(self.root, font=("Arial", 14))
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", self.check_input)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test, font=("Arial", 14))
        self.start_button.pack(pady=10)

    def start_test(self):
        self.current_text = random.choice(self.texts)
        self.text_label.configure(text=self.current_text)

        self.input_entry.delete(0, tk.END)
        self.input_entry.configure(state="normal")
        self.input_entry.focus()

        self.result_label.configure(text="")
        self.start_time = time.time()
        self.words_typed = 0
        self.accuracy = 0.0

    def check_input(self, event=None):
        self.user_input = self.input_entry.get().strip()

        if self.user_input == self.current_text:
            self.elapsed_time = time.time() - self.start_time
            self.calculate_result()
            self.input_entry.configure(state="disabled")
        else:
            messagebox.showinfo("Incorrect", "Incorrect input. Try again.")

    def calculate_result(self):
        words = self.current_text.split()
        self.words_typed = len(words)
        chars_typed = len(self.user_input)
        accuracy_percentage = (chars_typed / len(self.current_text)) * 100
        self.accuracy = round(accuracy_percentage, 2)

        wpm = (self.words_typed / self.elapsed_time) * 60
        wpm = round(wpm, 2)

        result_text = f"Time taken: {self.elapsed_time} seconds\n"
        result_text += f"Words typed: {self.words_typed}\n"
        result_text += f"Accuracy: {self.accuracy}%\n"
        result_text += f"WPM: {wpm}"
        self.result_label.configure(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    SpeedTypingTest(root)
    root.mainloop()
