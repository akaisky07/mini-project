from flask import Flask, render_template, request
import os
import google.generativeai as genai

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    input=request.form['input']

    os.environ['GOOGLE_API_KEY'] = "AIzaSyAiB2nQe1lfdip_h0Ap2wphPGzM-_bRJBY"
    genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
    from IPython.display import Markdown
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Summarize the following function in a concise and informative way"+input)

    return render_template('index.html', prediction = response.text)

if __name__=='__main__':
    app.run(debug=True)
