from flask import Flask, render_template, request, jsonify
from chat import get_response
from speech__recognition import get_recognize_google
from pyttsx3__speaking import speaking

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#@app.route('/')
#def index_get():
#    return render_template('base.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get('message')
    response = get_response(text)
    message = {'answer': response}
    return jsonify(message)

@app.route('/recognize')
def recognize_speech():
    # TODO: verifica si el texto es válido
    request = get_recognize_google()
    response = get_response(request)
    message = {'question': request, 'answer': response}
    speaking(response)
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
