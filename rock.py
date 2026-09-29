

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

user_score = 0
computer_score = 0

@app.route('/')
def index():
    return render_template('rock-index.html')

@app.route('/play', methods=['POST'])
def play():
    global user_score, computer_score

    user_choice = request.json.get('choice')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    result = determine_winner(user_choice, computer_choice)

    if result == 'win':
        user_score += 1
    elif result == 'lose':
        computer_score += 1

    return jsonify({'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result, 'user_score': user_score, 'computer_score': computer_score })

def determine_winner(user, computer):
    outcomes = {
        ('rock', 'scissors'): 'win',
        ('scissors', 'paper'): 'win',
        ('paper', 'rock'): 'win',
        ('scissors', 'rock'): 'lose',
        ('paper', 'scissors'): 'lose',
        ('rock', 'paper'): 'lose'
    }
    if user == computer:
        return 'draw'
    return outcomes.get((user, computer), 'draw')

if __name__ == '__main__':
    app.run(debug=True)