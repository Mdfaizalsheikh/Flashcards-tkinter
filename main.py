import tkinter as tk
from tkinter import messagebox


flashcards = {
    "Hello": "Hola",
    "Goodbye": "Adiós",
    "Please": "Por favor",
    "Thank you": "Gracias",
    "Yes": "Sí",
    "No": "No"
}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Flashcards")

        self.current_card_index = 0
        self.flashcards = list(flashcards.items())

        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.translation_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.translation_label.pack(pady=20)

        self.show_flashcard()

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side="right", padx=10, pady=10)

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_card)
        self.prev_button.pack(side="left", padx=10, pady=10)

        self.new_word_entry = tk.Entry(root, font=("Helvetica", 14))
        self.new_word_entry.pack(pady=5)

        self.new_translation_entry = tk.Entry(root, font=("Helvetica", 14))
        self.new_translation_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.pack(pady=5)

    def show_flashcard(self):
        word, translation = self.flashcards[self.current_card_index]
        self.word_label.config(text=word)
        self.translation_label.config(text=translation)

    def next_card(self):
        self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)
        self.show_flashcard()

    def prev_card(self):
        self.current_card_index = (self.current_card_index - 1) % len(self.flashcards)
        self.show_flashcard()

    def add_flashcard(self):
        new_word = self.new_word_entry.get().strip()
        new_translation = self.new_translation_entry.get().strip()
        if new_word and new_translation:
            flashcards[new_word] = new_translation
            self.flashcards = list(flashcards.items())
            self.new_word_entry.delete(0, tk.END)
            self.new_translation_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Flashcard added successfully!")
        else:
            messagebox.showerror("Error", "Both fields must be filled out.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
