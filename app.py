from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)

# Folder containing translations
TRANSLATIONS_FOLDER = "translations"

# Regular expression to match a verse
verse_pattern = re.compile(r"^\d?\s?[A-Za-z]+ \d+:\d+")

# Function to load the selected Bible translation
def load_translation(translation):
    file_path = os.path.join(TRANSLATIONS_FOLDER, f"{translation}.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.readlines()
    return []

# Search function for a word in the selected translation
def search_word(word, bible_text):
    results = []
    count = 0  # Initialize the word count
    for line in bible_text:
        if word.lower() in line.lower():  # Case-insensitive search
            results.append(line.strip())  # Add the matching line to results
            count += line.lower().count(word.lower())  # Count occurrences of the word
    return results, count

@app.route("/", methods=["GET", "POST"])
def index():
    translations = [f.split(".")[0] for f in os.listdir(TRANSLATIONS_FOLDER) if f.endswith(".txt")]
    verses = []
    word_count = 0
    selected_translation = None
    word = None
    if request.method == "POST":
        selected_translation = request.form["translation"]
        word = request.form["word"]
        bible_text = load_translation(selected_translation)
        verses, word_count = search_word(word, bible_text)
    return render_template("index.html", translations=translations, verses=verses, word=word, selected_translation=selected_translation, word_count=word_count)

if __name__ == "__main__":
    app.run(debug=True)
