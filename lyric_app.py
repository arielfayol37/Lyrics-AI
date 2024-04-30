import tkinter as tk
from tkinter import filedialog

from speech_to_text import get_text
from text_to_vector import *
import os
import threading

# import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

from sentence_transformers import SentenceTransformer
# import re
# import seaborn as sns

lyrics_directory = "lyrics_folder/"

# module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
# model = hub.load(module_url)
# print ("module %s loaded" % module_url)
# def embed_0(input):
#   return model(input)

def encode_text(text):
    # max_length = 512 # maybe we should reduce this because the input text should be quite short
    with torch.no_grad():
        max_length = 512
        lyric_tokens = bert_tokenizer.encode(text, add_special_tokens=True, \
                                                max_length=max_length, truncation=True, padding='max_length')
        lyric_tensor = torch.tensor([lyric_tokens])
        attention_mask = (lyric_tensor != 0).float()  # Create attention mask
        encoded_output = bert_model(lyric_tensor, attention_mask=attention_mask)[0]  # Take the hidden states                
        encoded_output_pooled = attention_pooling(encoded_output, attention_mask)
    return encoded_output_pooled

def embed(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight model
    return model.encode(text)

def process_files(lyrics_directory):
    lyrics = {}
    folder_path = lyrics_directory
    # Iterate over the files in the specified directory
    counter = -1
    for filename in os.listdir(folder_path):
        # Create the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it is a file (and not a directory)
        if os.path.isfile(file_path) and file_path[-4:] == ".txt":
            counter += 1
            lyrics[counter] = {"text":""}
        # Open the file using the 'open' function with 'r' mode (read mode)
            with open(file_path, 'r') as file:
                # Read the contents of the file
                content = file.read()
            lyrics[counter]["text"] = content
            lyrics[counter]["embedding"] = embed(content)
    
    return lyrics

counter = -1
# lyrics = process_files(lyrics_directory)
lyrics = {}
imported_files = []
# print(lyrics[0])

class lyric_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyric App")


        self.is_Listening = False
        # Listen button
        self.listen_button = tk.Button(root, text="Start Listening", command=self.toggle_listen)
        self.listen_button.grid(row=0, column=0, padx=10, pady=10)

        # Import Lyric Files button
        self.import_button = tk.Button(root, text="Import Lyric Files", command=self.import_lyric_files)
        self.import_button.grid(row=1, column=0, padx=10, pady=10)

        # listbox to display selected files
        self.listbox = tk.Listbox(root, width=30, height=10)
        self.listbox.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.listbox.bind("<Double-Button-1>", self.display_selected_file)  #double-click event

        # text display area
        self.text_display = tk.Text(root, height=20, width=40, font=("Arial", 15))
        self.text_display.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky='nsew')

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def toggle_listen(self):
        if not self.is_Listening:
            self.is_Listening = True
            self.listen_button.config(text="Stop Listening")
            self.audio_thread = threading.Thread(target=self.listen_audio)
            self.audio_thread.start()
        else:
            self.is_Listening = False
            self.listen_button.config(text="Start Listening")
            # Properly manage thread termination if necessary

    def listen_audio(self):
        while self.is_Listening:
            heard_text = get_text()
            heard_embedding = embed(heard_text)
            similarity_score = 0
            display_lyric = ""
            if heard_text != "":
                for lyric_id, value in lyrics.items():
                    score = np.inner(heard_embedding, value["embedding"]).item()
                    if score > similarity_score:
                        similarity_score = score
                        display_lyric = value["text"]
                print("display lyric", display_lyric)
                if display_lyric:
                    self.text_display.delete(1.0, tk.END)  # Clear previous text
                    self.text_display.insert(tk.END, display_lyric)


    def import_lyric_files(self):
        global counter
        # Open file 
        lyric_files = filedialog.askopenfilenames(title="Select Lyric Files", filetypes=(("Lyric files", "*.txt"), ("All files", "*.*")))

        # Display selected files 
        if lyric_files:
            self.listbox.delete(0, tk.END)  # Clear previous selection

            for filename in lyric_files:
                # Create the full file path
                file_path = filename
                
                # Check if it is a file (and not a directory)
                if os.path.isfile(file_path) and file_path[-4:] == ".txt" and file_path not in imported_files:
                    counter += 1
                    lyrics[counter] = {"text":""}
                # Open the file using the 'open' function with 'r' mode (read mode)
                    with open(file_path, 'r') as file:
                        # Read the contents of the file
                        content = file.read()
                    lyrics[counter]["text"] = content
                    lyrics[counter]["embedding"] = embed(content)
            
                self.listbox.insert(tk.END, os.path.basename(file_path))

    def display_selected_file(self, event):
        # Get the selected file from the listbox
        selected_file_index = self.listbox.curselection()
        if selected_file_index:
            selected_file = self.listbox.get(selected_file_index)
            # Displays the content from the file
            with open(selected_file, 'r') as f:
                content = f.read()
                self.text_display.delete(1.0, tk.END)  # Clear previous text
                self.text_display.insert(tk.END, content)


# Creates the main application window
root = tk.Tk()
app = lyric_app(root)

# Configure window resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()

