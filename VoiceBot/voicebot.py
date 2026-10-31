import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()
#записує аудіо
def capture_voice_input():
    with sr.Microphone() as source:
        print("Слухаю...")
        audio = recognizer.listen(source)
    return audio

#перетворює аудіо в текст
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language = 'uk-UA')
        print("Ви сказали: " + text)
    except:
        text = ""
        print("Sorry, I didn't understand that.")
    return text

#
def process_voice_command(text):
    if "привіт" in text.lower():
        print("Привіт! Як я можу Вам допомогти?")
    elif "прощавай" in text.lower():
        print("До побачення! Гарного дня!")
        return True
    elif "ютуб" or "youtube" or "відкрий ютуб" or "відкрий ютуб" in text.lower():
        webbrowser.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")
    elif "" in text.lower() or "" in text.lower():
        webbrowser.open("")
    else:
        print("Я Вас не розумію. Повторіть Ваш запит")
    return False

def main():
    audio = capture_voice_input()
    text = convert_voice_to_text(audio)
    process_voice_command(text)

if __name__ == "__main__":
    main()
