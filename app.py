import os
import json
from flask import Flask, render_template, request, redirect, url_for
from openai import AzureOpenAI

app = Flask(__name__)

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    azure_deployment="dall-e-3"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = client.images.generate( 
            prompt=prompt,
            size='1024x1024',
            n=1
        )
        image_url = json.loads(response.model_dump_json())['data'][0]['url']
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
