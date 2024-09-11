from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = 'Alice'
    is_logged_in = True
    return render_template('index.html', user=user, is_logged_in=is_logged_in)

if __name__ == '__main__':
    app.run(debug=True)

