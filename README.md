# Lyric App
---

The Lyric App is a Python application that allows users to import lyric files, listen to audio input, and display lyrics based on the audio input's similarity to the imported lyrics. The application is built using Tkinter for the GUI and incorporates functionalities for text processing, file handling, and audio processing.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/arielfayol37/Lyrics-AI.git
    ```

2. Navigate to the project directory:

    ```
    cd lyric-ai
    ```

3. Install the required dependencies. Ensure you have Python 3.x installed on your system. Install dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Starting the Application**: Run the script to launch the Lyric App:

    ```
    python3 lyric_app.py
    ```

2. Importing Lyric Files: Click on the "Import Lyric Files" button to select and import lyric files (in .txt format).

3. Listening to Audio: Click on the "Start Listening" button to begin listening to audio input. Click again to stop listening.

4. Displaying Lyrics: When audio input is detected, the application compares it with the imported lyric files and displays the most similar lyrics in the text display area.

5. Viewing Selected Files: Double-click on a file in the listbox to display its content in the text display area.

## Dependencies

- pyttsx3
- pyaudio
- speechRecognition
- torch
- numpy
- tensorflow
- tensorflow_hub
- transformers
- scikit-learn
- sentence-transformers

Ensure that the required modules (`speech_to_text`, `text_to_vector`, etc.) are correctly installed and accessible in the Python environment.

## Note

- Modify the `lyrics_directory` variable in the code to specify the directory containing the lyric files.

---

Feel free to reach out if you have any questions or encounter any issues while running the Lyric App!

