import os
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    response = openai.Completion.create(
        engine="davinci",  # You can change the engine if desired
        prompt=prompt,
        max_tokens=50  # Adjust this as needed
    )
    completion_text = response.choices[0].text.strip()
    return render_template('index.html', prompt=prompt, completion=completion_text)

if __name__ == '__main__':
    app.run(debug=True)
