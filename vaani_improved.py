import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys

class VoiceAssistant:
    def __init__(self):
        """Initialize the voice assistant with female voice"""
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.setup_voice()
        
    def setup_voice(self):
        """Configure voice settings for female voice"""
        voices = self.engine.getProperty('voices')
        
        # Find and set female voice
        female_voice = None
        for voice in voices:
            # Look for female voices (common names/patterns)
            if any(name in voice.name.lower() for name in ['zira', 'female', 'woman', 'hazel', 'susan']):
                female_voice = voice
                break
        
        # If no specific female voice found, use index 1 (usually female)
        if female_voice is None and len(voices) > 1:
            female_voice = voices[1]
        elif female_voice is None:
            female_voice = voices[0]
            
        self.engine.setProperty('voice', female_voice.id)
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        print(f"✅ Voice set to: {female_voice.name}")
    
    def speak(self, text):
        """Make the assistant speak"""
        print(f"Vaani: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to user input with improved error handling"""
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Ready! Please speak now...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
            
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand that. Please try again.")
            return None
        except sr.RequestError:
            self.speak("I'm having trouble with the speech service. Please check your internet connection.")
            return None
        except sr.WaitTimeoutError:
            print("No speech detected. Continuing...")
            return None
        except Exception as e:
            self.speak("I'm having trouble with the microphone.")
            print(f"Error: {e}")
            return None
    
    def process_command(self, command):
        """Process voice commands with expanded functionality"""
        if not command:
            return True
            
        # Greeting commands
        if any(word in command for word in ['hello', 'hi', 'hey']):
            self.speak("Hello! I'm Vaani, your voice assistant. How can I help you today?")
        
        # Time and date
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            
        elif any(word in command for word in ['date', 'day', 'today']):
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}")
        
        # Weather (placeholder - you can integrate with weather API)
        elif 'weather' in command:
            self.speak("I don't have access to weather data yet, but you can check your weather app or ask me to search for weather online.")
        
        # Web searches and websites
        elif 'search' in command or 'google' in command:
            search_term = command.replace('search for', '').replace('search', '').replace('google', '').strip()
            if search_term:
                url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
                webbrowser.open(url)
                self.speak(f"Searching for {search_term}")
            else:
                self.speak("What would you like me to search for?")
        
        elif 'youtube' in command:
            if 'search' in command:
                search_term = command.replace('search youtube for', '').replace('youtube search', '').strip()
                url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
                webbrowser.open(url)
                self.speak(f"Searching YouTube for {search_term}")
            else:
                webbrowser.open("https://www.youtube.com")
                self.speak("Opening YouTube")
        
        elif 'gmail' in command or 'email' in command:
            webbrowser.open("https://mail.google.com")
            self.speak("Opening Gmail")
            
        elif 'news' in command:
            webbrowser.open("https://news.google.com")
            self.speak("Opening Google News")
        
        # System commands
        elif any(word in command for word in ['calculator', 'calc']):
            if sys.platform == "win32":
                os.system("calc")
                self.speak("Opening calculator")
            else:
                self.speak("Please open your calculator app manually")
        
        elif 'notepad' in command:
            if sys.platform == "win32":
                os.system("notepad")
                self.speak("Opening notepad")
            else:
                self.speak("Please open your text editor manually")
        
        # Personal responses
        elif any(word in command for word in ['thank you', 'thanks']):
            self.speak("You're welcome! I'm happy to help.")
        
        elif any(word in command for word in ['how are you', 'how do you do']):
            self.speak("I'm doing great! Thank you for asking. How can I assist you?")
        
        elif 'your name' in command or 'who are you' in command:
            self.speak("I'm Vaani, your personal voice assistant. I'm here to help you with various tasks.")
        
        # Exit commands
        elif any(word in command for word in ['goodbye', 'bye', 'exit', 'quit', 'stop']):
            self.speak("Goodbye! Have a wonderful day!")
            return False
        
        # Help command
        elif 'help' in command:
            help_text = """I can help you with:
            - Telling time and date
            - Searching the web
            - Opening websites like YouTube, Gmail, and News
            - Opening system applications
            - Basic conversations
            Just speak naturally and I'll do my best to help!"""
            self.speak(help_text)
        
        else:
            self.speak("I'm not sure how to help with that. Try saying 'help' to see what I can do.")
        
        return True
    
    def run(self):
        """Main loop for the voice assistant"""
        self.speak("Hello! I'm Vaani, your voice assistant. I'm ready to help you!")
        
        while True:
            try:
                command = self.listen()
                if command:
                    if not self.process_command(command):
                        break
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                self.speak("I encountered an error. Let me try again.")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
