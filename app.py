from flask import Flask, request
import g4f
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    input = request.form.get('inputt')
    response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    messages=input,
    timeout=120,
    )
    return "RESPONSE: " + str(response)
