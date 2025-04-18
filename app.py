from flask import Flask, send_file, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'secret143'

@app.route('/')
def index():
    session['number'] = random.randint(1, 100)
    session['attempts'] = 0
    return send_file('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    guess = int(data['guess'])
    number = session.get('number')
    session['attempts'] += 1

    if guess < number:
        result = 'Too Low!'
    elif guess > number:
        result = 'Too High!'
    else:
        result = 'Correct!'

    return jsonify({
        'result': result,
        'attempts': session['attempts']
    })

if __name__ == '__main__':
    app.run(debug=True)
