giimport csv
import random
import tkinter as tk

def display_random_word():
    with open('words.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        word_data = random.choice(data)
        word = word_data[0]
        synonyms = word_data[1]
        antonyms = word_data[2]
        usage = word_data[3]
        word_label.config(text=f"Word: {word}")
        synonyms_label.config(text=f"Synonyms: {synonyms}")
        antonyms_label.config(text=f"Antonyms: {antonyms}")
        usage_label.config(text=f"Usage: {usage}")

root = tk.Tk()
root.title("Random Word Display")

word_label = tk.Label(root, text="")
synonyms_label = tk.Label(root, text="")
antonyms_label = tk.Label(root, text="")
usage_label = tk.Label(root, text="")

word_label.pack()
synonyms_label.pack()
antonyms_label.pack()
usage_label.pack()

display_button = tk.Button(root, text="Display Random Word", command=display_random_word)
display_button.pack()

root.mainloop()
