from flask import Flask, render_template, make_response, send_from_directory
from flask import redirect, request, jsonify, url_for
from getKeyWords import sample_analyze_entities
from fill_blanks import get_blank_questions
from getPDF import getPDF

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template('index.html', title='Flashcard Generator')


@app.route("/input-page")
def input_page():
    return render_template('input_page.html', title='Flashcard Generator')

@app.route("/info")
def info():
    return render_template('info.html', title='Info')

@app.route("/us")
def about_us():
    return render_template('about_us.html', title='About Us')

@app.route("/submit-text", methods=['POST'])
def submit_text():
    text = request.form.get('text')
    keywords = sample_analyze_entities(text)
    # Return them
    return render_template('keyword_return.html', keywords=keywords, text=text, title='Customize Your Preference')


@app.route("/submit-keywords", methods=['POST'])
def make_flashcards():
    text = request.form.get('text')
    keywords = [word for word in request.form.get('keywords').split(",") if len(word) > 1]
    filename = getPDF(text, keywords)
    # Return them using send_from_directory
    return send_from_directory('', filename)


if __name__ == "__main__":
    app.run()
