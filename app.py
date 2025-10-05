import streamlit as st
import datetime

# Page config
st.set_page_config(
    page_title="Vaani - Voice Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main-header {
        text-align: center;
        color: white;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def process_command(command):
    """Process text commands and return response"""
    if not command:
        return "Please say something!"
    
    command_lower = command.lower()
    
    # Greetings
    if any(word in command_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm Vaani, your voice assistant. How can I help you? 😊"
    
    # Time and date
    elif 'time' in command_lower:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"🕐 The current time is {current_time}"
        
    elif any(word in command_lower for word in ['date', 'day', 'today']):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"📅 Today is {current_date}"
    
    # Websites
    elif 'youtube' in command_lower:
        return "🎥 I would open YouTube for you!"
        
    elif 'gmail' in command_lower or 'email' in command_lower:
        return "📧 I would open Gmail for you!"
        
    elif 'google' in command_lower:
        return "🔍 I would open Google for you!"
        
    elif 'news' in command_lower:
        return "📰 I would open Google News for you!"
    
    # Personal responses
    elif any(word in command_lower for word in ['thank you', 'thanks']):
        return "You're welcome! 😊"
    
    elif any(word in command_lower for word in ['how are you']):
        return "I'm doing great! Thank you for asking. 😄"
    
    elif 'your name' in command_lower or 'who are you' in command_lower:
        return "I'm Vaani, your personal voice assistant! 🤖"
    
    # Help
    elif 'help' in command_lower:
        return """🆘 I can help you with:
• Time and date
• Opening websites (YouTube, Gmail, Google, News)
• Basic conversations
• Just type naturally and I'll respond!"""
    
    # Exit
    elif any(word in command_lower for word in ['goodbye', 'bye', 'exit']):
        return "Goodbye! Have a great day! 👋"
    
    else:
        return "🤔 I'm not sure how to help with that. Try typing 'help' to see what I can do!"

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Header
st.markdown('<h1 class="main-header">🤖 Vaani</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your Personal Voice Assistant</p>', unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response
    response = process_command(prompt)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# Sidebar
with st.sidebar:
    st.header("📋 Commands")
    st.write("• **Hello** - Greet Vaani")
    st.write("• **What time is it?** - Get current time")
    st.write("• **What's the date?** - Get current date")
    st.write("• **Open YouTube** - Website commands")
    st.write("• **Help** - See all commands")
    st.write("• **Goodbye** - Say bye")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
