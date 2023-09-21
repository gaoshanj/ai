import os
from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = openai.Image.create(
            prompt=prompt,
            size='1024x1024',
            n=1
        )
        image_url = response["data"][0]["url"]
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
