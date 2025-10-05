import pyttsx3

def test_voices():
    """Test all available voices and identify female voices"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    print(f"Found {len(voices)} voices on your system:\n")
    
    for i, voice in enumerate(voices):
        print(f"Voice {i}:")
        print(f"  Name: {voice.name}")
        print(f"  ID: {voice.id}")
        print(f"  Gender: {'Female' if any(name in voice.name.lower() for name in ['zira', 'female', 'woman', 'hazel', 'susan']) else 'Male/Unknown'}")
        
        # Test the voice
        engine.setProperty('voice', voice.id)
        engine.say(f"Hello, this is voice {i}. My name is {voice.name}")
        engine.runAndWait()
        print()

if __name__ == "__main__":
    test_voices()
