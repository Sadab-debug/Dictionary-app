from flask import Flask, render_template, request
import pyttsx3
import threading

app = Flask(__name__)

# Define the word dictionary
word = {
    'apple': 'one kind of fruit which usually contains vitamin C',
    'teacher': 'someone who teaches',
    'flood': 'one kind of natural disaster which usually occurs due to excessive rainfall or tsunami',
}



def speak_message(message, voice_id=None):
    engine = pyttsx3.init()
    if voice_id is not None:
        engine.setProperty('voice', voice_id)
    engine.say(message)
    engine.runAndWait()
    


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['word'].strip().lower()
        output = word.get(user, "Word not found")

        if output == "Word not found":
            result_message = "Sorry, the word is not in the dictionary."
        else:
            result_message = f"Sir, meaning of the word {user} is {output}"

        # Use a separate thread for text-to-speech
        threading.Thread(target=speak_message, args=(result_message,)).start()

        return render_template('index.html', result=result_message)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

