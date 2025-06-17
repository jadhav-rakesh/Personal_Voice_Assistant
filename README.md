# 🎤 Voice Assistant

This project is a friendly voice assistant powered by **Rakesh's profile**, designed to provide quick, conversational answers about his background, skills, goals, and even fun facts. It leverages **Streamlit** for a simple web interface, **SpeechRecognition** for voice input, **pyttsx3** for text-to-speech output, and **LangChain** to connect with a powerful **Deepseek LLM** via OpenRouter.

It's perfect for anyone wanting to interact with a personalized AI assistant and explore the capabilities of conversational AI, speech-to-text, and text-to-speech technologies.

## ✨ Features

* **🎙️ Voice Interaction:** Speak directly to the assistant, and it will understand your queries.
* **🗣️ Conversational AI:** Get natural, short, and chill responses based on Rakesh's detailed profile.
* **🧠 Contextual Understanding:** The assistant remembers past conversations to provide more relevant answers.
* **🚀 Powered by OpenRouter:** Utilizes a Deepseek LLM for intelligent and dynamic responses.
* **💻 Streamlit UI:** A clean and intuitive web interface for easy interaction.

## 🛠️ Technologies Used

* **Python 3.9+**
* **Streamlit:** For building the web application.
* **SpeechRecognition:** For converting speech to text.
* **pyttsx3:** For converting text to speech.
* **LangChain:** For orchestrating the LLM interactions and managing chat history.
* **OpenRouter.ai:** As an API gateway to access the Deepseek LLM.
* **python-dotenv:** For managing environment variables.

## 🚀 Getting Started

Follow these steps to get your Rakesh's Voice Assistant up and running locally.

### Prerequisites

* Python 3.9 or higher installed on your system.
* An API key from [OpenRouter.ai](https://openrouter.ai/).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/rakesh-voice-assistant.git](https://github.com/your-username/rakesh-voice-assistant.git)
    cd rakesh-voice-assistant
    ```

    **(Note: Replace `your-username` with your actual GitHub username or the repository's owner.)**

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    **(You'll need to create a `requirements.txt` file first. See the "Dependencies" section below.)**

4.  **Set up environment variables:**

    Create a `.env` file in the root directory of your project and add your OpenRouter API key:

    ```
    OPENROUTER_API_KEY="YOUR_OPENROUTER_API_KEY"
    ```

    Replace `"YOUR_OPENROUTER_API_KEY"` with your actual API key.

5.  **Create `rakesh_profile.txt`:**

    In the same root directory, create a file named `rakesh_profile.txt` and populate it with details about Rakesh. This content will be used by the AI to answer questions. For example:

    ```
    Rakesh is a software engineer with 5 years of experience in full-stack development.
    He specializes in Python, JavaScript, and cloud technologies (AWS).
    His goals include mastering machine learning and contributing to open-source projects.
    Fun fact: He loves hiking and has climbed several peaks in the Himalayas.
    ```

### Running the Application

Once everything is set up, run the Streamlit application:

```bash
streamlit run app.py
