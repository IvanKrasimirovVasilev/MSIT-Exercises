from flask import Flask, render_template

app = Flask(__name__)

navigation = [
    {"name": "Home", "url": "/"},
    {"name": "About", "url": "/about"},
]

@app.route('/')
def index():
    return render_template('template_inheritance_index.html', navigation=navigation)

@app.route('/about')
def about():
    return render_template('template_inheritance_about.html', navigation=navigation)

if __name__ == '__main__':
    app.run(debug=True)