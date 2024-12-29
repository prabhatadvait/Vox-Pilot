# Vox-Pilot 🎙️

## 📖 Overview

**Vox-Pilot** is a virtual assistant built using Python and utilizes speech recognition to understand voice commands. It can perform various operations, such as opening YouTube or other applications, based on user input. By leveraging Python's powerful libraries, the assistant efficiently translates spoken words into actions, providing a seamless and interactive experience.

## ⚡ Features

- 🗣️ **Speech Recognition**: Converts voice commands to text.
- 🔄 **Task Automation**: Opens websites and applications based on voice input.
- 🐍 **Python Implementation**: Developed using Python's robust libraries like `speech_recognition` and `pyttsx3`.
- 🌐 **Website Opening**: Supports opening websites like YouTube, Google, and more via voice commands.
- 💻 **Application Launching**: Can launch desktop applications like Notepad, Chrome, etc., based on spoken instructions.

## 🧰 Technologies Used

- **Python**: Programming language used for development.
- **speech_recognition**: Library for recognizing speech and converting it to text.
- **pyttsx3**: Text-to-speech conversion library.
- **webbrowser**: Python library to open websites in the browser.
- **os**: Python's built-in library to interact with the operating system and open applications.

## 🚀 Installation

To install and set up the project locally, follow these steps:

1. 🔗 Clone the repository:
    ```bash
    git clone https://github.com/prabhatadvait/Vox-Pilot.git
    ```

2. 🔽 Navigate into the project directory:
    ```bash
    cd Vox-Pilot
    ```

3. 🧑‍💻 Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. 📦 Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. 🗣️ Make sure to install the necessary system dependencies for speech recognition:
    - For Windows: You might need to install [PyAudio](https://pypi.org/project/PyAudio/) for microphone access.
    - For Linux/macOS: Install the `portaudio` library, which is required for PyAudio.

## 🏁 Usage

1. 🗣️ Ensure your microphone is connected and working.
2. ▶️ Run the virtual assistant script:
    ```bash
    python vox_pilot.py
    ```

3. 🎤 Once the assistant starts, say a command like "Open YouTube" or "Open Notepad", and the assistant will execute the action accordingly.

### Example

```bash
$ python vox_pilot.py
Listening for commands...
User: "Open YouTube"
Assistant: "Opening YouTube..."
