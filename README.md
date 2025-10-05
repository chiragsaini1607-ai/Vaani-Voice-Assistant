# Vaani - Voice Assistant

A clean voice assistant with female voice and web UI using Streamlit.

## Setup

1. **Activate your virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   # For voice assistant
   pip install -r requirements.txt
   
   # For web UI
   pip install -r requirements_streamlit.txt
   ```

## Usage

### Voice Assistant (Local)
```bash
python vaani_clean.py
```

### Web UI (Streamlit)
```bash
streamlit run app.py
```

### Test Voices
```bash
python test_voices.py
```

## Voice Commands

- **Greetings:** "Hello", "Hi", "Hey"
- **Time:** "What time is it?"
- **Date:** "What's the date?", "What day is it?"
- **Websites:** "Open YouTube", "Open Gmail", "Open Google"
- **News:** "Open news"
- **Personal:** "How are you?", "What's your name?"
- **Help:** "Help" - shows available commands
- **Exit:** "Goodbye", "Bye", "Exit"

## Features

### Voice Assistant:
- ✅ Female voice (automatically selected)
- ✅ No API keys needed
- ✅ Fast responses
- ✅ Works offline (except speech recognition)

### Web UI:
- ✅ Beautiful chat interface
- ✅ Real-time messaging
- ✅ Mobile-friendly design
- ✅ Easy to share and deploy

## Files

- `vaani_clean.py` - Main voice assistant
- `app.py` - Streamlit web UI
- `test_voices.py` - Test available voices
- `requirements.txt` - Voice assistant dependencies
- `requirements_streamlit.txt` - Web UI dependencies

## Deployment

Deploy the Streamlit app to Streamlit Cloud:
1. Push to GitHub
2. Go to share.streamlit.io
3. Connect your repository
4. Deploy `app.py`
