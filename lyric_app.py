import tkinter as tk
from tkinter import filedialog

class lyric_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyric App")
	
        self.listening = False

        # Listen button
        self.listen_button_text = tk.StringVar()
        self.listen_button_text.set("Listen")
        self.listen_button = tk.Button(root, textvariable=self.listen_button_text, command=self.toggle_listen)
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
        # Toggle listening state and update button text
        self.listening = not self.listening
        if self.listening:
            self.listen_button_text.set("Stop")
            # Add code to start listening here
        else:
            self.listen_button_text.set("Listen")
            # Add code to stop listening here

    def import_lyric_files(self):
        # Open file 
        lyric_files = filedialog.askopenfilenames(title="Select Lyric Files", filetypes=(("Lyric files", "*.txt"), ("All files", "*.*")))
        # Display selected files 
        if lyric_files:
            for file in lyric_files:
                self.listbox.insert(tk.END, file)

    def display_selected_file(self, event):

        # Clear the text display area
        self.text_display.delete(1.0, tk.END)

        # Get the selected file from the listbox
        selected_file_index = self.listbox.curselection()
        if selected_file_index:
            selected_file = self.listbox.get(selected_file_index)
            # Displays the content from the file
            with open(selected_file, 'r') as f:
                content = f.read()
                self.text_display.insert(tk.END, content)


# Creates the main application window
root = tk.Tk()
app = lyric_app(root)

# Configure window resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()

