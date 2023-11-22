from flask import Flask, render_template, request
import os
from openai import AzureOpenAI
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form.get('prompt')

        client = AzureOpenAI(
            api_version="2023-12-01-preview",
            azure_endpoint="https://dalle3-demo0416.openai.azure.com/openai/deployments/Dalle3/images/generations?api-version=2023-06-01-preview",
            api_key="890c9c0619cb40489e0a5d331da7ceef",
        )

        result = client.images.generate(
            model="dall-e-3", # the name of your DALL-E 3 deployment
            prompt=prompt,
            n=1
        )

        image_url = json.loads(result.model_dump_json())['data'][0]['url']

        return render_template('home.html', image_url=image_url)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)