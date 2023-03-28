from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loading')
def loading():
    return render_template('loading.html')


@app.route('/process_data')
def process_data():
    time.sleep(5)  # Simulate processing time
    return jsonify({"result": "Data processed"})


if __name__ == '__main__':
    app.run(debug=True)
