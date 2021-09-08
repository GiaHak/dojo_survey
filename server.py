from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key="dojo"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/output')


@app.route('/output')
def success():
    return render_template('output.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
