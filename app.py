import streamlit as st
import datetime

# Page config
st.set_page_config(
    page_title="Vaani - Voice Assistant",
    page_icon="🤖",
    layout="centered"
)

def process_command(command):
    """Process text commands and return response"""
    if not command:
        return "Please say something!"
    
    command_lower = command.lower()
    
    if any(word in command_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm Vaani, your voice assistant. How can I help you?"
    elif 'time' in command_lower:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    elif any(word in command_lower for word in ['date', 'day', 'today']):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}"
    elif 'youtube' in command_lower:
        return "I would open YouTube for you!"
    elif 'gmail' in command_lower or 'email' in command_lower:
        return "I would open Gmail for you!"
    elif 'help' in command_lower:
        return "I can help you with time, date, opening websites, and basic conversations!"
    elif any(word in command_lower for word in ['goodbye', 'bye', 'exit']):
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to help with that. Try saying help!"

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'last_response' not in st.session_state:
    st.session_state.last_response = ""

# Header
st.title("🤖 Vaani")
st.subheader("Your Personal Voice Assistant")

# Simple voice button
if st.button("🎤 Click to Speak", type="primary"):
    st.info("🎤 Voice recognition would work here in a full deployment. For now, use the text input below.")

# Text input
user_input = st.text_input("💬 Type your message:", placeholder="Try: Hello, What time is it?, Help")

# Process input
if user_input:
    # Add to messages
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get response
    response = process_command(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.last_response = response

# Auto-speak the last response
if st.session_state.last_response:
    # Simple text-to-speech using HTML5
    speech_html = f"""
    <div style="background: #e8f4f8; padding: 15px; border-radius: 10px; margin: 10px 0;">
        <p><strong>🔊 Vaani says:</strong> {st.session_state.last_response}</p>
        <button onclick="speakText()" style="
            background: #00c851; 
            color: white; 
            border: none; 
            padding: 8px 15px; 
            border-radius: 5px; 
            cursor: pointer;
        ">🔊 Play Audio</button>
        <button onclick="stopSpeech()" style="
            background: #ff4444; 
            color: white; 
            border: none; 
            padding: 8px 15px; 
            border-radius: 5px; 
            cursor: pointer;
            margin-left: 10px;
        ">🔇 Stop</button>
    </div>
    
    <script>
    function speakText() {{
        if ('speechSynthesis' in window) {{
            const text = "{st.session_state.last_response}";
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 0.8;
            utterance.pitch = 1.1;
            speechSynthesis.speak(utterance);
        }} else {{
            alert('Speech not supported in this browser');
        }}
    }}
    
    function stopSpeech() {{
        if ('speechSynthesis' in window) {{
            speechSynthesis.cancel();
        }}
    }}
    
    // Auto-play (some browsers block this)
    setTimeout(function() {{
        speakText();
    }}, 500);
    </script>
    """
    st.components.v1.html(speech_html, height=120)

# Display conversation
if st.session_state.messages:
    st.markdown("### 💬 Conversation")
    for message in st.session_state.messages[-6:]:  # Show last 6 messages
        if message["role"] == "user":
            st.markdown(f"**👤 You:** {message['content']}")
        else:
            st.markdown(f"**🤖 Vaani:** {message['content']}")

# Sidebar
with st.sidebar:
    st.header("🚀 Quick Commands")
    
    if st.button("👋 Hello"):
        st.session_state.messages.append({"role": "user", "content": "Hello"})
        response = process_command("hello")
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.last_response = response
        st.rerun()
    
    if st.button("🕐 Time"):
        st.session_state.messages.append({"role": "user", "content": "What time is it?"})
        response = process_command("what time is it")
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.last_response = response
        st.rerun()
    
    if st.button("📅 Date"):
        st.session_state.messages.append({"role": "user", "content": "What's the date?"})
        response = process_command("what's the date")
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.last_response = response
        st.rerun()
    
    if st.button("🗑️ Clear"):
        st.session_state.messages = []
        st.session_state.last_response = ""
        st.rerun()
    
    st.markdown("---")
    st.markdown("**💡 How to use:**")
    st.markdown("1. Type your message")
    st.markdown("2. Vaani responds with text")
    st.markdown("3. Click 🔊 Play Audio to hear")
    st.markdown("4. Use quick buttons for fast commands")
