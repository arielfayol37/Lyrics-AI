# Lyric App Documentation
---
## [toggle_listen()](#toggle_listen)
Toggle Listening

## [listen_audio()](#listen_audio)
Listen to Audio

## [import_lyric_files()](#import_lyric_files)
Import Lyric Files

## [display_selected_file(event)](#display_selected_file)
Display Selected File

## [__init__(self, root)](#init)
Initialize GUI Application

## [lyric_app(root)](#lyric_app)
Constructor Method for lyric_app Class

## Introduction
---
This application allows users to import lyric files, listen to audio input, and display lyrics based on the audio input's similarity to the imported lyrics. The application is built using the Tkinter library for the GUI, and it incorporates functionalities for text processing, file handling, and audio processing.

## Code Structure
The code is divided into several sections, each serving a specific purpose:

1. **Importing Libraries**: The necessary libraries are imported, including Tkinter for GUI development, filedialog for file handling, and various modules for text and audio processing.

2. **Text Encoding Functions**: Functions for encoding text into numerical representations are defined. This includes `encode_text` for encoding using BERT embeddings and `embed` for encoding using Sentence Transformers.

3. **File Processing**: The `process_files` function reads text files from a specified directory, extracts their content, and encodes the text using the `embed` function.

4. **GUI Class**: The `lyric_app` class defines the GUI application. It includes buttons for starting and stopping audio listening, importing lyric files, a listbox for displaying selected files, and a text area for displaying lyrics.

5. **Event Handlers**: Event handlers are defined for interacting with GUI elements. These include functions for toggling audio listening, importing lyric files, and displaying selected files.

6. **Main Application**: The main application window is created using Tkinter, and an instance of the `lyric_app` class is instantiated.

## Method Details

1. **`toggle_listen()`**
   - **Purpose**: This method toggles the audio listening functionality of the application.
   - **Functionality**:
     - Changes the button text and starts or stops the audio listening thread accordingly.
   - **Usage**: It is triggered by clicking the "Start Listening" button and controls the audio input processing.

2. **`listen_audio()`**
   - **Purpose**: This method continuously listens for audio input while the application is in the listening state.
   - **Functionality**:
     - Utilizes `get_text()` to retrieve the text from audio input.
     - Encodes the text into numerical vectors using `embed()`.
     - Compares the embeddings with preprocessed lyrics and displays the most similar lyrics.
   - **Usage**: Called when the application is in the listening state to process audio input and display relevant lyrics.

3. **`import_lyric_files()`**
   - **Purpose**: This method handles the importation of lyric files into the application.
   - **Functionality**:
     - Opens a file dialog for users to select and import lyric files.
     - Displays the selected files in the listbox.
   - **Usage**: Triggered by clicking the "Import Lyric Files" button to allow users to import lyric files into the application.

4. **`display_selected_file(event)`**
   - **Purpose**: This method displays the content of a selected file in the text display area.
   - **Functionality**:
     - Retrieves the selected file from the listbox.
     - Reads the file's content and displays it in the text display area.
   - **Usage**: Triggered by double-clicking a file in the listbox to display its content in the text display area.

5. **`__init__(self, root)`**
   - **Purpose**: This method initializes the GUI application.
   - **Functionality**:
     - Sets up the main application window and its components, including buttons, listbox, and text display area.
   - **Usage**: Called when an instance of the `lyric_app` class is created to initialize the GUI.

6. **`lyric_app(root)`**
   - **Purpose**: Constructor method for the `lyric_app` class.
   - **Functionality**:
     - Initializes the main application window and its components.
   - **Usage**: Creates an instance of the `lyric_app` class, which serves as the main GUI application.

## Usage
1. **Starting the Application**: Run the script to launch the Lyric App.
2. **Importing Lyric Files**: Click on the "Import Lyric Files" button to select and import lyric files (in .txt format).
3. **Listening to Audio**: Click on the "Start Listening" button to begin listening to audio input. Click again to stop listening.
4. **Displaying Lyrics**: When audio input is detected, the application compares it with the imported lyric files and displays the most similar lyrics in the text display area.
5. **Viewing Selected Files**: Double-click on a file in the listbox to display its content in the text display area.

## Dependencies
-Python3
-pyaudio
-speechRecognition
-torch
-numpy
-tensorflow
-tensorflow_hub
-transformers
-scikit-learn
-sentence-transformers

## Note
- Ensure that the required modules (`speech_to_text`, `text_to_vector`, etc.) are correctly installed and accessible in the Python environment.
- Modify the `lyrics_directory` variable to specify the directory containing the lyric files.

