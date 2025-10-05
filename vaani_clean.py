import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys

class VaaniClean:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.setup_voice()
        
    def setup_voice(self):
        """Set up female voice"""
        voices = self.engine.getProperty('voices')
        
        # Find female voice
        for voice in voices:
            if any(name in voice.name.lower() for name in ['zira', 'female', 'woman', 'hazel', 'susan']):
                self.engine.setProperty('voice', voice.id)
                print(f"✅ Using female voice: {voice.name}")
                break
        else:
            # Use index 1 if available (usually female)
            if len(voices) > 1:
                self.engine.setProperty('voice', voices[1].id)
                print(f"✅ Using voice: {voices[1].name}")
        
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
    
    def speak(self, text):
        """Make Vaani speak"""
        print(f"Vaani: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to user input"""
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Ready! Please speak now...")
                audio = self.recognizer.listen(source, timeout=5)
            
            text = self.recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            self.speak("Speech service error.")
            return None
        except:
            return None
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return True
        
        # Greetings
        if any(word in command for word in ['hello', 'hi', 'hey']):
            self.speak("Hello! I'm Vaani, your voice assistant. How can I help you?")
        
        # Time and date
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            
        elif any(word in command for word in ['date', 'day', 'today']):
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}")
        
        # Websites
        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            self.speak("Opening YouTube")
            
        elif 'gmail' in command or 'email' in command:
            webbrowser.open("https://mail.google.com")
            self.speak("Opening Gmail")
            
        elif 'google' in command:
            webbrowser.open("https://www.google.com")
            self.speak("Opening Google")
            
        elif 'news' in command:
            webbrowser.open("https://news.google.com")
            self.speak("Opening Google News")
        
        # System commands
        elif 'calculator' in command or 'calc' in command:
            if sys.platform == "win32":
                os.system("calc")
                self.speak("Opening calculator")
            else:
                self.speak("Please open your calculator app")
        
        # Personal responses
        elif any(word in command for word in ['thank you', 'thanks']):
            self.speak("You're welcome!")
        
        elif any(word in command for word in ['how are you']):
            self.speak("I'm doing great! Thank you for asking.")
        
        elif 'your name' in command or 'who are you' in command:
            self.speak("I'm Vaani, your personal voice assistant.")
        
        # Help
        elif 'help' in command:
            help_text = """I can help you with:
            Time and date,
            Opening websites like YouTube and Gmail,
            Basic system commands,
            And simple conversations.
            Just speak naturally!"""
            self.speak(help_text)
        
        # Exit
        elif any(word in command for word in ['goodbye', 'bye', 'exit', 'quit']):
            self.speak("Goodbye! Have a great day!")
            return False
        
        else:
            self.speak("I'm not sure how to help with that. Try saying 'help' to see what I can do.")
        
        return True
    
    def run(self):
        """Main loop"""
        self.speak("Hello! I'm Vaani, your voice assistant. I'm ready to help!")
        
        while True:
            try:
                command = self.listen()
                if command:
                    if not self.process_command(command):
                        break
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break

if __name__ == "__main__":
    assistant = VaaniClean()
    assistant.run()
