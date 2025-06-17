import os
import streamlit as st
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# 🔐 Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# 📄 Load Rakesh's profile
with open("rakesh_profile.txt", "r", encoding="utf-8") as f:
    rakesh_profile = f.read()

# 🎙️ TTS setup (safe re-init per response)
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        st.warning(f"Voice error: {e}")

# 🎧 Speech recognition setup
recognizer = sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Hmm, I didn’t catch that."
        except sr.WaitTimeoutError:
            return "Timeout. Try again."
        except Exception as e:
            return f"Error: {str(e)}"

# 🧠 LLM setup
llm = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",
    temperature=0.6,
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# 💬 Prompt setup
prompt = ChatPromptTemplate.from_messages([
    ("system", f"You are Rakesh’s friendly voice assistant. Keep answers chill, short, and conversational. Here’s what you know:\n{rakesh_profile}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# 💾 Session memory setup
if "history" not in st.session_state:
    st.session_state.history = InMemoryChatMessageHistory()
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

chat_chain = RunnableWithMessageHistory(
    prompt | llm,
    lambda session_id: st.session_state.history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

# 🌐 Streamlit UI
st.set_page_config(page_title="🎤 Rakesh's Voice Assistant")
st.title("👋 Hey, I'm Rakesh's Voice Assistant")
st.caption("Ask me anything about Rakesh — background, skills, goals, or fun facts.")

# Show conversation history
for msg in st.session_state.chat_log:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Voice input button
if st.button("🎙️ Tap to Speak"):
    user_text = listen()
    st.session_state.chat_log.append({"role": "human", "content": user_text})
    with st.chat_message("human"):
        st.markdown(user_text)

    response = chat_chain.invoke(
        {"input": user_text},
        config={"configurable": {"session_id": "rakesh-session"}}
    )

    answer = response.content.strip()
    #short_answer = answer.split("\n")[0]  # Grab only first short line

    st.session_state.chat_log.append({"role": "ai", "content": answer})
    with st.chat_message("ai"):
        st.markdown(answer)

    speak(answer)
